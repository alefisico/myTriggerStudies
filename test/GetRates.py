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
	HTErr = [ 0., 0., 0., 0., 0. ]
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
		#print i[0], np.around( i[1], 3)

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
	c.SaveAs("TriggerRate_"+outName+'_'+PU+".pdf")


def plotRatesComp( listRates, outName, PU, HT, Mass ):
	"""docstring for plotRates"""

	histo = TH2F("xbox",'box', 7, 350., 1050., 13, 0., 65. )
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

	Pt = [ 40., 100., 200. ]
	Mass = [ 0., 10., 20., 30., 40., 50. ]

	ptBin = array('f', [ 0., 40., 100., 200., 300., 350. ] )
	massBin = array( 'f', [ 0., 10., 20., 30., 40., 50., 60., 70. ])
	histo = TH2F("xbox",'box', 5, ptBin, 7, massBin )
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
	histo.Draw("box same")
	histo.Draw("texte same")
	setTriggerRatesComp( 'QCD 13TeV '+PU, outName )
	c.SaveAs("TriggerRate_"+outName+'_'+PU+".pdf")



if __name__ == '__main__':
	
	numTriggers = 270
	#PU = 'PU40bx50'
	#PU = 'PU20bx25'
	#PU = 'PU40bx25'
	PU = sys.argv[1]
	process = sys.argv[2]

	name0, run0, passed0, failed0, rates0, ratesErr0 = grabTriggerNumbers( 'dump_QCD_Pt-30to50_'+PU+'_5k_Filt.log', numTriggers, 161500000., PU )
	name1, run1, passed1, failed1, rates1, ratesErr1 = grabTriggerNumbers( 'dump_QCD_Pt-50to80_'+PU+'_5k_Filt.log', numTriggers, 22110000., PU )
	name2, run2, passed2, failed2, rates2, ratesErr2 = grabTriggerNumbers( 'dump_QCD_Pt-80to120_'+PU+'_5k_Filt.log', numTriggers, 3000114.3, PU )
	name3, run3, passed3, failed3, rates3, ratesErr3 = grabTriggerNumbers( 'dump_QCD_Pt-120to170_'+PU+'_5k_Filt.log', numTriggers, 493200., PU )
	name4, run4, passed4, failed4, rates4, ratesErr4 = grabTriggerNumbers( 'dump_QCD_Pt-170to300_'+PU+'_5k_Filt.log', numTriggers, 120300., PU )
	name5, run5, passed5, failed5, rates5, ratesErr5 = grabTriggerNumbers( 'dump_QCD_Pt-300to470_'+PU+'_5k_Filt.log', numTriggers, 7475., PU )
	name6, run6, passed6, failed6, rates6, ratesErr6 = grabTriggerNumbers( 'dump_QCD_Pt-470to600_'+PU+'_5k_Filt.log', numTriggers, 587.1, PU  )
	name7, run7, passed7, failed7, rates7, ratesErr7 = grabTriggerNumbers( 'dump_QCD_Pt-600to800_'+PU+'_5k_Filt.log', numTriggers, 167., PU )
	name8, run8, passed8, failed8, rates8, ratesErr8 = grabTriggerNumbers( 'dump_QCD_Pt-800to1000_'+PU+'_5k_Filt.log', numTriggers, 28.25, PU  )
	name9, run9, passed9, failed9, rates9, ratesErr9 = grabTriggerNumbers( 'dump_QCD_Pt-1000to1400_'+PU+'_5k_Filt.log', numTriggers, 8.195, PU  )
	name10, run10, passed10, failed10, rates10, ratesErr10 = grabTriggerNumbers( 'dump_QCD_Pt-1400to1800_'+PU+'_5k_Filt.log', numTriggers, 0.7346, PU )

	if 'PU20bx25' in PU:
		name11, run11, passed11, failed11, rates11, ratesErr11 = grabTriggerNumbers( 'dump_QCD_Pt-1800_'+PU+'_5k_Filt.log', numTriggers, 0.1091 , PU )
		listRates = [ #rates0[i] + rates1[i] + rates2[i] + 
				rates3[i] + rates4[i] + rates5[i] + rates6[i] + rates7[i] + rates8[i] + rates9[i] + rates10[i] + rates11[i]
				for i in xrange( len( rates1 ) )]
		listRatesErr = [ #ratesErr0[i] + ratesErr1[i] + ratesErr2[i] + 
				ratesErr3[i] + ratesErr4[i] + ratesErr5[i] + ratesErr6[i] + ratesErr7[i] + ratesErr8[i] + ratesErr9[i] + ratesErr10[i] + ratesErr11[i] 
				for i in xrange( len( ratesErr1 ) )]
	else:
		listRates = [ rates0[i] + rates1[i] + rates2[i] + rates3[i] + rates4[i] + rates5[i] + rates6[i] + rates7[i] + rates8[i] + rates9[i] + rates10[i] for i in xrange( len( rates1 ) )]
		listRatesErr = [ ratesErr0[i] +ratesErr1[i] + ratesErr2[i] + ratesErr3[i] + ratesErr4[i] + ratesErr5[i] + ratesErr6[i] + ratesErr7[i] + ratesErr8[i] + ratesErr9[i] + ratesErr10[i] for i in xrange( len( ratesErr1 ) )]
	#print listRates
	#print listRatesErr

	if 'simple' in process:
		triggerList = [
				['HT', array( 'd', listRates[0:5] ), array('d', listRatesErr[0:5] )],
				['PFNoPUHT', array( 'd', listRates[5:10] ), array('d', listRatesErr[5:10] )],
				['PFHT', array( 'd', listRates[10:15] ), array('d', listRatesErr[10:15] )],
				['PFHTTrim', array( 'd', listRates[15:20] ), array('d', listRatesErr[15:20] )],
				['PFTrimHT', array( 'd', listRates[20:25] ), array('d', listRatesErr[20:25] )],
				['AK8PFHT', array( 'd', listRates[25:30] ), array('d', listRatesErr[25:30] )],
				['AK8PFTrimHT', array( 'd', listRates[30:35] ), array('d', listRatesErr[30:35] )],
				['AK8PFHTTrim', array( 'd', listRates[35:40] ), array('d', listRatesErr[35:40] )],
				['AK8PFNOJECHTTrim', array( 'd', listRates[40:45] ), array('d', listRatesErr[40:45] )],
				['AK8PFNOJECTrimHT', array( 'd', listRates[45:50] ), array('d', listRatesErr[45:50] )],
				]

		plotRates( [ triggerList[0], triggerList[1], triggerList[2] ], 'oldTriggers', PU )
		plotRates( [ triggerList[2], triggerList[3] , triggerList[4], triggerList[5], triggerList[6], triggerList[7], triggerList[8], triggerList[9] 
			], 'newTriggers', PU )

	elif '2d' in process:

		AK8PFTrimHT450_TrimMass = [ listRates[50], listRates[66], listRates[51], listRates[54], listRates[55], listRates[58], listRates[59], listRates[62], listRates[63], listRates[67], listRates[68], listRates[71] ]
		AK8PFTrimHT450_TrimMass_Err = [ listRatesErr[50], listRatesErr[66], listRatesErr[51], listRatesErr[54], listRatesErr[55], listRatesErr[58], listRatesErr[59], listRatesErr[62], listRatesErr[63], listRatesErr[67], listRatesErr[68], listRatesErr[71] ]
		AK8PFTrimHT550_TrimMass = [ listRates[72], listRates[88], listRates[73], listRates[76], listRates[77], listRates[80], listRates[81], listRates[84], listRates[85], listRates[89], listRates[90], listRates[93] ]
		AK8PFTrimHT550_TrimMass_Err = [ listRatesErr[72], listRatesErr[88], listRatesErr[73], listRatesErr[76], listRatesErr[77], listRatesErr[80], listRatesErr[81], listRatesErr[84], listRatesErr[85], listRatesErr[89], listRatesErr[90], listRatesErr[93] ]
		AK8PFTrimHT650_TrimMass = [ listRates[94], listRates[110], listRates[95], listRates[98], listRates[99], listRates[102], listRates[103], listRates[106], listRates[107], listRates[111], listRates[112], listRates[115] ]
		AK8PFTrimHT650_TrimMass_Err = [ listRatesErr[94], listRatesErr[110], listRatesErr[95], listRatesErr[98], listRatesErr[99], listRatesErr[102], listRatesErr[103], listRatesErr[106], listRatesErr[107], listRatesErr[111], listRatesErr[112], listRatesErr[115] ]
		AK8PFTrimHT750_TrimMass = [ listRates[116], listRates[132], listRates[117], listRates[120], listRates[121], listRates[124], listRates[125], listRates[128], listRates[129], listRates[133], listRates[134], listRates[137] ]
		AK8PFTrimHT750_TrimMass_Err = [ listRatesErr[116], listRatesErr[132], listRatesErr[117], listRatesErr[120], listRatesErr[121], listRatesErr[124], listRatesErr[125], listRatesErr[128], listRatesErr[129], listRatesErr[133], listRatesErr[134], listRatesErr[137] ]
		AK8PFTrimHT850_TrimMass = [ listRates[138], listRates[154], listRates[139], listRates[142], listRates[143], listRates[146], listRates[147], listRates[150], listRates[151], listRates[155], listRates[156], listRates[159] ]
		AK8PFTrimHT850_TrimMass_Err = [ listRatesErr[138], listRatesErr[154], listRatesErr[139], listRatesErr[142], listRatesErr[143], listRatesErr[146], listRatesErr[147], listRatesErr[150], listRatesErr[151], listRatesErr[155], listRatesErr[156], listRatesErr[159] ]


		AK8PFTrimHTList = [
			['AK8PFTrimHT450_TrimMass', array( 'd', AK8PFTrimHT450_TrimMass ), array('d', AK8PFTrimHT450_TrimMass_Err )],
			['AK8PFTrimHT550_TrimMass', array( 'd', AK8PFTrimHT550_TrimMass ), array('d', AK8PFTrimHT550_TrimMass_Err )],
			['AK8PFTrimHT650_TrimMass', array( 'd', AK8PFTrimHT650_TrimMass ), array('d', AK8PFTrimHT650_TrimMass_Err )],
			['AK8PFTrimHT750_TrimMass', array( 'd', AK8PFTrimHT750_TrimMass ), array('d', AK8PFTrimHT750_TrimMass_Err )],
			['AK8PFTrimHT850_TrimMass', array( 'd', AK8PFTrimHT850_TrimMass ), array('d', AK8PFTrimHT850_TrimMass_Err )],
			]

		
		AK8PFNOJECTrimHT450_TrimMass = [ listRates[160], listRates[176], listRates[161], listRates[164], listRates[165], listRates[168], listRates[169], listRates[172], listRates[173], listRates[177], listRates[178], listRates[181] ]
		AK8PFNOJECTrimHT450_TrimMass_Err = [ listRatesErr[160], listRatesErr[176], listRatesErr[161], listRatesErr[164], listRatesErr[165], listRatesErr[168], listRatesErr[169], listRatesErr[172], listRatesErr[173], listRatesErr[177], listRatesErr[178], listRatesErr[181] ]
		AK8PFNOJECTrimHT550_TrimMass = [ listRates[182], listRates[198], listRates[183], listRates[186], listRates[187], listRates[190], listRates[191], listRates[194], listRates[195], listRates[199], listRates[200], listRates[203] ]
		AK8PFNOJECTrimHT550_TrimMass_Err = [ listRatesErr[182], listRatesErr[198], listRatesErr[183], listRatesErr[186], listRatesErr[187], listRatesErr[190], listRatesErr[191], listRatesErr[194], listRatesErr[195], listRatesErr[199], listRatesErr[200], listRatesErr[203] ]
		AK8PFNOJECTrimHT650_TrimMass = [ listRates[204], listRates[220], listRates[205], listRates[208], listRates[209], listRates[212], listRates[213], listRates[216], listRates[217], listRates[221], listRates[222], listRates[225] ]
		AK8PFNOJECTrimHT650_TrimMass_Err = [ listRatesErr[204], listRatesErr[220], listRatesErr[205], listRatesErr[208], listRatesErr[209], listRatesErr[212], listRatesErr[213], listRatesErr[216], listRatesErr[217], listRatesErr[221], listRatesErr[222], listRatesErr[225] ]
		AK8PFNOJECTrimHT750_TrimMass = [ listRates[226], listRates[242], listRates[227], listRates[230], listRates[231], listRates[234], listRates[235], listRates[238], listRates[239], listRates[243], listRates[244], listRates[247] ]
		AK8PFNOJECTrimHT750_TrimMass_Err = [ listRatesErr[226], listRatesErr[242], listRatesErr[227], listRatesErr[230], listRatesErr[231], listRatesErr[234], listRatesErr[235], listRatesErr[238], listRatesErr[239], listRatesErr[243], listRatesErr[244], listRatesErr[247] ]
		AK8PFNOJECTrimHT850_TrimMass = [ listRates[248], listRates[264], listRates[249], listRates[252], listRates[253], listRates[256], listRates[257], listRates[260], listRates[261], listRates[265], listRates[266], listRates[269] ]
		AK8PFNOJECTrimHT850_TrimMass_Err = [ listRatesErr[248], listRatesErr[264], listRatesErr[249], listRatesErr[252], listRatesErr[253], listRatesErr[256], listRatesErr[257], listRatesErr[260], listRatesErr[261], listRatesErr[265], listRatesErr[266], listRatesErr[269] ]

		AK8PFTrimNOJECHTList = [
			['AK8PFNOJECTrimHT450_TrimMass', array( 'd', AK8PFNOJECTrimHT450_TrimMass ), array('d', AK8PFNOJECTrimHT450_TrimMass_Err )],
			['AK8PFNOJECTrimHT550_TrimMass', array( 'd', AK8PFNOJECTrimHT550_TrimMass ), array('d', AK8PFNOJECTrimHT550_TrimMass_Err )],
			['AK8PFNOJECTrimHT650_TrimMass', array( 'd', AK8PFNOJECTrimHT650_TrimMass ), array('d', AK8PFNOJECTrimHT650_TrimMass_Err )],
			['AK8PFNOJECTrimHT750_TrimMass', array( 'd', AK8PFNOJECTrimHT750_TrimMass ), array('d', AK8PFNOJECTrimHT750_TrimMass_Err )],
			['AK8PFNOJECTrimHT850_TrimMass', array( 'd', AK8PFNOJECTrimHT850_TrimMass ), array('d', AK8PFNOJECTrimHT850_TrimMass_Err )],
			]

		HT = [ 450., 550., 650., 750., 850. ]
		Mass = [ 0., 5., 10., 15., 20., 25., 30., 35., 40., 45., 50., 55. ]

		plotRatesComp( AK8PFTrimHTList, 'AK8PFTrimHT', PU, HT, Mass )
		plotRatesComp( AK8PFTrimNOJECHTList, 'AK8PFNOJECTrimHT', PU, HT, Mass )

		AK8PFTrimHT450_TrimPt40 = [ listRates[50], listRates[51], listRates[55], listRates[59], listRates[63], listRates[68] ]
		AK8PFTrimHT450_TrimPt40_Err = [ listRatesErr[50], listRatesErr[51], listRatesErr[55], listRatesErr[59], listRatesErr[63], listRatesErr[68] ]
		AK8PFTrimHT450_TrimPt100 = [ 0, listRates[52], listRates[56], listRates[60], listRates[64], listRates[70] ]
		AK8PFTrimHT450_TrimPt100_Err = [ 0, listRatesErr[52], listRatesErr[56], listRatesErr[60], listRatesErr[64], listRatesErr[70] ]
		AK8PFTrimHT450_TrimPt200 = [ 0, listRates[53], listRates[57], listRates[61], listRates[65], listRates[69] ]
		AK8PFTrimHT450_TrimPt200_Err = [ 0, listRatesErr[53], listRatesErr[57], listRatesErr[61], listRatesErr[65], listRatesErr[69] ]

		AK8PFTrimHT450List = [
			['AK8PFTrimHT450_TrimPt40', array( 'd', AK8PFTrimHT450_TrimPt40), array('d', AK8PFTrimHT450_TrimPt40_Err )],
			['AK8PFTrimHT450_TrimPt100', array( 'd', AK8PFTrimHT450_TrimPt100), array('d', AK8PFTrimHT450_TrimPt100_Err )],
			['AK8PFTrimHT450_TrimPt200', array( 'd', AK8PFTrimHT450_TrimPt200), array('d', AK8PFTrimHT450_TrimPt200_Err )],
			]

		plotRatesCompPtMass( AK8PFTrimHT450List, 'AK8PFTrimHT450_TrimMassPt', PU)

		AK8PFTrimHT550_TrimPt40 = [ listRates[72], listRates[73], listRates[77], listRates[81], listRates[85], listRates[90] ]
		AK8PFTrimHT550_TrimPt40_Err = [ listRatesErr[72], listRatesErr[73], listRatesErr[77], listRatesErr[81], listRatesErr[85], listRatesErr[90] ]
		AK8PFTrimHT550_TrimPt100 = [ 0, listRates[74], listRates[78], listRates[82], listRates[86], listRates[92] ]
		AK8PFTrimHT550_TrimPt100_Err = [ 0, listRatesErr[74], listRatesErr[78], listRatesErr[82], listRatesErr[86], listRatesErr[92] ]
		AK8PFTrimHT550_TrimPt200 = [ 0, listRates[75], listRates[79], listRates[83], listRates[87], listRates[91] ]
		AK8PFTrimHT550_TrimPt200_Err = [ 0, listRatesErr[75], listRatesErr[79], listRatesErr[83], listRatesErr[87], listRatesErr[91] ]

		AK8PFTrimHT550List = [
			['AK8PFTrimHT550_TrimPt40', array( 'd', AK8PFTrimHT550_TrimPt40), array('d', AK8PFTrimHT550_TrimPt40_Err )],
			['AK8PFTrimHT550_TrimPt100', array( 'd', AK8PFTrimHT550_TrimPt100), array('d', AK8PFTrimHT550_TrimPt100_Err )],
			['AK8PFTrimHT550_TrimPt200', array( 'd', AK8PFTrimHT550_TrimPt200), array('d', AK8PFTrimHT550_TrimPt200_Err )],
			]

		plotRatesCompPtMass( AK8PFTrimHT550List, 'AK8PFTrimHT550_TrimMassPt', PU)

		AK8PFTrimHT650_TrimPt40 = [ listRates[94], listRates[95], listRates[99], listRates[103], listRates[107], listRates[112] ]
		AK8PFTrimHT650_TrimPt40_Err = [ listRatesErr[94], listRatesErr[95], listRatesErr[99], listRatesErr[103], listRatesErr[107], listRatesErr[112] ]
		AK8PFTrimHT650_TrimPt100 = [ 0, listRates[96], listRates[100], listRates[104], listRates[108], listRates[114] ]
		AK8PFTrimHT650_TrimPt100_Err = [ 0, listRatesErr[96], listRatesErr[100], listRatesErr[104], listRatesErr[108], listRatesErr[114] ]
		AK8PFTrimHT650_TrimPt200 = [ 0, listRates[97], listRates[101], listRates[105], listRates[109], listRates[113] ]
		AK8PFTrimHT650_TrimPt200_Err = [ 0, listRatesErr[97], listRatesErr[101], listRatesErr[105], listRatesErr[109], listRatesErr[113] ]

		AK8PFTrimHT650List = [
			['AK8PFTrimHT650_TrimPt40', array( 'd', AK8PFTrimHT650_TrimPt40), array('d', AK8PFTrimHT650_TrimPt40_Err )],
			['AK8PFTrimHT650_TrimPt100', array( 'd', AK8PFTrimHT650_TrimPt100), array('d', AK8PFTrimHT650_TrimPt100_Err )],
			['AK8PFTrimHT650_TrimPt200', array( 'd', AK8PFTrimHT650_TrimPt200), array('d', AK8PFTrimHT650_TrimPt200_Err )],
			]

		plotRatesCompPtMass( AK8PFTrimHT650List, 'AK8PFTrimHT650_TrimMassPt', PU)

		AK8PFTrimHT750_TrimPt40 = [ listRates[116], listRates[117], listRates[121], listRates[125], listRates[129], listRates[134] ]
		AK8PFTrimHT750_TrimPt40_Err = [ listRatesErr[116], listRatesErr[117], listRatesErr[121], listRatesErr[125], listRatesErr[129], listRatesErr[134] ]
		AK8PFTrimHT750_TrimPt100 = [ 0, listRates[118], listRates[122], listRates[126], listRates[130], listRates[134] ]
		AK8PFTrimHT750_TrimPt100_Err = [ 0, listRatesErr[118], listRatesErr[122], listRatesErr[126], listRatesErr[130], listRatesErr[134] ]
		AK8PFTrimHT750_TrimPt200 = [ 0, listRates[119], listRates[123], listRates[127], listRates[131], listRates[133] ]
		AK8PFTrimHT750_TrimPt200_Err = [ 0, listRatesErr[119], listRatesErr[123], listRatesErr[127], listRatesErr[131], listRatesErr[133] ]

		AK8PFTrimHT750List = [
			['AK8PFTrimHT750_TrimPt40', array( 'd', AK8PFTrimHT750_TrimPt40), array('d', AK8PFTrimHT750_TrimPt40_Err )],
			['AK8PFTrimHT750_TrimPt100', array( 'd', AK8PFTrimHT750_TrimPt100), array('d', AK8PFTrimHT750_TrimPt100_Err )],
			['AK8PFTrimHT750_TrimPt200', array( 'd', AK8PFTrimHT750_TrimPt200), array('d', AK8PFTrimHT750_TrimPt200_Err )],
			]

		plotRatesCompPtMass( AK8PFTrimHT750List, 'AK8PFTrimHT750_TrimMassPt', PU)

		AK8PFTrimHT850_TrimPt40 = [ listRates[138], listRates[139], listRates[143], listRates[147], listRates[151], listRates[156] ]
		AK8PFTrimHT850_TrimPt40_Err = [ listRatesErr[138], listRatesErr[139], listRatesErr[143], listRatesErr[147], listRatesErr[151], listRatesErr[156] ]
		AK8PFTrimHT850_TrimPt100 = [ 0, listRates[140], listRates[144], listRates[148], listRates[152], listRates[158] ]
		AK8PFTrimHT850_TrimPt100_Err = [ 0, listRatesErr[140], listRatesErr[144], listRatesErr[148], listRatesErr[152], listRatesErr[158] ]
		AK8PFTrimHT850_TrimPt200 = [ 0, listRates[141], listRates[145], listRates[149], listRates[153], listRates[157] ]
		AK8PFTrimHT850_TrimPt200_Err = [ 0, listRatesErr[141], listRatesErr[145], listRatesErr[149], listRatesErr[153], listRatesErr[157] ]

		AK8PFTrimHT850List = [
			['AK8PFTrimHT850_TrimPt40', array( 'd', AK8PFTrimHT850_TrimPt40), array('d', AK8PFTrimHT850_TrimPt40_Err )],
			['AK8PFTrimHT850_TrimPt100', array( 'd', AK8PFTrimHT850_TrimPt100), array('d', AK8PFTrimHT850_TrimPt100_Err )],
			['AK8PFTrimHT850_TrimPt200', array( 'd', AK8PFTrimHT850_TrimPt200), array('d', AK8PFTrimHT850_TrimPt200_Err )],
			]

		plotRatesCompPtMass( AK8PFTrimHT850List, 'AK8PFTrimHT850_TrimMassPt', PU)
