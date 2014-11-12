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
#import tarfile
#import optparse


gROOT.Reset()
gROOT.SetBatch()
setTDRStyle()
gROOT.ForceStyle()
gROOT.SetStyle('tdrStyle')


gStyle.SetOptStat(0)

def plot( inFileQCD, inFileSignal, inFileBoosted, dir, name, xmin, xmax):
	"""docstring for plot"""

	outputFileName = name+'_'+dir+'_DiffPtThreshold.pdf' 
	print 'Processing.......', outputFileName

	qcd40 = inFileQCD.Get( dir+'/'+name+'40' )
	qcd100 = inFileQCD.Get( dir+'/'+name+'100' )
	qcd150 = inFileQCD.Get( dir+'/'+name+'150' )
	qcd200 = inFileQCD.Get( dir+'/'+name+'200' )
	signal40 = inFileSignal.Get( dir+'/'+name+'40' )
	signal100 = inFileSignal.Get( dir+'/'+name+'100' )
	signal150 = inFileSignal.Get( dir+'/'+name+'150' )
	signal200 = inFileSignal.Get( dir+'/'+name+'200' )
	boosted40 = inFileBoosted.Get( dir+'/'+name+'40' )
	boosted100 = inFileBoosted.Get( dir+'/'+name+'100' )
	boosted150 = inFileBoosted.Get( dir+'/'+name+'150' )
	boosted200 = inFileBoosted.Get( dir+'/'+name+'200' )

	binWidth = qcd40.GetBinWidth(1)
	qcd40.GetYaxis().SetTitle( 'Events /' + str(binWidth) )
	qcd40.SetMinimum( 10. )
	listMax = [ qcd40.GetBinContent( qcd40.GetMaximumBin() ), qcd100.GetBinContent( qcd100.GetMaximumBin() ), qcd150.GetBinContent( qcd150.GetMaximumBin() ), qcd200.GetBinContent( qcd200.GetMaximumBin() ) ]
	qcd40.SetMaximum( 2* max( listMax ) ) 

	qcd40.SetLineColor(4)
	qcd40.SetLineWidth(2)
	qcd100.SetLineColor(2)
	qcd100.SetLineWidth(2)
	qcd150.SetLineColor(3)
	qcd150.SetLineWidth(2)
	qcd200.SetLineColor(7)
	qcd200.SetLineWidth(2)
	signal40.SetLineColor(4)
	signal40.SetLineWidth(2)
	signal40.SetLineStyle(2)
	signal100.SetLineColor(2)
	signal100.SetLineWidth(2)
	signal100.SetLineStyle(2)
	signal150.SetLineColor(3)
	signal150.SetLineWidth(2)
	signal150.SetLineStyle(2)
	signal200.SetLineColor(7)
	signal200.SetLineWidth(2)
	signal200.SetLineStyle(2)
	boosted40.SetLineColor(4)
	boosted40.SetLineWidth(2)
	boosted40.SetLineStyle(3)
	boosted100.SetLineColor(2)
	boosted100.SetLineWidth(2)
	boosted100.SetLineStyle(3)
	boosted150.SetLineColor(3)
	boosted150.SetLineWidth(2)
	boosted150.SetLineStyle(3)
	boosted200.SetLineColor(7)
	boosted200.SetLineWidth(2)
	boosted200.SetLineStyle(3)

	legend=TLegend(0.60,0.60,0.90,0.90)
	legend.SetFillStyle(0)
	legend.SetTextSize(0.03)
	legend.AddEntry( qcd40, 'QCD - Pt40', 'l')
	legend.AddEntry( qcd100, 'QCD - Pt100', 'l')
	legend.AddEntry( qcd150, 'QCD - Pt150', 'l')
	legend.AddEntry( qcd200, 'QCD - Pt200', 'l')
	legend.AddEntry( signal40, 'Signal - Pt40', 'l')
	legend.AddEntry( signal100, 'Signal - Pt100', 'l')
	legend.AddEntry( signal150, 'Signal - Pt150', 'l')
	legend.AddEntry( signal200, 'Signal - Pt200', 'l')
	legend.AddEntry( boosted40, 'Only boosted Signal - Pt40', 'l')
	legend.AddEntry( boosted100, 'Only boosted Signal - Pt100', 'l')
	legend.AddEntry( boosted150, 'Only boosted Signal - Pt150', 'l')
	legend.AddEntry( boosted200, 'Only boosted Signal - Pt200', 'l')

	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	can.SetLogy()
	qcd40.Draw()
	qcd100.Draw("same")
	qcd150.Draw("same")
	qcd200.Draw("same")
	signal40.Draw("same")
	signal100.Draw("same")
	signal150.Draw("same")
	signal200.Draw("same")
	boosted40.Draw("same")
	boosted100.Draw("same")
	boosted150.Draw("same")
	boosted200.Draw("same")
	legend.Draw()
	setOverlap( 'RPV Stop 100 GeV - Scaled to 10 fb^{-1}')
	can.SaveAs( outputFileName )
	del can


def plot2D( inFile, signal, trigger, name, inFileName, xmax, xmax2, PU ):
	"""docstring for plot"""


	outputFileName = trigger+'_'+name+'_'+signal+'_'+PU+'_TriggerOverlap.pdf' 
	print 'Processing.......', outputFileName

	histos = inFile.Get( trigger+'/'+name )
	if 'vsPFHT800' in inFileName:
		if 'vsPFHT800' in trigger: newLabel = 'PFHT800'
		elif 'vsPFHT850' in trigger: newLabel = 'PFHT850'
		elif 'vsPFHT900' in trigger: newLabel = 'PFHT900'
	else: newLabel = inFileName

	#histo.GetXaxis().SetTitle( 'HT [GeV]' )
	#histo.GetYaxis().SetTitle( 'Leading Jet Mass [GeV]')
		
	#histo.GetXaxis().SetRange( 6, 15 )
	#histo.GetYaxis().SetRange( 0, 12 )
	#gStyle.SetPaintTextFormat("4.3f")
	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	can.SetLogz()
	histos.Draw('colz')
	#histo.Draw('same texte')
	setOverlapHistos( signal + ' 13 TeV '+ PU, newLabel )
	can.SaveAs( 'Plots/'+outputFileName )
	del can



if __name__ == '__main__':

	#PU = sys.argv[2]
	#Signal = sys.argv[1] #'RPVSt100tojj'	
	inputFileQCD = TFile.Open('simpleAnalyzer_QCDAll_Tune4C_13TeV_pythia8_PU40bx25.root')
	inputFileSignal = TFile.Open('simpleAnalyzer_RPVSt100tojj_13TeV_pythia8_PU40bx25.root')
	inputFileBoosted = TFile.Open('simpleAnalyzer_RPVSt100tojj_13TeV_pythia8_PU40bx25_boosted.root')

	plotsList = [
			[ 'histosUngroomedJets', 'HT', 0, 0 ],
			[ 'histosUngroomedJets', 'numJets', 0, 0 ],
			[ 'histosUngroomedJets', 'jetPt', 0, 0 ],
			[ 'histosUngroomedJets', 'jetMass', 0, 0 ],
			[ 'histosUngroomedJets', 'jetEta', 0, 0 ],
			[ 'histosUngroomedJets', 'jet1Pt', 0, 0 ],
			[ 'histosUngroomedJets', 'jet1Mass', 0, 0 ],
			[ 'histosUngroomedJets', 'jet1Eta', 0, 0 ],
			[ 'histosUngroomedJets', 'jetMass1Mass', 0, 0 ],
			[ 'histosTrimmedJets', 'HT', 0, 0 ],
			[ 'histosTrimmedJets', 'numJets', 0, 0 ],
			[ 'histosTrimmedJets', 'jetPt', 0, 0 ],
			[ 'histosTrimmedJets', 'jetMass', 0, 0 ],
			[ 'histosTrimmedJets', 'jetEta', 0, 0 ],
			[ 'histosTrimmedJets', 'jet1Pt', 0, 0 ],
			[ 'histosTrimmedJets', 'jet1Mass', 0, 0 ],
			[ 'histosTrimmedJets', 'jet1Eta', 0, 0 ],
			[ 'histosTrimmedJets', 'jetMass1Mass', 0, 0 ],
			]


	for i in plotsList: 
		#if 'vs' in i[0]: plot2D( inputFile, Signal, k, i[0], i[1], i[2], i[3], PU )
			#elif 'Overlap' in i[0]: plotOverlap( inputFile, Signal, k, i[0], i[1], i[2], i[3], PU )
			#else: plot( inputFile, Signal, k, i[0], i[1], i[2], i[3], PU )
		plot( inputFileQCD, inputFileSignal, inputFileBoosted, i[0], i[1], i[2], i[3] )
