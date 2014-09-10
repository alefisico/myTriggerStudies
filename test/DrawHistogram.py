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

def plot( inFile, trigger, name, inPlotName, xmax, log ):
	"""docstring for plot"""

	outputFileName = name+'_QCD_TriggerStudies.pdf' 
	print 'Processing.......', outputFileName

	histos = {}
	legend=TLegend(0.65,0.70,0.90,0.90)
	legend.SetFillStyle(0)
	legend.SetTextSize(0.03)

	if trigger[0][0] is trigger[1][0]:
		for i in trigger: 
			histos[ i[1] ] = inFile.Get( 'triggerPlotter'+i[0]+'/'+i[1] )
			legend.AddEntry( histos[ i[1] ], i[2] , 'l' )
	else:
		for i in trigger: 
			histos[ i[0] ] = inFile.Get( 'triggerPlotter'+i[0]+'/'+i[1] )
			legend.AddEntry( histos[ i[0] ], i[2] , 'l' )

	histos.values()[0].GetXaxis().SetTitle( inPlotName )
	binWidth = histos.values()[0].GetBinWidth(1)
	histos.values()[0].GetYaxis().SetTitle( 'Events / '+str(binWidth) )

	k = 0
	listMax = []

	for t, histo in histos.items():
		k += 1
		histo.SetLineColor(k)
		histo.SetLineWidth(2)
		listMax.append( histo.GetBinContent(histo.GetMaximumBin()) )
	#	legend.AddEntry( histo, t , 'l' )

	histos.values()[0].SetMaximum( 2* max( listMax ) ) 
	histos.values()[0].GetXaxis().SetRange( 0, xmax )

	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	if log: can.SetLogy()
	#h1.Sumw2()
	histos.values()[0].Draw('hist')
	for q in range( 1, len( histos.keys() ) ): histos.values()[q].Draw('hist same')
	legend.Draw()
	setSelectionTrigger( 'QCD 13 TeV PU20bx25' )
	can.SaveAs( 'Plots/'+outputFileName )
	del can

def plot2D( inFile, trigger, name, outName, plotName, inPlotName, inPlotName2, xmax, xmax2, PU ):
	"""docstring for plot"""

	outputFileName = trigger+'_'+outName+'_'+PU+'_QCD_TriggerStudies.pdf' 
	print 'Processing.......', outputFileName
	h1 = inFile.Get( 'triggerPlotter'+trigger+'/'+name )

	h1.SetTitle( plotName )
	h1.GetXaxis().SetTitle( inPlotName )
	h1.GetYaxis().SetTitle( inPlotName2 )

	if not '' in (xmax or xmax2):
		h1.GetXaxis().SetRange( 0, xmax )
		h1.GetYaxis().SetRange( 0, xmax2 )

	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	can.SetLogz()
	h1.Draw('colz')
	setSelectionTrigger2D( 'QCD 13 TeV '+PU, trigger )
	can.SaveAs( 'Plots/'+outputFileName )
	del can



if __name__ == '__main__':

	PU = sys.argv[0]
	process = sys.argv[1]
	####### Labels:
	# HT
	# - regular: AK4 calojets with AK4 corr
	# - NOJEC: AK4 calojets 
	# PFNoPUHT
	# - regular: AK4 jets with AK4 corr and NoPU
	# - NOJEC: AK4 jets with NoPU
	# PFHT
	# - regular: AK4 jets with AK4 corr
	# - NOJEC: AK4 jets
	# AK8PFHT
	# - regular: AK8 jets with AK4 corr
	# - NOJEC: AK8 jets
	# AK8PFTrimHT
	# - regular: AK8 jets with AK4 corr and then trimming
	# PFAK8HT
	# - NOJEC: with AK4 corr jets, recluster using AK8
	# PFAK8Trim
	# - NOJEC: with AK4 corr jets, recluster using AK8 and trimming

	
	inputFile = TFile.Open('HistoFiles/hlt_jetmass_QCD_Pt-ALL_TuneZ2star_13TeV_pythia8_'+PU+'.root')

	if process is '2D':
		Plots_2D = [ 
			[ 'HT', 'HTvsJet1mass', 'HTvsJet1mass','HT vs Leading Jet Mass', 'HT [GeV]', 'Leading Jet Mass [GeV]', '', '' ],
			[ 'PFNoPUHT', 'HTvsJet1mass', 'HTvsJet1mass', 'HT vs Leading Jet Mass', 'HT [GeV]', 'Leading Jet Mass [GeV]', '', '' ],
			[ 'PFHT', 'HTvsJet1mass', 'HTvsJet1mass', 'HT vs Leading Jet Mass', 'HT [GeV]', 'Leading Jet Mass [GeV]', '', '' ],
			[ 'PFAK8HT', 'HTvsJet1mass_NOJEC', 'HTvsJet1mass', 'HT vs Leading Jet Mass', 'HT [GeV]', 'Leading Jet Mass [GeV]', '', '' ],
			[ 'PFAK8Trim', 'HTvsJet1mass_NOJEC', 'HTvsJet1mass', 'HT vs Leading Jet Mass', 'HT [GeV]', 'Leading Jet Mass [GeV]', '', '' ],
			[ 'AK8PFHT', 'HTvsJet1mass', 'HTvsJet1mass', 'HT vs Leading Jet Mass', 'HT [GeV]', 'Leading Jet Mass [GeV]', '', '' ],
			[ 'AK8PFTrimHT', 'HTvsJet1mass', 'HTvsJet1mass', 'HT vs Leading Jet Mass', 'HT [GeV]', 'Leading Jet Mass [GeV]', '', '' ],
			[ 'HT', 'HTvsJet1pt', 'HTvsJet1pt','HT vs Leading Jet Pt', 'HT [GeV]', 'Leading Jet Pt [GeV]', '', '' ],
			[ 'PFNoPUHT', 'HTvsJet1pt', 'HTvsJet1pt', 'HT vs Leading Jet Pt', 'HT [GeV]', 'Leading Jet Pt [GeV]', '', '' ],
			[ 'PFHT', 'HTvsJet1pt', 'HTvsJet1pt', 'HT vs Leading Jet Pt', 'HT [GeV]', 'Leading Jet Pt [GeV]', '', '' ],
			[ 'PFAK8HT', 'HTvsJet1pt_NOJEC', 'HTvsJet1pt', 'HT vs Leading Jet Pt', 'HT [GeV]', 'Leading Jet Pt [GeV]', '', '' ],
			[ 'PFAK8Trim', 'HTvsJet1pt_NOJEC', 'HTvsJet1pt', 'HT vs Leading Jet Pt', 'HT [GeV]', 'Leading Jet Pt [GeV]', '', '' ],
			[ 'AK8PFHT', 'HTvsJet1pt', 'HTvsJet1pt', 'HT vs Leading Jet Pt', 'HT [GeV]', 'Leading Jet Pt [GeV]', '', '' ],
			[ 'AK8PFTrimHT', 'HTvsJet1pt', 'HTvsJet1pt', 'HT vs Leading Jet Pt', 'HT [GeV]', 'Leading Jet Pt [GeV]', '', '' ],
			[ 'HT', 'HTvsEventJetMass', 'HTvsEventJetMass','HT vs Event Jet Mass', 'HT [GeV]', 'Event Jet Mass [GeV]', '', '' ],
			[ 'PFNoPUHT', 'HTvsEventJetMass', 'HTvsEventJetMass', 'HT vs Event Jet Mass', 'HT [GeV]', 'Event Jet Mass [GeV]', '', '' ],
			[ 'PFHT', 'HTvsEventJetMass', 'HTvsEventJetMass', 'HT vs Event Jet Mass', 'HT [GeV]', 'Event Jet Mass [GeV]', '', '' ],
			[ 'PFAK8HT', 'HTvsEventJetMass_NOJEC', 'HTvsEventJetMass', 'HT vs Event Jet Mass', 'HT [GeV]', 'Event Jet Mass [GeV]', '', '5' ],
			[ 'PFAK8Trim', 'HTvsEventJetMass_NOJEC', 'HTvsEventJetMass', 'HT vs Event Jet Mass', 'HT [GeV]', 'Event Jet Mass [GeV]', '', '5' ],
			[ 'AK8PFHT', 'HTvsEventJetMass', 'HTvsEventJetMass', 'HT vs Event Jet Mass', 'HT [GeV]', 'Event Jet Mass [GeV]', '', '' ],
			[ 'AK8PFTrimHT', 'HTvsEventJetMass', 'HTvsEventJetMass', 'HT vs Event Jet Mass', 'HT [GeV]', 'Event Jet Mass [GeV]', '', '' ],
			]

		for i in Plots_2D: plot2D( inputFile, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[6], PU )

	elif process is '1D'
		Plots = [
			[[ ['HT', 'hltHT', 'Trigger HT'], ['HT', 'ht', 'My HT']], 'offlineHT_HT', 'HT [GeV]', 100, True ],
			[[ ['PFHT', 'hltHT', 'Trigger HT'], ['PFHT', 'ht', 'My HT']], 'offlineHT_PFHT', 'HT [GeV]', 100, True ],
			[[ ['PFAK8TrimHT', 'hltHT', 'Trigger HT'], ['PFAK8TrimHT', 'ht', 'My HT']], 'offlineHT_PFAK8TrimHT', 'HT [GeV]', 100, True ],
			[[ ['AK8PFTrimHT', 'hltHT', 'Trigger HT'], ['AK8PFTrimHT', 'ht', 'My HT']], 'offlineHT_AK8PFTrimHT', 'HT [GeV]', 100, True ],
			[[ ['HT', 'ht', 'HT'], ['PFHT', 'ht', 'PFHT'], ['PFNoPUHT', 'ht', 'PFNoPUHT'] ], 'oldTriggers_ht', 'HT [GeV]', 100, True ],
			[[ ['HT', 'numJets', 'HT'], ['PFHT', 'numJets', 'PFHT'], ['PFNoPUHT', 'numJets', 'PFNoPUHT'] ], 'oldTriggers_numJets', 'Jet Multiplicity', 100, False ],
			[[ ['HT', 'jet1pt', 'HT'], ['PFHT', 'jet1pt', 'PFHT'], ['PFNoPUHT', 'jet1pt', 'PFNoPUHT'] ], 'oldTriggers_jet1pt', 'Leading Jet Pt [GeV]', 100, True ],
			[[ ['HT', 'jet1mass', 'HT'], ['PFHT', 'jet1mass', 'PFHT'], ['PFNoPUHT', 'jet1mass', 'PFNoPUHT'] ], 'oldTriggers_jet1mass', 'Leading Jet Mass [GeV]', 100, True ],
			[[ ['HT', 'eventJetMass', 'HT'], ['PFHT', 'eventJetMass', 'PFHT'], ['PFNoPUHT', 'eventJetMass', 'PFNoPUHT'] ], 'oldTriggers_eventJetMass', 'Event Jet Mass [GeV]', 100, True ],
			[[ ['PFHT', 'ht', 'PFHT'], ['PFAK8Trim', 'ht_NOJEC', 'AK4 to AK8 Trim'], ['AK8PFTrimHT', 'ht', 'AK8 with AK4 JEC - Trim'] ], 'newTriggers_ht', 'HT [GeV]', 100, True ],
			[[ ['PFHT', 'numJets', 'PFHT'], ['PFAK8Trim', 'numJets_NOJEC', 'AK4 to AK8 Trim'], ['AK8PFTrimHT', 'numJets', 'AK8 with AK4 JEC - Trim'] ], 'newTriggers_numJets', 'Jet Multiplicity', 100, False ],
			[[ ['PFHT', 'jet1pt', 'PFHT'], ['PFAK8Trim', 'jet1pt_NOJEC', 'AK4 to AK8 Trim'], ['AK8PFTrimHT', 'jet1pt', 'AK8 with AK4 JEC - Trim'] ], 'newTriggers_jet1pt', 'Leading Jet Pt [GeV]', 100, True ],
			[[ ['PFHT', 'jet1mass', 'PFHT'], ['PFAK8Trim', 'jet1mass_NOJEC', 'AK4 to AK8 Trim'], ['AK8PFTrimHT', 'jet1mass', 'AK8 with AK4 JEC - Trim'] ], 'newTriggers_jet1mass', 'Leading Jet Mass [GeV]', 100, True ],
			[[ ['PFHT', 'eventJetMass', 'PFHT'], ['PFAK8Trim', 'eventJetMass_NOJEC', 'AK4 to AK8 Trim'], ['AK8PFTrimHT', 'eventJetMass', 'AK8 with AK4 JEC - Trim'] ], 'newTriggers_eventJetMass', 'Event Jet Mass [GeV]', 100, True ],
			[[ ['PFAK8Trim', 'ht_NOJEC', 'AK4 to AK8 Trim'], ['PFAK8HT', 'ht_NOJEC', 'AK4 to AK8'] ], 'DiffTrimPFAK8_ht', 'HT [GeV]', 100, True ],
			[[ ['PFAK8Trim', 'numJets_NOJEC', 'AK4 to AK8 Trim'], ['PFAK8HT', 'numJets_NOJEC', 'AK4 to AK8'] ], 'DiffTrimPFAK8_numJets', 'Jet Multiplicity', 100, False ],
			[[ ['PFAK8Trim', 'jet1pt_NOJEC', 'AK4 to AK8 Trim'], ['PFAK8HT', 'jet1pt_NOJEC', 'AK4 to AK8'] ], 'DiffTrimPFAK8_jet1pt', 'Leading Jet Pt [GeV]', 100, True ],
			[[ ['PFAK8Trim', 'jet1mass_NOJEC', 'AK4 to AK8 Trim'], ['PFAK8HT', 'jet1mass_NOJEC', 'AK4 to AK8'] ], 'DiffTrimPFAK8_jet1mass', 'Leading Jet Mass [GeV]', 100, True ],
			[[ ['PFAK8Trim', 'eventJetMass_NOJEC', 'AK4 to AK8 Trim'], ['PFAK8HT', 'eventJetMass_NOJEC', 'AK4 to AK8'] ], 'DiffTrimPFAK8_eventJetMass', 'Event Jet Mass [GeV]', 100, True ],
			[[ ['AK8PFTrimHT', 'ht', 'AK8 with AK4 JEC Trim'], ['AK8PFHT', 'ht', 'AK8 with AK4 JEC'] ], 'DiffTrimAK8PF_ht', 'HT [GeV]', 100, True ],
			[[ ['AK8PFTrimHT', 'numJets', 'AK8 with AK4 JEC Trim'], ['AK8PFHT', 'numJets', 'AK8 with AK4 JEC'] ], 'DiffTrimAK8PF_numJets', 'Jet Multiplicity', 100, False ],
			[[ ['AK8PFTrimHT', 'jet1pt', 'AK8 with AK4 JEC Trim'], ['AK8PFHT', 'jet1pt', 'AK8 with AK4 JEC'] ], 'DiffTrimAK8PF_jet1pt', 'Leading Jet Pt [GeV]', 100, True ],
			[[ ['AK8PFTrimHT', 'jet1mass', 'AK8 with AK4 JEC Trim'], ['AK8PFHT', 'jet1mass', 'AK8 with AK4 JEC'] ], 'DiffTrimAK8PF_jet1mass', 'Leading Jet Mass [GeV]', 100, True ],
			[[ ['AK8PFTrimHT', 'eventJetMass', 'AK8 with AK4 JEC Trim'], ['AK8PFHT', 'eventJetMass', 'AK8 with AK4 JEC'] ], 'DiffTrimAK8PF_eventJetMass', 'Event Jet Mass [GeV]', 100, True ],
			[[ ['PFHT', 'ht', 'AK4 with AK4 JEC'], ['AK8PFHT', 'ht', 'AK8 with AK4 JEC'] ], 'DiffAKRadius_ht', 'HT [GeV]', 100, True ],
			[[ ['PFHT', 'numJets', 'AK4 with AK4 JEC'], ['AK8PFHT', 'numJets', 'AK8 with AK4 JEC'] ], 'DiffAKRadius_numJets', 'Jet Multiplicity', 100, False ],
			[[ ['PFHT', 'jet1pt', 'AK4 with AK4 JEC'], ['AK8PFHT', 'jet1pt', 'AK8 with AK4 JEC'] ], 'DiffAKRadius_jet1pt', 'Leading Jet Pt [GeV]', 100, True ],
			[[ ['PFHT', 'jet1mass', 'AK4 with AK4 JEC'], ['AK8PFHT', 'jet1mass', 'AK8 with AK4 JEC'] ], 'DiffAKRadius_jet1mass', 'Leading Jet Mass [GeV]', 100, True ],
			[[ ['PFHT', 'eventJetMass', 'AK4 with AK4 JEC'], ['AK8PFHT', 'eventJetMass', 'AK8 with AK4 JEC'] ], 'DiffAKRadius_eventJetMass', 'Event Jet Mass [GeV]', 100, True ],
			]

		for i in Plots: plot( inputFile, i[0], i[1], i[2], i[3], i[4], PU )
