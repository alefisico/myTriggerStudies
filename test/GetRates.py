#!/usr/bin/env python

import math,ROOT, sys
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

def grabTriggerNumbers( file, numTriggers, xs, PU ):

	txtFile = open( file )

	tmpList = []
	nameTrigger = []
	runTrigger = []
	passedTrigger = []
	failedTrigger = []

	with txtFile as fh:
		for line in fh:
			if 'TrigReport ---------- Path   Summary ------------' in line:
				for i in range(numTriggers+1):
					additionalData = next(fh)
					tmpList.append( additionalData.split() )

	for j in tmpList:
		nameTrigger.append( j[7] )
		runTrigger.append( j[3] )
		passedTrigger.append( j[4] )
		failedTrigger.append( j[5] )

	del nameTrigger[0]
	del runTrigger[0]
	del passedTrigger[0]
	del failedTrigger[0]
	run = map( float, runTrigger )
	passed = map( float, passedTrigger )
	failed = map( float, failedTrigger )
	
	rates, ratesErr = GetRates( run, passed, xs, PU )

	return nameTrigger, run, passed, failed, rates, ratesErr

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
		ilumi = 1.1e34
	collrate = (nfillb/mfillb)/xtime

	rateList = []
	rateErrList = []

	for i in range( len( passed ) ):
		#rateList.append( collrate * (1 - math.exp(-1* (xsec*ilumi*passed[i]/run[i])/collrate)) )
		rateList.append( xsec*ilumi*(passed[i]/run[i] ) )
		#rateErrList.append( xsec * ilumi * ((math.sqrt( passed[i] + (( passed[i])**2)/ run[i]))/ run[i]) )
		rateErrList.append( ( xsec * ilumi ) / run[i] * math.sqrt( passed[i] ) )

	return rateList, rateErrList

def plotRates( listRates, outName, PU ):
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
	for i in listRates: 
		dictGraphs[ i[0] ] = ROOT.TGraphErrors( len(t), t, i[1], tErr, i[2] )
		legend.AddEntry( dictGraphs[ i[0] ], i[0], 'l' )
		for j in i[1]: listMax.append( j )
		for k in xrange( len(i)+2 ):
			print i[0], np.around( i[1][k], 3), '\pm', np.around( i[2][k], 3 )
		print i[0], np.around( i[1], 3)

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
	c.SaveAs("TriggerRate_"+outName+'_'+PU+"_40k_120toInf.pdf")

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
	c.SaveAs("TriggerRate_"+outName+'_'+PU+"_CaloJet_test.pdf")

def plotRatesComp( listRates, outName, PU, HT, Mass ):
	"""docstring for plotRates"""

	histo = TH2F("xbox",'box', 7, 300., 1000., 14, -7.5, 62.5 )
	for i in xrange( len( HT ) ): 
		for k in xrange( len( Mass ) ):
			histo.Fill( HT[i], Mass[k], listRates[i][1][k] )
			print  HT[i], Mass[k], listRates[i][1][k] 
		#print i[0], np.around( i[1], 3)

	histo.SetTitle("Trigger Rates for "+outName+" "+PU)
	histo.GetXaxis().SetTitle("HT [GeV]")
	histo.GetYaxis().SetTitle("Leading Jet Mass [GeV]")


	c = TCanvas( "c1", "c1", 800, 500 )
	c.SetLogz()
	histo.Draw("colz")
	histo.Draw("texte same")
	setTriggerRatesComp( 'QCD 13TeV '+PU, outName )
	c.SaveAs("TriggerRate_"+outName+'_'+PU+".pdf")


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
	
	numTriggers = 278
	#PU = 'PU40bx50'
	#PU = 'PU20bx25'
	#PU = 'PU40bx25'
	PU = sys.argv[1]
	process = sys.argv[2]

	#name0, run0, passed0, failed0, rates0, ratesErr0 = grabTriggerNumbers( 'dump_QCD_Pt-30to50_'+PU+'_10k_Filt.log', numTriggers, 161500000., PU )
	name1, run1, passed1, failed1, rates1, ratesErr1 = grabTriggerNumbers( 'dump_QCD_Pt-50to80_'+PU+'_10k_Filt.log', numTriggers, 22110000., PU )
	name2, run2, passed2, failed2, rates2, ratesErr2 = grabTriggerNumbers( 'dump_QCD_Pt-80to120_'+PU+'_10k_Filt.log', numTriggers, 3000114.3, PU )
	name3, run3, passed3, failed3, rates3, ratesErr3 = grabTriggerNumbers( 'dump_QCD_Pt-120to170_'+PU+'_10k_Filt.log', numTriggers, 493200., PU )
	name4, run4, passed4, failed4, rates4, ratesErr4 = grabTriggerNumbers( 'dump_QCD_Pt-170to300_'+PU+'_10k_Filt.log', numTriggers, 120300., PU )
	name5, run5, passed5, failed5, rates5, ratesErr5 = grabTriggerNumbers( 'dump_QCD_Pt-300to470_'+PU+'_10k_Filt.log', numTriggers, 7475., PU )
	name6, run6, passed6, failed6, rates6, ratesErr6 = grabTriggerNumbers( 'dump_QCD_Pt-470to600_'+PU+'_10k_Filt.log', numTriggers, 587.1, PU  )
	name7, run7, passed7, failed7, rates7, ratesErr7 = grabTriggerNumbers( 'dump_QCD_Pt-600to800_'+PU+'_10k_Filt.log', numTriggers, 167., PU )
	name8, run8, passed8, failed8, rates8, ratesErr8 = grabTriggerNumbers( 'dump_QCD_Pt-800to1000_'+PU+'_10k_Filt.log', numTriggers, 28.25, PU  )
	name9, run9, passed9, failed9, rates9, ratesErr9 = grabTriggerNumbers( 'dump_QCD_Pt-1000to1400_'+PU+'_10k_Filt.log', numTriggers, 8.195, PU  )
	name10, run10, passed10, failed10, rates10, ratesErr10 = grabTriggerNumbers( 'dump_QCD_Pt-1400to1800_'+PU+'_10k_Filt.log', numTriggers, 0.7346, PU )

	if 'PU20bx25' in PU:
		name11, run11, passed11, failed11, rates11, ratesErr11 = grabTriggerNumbers( 'dump_QCD_Pt-1800_'+PU+'_10k_Filt.log', numTriggers, 0.1091 , PU )
		listRates = [ #rates0[i] + 
				rates1[i] + rates2[i] + rates3[i] + rates4[i] + rates5[i] + rates6[i] + rates7[i] + rates8[i] + rates9[i] + rates10[i] + rates11[i]
				for i in xrange( len( rates1 ) )]
		listRatesErr = [ #ratesErr0[i] + 
				ratesErr1[i] + ratesErr2[i] + ratesErr3[i] + ratesErr4[i] + ratesErr5[i] + ratesErr6[i] + ratesErr7[i] + ratesErr8[i] + ratesErr9[i] + ratesErr10[i] + ratesErr11[i] 
				for i in xrange( len( ratesErr1 ) )]
	else:
		listRates = [ #rates0[i] + 
				rates1[i] + rates2[i] + rates3[i] + rates4[i] + rates5[i] + rates6[i] + rates7[i] + rates8[i] + rates9[i] + rates10[i] 
				for i in xrange( len( rates1 ) )]
		listRatesErr = [ #ratesErr0[i] + 
				ratesErr1[i] + ratesErr2[i] + ratesErr3[i] + ratesErr4[i] + ratesErr5[i] + ratesErr6[i] + ratesErr7[i] + ratesErr8[i] + ratesErr9[i] + ratesErr10[i] 
				for i in xrange( len( ratesErr1 ) )]
	#print listRates
	#print listRatesErr

	if 'simple' in process:
		triggerList = [
				#['HT', array( 'd', listRates[1:6] ), array('d', listRatesErr[1:6] )],
				#['PFNoPUHT', array( 'd', listRates[5:10] ), array('d', listRatesErr[5:10] )],
				['PFHT', array( 'd', listRates[0:5] ), array('d', listRatesErr[0:5] )],
				['PFTrimHT', array( 'd', listRates[7:12] ), array('d', listRatesErr[7:12] )],
				['AK8PFHT', array( 'd', listRates[12:17] ), array('d', listRatesErr[12:17] )],
				['AK8PFTrimHT', array( 'd', listRates[17:22] ), array('d', listRatesErr[17:22] )],
				['AK8PFNOJECTrimHT', array( 'd', listRates[22:27] ), array('d', listRatesErr[22:27] )],
				]
		PFHTtrigger = [ ['PFHT', array( 'd', listRates[0:7] ), array('d', listRatesErr[0:7] ) ] ]
		print 'AK8PFJet360Trim_Mass30', listRates[27], listRatesErr[27]

		plotRates( [ PFHTtrigger[0] ] , 'PFHTtriggers', PU )
		plotRates( [ triggerList[0], triggerList[2] , triggerList[4] #, triggerList[4], triggerList[5]
			], 'newTriggers', PU )

		CaloHTtrigger = [ 
				['AK8PFTrimHT450', array( 'd', listRates[268:273] ), array('d', listRatesErr[268:273] ) ],
				['AK8PFTrimHT850', array( 'd', listRates[273:278] ), array('d', listRatesErr[273:278] ) ]
				]
		plotCaloJetRates( [ CaloHTtrigger[0] ] , 'AK8PFTrimHT450', PU )
		plotCaloJetRates( [ CaloHTtrigger[1] ] , 'AK8PFTrimHT850', PU )

	elif '2d' in process:


		AK8PFTrimHTList = [
			['AK8PFTrimHT450_TrimMass', array( 'd', listRates[28:40] ), array('d', listRatesErr[28:40])],
			['AK8PFTrimHT550_TrimMass', array( 'd', listRates[40:52] ), array('d', listRatesErr[40:52])],
			['AK8PFTrimHT650_TrimMass', array( 'd', listRates[52:64] ), array('d', listRatesErr[52:64])],
			['AK8PFTrimHT750_TrimMass', array( 'd', listRates[64:76] ), array('d', listRatesErr[64:76])],
			['AK8PFTrimHT850_TrimMass', array( 'd', listRates[76:88] ), array('d', listRatesErr[76:88])],
			]

		
		AK8PFTrimNOJECHTList = [
			['AK8PFNOJECTrimHT450_TrimMass', array( 'd', listRates[88:100] ), array('d', listRatesErr[88:100])],
			['AK8PFNOJECTrimHT550_TrimMass', array( 'd', listRates[100:112] ), array('d', listRatesErr[100:112])],
			['AK8PFNOJECTrimHT650_TrimMass', array( 'd', listRates[112:124] ), array('d', listRatesErr[112:124])],
			['AK8PFNOJECTrimHT750_TrimMass', array( 'd', listRates[124:136] ), array('d', listRatesErr[124:136])],
			['AK8PFNOJECTrimHT850_TrimMass', array( 'd', listRates[136:148] ), array('d', listRatesErr[136:148])],
			]

		PFTrimHTList = [
			['PFTrimHT450_TrimMass', array( 'd', listRates[148:160] ), array('d', listRatesErr[148:160])],
			['PFTrimHT550_TrimMass', array( 'd', listRates[160:172] ), array('d', listRatesErr[160:172])],
			['PFTrimHT650_TrimMass', array( 'd', listRates[172:184] ), array('d', listRatesErr[172:184])],
			['PFTrimHT750_TrimMass', array( 'd', listRates[184:196] ), array('d', listRatesErr[184:196])],
			['PFTrimHT850_TrimMass', array( 'd', listRates[196:208] ), array('d', listRatesErr[196:208])],
			]

		PFHTList = [
			['PFHT450_TrimMass', array( 'd', listRates[208:220] ), array('d', listRatesErr[208:220])],
			['PFHT550_TrimMass', array( 'd', listRates[220:232] ), array('d', listRatesErr[220:232])],
			['PFHT650_TrimMass', array( 'd', listRates[232:244] ), array('d', listRatesErr[232:244])],
			['PFHT750_TrimMass', array( 'd', listRates[244:256] ), array('d', listRatesErr[244:256])],
			['PFHT850_TrimMass', array( 'd', listRates[256:268] ), array('d', listRatesErr[256:268])],
			]

		HT = [ 450., 550., 650., 750., 850. ]
		Mass = [ 0., 5., 10., 15., 20., 25., 30., 35., 40., 45., 50., 55. ]

		plotRatesComp( AK8PFTrimHTList, 'AK8PFTrimHT', PU, HT, Mass )
		plotRatesComp( AK8PFTrimNOJECHTList, 'AK8PFNOJECTrimHT', PU, HT, Mass )
		plotRatesComp( PFTrimHTList, 'PFTrimHT', PU, HT, Mass )
		plotRatesComp( PFHTList, 'PFHT', PU, HT, Mass )


#		AK8PFTrimHT450List = [
##			['AK8PFTrimHT450_TrimPt40', array( 'd', AK8PFTrimHT450_TrimPt40), array('d', AK8PFTrimHT450_TrimPt40_Err )],
##			['AK8PFTrimHT450_TrimPt100', array( 'd', AK8PFTrimHT450_TrimPt100), array('d', AK8PFTrimHT450_TrimPt100_Err )],
##			['AK8PFTrimHT450_TrimPt200', array( 'd', AK8PFTrimHT450_TrimPt200), array('d', AK8PFTrimHT450_TrimPt200_Err )],
#			['AK8PFTrimHT450_TrimPt40', array( 'd', listRates[47:59]), array('d', listRatesErr[47:59] )],
#			['AK8PFTrimHT450_TrimPt100', array( 'd', listRates[59:71]), array('d', listRatesErr[59:71] )],
#			['AK8PFTrimHT450_TrimPt150', array( 'd', listRates[71:83]), array('d', listRatesErr[71:83] )],
#			['AK8PFTrimHT450_TrimPt200', array( 'd', listRates[83:95]), array('d', listRatesErr[83:95] )],
#			['AK8PFTrimHT450_TrimPt250', array( 'd', listRates[95:107]), array('d', listRatesErr[95:107] )],
#			]
#
#		plotRatesCompPtMass( AK8PFTrimHT450List, 'AK8PFTrimHT450_TrimMassPt', PU)
#
##		AK8PFTrimHT550_TrimPt40 = [ listRates[72], listRates[73], listRates[77], listRates[81], listRates[85], listRates[90] ]
##		AK8PFTrimHT550_TrimPt40_Err = [ listRatesErr[72], listRatesErr[73], listRatesErr[77], listRatesErr[81], listRatesErr[85], listRatesErr[90] ]
##		AK8PFTrimHT550_TrimPt100 = [ 0, listRates[74], listRates[78], listRates[82], listRates[86], listRates[92] ]
##		AK8PFTrimHT550_TrimPt100_Err = [ 0, listRatesErr[74], listRatesErr[78], listRatesErr[82], listRatesErr[86], listRatesErr[92] ]
##		AK8PFTrimHT550_TrimPt200 = [ 0, listRates[75], listRates[79], listRates[83], listRates[87], listRates[91] ]
##		AK8PFTrimHT550_TrimPt200_Err = [ 0, listRatesErr[75], listRatesErr[79], listRatesErr[83], listRatesErr[87], listRatesErr[91] ]
#
#		AK8PFTrimHT550List = [
##			['AK8PFTrimHT550_TrimPt40', array( 'd', AK8PFTrimHT550_TrimPt40), array('d', AK8PFTrimHT550_TrimPt40_Err )],
##			['AK8PFTrimHT550_TrimPt100', array( 'd', AK8PFTrimHT550_TrimPt100), array('d', AK8PFTrimHT550_TrimPt100_Err )],
##			['AK8PFTrimHT550_TrimPt200', array( 'd', AK8PFTrimHT550_TrimPt200), array('d', AK8PFTrimHT550_TrimPt200_Err )],
#			['AK8PFTrimHT550_TrimPt40', array( 'd', listRates[119:131]), array('d', listRatesErr[119:131] )],
#			['AK8PFTrimHT550_TrimPt100', array( 'd', listRates[131:143]), array('d', listRatesErr[131:143] )],
#			['AK8PFTrimHT550_TrimPt150', array( 'd', listRates[143:155]), array('d', listRatesErr[143:155] )],
#			['AK8PFTrimHT550_TrimPt200', array( 'd', listRates[155:167]), array('d', listRatesErr[155:167] )],
#			['AK8PFTrimHT550_TrimPt250', array( 'd', listRates[167:179]), array('d', listRatesErr[167:179] )],
#			]
#
#		plotRatesCompPtMass( AK8PFTrimHT550List, 'AK8PFTrimHT550_TrimMassPt', PU)
#
##		AK8PFTrimHT650_TrimPt40 = [ listRates[94], listRates[95], listRates[99], listRates[103], listRates[107], listRates[112] ]
##		AK8PFTrimHT650_TrimPt40_Err = [ listRatesErr[94], listRatesErr[95], listRatesErr[99], listRatesErr[103], listRatesErr[107], listRatesErr[112] ]
##		AK8PFTrimHT650_TrimPt100 = [ 0, listRates[96], listRates[100], listRates[104], listRates[108], listRates[114] ]
##		AK8PFTrimHT650_TrimPt100_Err = [ 0, listRatesErr[96], listRatesErr[100], listRatesErr[104], listRatesErr[108], listRatesErr[114] ]
##		AK8PFTrimHT650_TrimPt200 = [ 0, listRates[97], listRates[101], listRates[105], listRates[109], listRates[113] ]
##		AK8PFTrimHT650_TrimPt200_Err = [ 0, listRatesErr[97], listRatesErr[101], listRatesErr[105], listRatesErr[109], listRatesErr[113] ]
#
#		AK8PFTrimHT650List = [
##			['AK8PFTrimHT650_TrimPt40', array( 'd', AK8PFTrimHT650_TrimPt40), array('d', AK8PFTrimHT650_TrimPt40_Err )],
##			['AK8PFTrimHT650_TrimPt100', array( 'd', AK8PFTrimHT650_TrimPt100), array('d', AK8PFTrimHT650_TrimPt100_Err )],
##			['AK8PFTrimHT650_TrimPt200', array( 'd', AK8PFTrimHT650_TrimPt200), array('d', AK8PFTrimHT650_TrimPt200_Err )],
#			['AK8PFTrimHT650_TrimPt40', array( 'd', listRates[191:203]), array('d', listRatesErr[191:203] )],
#			['AK8PFTrimHT650_TrimPt100', array( 'd', listRates[203:215]), array('d', listRatesErr[203:215] )],
#			['AK8PFTrimHT650_TrimPt150', array( 'd', listRates[215:227]), array('d', listRatesErr[215:227] )],
#			['AK8PFTrimHT650_TrimPt200', array( 'd', listRates[227:239]), array('d', listRatesErr[227:239] )],
#			['AK8PFTrimHT650_TrimPt250', array( 'd', listRates[239:251]), array('d', listRatesErr[239:251] )],
#			]
#
#		plotRatesCompPtMass( AK8PFTrimHT650List, 'AK8PFTrimHT650_TrimMassPt', PU)
#
##		AK8PFTrimHT750_TrimPt40 = [ listRates[116], listRates[117], listRates[121], listRates[125], listRates[129], listRates[134] ]
##		AK8PFTrimHT750_TrimPt40_Err = [ listRatesErr[116], listRatesErr[117], listRatesErr[121], listRatesErr[125], listRatesErr[129], listRatesErr[134] ]
##		AK8PFTrimHT750_TrimPt100 = [ 0, listRates[118], listRates[122], listRates[126], listRates[130], listRates[134] ]
##		AK8PFTrimHT750_TrimPt100_Err = [ 0, listRatesErr[118], listRatesErr[122], listRatesErr[126], listRatesErr[130], listRatesErr[134] ]
##		AK8PFTrimHT750_TrimPt200 = [ 0, listRates[119], listRates[123], listRates[127], listRates[131], listRates[133] ]
##		AK8PFTrimHT750_TrimPt200_Err = [ 0, listRatesErr[119], listRatesErr[123], listRatesErr[127], listRatesErr[131], listRatesErr[133] ]
#
#		AK8PFTrimHT750List = [
##			['AK8PFTrimHT750_TrimPt40', array( 'd', AK8PFTrimHT750_TrimPt40), array('d', AK8PFTrimHT750_TrimPt40_Err )],
##			['AK8PFTrimHT750_TrimPt100', array( 'd', AK8PFTrimHT750_TrimPt100), array('d', AK8PFTrimHT750_TrimPt100_Err )],
##			['AK8PFTrimHT750_TrimPt200', array( 'd', AK8PFTrimHT750_TrimPt200), array('d', AK8PFTrimHT750_TrimPt200_Err )],
#			['AK8PFTrimHT750_TrimPt40', array( 'd', listRates[263:275]), array('d', listRatesErr[263:275] )],
#			['AK8PFTrimHT750_TrimPt100', array( 'd', listRates[275:287]), array('d', listRatesErr[275:287] )],
#			['AK8PFTrimHT750_TrimPt150', array( 'd', listRates[287:299]), array('d', listRatesErr[287:299] )],
#			['AK8PFTrimHT750_TrimPt200', array( 'd', listRates[299:311]), array('d', listRatesErr[299:311] )],
#			['AK8PFTrimHT750_TrimPt250', array( 'd', listRates[311:323]), array('d', listRatesErr[311:323] )],
#			]
#
#		plotRatesCompPtMass( AK8PFTrimHT750List, 'AK8PFTrimHT750_TrimMassPt', PU)
#
##		AK8PFTrimHT850_TrimPt40 = [ listRates[138], listRates[139], listRates[143], listRates[147], listRates[151], listRates[156] ]
##		AK8PFTrimHT850_TrimPt40_Err = [ listRatesErr[138], listRatesErr[139], listRatesErr[143], listRatesErr[147], listRatesErr[151], listRatesErr[156] ]
##		AK8PFTrimHT850_TrimPt100 = [ 0, listRates[140], listRates[144], listRates[148], listRates[152], listRates[158] ]
##		AK8PFTrimHT850_TrimPt100_Err = [ 0, listRatesErr[140], listRatesErr[144], listRatesErr[148], listRatesErr[152], listRatesErr[158] ]
##		AK8PFTrimHT850_TrimPt200 = [ 0, listRates[141], listRates[145], listRates[149], listRates[153], listRates[157] ]
##		AK8PFTrimHT850_TrimPt200_Err = [ 0, listRatesErr[141], listRatesErr[145], listRatesErr[149], listRatesErr[153], listRatesErr[157] ]
#
#		AK8PFTrimHT850List = [
##			['AK8PFTrimHT850_TrimPt40', array( 'd', AK8PFTrimHT850_TrimPt40), array('d', AK8PFTrimHT850_TrimPt40_Err )],
##			['AK8PFTrimHT850_TrimPt100', array( 'd', AK8PFTrimHT850_TrimPt100), array('d', AK8PFTrimHT850_TrimPt100_Err )],
##			['AK8PFTrimHT850_TrimPt200', array( 'd', AK8PFTrimHT850_TrimPt200), array('d', AK8PFTrimHT850_TrimPt200_Err )],
#			['AK8PFTrimHT850_TrimPt40', array( 'd', listRates[335:347]), array('d', listRatesErr[335:347] )],
#			['AK8PFTrimHT850_TrimPt100', array( 'd', listRates[347:359]), array('d', listRatesErr[347:359] )],
#			['AK8PFTrimHT850_TrimPt150', array( 'd', listRates[359:371]), array('d', listRatesErr[359:371] )],
#			['AK8PFTrimHT850_TrimPt200', array( 'd', listRates[371:383]), array('d', listRatesErr[371:383] )],
#			['AK8PFTrimHT850_TrimPt250', array( 'd', listRates[383:395]), array('d', listRatesErr[383:395] )],
#			]
#
#		plotRatesCompPtMass( AK8PFTrimHT850List, 'AK8PFTrimHT850_TrimMassPt', PU)
#
#		AK8PFNOJECTrimHT450List = [
#			['AK8PFNOJECTrimHT450_TrimPt40', array( 'd', listRates[407:419]), array('d', listRatesErr[407:419] )],
#			['AK8PFNOJECTrimHT450_TrimPt100', array( 'd', listRates[419:431]), array('d', listRatesErr[419:431] )],
#			['AK8PFNOJECTrimHT450_TrimPt150', array( 'd', listRates[431:443]), array('d', listRatesErr[431:443] )],
#			['AK8PFNOJECTrimHT450_TrimPt200', array( 'd', listRates[443:455]), array('d', listRatesErr[443:455] )],
#			['AK8PFNOJECTrimHT450_TrimPt250', array( 'd', listRates[455:467]), array('d', listRatesErr[455:467] )],
#			]
#
#		plotRatesCompPtMass( AK8PFNOJECTrimHT450List, 'AK8PFNOJECTrimHT450_TrimMassPt', PU)
#
#		AK8PFNOJECTrimHT550List = [
#			['AK8PFNOJECTrimHT550_TrimPt40', array( 'd', listRates[479:491]), array('d', listRatesErr[479:491] )],
#			['AK8PFNOJECTrimHT550_TrimPt100', array( 'd', listRates[491:503]), array('d', listRatesErr[491:503] )],
#			['AK8PFNOJECTrimHT550_TrimPt150', array( 'd', listRates[503:515]), array('d', listRatesErr[503:515] )],
#			['AK8PFNOJECTrimHT550_TrimPt200', array( 'd', listRates[515:527]), array('d', listRatesErr[515:527] )],
#			['AK8PFNOJECTrimHT550_TrimPt250', array( 'd', listRates[527:539]), array('d', listRatesErr[527:539] )],
#			]
#
#		plotRatesCompPtMass( AK8PFNOJECTrimHT550List, 'AK8PFNOJECTrimHT550_TrimMassPt', PU)
#
#
#		AK8PFNOJECTrimHT650List = [
#			['AK8PFNOJECTrimHT650_TrimPt40', array( 'd', listRates[551:563]), array('d', listRatesErr[551:563] )],
#			['AK8PFNOJECTrimHT650_TrimPt100', array( 'd', listRates[563:575]), array('d', listRatesErr[563:575] )],
#			['AK8PFNOJECTrimHT650_TrimPt150', array( 'd', listRates[575:587]), array('d', listRatesErr[575:587] )],
#			['AK8PFNOJECTrimHT650_TrimPt200', array( 'd', listRates[587:599]), array('d', listRatesErr[587:599] )],
#			['AK8PFNOJECTrimHT650_TrimPt250', array( 'd', listRates[599:611]), array('d', listRatesErr[599:611] )],
#			]
#
#		plotRatesCompPtMass( AK8PFNOJECTrimHT650List, 'AK8PFNOJECTrimHT650_TrimMassPt', PU)
#
#
#		AK8PFNOJECTrimHT750List = [
#			['AK8PFNOJECTrimHT750_TrimPt40', array( 'd', listRates[623:635]), array('d', listRatesErr[623:635] )],
#			['AK8PFNOJECTrimHT750_TrimPt100', array( 'd', listRates[635:647]), array('d', listRatesErr[635:647] )],
#			['AK8PFNOJECTrimHT750_TrimPt150', array( 'd', listRates[647:659]), array('d', listRatesErr[647:659] )],
#			['AK8PFNOJECTrimHT750_TrimPt200', array( 'd', listRates[659:671]), array('d', listRatesErr[659:671] )],
#			['AK8PFNOJECTrimHT750_TrimPt250', array( 'd', listRates[671:683]), array('d', listRatesErr[671:683] )],
#			]
#
#		plotRatesCompPtMass( AK8PFNOJECTrimHT750List, 'AK8PFNOJECTrimHT750_TrimMassPt', PU)
#
#		AK8PFNOJECTrimHT850List = [
#			['AK8PFNOJECTrimHT850_TrimPt40', array( 'd', listRates[695:707]), array('d', listRatesErr[695:707] )],
#			['AK8PFNOJECTrimHT850_TrimPt100', array( 'd', listRates[707:719]), array('d', listRatesErr[707:719] )],
#			['AK8PFNOJECTrimHT850_TrimPt150', array( 'd', listRates[719:731]), array('d', listRatesErr[719:731] )],
#			['AK8PFNOJECTrimHT850_TrimPt200', array( 'd', listRates[731:743]), array('d', listRatesErr[731:743] )],
#			['AK8PFNOJECTrimHT850_TrimPt250', array( 'd', listRates[743:755]), array('d', listRatesErr[743:755] )],
#			]
#
#		plotRatesCompPtMass( AK8PFNOJECTrimHT850List, 'AK8PFNOJECTrimHT850_TrimMassPt', PU)
#
#
#		PFTrimHT450List = [
#			['PFTrimHT450_TrimPt40', array( 'd', listRates[767:779]), array('d', listRatesErr[767:779] )],
#			['PFTrimHT450_TrimPt100', array( 'd', listRates[779:791]), array('d', listRatesErr[779:791] )],
#			['PFTrimHT450_TrimPt150', array( 'd', listRates[791:803]), array('d', listRatesErr[791:803] )],
#			['PFTrimHT450_TrimPt200', array( 'd', listRates[803:815]), array('d', listRatesErr[803:815] )],
#			['PFTrimHT450_TrimPt250', array( 'd', listRates[815:827]), array('d', listRatesErr[815:827] )],
#			]
#
#		plotRatesCompPtMass( PFTrimHT450List, 'PFTrimHT450_TrimMassPt', PU)
#
#		PFTrimHT550List = [
#			['PFTrimHT550_TrimPt40', array( 'd', listRates[839:851]), array('d', listRatesErr[839:851] )],
#			['PFTrimHT550_TrimPt100', array( 'd', listRates[851:863]), array('d', listRatesErr[851:863] )],
#			['PFTrimHT550_TrimPt150', array( 'd', listRates[863:875]), array('d', listRatesErr[863:875] )],
#			['PFTrimHT550_TrimPt200', array( 'd', listRates[875:887]), array('d', listRatesErr[875:887] )],
#			['PFTrimHT550_TrimPt250', array( 'd', listRates[887:899]), array('d', listRatesErr[887:899] )],
#			]
#
#		plotRatesCompPtMass( PFTrimHT550List, 'PFTrimHT550_TrimMassPt', PU)
#
#
#		PFTrimHT650List = [
#			['PFTrimHT650_TrimPt40', array( 'd', listRates[911:923]), array('d', listRatesErr[911:923] )],
#			['PFTrimHT650_TrimPt100', array( 'd', listRates[923:935]), array('d', listRatesErr[923:935] )],
#			['PFTrimHT650_TrimPt150', array( 'd', listRates[935:947]), array('d', listRatesErr[935:947] )],
#			['PFTrimHT650_TrimPt200', array( 'd', listRates[947:959]), array('d', listRatesErr[947:959] )],
#			['PFTrimHT650_TrimPt250', array( 'd', listRates[959:971]), array('d', listRatesErr[959:971] )],
#			]
#
#		plotRatesCompPtMass( PFTrimHT650List, 'PFTrimHT650_TrimMassPt', PU)
#
#
#		PFTrimHT750List = [
#			['PFTrimHT750_TrimPt40', array( 'd', listRates[983:995]), array('d', listRatesErr[983:995] )],
#			['PFTrimHT750_TrimPt100', array( 'd', listRates[995:1007]), array('d', listRatesErr[995:1007] )],
#			['PFTrimHT750_TrimPt150', array( 'd', listRates[1007:1019]), array('d', listRatesErr[1007:1019] )],
#			['PFTrimHT750_TrimPt200', array( 'd', listRates[1019:1031]), array('d', listRatesErr[1019:1031] )],
#			['PFTrimHT750_TrimPt250', array( 'd', listRates[1031:1043]), array('d', listRatesErr[1031:1043] )],
#			]
#
#		plotRatesCompPtMass( PFTrimHT750List, 'PFTrimHT750_TrimMassPt', PU)
#
#		PFTrimHT850List = [
#			['PFTrimHT850_TrimPt40', array( 'd', listRates[1055:1067]), array('d', listRatesErr[1055:1067] )],
#			['PFTrimHT850_TrimPt100', array( 'd', listRates[1067:1079]), array('d', listRatesErr[1067:1079] )],
#			['PFTrimHT850_TrimPt150', array( 'd', listRates[1079:1091]), array('d', listRatesErr[1079:1091] )],
#			['PFTrimHT850_TrimPt200', array( 'd', listRates[1091:1103]), array('d', listRatesErr[1091:1103] )],
#			['PFTrimHT850_TrimPt250', array( 'd', listRates[1103:1115]), array('d', listRatesErr[1103:1115] )],
#			]
#
#		plotRatesCompPtMass( PFTrimHT850List, 'PFTrimHT850_TrimMassPt', PU)
