#!/usr/bin/env python
'''
File: DrawHistogram.py
Author: Alejandro Gomez Espinosa
Email: gomez@physics.rutgers.edu
Description: My Draw histograms. Check for options at the end.
'''

#from ROOT import TFile, TH1F, THStack, TCanvas, TMath, gROOT, gPad
from ROOT import *
from setTDRStyle import *
import time, os, math, sys
import tarfile
import optparse
from array import array


gROOT.Reset()
gROOT.SetBatch()
setTDRStyle()
gROOT.ForceStyle()
gROOT.SetStyle('tdrStyle')


gStyle.SetOptStat(0)
#---- open the files --------------------

inputFile1 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-30to50_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile2 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-50to80_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile3 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-80to120_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile4 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-120to170_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile5 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-170to300_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile6 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-300to470_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile7 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-470to600_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile8 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-600to800_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile9 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-800to1000_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile10 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-1000to1400_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile11 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-1400to1800_TuneZ2star_13TeV_pythia8_PU20bx25.root' )
inputFile12 = TFile.Open( 'HistoFiles/hlt_jetmass_QCD_Pt-1800_TuneZ2star_13TeV_pythia8_PU20bx25.root' )

scaleH1 = 161500000. * 0.9481 / 30000.
scaleH2 = 22110000. *0.8820 / 30000.
scaleH3 = 3000114.3 * 0.8456 / 29100. 
scaleH4 = 493200. * 0.8355 / 27000.  
scaleH5 = 120300. / 30000. 
scaleH6 = 7475. / 30000. 
scaleH7 = 587.1 / 30000. 
scaleH8 = 167. / 30000. 
scaleH9 = 28.25 / 26100. 
scaleH10 = 8.195 / 29100. 
scaleH11 = 0.7346 / 30000. 
scaleH12 = 0.1091 / 30000. 

def getP4( inputFile, treeName ):
	"""docstring for getP4"""
	tree1 = inputFile.Get( treeName + '/JetVariables')

	numEntries = tree1.GetEntries()
	list = []
	for i in xrange( numEntries ):

		tree1.GetEntry(i)
		p4 = TLorentzVector()
		listP4 = []
		HT = 0
		Njets = 0
		totMass = 0
		jet1Pt = -999
		jet1Mass = -999

		for j in xrange( len( tree1.jetPt ) ):
			if tree1.jetPt[j] > 40 and abs( tree1.jetEta[j] ) < 3.0 :
				p4.SetPtEtaPhiE( tree1.jetPt[j], tree1.jetEta[j], tree1.jetPhi[j], tree1.jetEnergy[j] )
				listP4.append( p4 )
				Njets += 1
				HT += tree1.jetPt[j]
				totMass += p4.M()

		list.append( [ HT, totMass, Njets, ( listP4[0].Pt() if HT > 0 else -999. ), ( listP4[0].M() if HT > 0 else -999. ) ] )

	return list

def drawHistos( process, inputFile1, inputFile2, inputFile3, inputFile4, inputFile5, inputFile6, inputFile7, inputFile8, inputFile9, inputFile10 ):
	"""docstring for treeplot"""
	
	listVariables1 = getP4( inputFile1, 'triggerPlotter' + process )
	listVariables2 = getP4( inputFile2, 'triggerPlotter' + process )
	listVariables3 = getP4( inputFile3, 'triggerPlotter' + process )
	listVariables4 = getP4( inputFile4, 'triggerPlotter' + process )
	listVariables5 = getP4( inputFile5, 'triggerPlotter' + process )
	listVariables6 = getP4( inputFile6, 'triggerPlotter' + process )
	listVariables7 = getP4( inputFile7, 'triggerPlotter' + process )
	listVariables8 = getP4( inputFile8, 'triggerPlotter' + process )
	listVariables9 = getP4( inputFile9, 'triggerPlotter' + process )
	listVariables10 = getP4( inputFile10, 'triggerPlotter' + process )
	
	jetMultiplicity = TH1F('NJets' + process, 'Number of Jets', 15, 0., 15. )
	HT = TH1F('HT' + process, 'HT [GeV]', 200, 0., 2000. )
	totalMass = TH1F('totalMass' + process, 'Event Jet Mass [GeV]', 50, 0., 500. )
	jet1Pt = TH1F('jet1Pt' + process, 'Leading Jet Pt [GeV]', 100, 0., 5000. )
	jet1Mass = TH1F('jet1Mass' + process, 'Leading Jet Mass [GeV]', 40, 0., 200. )

	for i in range( len( listVariables1 ) ):
		HT.Fill( listVariables1[i][0], scaleH1 )
		totalMass.Fill( listVariables1[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables1[i][2], scaleH1 )
		jet1Pt.Fill( listVariables1[i][3], scaleH1 )
		jet1Mass.Fill( listVariables1[i][4], scaleH1 )

	for i in range( len( listVariables2 ) ):
		HT.Fill( listVariables2[i][0], scaleH1 )
		totalMass.Fill( listVariables2[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables2[i][2], scaleH1 )
		jet1Pt.Fill( listVariables2[i][3], scaleH1 )
		jet1Mass.Fill( listVariables2[i][4], scaleH1 )

	for i in range( len( listVariables3 ) ):
		HT.Fill( listVariables3[i][0], scaleH1 )
		totalMass.Fill( listVariables3[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables3[i][2], scaleH1 )
		jet1Pt.Fill( listVariables3[i][3], scaleH1 )
		jet1Mass.Fill( listVariables3[i][4], scaleH1 )

	for i in range( len( listVariables4 ) ):
		HT.Fill( listVariables4[i][0], scaleH1 )
		totalMass.Fill( listVariables4[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables4[i][2], scaleH1 )
		jet1Pt.Fill( listVariables4[i][3], scaleH1 )
		jet1Mass.Fill( listVariables4[i][4], scaleH1 )

	for i in range( len( listVariables5 ) ):
		HT.Fill( listVariables5[i][0], scaleH1 )
		totalMass.Fill( listVariables5[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables5[i][2], scaleH1 )
		jet1Pt.Fill( listVariables5[i][3], scaleH1 )
		jet1Mass.Fill( listVariables5[i][4], scaleH1 )

	for i in range( len( listVariables6 ) ):
		HT.Fill( listVariables6[i][0], scaleH1 )
		totalMass.Fill( listVariables6[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables6[i][2], scaleH1 )
		jet1Pt.Fill( listVariables6[i][3], scaleH1 )
		jet1Mass.Fill( listVariables6[i][4], scaleH1 )

	for i in range( len( listVariables7 ) ):
		HT.Fill( listVariables7[i][0], scaleH1 )
		totalMass.Fill( listVariables7[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables7[i][2], scaleH1 )
		jet1Pt.Fill( listVariables7[i][3], scaleH1 )
		jet1Mass.Fill( listVariables7[i][4], scaleH1 )

	for i in range( len( listVariables8 ) ):
		HT.Fill( listVariables8[i][0], scaleH1 )
		totalMass.Fill( listVariables8[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables8[i][2], scaleH1 )
		jet1Pt.Fill( listVariables8[i][3], scaleH1 )
		jet1Mass.Fill( listVariables8[i][4], scaleH1 )

	for i in range( len( listVariables9 ) ):
		HT.Fill( listVariables9[i][0], scaleH1 )
		totalMass.Fill( listVariables9[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables9[i][2], scaleH1 )
		jet1Pt.Fill( listVariables9[i][3], scaleH1 )
		jet1Mass.Fill( listVariables9[i][4], scaleH1 )

	for i in range( len( listVariables10 ) ):
		HT.Fill( listVariables10[i][0], scaleH1 )
		totalMass.Fill( listVariables10[i][1], scaleH1 )
		jetMultiplicity.Fill( listVariables10[i][2], scaleH1 )
		jet1Pt.Fill( listVariables10[i][3], scaleH1 )
		jet1Mass.Fill( listVariables10[i][4], scaleH1 )


def treeplot():
	"""docstring for treeplot"""

	outputFile = TFile( 'HistoFiles/QCD_All_TriggerStudies.root', 'RECREATE' )

	drawHistos( '', inputFile1, inputFile2, inputFile3, inputFile4, inputFile5, inputFile6, inputFile7, inputFile8, inputFile9, inputFile10 )
	drawHistos( 'Trim', inputFile1, inputFile2, inputFile3, inputFile4, inputFile5, inputFile6, inputFile7, inputFile8, inputFile9, inputFile10 )
	drawHistos( 'AK8', inputFile1, inputFile2, inputFile3, inputFile4, inputFile5, inputFile6, inputFile7, inputFile8, inputFile9, inputFile10 )
	drawHistos( 'AK8Trim', inputFile1, inputFile2, inputFile3, inputFile4, inputFile5, inputFile6, inputFile7, inputFile8, inputFile9, inputFile10 )

	outputFile.cd()
	outputFile.Write()
	outputFile.Close()

def plot( name, plotName, inPlotName, xmax, log ):
	"""docstring for plot"""

	outputFileName = name+'_QCD_TriggerStudies.pdf' 
	print 'Processing.......', outputFileName
	histo1 = 'triggerPlotter/'+plotName
	histo2 = 'triggerPlotter/'+plotName+'_NOJEC'
	histo3 = 'triggerPlotterTrim/'+plotName
	histo4 = 'triggerPlotterTrim/'+plotName+'_NOJEC'
	histo5 = 'triggerPlotterAK8/'+plotName
	histo6 = 'triggerPlotterAK8/'+plotName+'_NOJEC'
	histo7 = 'triggerPlotterAK8Trim/'+plotName
	histo8 = 'triggerPlotterAK8Trim/'+plotName+'_NOJEC'

	h1 = inputFile1.Get( histo1 )
	h1.Scale( scaleH1 )
	h12 = inputFile1.Get( histo2 )
	h12.Scale( scaleH1 )
	h13 = inputFile1.Get( histo3 )
	h13.Scale( scaleH1 )
	h14 = inputFile1.Get( histo4 )
	h14.Scale( scaleH1 )
	h15 = inputFile1.Get( histo5 )
	h15.Scale( scaleH1 )
	h16 = inputFile1.Get( histo6 )
	h16.Scale( scaleH1 )
	h17 = inputFile1.Get( histo7 )
	h17.Scale( scaleH1 )
	h18 = inputFile1.Get( histo8 )
	h18.Scale( scaleH1 )

	
	h2 = inputFile2.Get( histo1 )
	h2.Scale( scaleH2 )
	h22 = inputFile2.Get( histo2 )
	h22.Scale( scaleH2 )
	h23 = inputFile2.Get( histo3 )
	h23.Scale( scaleH2 )
	h24 = inputFile2.Get( histo4 )
	h24.Scale( scaleH2 )
	h25 = inputFile2.Get( histo5 )
	h25.Scale( scaleH2 )
	h26 = inputFile2.Get( histo6 )
	h26.Scale( scaleH2 )
	h27 = inputFile2.Get( histo7 )
	h27.Scale( scaleH2 )
	h28 = inputFile2.Get( histo8 )
	h28.Scale( scaleH2 )

	h3 = inputFile3.Get( histo1 )
	h3.Scale( scaleH3 )
	h32 = inputFile3.Get( histo2 )
	h32.Scale( scaleH3 )
	h33 = inputFile3.Get( histo3 )
	h33.Scale( scaleH3 )
	h34 = inputFile3.Get( histo4 )
	h34.Scale( scaleH3 )
	h35 = inputFile3.Get( histo5 )
	h35.Scale( scaleH3 )
	h36 = inputFile3.Get( histo6 )
	h36.Scale( scaleH3 )
	h37 = inputFile3.Get( histo7 )
	h37.Scale( scaleH3 )
	h38 = inputFile3.Get( histo8 )
	h38.Scale( scaleH3 )

	h4 = inputFile4.Get( histo1 )
	h4.Scale( scaleH4 )
	h42 = inputFile4.Get( histo2 )
	h42.Scale( scaleH4 )
	h43 = inputFile4.Get( histo3 )
	h43.Scale( scaleH4 )
	h44 = inputFile4.Get( histo4 )
	h44.Scale( scaleH4 )
	h45 = inputFile4.Get( histo5 )
	h45.Scale( scaleH4 )
	h46 = inputFile4.Get( histo6 )
	h46.Scale( scaleH4 )
	h47 = inputFile4.Get( histo7 )
	h47.Scale( scaleH4 )
	h48 = inputFile4.Get( histo8 )
	h48.Scale( scaleH4 )

	h5 = inputFile5.Get( histo1 )
	h5.Scale( scaleH5 )
	h52 = inputFile5.Get( histo2 )
	h52.Scale( scaleH5 )
	h53 = inputFile5.Get( histo3 )
	h53.Scale( scaleH5 )
	h54 = inputFile5.Get( histo4 )
	h54.Scale( scaleH5 )
	h55 = inputFile5.Get( histo5 )
	h55.Scale( scaleH5 )
	h56 = inputFile5.Get( histo6 )
	h56.Scale( scaleH5 )
	h57 = inputFile5.Get( histo7 )
	h57.Scale( scaleH5 )
	h58 = inputFile5.Get( histo8 )
	h58.Scale( scaleH5 )

	h6 = inputFile6.Get( histo1 )
	h6.Scale( scaleH6 )
	h62 = inputFile6.Get( histo2 )
	h62.Scale( scaleH6 )
	h63 = inputFile6.Get( histo3 )
	h63.Scale( scaleH6 )
	h64 = inputFile6.Get( histo4 )
	h64.Scale( scaleH6 )
	h65 = inputFile6.Get( histo5 )
	h65.Scale( scaleH6 )
	h66 = inputFile6.Get( histo6 )
	h66.Scale( scaleH6 )
	h67 = inputFile6.Get( histo7 )
	h67.Scale( scaleH6 )
	h68 = inputFile6.Get( histo8 )
	h68.Scale( scaleH6 )

	h7 = inputFile7.Get( histo1 )
	h7.Scale( scaleH7 )
	h72 = inputFile7.Get( histo2 )
	h72.Scale( scaleH7 )
	h73 = inputFile7.Get( histo3 )
	h73.Scale( scaleH7 )
	h74 = inputFile7.Get( histo4 )
	h74.Scale( scaleH7 )
	h75 = inputFile7.Get( histo5 )
	h75.Scale( scaleH7 )
	h76 = inputFile7.Get( histo6 )
	h76.Scale( scaleH7 )
	h77 = inputFile7.Get( histo7 )
	h77.Scale( scaleH7 )
	h78 = inputFile7.Get( histo8 )
	h78.Scale( scaleH7 )

	h8 = inputFile8.Get( histo1 )
	h8.Scale( scaleH8 )
	h82 = inputFile8.Get( histo2 )
	h82.Scale( scaleH8 )
	h83 = inputFile8.Get( histo3 )
	h83.Scale( scaleH8 )
	h84 = inputFile8.Get( histo4 )
	h84.Scale( scaleH8 )
	h85 = inputFile8.Get( histo5 )
	h85.Scale( scaleH8 )
	h86 = inputFile8.Get( histo6 )
	h86.Scale( scaleH8 )
	h87 = inputFile8.Get( histo7 )
	h87.Scale( scaleH8 )
	h88 = inputFile8.Get( histo8 )
	h88.Scale( scaleH8 )

	h9 = inputFile9.Get( histo1 )
	h9.Scale( scaleH9 )
	h92 = inputFile9.Get( histo2 )
	h92.Scale( scaleH9 )
	h93 = inputFile9.Get( histo3 )
	h93.Scale( scaleH9 )
	h94 = inputFile9.Get( histo4 )
	h94.Scale( scaleH9 )
	h95 = inputFile9.Get( histo5 )
	h95.Scale( scaleH9 )
	h96 = inputFile9.Get( histo6 )
	h96.Scale( scaleH9 )
	h97 = inputFile9.Get( histo7 )
	h97.Scale( scaleH9 )
	h98 = inputFile9.Get( histo8 )
	h98.Scale( scaleH9 )

	h10 = inputFile10.Get( histo1 )
	h10.Scale( scaleH10 )
	h102 = inputFile10.Get( histo2 )
	h102.Scale( scaleH10 )
	h103 = inputFile10.Get( histo3 )
	h103.Scale( scaleH10 )
	h104 = inputFile10.Get( histo4 )
	h104.Scale( scaleH10 )
	h105 = inputFile10.Get( histo5 )
	h105.Scale( scaleH10 )
	h106 = inputFile10.Get( histo6 )
	h106.Scale( scaleH10 )
	h107 = inputFile10.Get( histo7 )
	h107.Scale( scaleH10 )
	h108 = inputFile10.Get( histo8 )
	h108.Scale( scaleH10 )

	h11 = inputFile11.Get( histo1 )
	h11.Scale( scaleH11 )
	h112 = inputFile11.Get( histo2 )
	h112.Scale( scaleH11 )
	h113 = inputFile11.Get( histo3 )
	h113.Scale( scaleH11 )
	h114 = inputFile11.Get( histo4 )
	h114.Scale( scaleH11 )
	h115 = inputFile11.Get( histo5 )
	h115.Scale( scaleH11 )
	h116 = inputFile11.Get( histo6 )
	h116.Scale( scaleH11 )
	h117 = inputFile11.Get( histo7 )
	h117.Scale( scaleH11 )
	h118 = inputFile11.Get( histo8 )
	h118.Scale( scaleH11 )

	h12 = inputFile12.Get( histo1 )
	h12.Scale( scaleH12 )
	h122 = inputFile12.Get( histo2 )
	h122.Scale( scaleH12 )
	h123 = inputFile12.Get( histo3 )
	h123.Scale( scaleH12 )
	h124 = inputFile12.Get( histo4 )
	h124.Scale( scaleH12 )
	h125 = inputFile12.Get( histo5 )
	h125.Scale( scaleH12 )
	h126 = inputFile12.Get( histo6 )
	h126.Scale( scaleH12 )
	h127 = inputFile12.Get( histo7 )
	h127.Scale( scaleH12 )
	h128 = inputFile12.Get( histo8 )
	h128.Scale( scaleH12 )
	#----- Drawing -----------------------

	h1.GetXaxis().SetTitle( inPlotName )
	binWidth = h1.GetBinWidth(1)
	h1.GetYaxis().SetTitle( 'Events /'+str(binWidth) )
	h1.Add( h2 )
	h1.Add( h3 )
	h1.Add( h4 )
	h1.Add( h5 )
	h1.Add( h6 )
	h1.Add( h7 )
	h1.Add( h8 )
	h1.Add( h9 )
	h1.Add( h10 )
	h1.Add( h11 )
	h1.Add( h12 )

	h12.Add( h22 )
	h12.Add( h32 )
	h12.Add( h42 )
	h12.Add( h52 )
	h12.Add( h62 )
	h12.Add( h72 )
	h12.Add( h82 )
	h12.Add( h92 )
	h12.Add( h102 )
	h12.Add( h112 )
	h12.Add( h122 )

	h13.Add( h23 )
	h13.Add( h33 )
	h13.Add( h43 )
	h13.Add( h53 )
	h13.Add( h63 )
	h13.Add( h73 )
	h13.Add( h83 )
	h13.Add( h93 )
	h13.Add( h103 )
	h13.Add( h113 )
	h13.Add( h123 )

	h14.Add( h24 )
	h14.Add( h34 )
	h14.Add( h44 )
	h14.Add( h54 )
	h14.Add( h64 )
	h14.Add( h74 )
	h14.Add( h84 )
	h14.Add( h94 )
	h14.Add( h104 )

	h15.Add( h25 )
	h15.Add( h35 )
	h15.Add( h45 )
	h15.Add( h55 )
	h15.Add( h65 )
	h15.Add( h75 )
	h15.Add( h85 )
	h15.Add( h95 )
	h15.Add( h105 )
	h15.Add( h115 )
	h15.Add( h125 )

	h16.Add( h26 )
	h16.Add( h36 )
	h16.Add( h46 )
	h16.Add( h56 )
	h16.Add( h66 )
	h16.Add( h76 )
	h16.Add( h86 )
	h16.Add( h96 )
	h16.Add( h106 )
	h16.Add( h116 )
	h16.Add( h126 )

	h17.Add( h27 )
	h17.Add( h37 )
	h17.Add( h47 )
	h17.Add( h57 )
	h17.Add( h67 )
	h17.Add( h77 )
	h17.Add( h87 )
	h17.Add( h97 )
	h17.Add( h107 )
	h17.Add( h117 )
	h17.Add( h127 )

	h18.Add( h28 )
	h18.Add( h38 )
	h18.Add( h48 )
	h18.Add( h58 )
	h18.Add( h68 )
	h18.Add( h78 )
	h18.Add( h88 )
	h18.Add( h98 )
	h18.Add( h108 )
	h18.Add( h118 )
	h18.Add( h128 )


	h1.SetLineColor(1)
	h1.SetLineWidth(2)
	h12.SetLineColor(1)
	h12.SetLineStyle(2)
	h13.SetLineColor(2)
	h13.SetLineWidth(2)
	h14.SetLineColor(2)
	h14.SetLineStyle(2)
	h15.SetLineColor(3)
	h15.SetLineWidth(2)
	h16.SetLineColor(3)
	h16.SetLineStyle(2)
	h17.SetLineColor(4)
	h17.SetLineWidth(2)
	h18.SetLineColor(4)
	h18.SetLineStyle(2)
	h1.SetMaximum(2*max(h1.GetBinContent(h1.GetMaximumBin()),h12.GetBinContent(h12.GetMaximumBin()),h13.GetBinContent(h13.GetMaximumBin()),h14.GetBinContent(h14.GetMaximumBin()),h15.GetBinContent(h15.GetMaximumBin()),h16.GetBinContent(h16.GetMaximumBin()),h17.GetBinContent(h17.GetMaximumBin()),h18.GetBinContent(h18.GetMaximumBin())))
	h1.GetXaxis().SetRange( 0, xmax )

	legend=TLegend(0.70,0.60,0.90,0.85)
	legend.SetFillStyle(0)
	legend.AddEntry(h1, 'PFNoPUHT', "l")
	legend.AddEntry(h12, 'PFNoPUHT NOJEC', "l")
	legend.AddEntry(h13, 'PFNoPUHTTrim', "l")
	legend.AddEntry(h14, 'PFNoPUHTTrim NOJEC', "l")
	legend.AddEntry(h15, 'PFNoPUHTAK8', "l")
	legend.AddEntry(h16, 'PFNoPUHTAK8 NOJEC', "l")
	legend.AddEntry(h17, 'PFNoPUHTAK8Trim', "l")
	legend.AddEntry(h18, 'PFNoPUHTAK8Trim NOJEC', "l")
	legend.SetTextSize(0.03)

	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	if log: can.SetLogy()
	#h1.Sumw2()
	#h12.Sumw2()
	#h13.Sumw2()
	#h14.Sumw2()
	h1.Draw('hist')
	h12.Draw('same hist')
	h13.Draw('same hist')
	h14.Draw('same hist')
	h15.Draw('same hist')
	h16.Draw('same hist')
	h17.Draw('same hist')
	h18.Draw('same hist')
	legend.Draw()
	setSelectionTrigger( 'QCD 13 TeV PU20bx25' )
	can.SaveAs( outputFileName )
	del can

def plot2D( name, plotName, plotName2, inPlotName, inPlotName2, xmax, xmax2 ):
	"""docstring for plot"""

	outputFileName = name+'_QCD_TriggerStudies.pdf' 
	print 'Processing.......', outputFileName
	histo1 = 'triggerPlotter'+plotName
	histo2 = 'triggerPlotter'+plotName2

	h1 = inputFile1.Get( histo1 )
	h1.Scale( scaleH1 )
	h12 = inputFile1.Get( histo2 )
	h12.Scale( scaleH1 )
	
	h2 = inputFile2.Get( histo1 )
	h2.Scale( scaleH2 )
	h22 = inputFile2.Get( histo2 )
	h22.Scale( scaleH2 )

	h3 = inputFile3.Get( histo1 )
	h3.Scale( scaleH3 )
	h32 = inputFile3.Get( histo2 )
	h32.Scale( scaleH3 )

	h4 = inputFile4.Get( histo1 )
	h4.Scale( scaleH4 )
	h42 = inputFile4.Get( histo2 )
	h42.Scale( scaleH4 )

	h5 = inputFile5.Get( histo1 )
	h5.Scale( scaleH5 )
	h52 = inputFile5.Get( histo2 )
	h52.Scale( scaleH5 )

	h6 = inputFile6.Get( histo1 )
	h6.Scale( scaleH6 )
	h62 = inputFile6.Get( histo2 )
	h62.Scale( scaleH6 )

	h7 = inputFile7.Get( histo1 )
	h7.Scale( scaleH7 )
	h72 = inputFile7.Get( histo2 )
	h72.Scale( scaleH7 )

	h8 = inputFile8.Get( histo1 )
	h8.Scale( scaleH8 )
	h82 = inputFile8.Get( histo2 )
	h82.Scale( scaleH8 )

	h9 = inputFile9.Get( histo1 )
	h9.Scale( scaleH9 )
	h92 = inputFile9.Get( histo2 )
	h92.Scale( scaleH9 )

	h10 = inputFile10.Get( histo1 )
	h10.Scale( scaleH10 )
	h102 = inputFile10.Get( histo2 )
	h102.Scale( scaleH10 )

	h11 = inputFile11.Get( histo1 )
	h11.Scale( scaleH11 )
	h112 = inputFile11.Get( histo2 )
	h112.Scale( scaleH11 )

	h12 = inputFile12.Get( histo1 )
	h12.Scale( scaleH12 )
	h122 = inputFile12.Get( histo2 )
	h122.Scale( scaleH12 )
	#----- Drawing -----------------------

	h1.GetXaxis().SetTitle( inPlotName )
	h2.GetYaxis().SetTitle( inPlotName2 )

	h1.Add( h2 )
	h1.Add( h3 )
	h1.Add( h4 )
	h1.Add( h5 )
	h1.Add( h6 )
	h1.Add( h7 )
	h1.Add( h8 )
	h1.Add( h9 )
	h1.Add( h10 )
	h1.Add( h11 )
	h1.Add( h12 )

	h12.Add( h22 )
	h12.Add( h32 )
	h12.Add( h42 )
	h12.Add( h52 )
	h12.Add( h62 )
	h12.Add( h72 )
	h12.Add( h82 )
	h12.Add( h92 )
	h12.Add( h102 )
	h12.Add( h112 )
	h12.Add( h122 )

	h1.GetXaxis().SetRange( 0, xmax )
	h2.GetXaxis().SetRange( 0, xmax2 )

	legend=TLegend(0.70,0.60,0.90,0.85)
	legend.SetFillStyle(0)
	legend.AddEntry(h1, 'PFNoPUHT', "l")
	legend.AddEntry(h12, 'PFNoPUHT NOJEC', "l")
	legend.AddEntry(h13, 'PFNoPUHTTrim', "l")
	legend.AddEntry(h14, 'PFNoPUHTTrim NOJEC', "l")
	legend.AddEntry(h15, 'PFNoPUHTAK8', "l")
	legend.AddEntry(h16, 'PFNoPUHTAK8 NOJEC', "l")
	legend.AddEntry(h17, 'PFNoPUHTAK8Trim', "l")
	legend.AddEntry(h18, 'PFNoPUHTAK8Trim NOJEC', "l")
	legend.SetTextSize(0.03)

	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	if log: can.SetLogy()
	#h1.Sumw2()
	#h12.Sumw2()
	#h13.Sumw2()
	#h14.Sumw2()
	h1.Draw('hist')
	h12.Draw('same hist')
	h13.Draw('same hist')
	h14.Draw('same hist')
	h15.Draw('same hist')
	h16.Draw('same hist')
	h17.Draw('same hist')
	h18.Draw('same hist')
	legend.Draw()
	setSelectionTrigger( 'QCD 13 TeV PU20bx25' )
	can.SaveAs( outputFileName )
	del can
if __name__ == '__main__':
	
	plot( 'HT', 'ht', 'HT [GeV]', 300, True )
	plot( 'jet1pt', 'jet1pt', 'Leading Jet Pt [GeV]', 100, True )
	plot( 'jet1mass', 'jet1mass', 'Leading Jet Mass [GeV]', 20, True )
	plot( 'eventJetMass', 'eventJetMass', 'Event Jet Mass [GeV]', 100, True )

	#treeplot(  )
