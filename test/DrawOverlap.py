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

def plot( inFile, signal, trigger, name, inFileName, xmin, xmax, PU):
	"""docstring for plot"""

	outputFileName = trigger+'_'+name+'_'+signal+'_'+PU+'_TriggerOverlap.pdf' 
	print 'Processing.......', outputFileName

	histos = inFile.Get( trigger+'/'+name )

	binWidth = histos.GetBinWidth(1)
	if 'overlap' in name: 
		histos.GetYaxis().SetTitle( 'Percentage')
		histos.SetMinimum( 0. )
		if 'QCD' in signal:
			histos.Scale( 1 / histos.Integral() )
	else: histos.GetYaxis().SetTitle( 'Events /' + str(binWidth) )

	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	histos.Draw()
	if 'overlap' in name: setOverlap( signal + ' 13 TeV '+ PU )
	else: setOverlapHistos( signal + ' 13 TeV '+ PU, inFileName )
	can.SaveAs( 'Plots/'+outputFileName )
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

def plotOverlap( inFile, signal, trigger, name, inFileName, xmax, xmax2, PU ):
	"""docstring for plot"""

	outputFileName = trigger+'_'+name+'_'+signal+'_'+PU+'_TriggerOverlap.pdf' 
	print 'Processing.......', outputFileName

	histo = inFile.Get( trigger+'/'+name )

	nEvents = histo.Integral()
	histo.Sumw2()
	histo.Scale(1/nEvents)
	labelBin = histo.GetXaxis().GetBinLabel(1)
	newLabelBin = labelBin.replace('TrimR0p1PT0p03Mass00_', '')
	histo.SetMarkerSize(2)
	histo.GetXaxis().SetBinLabel(1, newLabelBin)
	histo.GetYaxis().SetBinLabel(1, newLabelBin)
		
	#histo.GetXaxis().SetRange( 6, 15 )
	histo.SetMinimum( 0 )
	histo.SetMaximum( 0.6 )
	gStyle.SetPaintTextFormat("4.3f")
	gStyle.SetPadLeftMargin(0.3)
	gStyle.SetPadBottomMargin(0.2)
	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	#can.SetLogz()
	can.SetGrid()
	histo.Draw('colz')
	histo.Draw('texte same')
	setOverlap( signal + ' '+ PU)
	can.SaveAs( 'Plots/'+outputFileName )
	del can
	gROOT.Reset()




if __name__ == '__main__':

	PU = sys.argv[2]
	Signal = sys.argv[1] #'RPVSt100tojj'	
	inputFile = TFile.Open('overlapStudies_'+Signal+'_'+PU+'.root')
	plotsList = [
#			[ 'totalOverlapOverFourTriggers', '', 20, 50 ],
			#[ 'overlapTriggers', '', 20, 50 ],
#			[ 'overlapThreeSimpleTriggers', '', 20, 50 ],
#			[ 'MassOneAll', 'NO Trigger', 20, 50 ],
#			[ 'MassOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
#			[ 'MassTwo', 'PFHT900', 20, 50 ],
#			[ 'MassBoth', 'Both', 20, 50 ],
#			[ 'PtOneAll', 'NO Trigger', 20, 50 ],
#			[ 'PtOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
#			[ 'PtTwo', 'PFHT900', 20, 50 ],
#			[ 'PtBoth', 'Both', 20, 50 ],
#			[ 'HTOneAll', 'NO Trigger', 20, 50 ],
#			[ 'HTOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
#			[ 'HTTwo', 'PFHT900', 20, 50 ],
#			[ 'HTBoth', 'Both', 20, 50 ],
			[ 'HTvsMassOneAll', 'NO Trigger', 20, 50 ],
			[ 'HTvsMassOne', 'AK8PFHT850TrimMass', 20, 50 ],
			[ 'HTvsMassTwo', 'PFHT800', 20, 50 ],
			[ 'HTvsMassBoth', 'Both', 20, 50 ],
#			[ 'HTvsPtOneAll', 'NO Trigger', 20, 50 ],
#			[ 'HTvsPtOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
#			[ 'HTvsPtTwo', 'PFHT900', 20, 50 ],
#			[ 'HTvsPtBoth', 'Both', 20, 50 ],
#			[ 'PtvsMassOneAll', 'NO Trigger', 20, 50 ],
#			[ 'PtvsMassOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
#			[ 'PtvsMassTwo', 'PFHT900', 20, 50 ],
#			[ 'PtvsMassBoth', 'Both', 20, 50 ],
			]

	cat = [ 
			'AK8PFHT850TrimMass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30',
			'AK8PFHT800TrimMass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30',
			'AK8PFHT800TrimMass00TrimModvsPFHT900vsAK8PFJet360TrimModMass30',
			'AK8PFHT750TrimMass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30',
			'AK8PFHT850TrimMass50TrimModvsPFHT850vsAK8PFJet360TrimModMass30',
			'AK8PFTrimHT850Mass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30',
			'AK8PFTrimHT800Mass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30',
			'AK8PFTrimHT750Mass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30',
			'AK8PFTrimHT800Mass00TrimModvsPFHT900vsAK8PFJet360TrimModMass30',
			'AK8PFHT850TrimMass50TrimModvsPFHT800vsAK8PFJet360TrimModMass30'
			]

	for k in cat: 
		for i in plotsList: 
			if 'vs' in i[0]: plot2D( inputFile, Signal, k, i[0], i[1], i[2], i[3], PU )
			elif 'Overlap' in i[0]: plotOverlap( inputFile, Signal, k, i[0], i[1], i[2], i[3], PU )
			else: plot( inputFile, Signal, k, i[0], i[1], i[2], i[3], PU )
