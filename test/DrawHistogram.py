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
	#----- Drawing -----------------------

	h1.GetXaxis().SetTitle( inPlotName )
	binWidth = h1.GetBinWidth(1)
	h1.GetYaxis().SetTitle( 'Events /'+str(binWidth) )


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

def plot2D( inFile, trigger, name, outName, plotName, inPlotName, inPlotName2, xmax, xmax2 ):
	"""docstring for plot"""

	outputFileName = trigger+'_'+outName+'_QCD_TriggerStudies.pdf' 
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
	setSelectionTrigger2D( 'QCD 13 TeV PU20bx25', trigger )
	can.SaveAs( 'Plots/'+outputFileName )
	del can



if __name__ == '__main__':

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

	
	inputFile = TFile.Open('HistoFiles/hlt_jetmass_QCD_Pt-ALL_TuneZ2star_13TeV_pythia8_PU20bx25.root')

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

	for i in range( len( Plots_2D ) ):
		plot2D( inputFile, Plots_2D[i][0], Plots_2D[i][1], Plots_2D[i][2], Plots_2D[i][3], Plots_2D[i][4], Plots_2D[i][5], Plots_2D[i][6], Plots_2D[i][6] )

#	HT = 'triggerPlotterHT'
#
#	plot( 'HT', 'ht', 'HT [GeV]', 300, True )
#	plot( 'jet1pt', 'jet1pt', 'Leading Jet Pt [GeV]', 100, True )
#	plot( 'jet1mass', 'jet1mass', 'Leading Jet Mass [GeV]', 20, True )
#	plot( 'eventJetMass', 'eventJetMass', 'Event Jet Mass [GeV]', 100, True )

	#treeplot(  )
