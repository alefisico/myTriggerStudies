#!/usr/bin/env python

import math,ROOT, sys
import collections
from array import array
import numpy as np
from setTDRStyle import *
from ROOT import gROOT, TFile, TChain, TTree, TH1F, TF1, TLegend, TCanvas, gStyle, TH2F

gROOT.Reset()
gROOT.SetBatch()
setTDRStyle()
gROOT.ForceStyle()
gROOT.SetStyle('tdrStyle')


gStyle.SetOptStat(0)

def grabTriggerNumbers( file, xs, PU ):

	txtFile = open( file )
	tmpList = []
	completeList = []

	with txtFile as fh:
		for line in fh:	tmpList.append( line.split() )

	for j in tmpList:
		rate, rateErr = GetRates( float(j[1]), float(j[2]), xs, PU )
		completeList.append( [ j[0], int(j[1]), int(j[2]), int(j[3]), rate, rateErr ] )

	return completeList

def GetRates( run, passed, xs, PU ):

	##############################
	# nfillb is number of filled bunches. So for 50ns sample it's usually 1331, and for 25ns sample it's 2662. 
	# mfillb is the maximum number of bunches that could be in the ring, so it's 3564. 
	# xtime is the bunch crossing spacing, so 50e-9 if you're using 50ns samples and 25e-9 if you're using 25ns samples. 
	# xs is the cross section of the sample, and 
	# ilumi is the luminosity you want to find the rate for. So if you're interested in the rate you would get if it was 50ns bunch crossing then you could use 7e33 I think, and the worst case scenario in 2015 (that is 25ns bunch crossing, highest luminosity) is 1.4e34. 
	# nevt is the total number of events of your sample. 
	###############################

	mfillb = 3564.
	xsec = xs*1e-36
	if 'bx50' in PU:
		nfillb = 1331.
		xtime = 50e-9
		ilumi = 4e33
	elif 'bx25' in PU:
		nfillb = 2662.
		xtime = 25e-9
		ilumi = 1.4e34
	collrate = (nfillb/mfillb)/xtime

	#rateList.append( collrate * (1 - math.exp(-1* (xsec*ilumi*passed[i]/run[i])/collrate)) )
	rate = xsec*ilumi*(passed/run)
	#rateErrList.append( xsec * ilumi * ((math.sqrt( passed[i] + (( passed[i])**2)/ run[i]))/ run[i]) )
	rateErr = ( xsec * ilumi ) / run * math.sqrt( passed )

	return rate, rateErr

def plotRates( listRates, listNames, outName, PU ):
	"""docstring for plotRates"""

	#HT = [ 350., 650., 700., 750., 800., 850. ]
	#HT = [ 650., 700., 750., 800., 850. ]
	HT = [ 450., 550., 650., 750., 850. ]
	addHT = [ 450., 550., 650., 750., 850., 900., 950. ]
	HTErr = [ 0., 0., 0., 0., 0. ]
	addHTErr = [ 0., 0., 0., 0., 0., 0., 0. ]
	if 'PFHT' in outName:
		t = array( 'd', addHT)
		tErr = array( 'd', addHTErr)
	else:
		t = array( 'd', HT)
		tErr = array( 'd', HTErr)

	legend=TLegend(0.55,0.70,0.85,0.90)
	legend.SetFillColor(0)
	legend.SetTextSize(0.03)

	officialHT = [ 650., 700., 750. ]
	officialHTErr = [ 0., 0., 0. ]
	if 'bx50' in PU:
		officialRate = [ 45.17, 34.58, 26.70 ]
		officialRateErr = [ 1.25, 1.08, 0.92 ]
	elif 'bx25' in PU:
		officialRate = [ 107.10, 81.44, 62.81 ]
		officialRateErr = [ 2.07, 1.69, 1.69 ]
	a = array( 'd', officialHT ) 
	d = array( 'd', officialHTErr ) 
	b = array( 'd', officialRate ) 
	c = array( 'd', officialRateErr ) 
	g4 = ROOT.TGraphErrors(len(a), a, b, d, c)
	g4.SetLineColor(1)
	g4.SetLineWidth(2)
	legend.AddEntry(g4, 'Official HLT_PFNoPUHT', "l")

	dictGraphs = {}
	listMax = []
	for i in range( len( listRates ) ): 
		rates = []
		ratesErr = []
		tmpPrint = []
		for trigger in listRates[i]:
			rates.append( trigger[4] )
			ratesErr.append( trigger[5] )
			print trigger[0][4:-3], np.around( trigger[4],2), '\pm',  np.around( trigger[5], 1)
		dictGraphs[ listNames[i] ] = ROOT.TGraphErrors( len(t), t, array( 'd', rates), tErr, array( 'd', ratesErr ) )
		legend.AddEntry( dictGraphs[ listNames[i] ], listNames[i], 'l' )
		for j in rates: listMax.append( j )

	dictGraphs.values()[0].SetTitle("Trigger Rates for "+PU)
	dictGraphs.values()[0].GetXaxis().SetTitle("HT [GeV]")
	dictGraphs.values()[0].GetYaxis().SetTitle("Rate [Hz]")
	dictGraphs.values()[0].SetMaximum( max( listMax )+50 )

	k = 1
	for t, histo in dictGraphs.items():
		k += 1
		histo.SetLineColor(k)
		histo.SetLineWidth(2)

	c = TCanvas( "c1", "c1", 800, 500 )
	dictGraphs.values()[0].Draw('lpa')
	for q in range( 1, len( dictGraphs.keys() ) ): dictGraphs.values()[q].Draw('lp')
	g4.Draw("lp")
	legend.Draw()
	setTriggerRates( 'QCD 13TeV '+PU )
	c.SaveAs("Rates/TriggerRate_"+outName+'_'+PU+"_30k_50toInf.pdf")

def plotCaloJetRates( listRates, outName, PU ):
	"""docstring for plotRates"""

	CaloHT = [ 250., 300., 350., 400., 450. ]
	addCaloHT = [ 550., 600., 650., 700., 750. ]
	CaloHTErr = [ 0., 0., 0., 0., 0. ]
	if 'HT850' in outName:
		t = array( 'd', addCaloHT)
		tErr = array( 'd', CaloHTErr)
	else:
		t = array( 'd', CaloHT)
		tErr = array( 'd', CaloHTErr)

	legend=TLegend(0.55,0.70,0.85,0.90)
	legend.SetFillColor(0)
	legend.SetTextSize(0.03)

	dictGraphs = {}
	listMax = []
	for i in listRates: 
		dictGraphs[ i[0] ] = ROOT.TGraphErrors( len(t), t, i[1], tErr, i[2] )
		legend.AddEntry( dictGraphs[ i[0] ], i[0], 'l' )
		for j in i[1]: listMax.append( j )
		for k in xrange( len(i)+2 ):
			print i[0], np.around( i[1][k], 3), '\pm', np.around( i[2][k], 3 )
		print i[0], np.around( i[1], 3)

	dictGraphs.values()[0].SetTitle("Trigger Rates for "+PU)
	dictGraphs.values()[0].GetXaxis().SetTitle("Calo HT [GeV]")
	dictGraphs.values()[0].GetYaxis().SetTitle("Rate [Hz]")
	dictGraphs.values()[0].SetMaximum( max( listMax )+50 )

	k = 1
	for t, histo in dictGraphs.items():
		k += 1
		histo.SetLineColor(k)
		histo.SetLineWidth(2)

	c = TCanvas( "c1", "c1", 800, 500 )
	dictGraphs.values()[0].Draw('lpa')
	for q in range( 1, len( dictGraphs.keys() ) ): dictGraphs.values()[q].Draw('lp')
	legend.Draw()
	setTriggerRates( 'QCD 13TeV '+PU )
	c.SaveAs("Rates/TriggerRate_"+outName+'_'+PU+"_CaloJet_test.pdf")

def plotRatesComp( listRates, outName, PU, HT, Mass ):
	"""docstring for plotRates"""

	gStyle.SetPaintTextFormat("4.3f")
	histo = TH2F("xbox",'box', 7, 650., 1000., 20, -5.0, 95.0 )
	for i in xrange( len( HT ) ): 
		for k in xrange( len( Mass ) ):
			histo.Fill( HT[i], Mass[k], listRates[i][k][4] )
			print  HT[i], Mass[k], listRates[i][k][4] 
	#print i[0], np.around( i[1], 3)

	histo.SetTitle("Trigger Rates for "+outName+" "+PU)
	histo.GetXaxis().SetTitle("HT [GeV]")
	histo.GetYaxis().SetTitle("Leading Jet Mass [GeV]")


	c = TCanvas( "c1", "c1", 800, 500 )
	c.SetLogz()
	histo.Draw("colz")
	histo.Draw("texte same")
	setTriggerRatesComp( 'QCD 13TeV '+PU, outName )
	c.SaveAs("Rates/TriggerRate_"+outName+'_'+PU+".pdf")


def plotRatesCompPtMass( listRates, outName, PU):
	"""docstring for plotRates"""

	Pt = [ 40., 100., 150., 200., 250. ]
	Mass = [ 0., 5., 10., 15., 20., 25., 30., 35., 40., 45., 50., 55. ]

	ptBin = array('f', [ 0., 25., 75., 125., 175., 225., 275., 300. ] )
	massBin = array( 'f', [ -5.5, -2.5, 2.5, 7.5, 12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5, 52.5, 57.5, 62.5 ])
	histo = TH2F("xbox",'box', len(ptBin)-1, ptBin, len(massBin)-1, massBin )
	for i in xrange( len(Pt) ): 
		for k in xrange( len( Mass ) ):
			histo.Fill( Pt[i], Mass[k], listRates[i][1][k] )
			#print  Pt[i], Mass[k], listRates[i][1][k] 
		#print i[0], np.around( i[1], 3)

	histo.SetTitle("Trigger Rates for "+outName+" "+PU)
	histo.GetXaxis().SetTitle("Leading Jet Pt [GeV]")
	histo.GetYaxis().SetTitle("Leading Jet Mass [GeV]")


	c = TCanvas( "c1", "c1", 800, 500 )
	#c.SetLogz()
	histo.Draw("colz")
	#histo.Draw("box same")
	histo.Draw("texte same")
	setTriggerRatesComp( 'QCD 13TeV '+PU, outName )
	c.SaveAs("TriggerRate_"+outName+'_'+PU+".pdf")



if __name__ == '__main__':


	PU = sys.argv[1]
	process = sys.argv[2]

	ptBin = {}
	#ptBin['50to80'] = 22110000.
	#ptBin['80to120'] = 3000114.3
	ptBin['120to170'] = 493200.
	ptBin['170to300'] = 120300.
	ptBin['300to470'] = 7475.
	ptBin['470to600'] = 587.1
	ptBin['600to800'] = 167.
	ptBin['800to1000'] = 28.25

	tmpRates = {}
	tmpListRates = []
	rates = []
	for bin, XS in ptBin.iteritems(): tmpRates[ bin ] = grabTriggerNumbers('Rates/rates_QCD_Pt-'+bin+'_Tune4C_13TeV_pythia8_'+PU+'.txt', XS, PU)

	### This is unnecesary but I want to keep track of the rates per ptBin
	for bin, listPerBin in tmpRates.items():
		for i in listPerBin: tmpListRates.append( i )

	d = collections.defaultdict(list)
	for item in tmpListRates: d[item[0]].append(item)
	for key, value in d.items(): rates.append( [key] + map(sum, zip(*value)[1:]) )
		
	rates.sort()
	PFHT = []
	PFTrimHT = []
	AK8PFHT = []
	AK8PFTrimHT = []
	AK8PFNOJECTrimHT = []
	PFTrimHT450 = []
	PFTrimHT550 = []
	PFTrimHT650 = []
	PFTrimHT750 = []
	PFTrimHT850 = []
	AK8PFTrimHT450 = []
	AK8PFTrimHT550 = []
	AK8PFTrimHT650 = []
	AK8PFTrimHT700 = []
	AK8PFTrimHT750 = []
	AK8PFTrimHT800 = []
	AK8PFTrimHT850 = []
	AK8PFTrimHT900 = []
	AK8PFTrimHT450TrimMod = []
	AK8PFTrimHT550TrimMod = []
	AK8PFTrimHT650TrimMod = []
	AK8PFTrimHT700TrimMod = []
	AK8PFTrimHT750TrimMod = []
	AK8PFTrimHT800TrimMod = []
	AK8PFTrimHT850TrimMod = []
	AK8PFTrimHT900TrimMod = []
	AK8PFTrimHT450AK4CaloHT = []
	AK8PFTrimHT550AK4CaloHT = []
	AK8PFTrimHT650AK4CaloHT = []
	AK8PFTrimHT750AK4CaloHT = []
	AK8PFTrimHT850AK4CaloHT = []

	for triggerInfo in rates:
		if not '_Mass' in triggerInfo[0] and not '_TrimMass' in triggerInfo[0] and not '_Calo' in triggerInfo[0]:
			if 'HLT_PFHT' in triggerInfo[0]: PFHT.append( triggerInfo )
			if 'HLT_PFTrimHT' in triggerInfo[0]: PFTrimHT.append( triggerInfo )
			if 'HLT_AK8PFHT' in triggerInfo[0]: AK8PFHT.append( triggerInfo )
			if 'HLT_AK8PFTrimHT' in triggerInfo[0]: AK8PFTrimHT.append( triggerInfo )
			if 'HLT_AK8PFNOJECTrimHT' in triggerInfo[0]: AK8PFNOJECTrimHT.append( triggerInfo )
		elif '_TrimMass' in triggerInfo[0]:
			if 'HLT_PFTrimHT450_TrimMass' in triggerInfo[0]: PFTrimHT450.append( triggerInfo )
			elif 'HLT_PFTrimHT550_TrimMass' in triggerInfo[0]: PFTrimHT550.append( triggerInfo )
			elif 'HLT_PFTrimHT650_TrimMass' in triggerInfo[0]: PFTrimHT650.append( triggerInfo )
			elif 'HLT_PFTrimHT750_TrimMass' in triggerInfo[0]: PFTrimHT750.append( triggerInfo )
			elif 'HLT_PFTrimHT850_TrimMass' in triggerInfo[0]: PFTrimHT850.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT450_TrimMass' in triggerInfo[0]: AK8PFTrimHT450.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT550_TrimMass' in triggerInfo[0]: AK8PFTrimHT550.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT650_TrimMass' in triggerInfo[0]: AK8PFTrimHT650.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT650_HT700_TrimMass' in triggerInfo[0]: AK8PFTrimHT700.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT750_TrimMass' in triggerInfo[0]: AK8PFTrimHT750.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT650_HT800_TrimMass' in triggerInfo[0]: AK8PFTrimHT800.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT850_TrimMass' in triggerInfo[0]: AK8PFTrimHT850.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT650_HT900_TrimMass' in triggerInfo[0]: AK8PFTrimHT900.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT450_TrimMod_TrimMass' in triggerInfo[0]: AK8PFTrimHT450TrimMod.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT550_TrimMod_TrimMass' in triggerInfo[0]: AK8PFTrimHT550TrimMod.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT650_TrimMod_TrimMass' in triggerInfo[0]: AK8PFTrimHT650TrimMod.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT650_TrimMod_HT700_TrimMass' in triggerInfo[0]: AK8PFTrimHT700TrimMod.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT750_TrimMod_TrimMass' in triggerInfo[0]: AK8PFTrimHT750TrimMod.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT650_TrimMod_HT800_TrimMass' in triggerInfo[0]: AK8PFTrimHT800TrimMod.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT850_TrimMod_TrimMass' in triggerInfo[0]: AK8PFTrimHT850TrimMod.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT650_TrimMod_HT900_TrimMass' in triggerInfo[0]: AK8PFTrimHT900TrimMod.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT450_AK4CaloHT_TrimMass' in triggerInfo[0]: AK8PFTrimHT450AK4CaloHT.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT550_AK4CaloHT_TrimMass' in triggerInfo[0]: AK8PFTrimHT550AK4CaloHT.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT650_AK4CaloHT_TrimMass' in triggerInfo[0]: AK8PFTrimHT650AK4CaloHT.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT750_AK4CaloHT_TrimMass' in triggerInfo[0]: AK8PFTrimHT750AK4CaloHT.append( triggerInfo )
			elif 'HLT_AK8PFTrimHT850_AK4CaloHT_TrimMass' in triggerInfo[0]: AK8PFTrimHT850AK4CaloHT.append( triggerInfo )

	if 'simple' in process:
		for trigger in rates:
			if 'AK8PFJet360Trim_Mass30_v1' in trigger[0]: print 'AK8PFJet360Trim_Mass30', np.around(trigger[4], 2), np.around(trigger[5], 1)
			if 'AK8PFJet360Trim_Mass30_TrimMod_v1' in trigger[0]: print 'AK8PFJet360Trim_Mass30_TrimMod', np.around(trigger[4], 2), np.around(trigger[5], 1)
			if 'PFHT900_v1' in trigger[0]: print 'PFHT900', np.around(trigger[4], 2), np.around(trigger[5], 1)

		plotRates( [ PFHT ], [ 'PFHT' ], 'PFHTtriggers', PU )
		plotRates( [ PFHT, AK8PFHT, AK8PFNOJECTrimHT ], [ 'PFHT', 'AK8PFHT', 'AK8PFNOJECTrimHT' ],'newTriggers', PU )

		#CaloHTtrigger = [ 
		#		['AK8PFTrimHT450', array( 'd', listRates[268:273] ), array('d', listRatesErr[268:273] ) ],
		#		['AK8PFTrimHT850', array( 'd', listRates[273:278] ), array('d', listRatesErr[273:278] ) ]
		#		]
		#plotCaloJetRates( [ CaloHTtrigger[0] ] , 'AK8PFTrimHT450', PU )
		#plotCaloJetRates( [ CaloHTtrigger[1] ] , 'AK8PFTrimHT850', PU )

	elif '2d' in process:

		#HT = [ 450., 550., 650., 750., 850. ]
		HT = [ 700., 750., 800., 850., 900. ]
		Mass = [ 0., 5., 10., 15., 20., 25., 30., 35., 40., 45., 50., 55., 60., 65., 70., 75., 80., 85. ]
		Mass2 = [ 0., 5., 10., 15., 20., 25., 30., 35., 40., 45., 50., 55. ]

		#plotRatesComp( [ AK8PFTrimHT450, AK8PFTrimHT550, AK8PFTrimHT650, AK8PFTrimHT750, AK8PFTrimHT850 ], 'AK8PFTrimHT', PU, HT, Mass )
		plotRatesComp( [ AK8PFTrimHT700, AK8PFTrimHT750, AK8PFTrimHT800, AK8PFTrimHT850, AK8PFTrimHT900 ], 'AK8PFTrimHT', PU, HT, Mass )
		#plotRatesComp( [ AK8PFTrimHT450TrimMod, AK8PFTrimHT550TrimMod, AK8PFTrimHT650TrimMod, AK8PFTrimHT750TrimMod, AK8PFTrimHT850TrimMod ], 'AK8PFTrimHT_TrimMod', PU, HT, Mass )
		plotRatesComp( [ AK8PFTrimHT700TrimMod, AK8PFTrimHT750TrimMod, AK8PFTrimHT800TrimMod, AK8PFTrimHT850TrimMod, AK8PFTrimHT900TrimMod ], 'AK8PFTrimHT_TrimMod', PU, HT, Mass )
		#plotRatesComp( [ AK8PFTrimHT450AK4CaloHT, AK8PFTrimHT550AK4CaloHT, AK8PFTrimHT650AK4CaloHT, AK8PFTrimHT750AK4CaloHT, AK8PFTrimHT850AK4CaloHT ], 'AK8PFTrimHT_AK4CaloHT', PU, HT, Mass )
		#plotRatesComp( [ PFTrimHT450, PFTrimHT550, PFTrimHT650, PFTrimHT750, PFTrimHT850 ], 'PFTrimHT', PU, HT, Mass2 )

