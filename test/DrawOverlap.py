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

	#histo.GetXaxis().SetTitle( 'HT [GeV]' )
	#histo.GetYaxis().SetTitle( 'Leading Jet Mass [GeV]')
		
	#histo.GetXaxis().SetRange( 6, 15 )
	#histo.GetYaxis().SetRange( 0, 12 )
	#gStyle.SetPaintTextFormat("4.3f")
	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	can.SetLogz()
	histos.Draw('colz')
	#histo.Draw('same texte')
	setOverlapHistos( signal + ' 13 TeV '+ PU, inFileName )
	can.SaveAs( 'Plots/'+outputFileName )
	del can



if __name__ == '__main__':

	PU = sys.argv[1]
	Signal = sys.argv[2] #'RPVSt100tojj'	
	inputFile = TFile.Open('overlapStudies_'+Signal+'_'+PU+'.root')
	plotsList = [
			[ 'overlapOverAllTriggers', '', 20, 50 ],
			[ 'overlapTriggers', '', 20, 50 ],
			[ 'overlapSimpleTriggers', '', 20, 50 ],
			[ 'MassOneAll', 'NO Trigger', 20, 50 ],
			[ 'MassOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
			[ 'MassTwo', 'PFHT900', 20, 50 ],
			[ 'MassBoth', 'Both', 20, 50 ],
			[ 'PtOneAll', 'NO Trigger', 20, 50 ],
			[ 'PtOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
			[ 'PtTwo', 'PFHT900', 20, 50 ],
			[ 'PtBoth', 'Both', 20, 50 ],
			[ 'HTOneAll', 'NO Trigger', 20, 50 ],
			[ 'HTOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
			[ 'HTTwo', 'PFHT900', 20, 50 ],
			[ 'HTBoth', 'Both', 20, 50 ],
			[ 'HTvsMassOneAll', 'NO Trigger', 20, 50 ],
			[ 'HTvsMassOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
			[ 'HTvsMassTwo', 'PFHT900', 20, 50 ],
			[ 'HTvsMassBoth', 'Both', 20, 50 ],
			[ 'HTvsPtOneAll', 'NO Trigger', 20, 50 ],
			[ 'HTvsPtOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
			[ 'HTvsPtTwo', 'PFHT900', 20, 50 ],
			[ 'HTvsPtBoth', 'Both', 20, 50 ],
			[ 'PtvsMassOneAll', 'NO Trigger', 20, 50 ],
			[ 'PtvsMassOne', 'AK8PFTrimHT850TrimMass', 20, 50 ],
			[ 'PtvsMassTwo', 'PFHT900', 20, 50 ],
			[ 'PtvsMassBoth', 'Both', 20, 50 ],
			]

	cat = [ 
			'AK8PFTrimHT850TrimMass50vsPFHT900', 
			'AK8PFTrimHT850TrimMass50TrimModvsPFHT900', 
			#'AK8PFTrimHT850TrimMass40AK4CaloHTvsPFHT900', 
			'AK8PFTrimHT850TrimMass50vsAK8PFJet360TrimMass30TrimMod',
			'AK8PFTrimHT850TrimMass50TrimModvsAK8PFJet360TrimMass30TrimMod', 
			#'AK8PFTrimHT850TrimMass40AK4CaloHTvsAK8PFJet360TrimMass30TrimMod' 
			]

	for k in cat: 
		for i in plotsList: 
			if 'vs' in i[0]: plot2D( inputFile, Signal, k, i[0], i[1], i[2], i[3], PU )
			else: plot( inputFile, Signal, k, i[0], i[1], i[2], i[3], PU )
