#!/usr/bin/env python

import math,ROOT
from array import array
import numpy as np
from ROOT import gROOT, TFile, TChain, TTree, TH1F, TF1, TLegend, TCanvas

gROOT.Reset()
gROOT.SetBatch()

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
		rateList.append( collrate * (1 - math.exp(-1* (xsec*ilumi*passed[i]/run[i])/collrate)) )
		rateErrList.append( xsec * ilumi * ((math.sqrt( passed[i] + (( passed[i])**2)/ run[i]))/ run[i]) )

	return rateList, rateErrList

def plotRates( listRates, listRatesErr, PU ):
	"""docstring for plotRates"""

	#HT = [ 350., 650., 700., 750., 800., 850. ]
	#HT = [ 650., 700., 750., 800., 850. ]
	HT = [ 450., 550., 650., 750., 850. ]
	HTErr = [ 0., 0., 0., 0., 0. ]
	t = array( 'd', HT)
	x = array( 'd', listRates[0:4])
	y = array( 'd', listRates[5:9])
	z = array( 'd', listRates[10:14])
	tErr = array( 'd', HTErr)
	xErr = array( 'd', listRatesErr[1:6])
	yErr = array( 'd', listRatesErr[7:12])
	zErr = array( 'd', listRatesErr[13:18])
	print x, y, z
	g1 = ROOT.TGraphErrors(len(t), t, x, tErr, xErr)
	g2 = ROOT.TGraphErrors(len(t), t, y, tErr, yErr)
	g3 = ROOT.TGraphErrors(len(t), t, z, tErr, zErr)


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

	legend=TLegend(0.60,0.70,0.90,0.90)
	legend.SetFillColor(0)
	legend.AddEntry(g1, 'HLT_HT', "l")
	legend.AddEntry(g3, 'HLT_PFHT', "l")
	legend.AddEntry(g2, 'HLT_PFNoPUHT', "l")
	#legend.AddEntry(g2, 'HLT_PFNoPUAK8HT', "l")
	#legend.AddEntry(g3, 'HLT_PFNoPUAK8HTTrim', "l")
	legend.AddEntry(g4, 'Official HLT_PFNoPUHT', "l")
	legend.SetTextSize(0.03)

	c = TCanvas( "c1", "c1", 800, 600 )
	g1.SetTitle("Trigger Rates for "+PU)
	g1.GetXaxis().SetTitle("HT [GeV]")
	g1.GetYaxis().SetTitle("Rate [Hz]")
	maxRate = max( listRates[0:4], listRates[5:9], listRates[10:14] )
	g1.SetMaximum( maxRate[0]+50 )
	g1.SetLineColor( ROOT.kBlue )
	g1.SetLineWidth( 2 )
	g2.SetLineColor( ROOT.kRed )
	g2.SetLineWidth( 2 )
	g3.SetLineColor( ROOT.kGreen )
	g3.SetLineWidth( 2 )
	g4.SetLineColor( ROOT.kBlack )
	g4.SetLineWidth( 2 )
	g1.Draw("lpa")
	g2.Draw("lp")
	g3.Draw("lp")
	g4.Draw("lp")
	legend.Draw()
	c.SaveAs("TriggerRate"+PU+".pdf")
	#c.SaveAs("TriggerRate"+PU+"_tmp.pdf")



if __name__ == '__main__':
	
	numTriggers = 34
	#PU = 'PU40bx50'
	PU = 'PU20bx25'
	#PU = 'PU40bx25'

	name0, run0, passed0, failed0, rates0, ratesErr0 = grabTriggerNumbers( 'dump_QCD_Pt-30to50_'+PU+'_Filt.log', numTriggers,161500000. * 0.9481 , PU )
	name1, run1, passed1, failed1, rates1, ratesErr1 = grabTriggerNumbers( 'dump_QCD_Pt-50to80_'+PU+'_Filt.log', numTriggers, 22110000. *0.8821, PU )
	name2, run2, passed2, failed2, rates2, ratesErr2 = grabTriggerNumbers( 'dump_QCD_Pt-80to120_'+PU+'_Filt.log', numTriggers, 3000000. * 0.8456, PU )
	name3, run3, passed3, failed3, rates3, ratesErr3 = grabTriggerNumbers( 'dump_QCD_Pt-120to170_'+PU+'_Filt.log', numTriggers, 493200. * 0.8355, PU )
	name4, run4, passed4, failed4, rates4, ratesErr4 = grabTriggerNumbers( 'dump_QCD_Pt-170to300_'+PU+'_Filt.log', numTriggers, 12030., PU )
	name5, run5, passed5, failed5, rates5, ratesErr5 = grabTriggerNumbers( 'dump_QCD_Pt-300to470_'+PU+'_Filt.log', numTriggers, 7475., PU )
	name6, run6, passed6, failed6, rates6, ratesErr6 = grabTriggerNumbers( 'dump_QCD_Pt-470to600_'+PU+'_Filt.log', numTriggers, 587.1, PU  )
	name7, run7, passed7, failed7, rates7, ratesErr7 = grabTriggerNumbers( 'dump_QCD_Pt-600to800_'+PU+'_Filt.log', numTriggers, 167., PU )
	name8, run8, passed8, failed8, rates8, ratesErr8 = grabTriggerNumbers( 'dump_QCD_Pt-800to1000_'+PU+'_Filt.log', numTriggers, 28.25, PU  )
	name9, run9, passed9, failed9, rates9, ratesErr9 = grabTriggerNumbers( 'dump_QCD_Pt-1000to1400_'+PU+'_Filt.log', numTriggers, 8.975, PU  )
	name10, run10, passed10, failed10, rates10, ratesErr10 = grabTriggerNumbers( 'dump_QCD_Pt-1400to1800_'+PU+'_Filt.log', numTriggers, 0.8975, PU )
	name11, run11, passed11, failed11, rates11, ratesErr11 = grabTriggerNumbers( 'dump_QCD_Pt-1800_'+PU+'_Filt.log', numTriggers, 0.1091 , PU )

	listRates = [ rates0[i] + rates1[i] + rates2[i] + rates3[i] + rates4[i] + rates5[i] + rates6[i] + rates7[i] + rates8[i] + rates9[i] + rates10[i] + rates11[i] for i in xrange( len( rates1 ) )]
	listRatesErr = [ ratesErr0[i] +ratesErr1[i] + ratesErr2[i] + ratesErr3[i] + ratesErr4[i] + ratesErr5[i] + ratesErr6[i] + ratesErr7[i] + ratesErr8[i] + ratesErr9[i] + ratesErr10[i] + ratesErr11[i] for i in xrange( len( ratesErr1 ) )]
	print listRates
	print listRatesErr
	plotRates( listRates, listRatesErr, PU )

