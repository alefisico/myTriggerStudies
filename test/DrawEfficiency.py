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

def plot( inFile, signal, trigger, name, xmin, xmax, PU):
	"""docstring for plot"""

	outputFileName = trigger+'_'+name+'Efficiency_'+signal+'_'+PU+'_TriggerEfficiency.pdf' 
	print 'Processing.......', outputFileName

	histos = {}
	histos[ name+'Efficiency' ] = inFile.Get( trigger+'/'+name+'Efficiency' )
	histos[ name+'Denom' ] = inFile.Get( trigger+'/'+name+'Denom' )
	histos[ name+'Passing' ] = inFile.Get( trigger+'/'+name+'Passing' )

	for plot, histo in histos.iteritems():

		binWidth = histos.values()[0].GetBinWidth(1)
		
		if 'Efficiency' in plot:

			#histos[ name+'Passing'].Rebin( 2 )
			#histos[ name+'Denom'].Rebin( 2 )
			effHisto = TGraphAsymmErrors( histos[ name+'Passing'], histos[ name+'Denom' ], "B" )
			effHisto.GetYaxis().SetTitle( 'Efficiency / '+str(binWidth) )
			effHisto.GetXaxis().SetTitle( name + ' [GeV]' )
			effHisto.SetMaximum( 1.1 ) 
			effHisto.SetMinimum( -0.1 ) 
			effHisto.GetXaxis().SetRange( xmin, xmax )

			can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
			#gStyle.SetOptStat(1111)
			effHisto.Draw("AP")
			setEfficiencyTrigger( signal + ' 13 TeV '+ PU, trigger )
			can.SaveAs( 'Plots/'+outputFileName )
			del can
		else:
			histo.GetYaxis().SetTitle( 'Events / '+str(binWidth) )
			histo.GetXaxis().SetTitle( name + ' [GeV]' )
			#histo.GetXaxis().SetRange( xmin, xmax )

			can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
			can.SetLogy()
			histo.Sumw2()
			histo.Draw()
			setSelectionTrigger( signal + ' 13 TeV '+ PU, trigger, plot )
			can.SaveAs( 'Plots/'+trigger+'_'+plot+'_'+signal+'_'+PU+'_TriggerEfficiency.pdf' )
			del can


def plot2D( inFile, signal, trigger, name, xmax, xmax2, PU ):
	"""docstring for plot"""

	outputFileName = trigger+'_'+name+'Efficiency_'+signal+'_'+PU+'_TriggerEfficiency.pdf' 
	print 'Processing.......', outputFileName

	histos = {}
	histos[ name+'Efficiency' ] = inFile.Get( trigger+'/'+name+'2Defficiency' )
	histos[ name+'Denom' ] = inFile.Get( trigger+'/'+name+'Denom' )
	histos[ name+'Passing' ] = inFile.Get( trigger+'/'+name+'Passing' )

	for plot, histo in histos.iteritems():

		histo.GetXaxis().SetTitle( 'HT [GeV]' )
		histo.GetYaxis().SetTitle( 'Leading Jet Mass [GeV]')
		
		if 'Efficiency' in plot:
			histo.GetXaxis().SetRange( 6, 15 )
			histo.GetYaxis().SetRange( 0, 12 )
			gStyle.SetPaintTextFormat("4.3f")
			can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
			histo.Draw('colz')
			histo.Draw('same texte')
			setSelectionTrigger2D( signal + ' 13 TeV '+ PU, trigger, '' )
			can.SaveAs( 'Plots/'+outputFileName )
			del can
		else:
			histo.GetXaxis().SetRange( 0, 70 )
			histo.GetYaxis().SetRange( 0, 30 )
			can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
			can.SetLogz()
			histo.Draw('colz')
			setSelectionTrigger2D( signal + ' 13 TeV '+ PU, trigger, plot )
			can.SaveAs( 'Plots/'+trigger+'_'+plot+'_'+signal+'_'+PU+'_TriggerEfficiency.pdf' )
			del can



if __name__ == '__main__':

	PU = sys.argv[1]
	Signal = sys.argv[2] #'RPVSt100tojj'	
	inputFile = TFile.Open('filesWithHistos_'+Signal+'_13TeV_pythia8_'+PU+'.root')
	plotsList = [
#			['PFHT450', 'HT', 20, 50 ],
#			['PFHT450', 'jetMass', 0, 100 ],
#			['PFHT550', 'HT', 20, 50 ],
#			['PFHT550', 'jetMass', 0, 100 ],
#			['PFHT650', 'HT', 20, 50 ],
#			['PFHT650', 'jetMass', 0, 100 ],
#			['PFHT750', 'HT', 20, 50 ],
#			['PFHT750', 'jetMass', 0, 100 ],
#			['PFHT850', 'HT', 20, 50 ],
#			['PFHT850', 'jetMass', 0, 100 ],
#			['PFHT900', 'HT', 30, 65 ],
#			['PFHT900', 'jetMass', 0, 100 ],
#			['PFHT950', 'HT', 20, 50 ],
#			['PFHT950', 'jetMass', 0, 100 ],
#			['PFTrimHT450', 'HT', 20, 50 ],
#			['PFTrimHT450', 'jetMass', 0, 100 ],
#			['PFTrimHT450', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550', 'HT', 20, 50 ],
#			['PFTrimHT550', 'jetMass', 0, 100 ],
#			['PFTrimHT550', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650', 'HT', 20, 50 ],
#			['PFTrimHT650', 'jetMass', 0, 100 ],
#			['PFTrimHT650', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750', 'HT', 20, 50 ],
#			['PFTrimHT750', 'jetMass', 0, 100 ],
#			['PFTrimHT750', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850', 'HT', 20, 50 ],
#			['PFTrimHT850', 'jetMass', 0, 100 ],
#			['PFTrimHT850', 'jetMassHT', 0, 100 ],
#			['AK8PFHT450', 'HT', 20, 50 ],
#			['AK8PFHT450', 'jetMass', 0, 100 ],
#			['AK8PFHT450', 'jetMassHT', 0, 100 ],
#			['AK8PFHT550', 'HT', 20, 50 ],
#			['AK8PFHT550', 'jetMass', 0, 100 ],
#			['AK8PFHT550', 'jetMassHT', 0, 100 ],
#			['AK8PFHT650', 'HT', 20, 50 ],
#			['AK8PFHT650', 'jetMass', 0, 100 ],
#			['AK8PFHT650', 'jetMassHT', 0, 100 ],
#			['AK8PFHT750', 'HT', 20, 50 ],
#			['AK8PFHT750', 'jetMass', 0, 100 ],
#			['AK8PFHT750', 'jetMassHT', 0, 100 ],
#			['AK8PFHT850', 'HT', 20, 50 ],
#			['AK8PFHT850', 'jetMass', 0, 100 ],
#			['AK8PFHT850', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450', 'HT', 20, 50 ],
#			['AK8PFTrimHT450', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550', 'HT', 20, 50 ],
#			['AK8PFTrimHT550', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650', 'HT', 20, 50 ],
#			['AK8PFTrimHT650', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750', 'HT', 20, 50 ],
#			['AK8PFTrimHT750', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850', 'HT', 20, 50 ],
#			['AK8PFTrimHT850', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass00', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass00', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass00', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass05', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass05', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass05', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass10', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass10', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass10', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass15', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass15', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass15', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass20', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass20', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass20', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass25', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass25', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass25', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass30', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass30', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass30', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass35', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass35', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass35', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass40', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass40', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass40', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass45', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass45', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass45', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass50', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass50', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass50', 'jetMassHT', 0, 100 ],
#			['PFTrimHT450TrimMass55', 'HT', 20, 50 ],
#			['PFTrimHT450TrimMass55', 'jetMass', 0, 100 ],
#			['PFTrimHT450TrimMass55', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass00', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass00', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass00', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass05', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass05', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass05', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass10', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass10', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass10', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass15', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass15', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass15', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass20', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass20', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass20', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass25', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass25', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass25', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass30', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass30', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass30', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass35', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass35', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass35', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass40', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass40', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass40', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass45', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass45', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass45', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass50', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass50', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass50', 'jetMassHT', 0, 100 ],
#			['PFTrimHT550TrimMass55', 'HT', 20, 50 ],
#			['PFTrimHT550TrimMass55', 'jetMass', 0, 100 ],
#			['PFTrimHT550TrimMass55', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass00', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass00', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass00', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass05', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass05', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass05', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass10', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass10', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass10', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass15', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass15', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass15', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass20', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass20', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass20', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass25', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass25', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass25', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass30', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass30', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass30', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass35', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass35', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass35', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass40', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass40', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass40', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass45', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass45', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass45', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass50', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass50', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass50', 'jetMassHT', 0, 100 ],
#			['PFTrimHT650TrimMass55', 'HT', 20, 50 ],
#			['PFTrimHT650TrimMass55', 'jetMass', 0, 100 ],
#			['PFTrimHT650TrimMass55', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass00', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass00', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass00', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass05', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass05', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass05', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass10', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass10', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass10', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass15', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass15', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass15', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass20', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass20', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass20', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass25', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass25', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass25', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass30', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass30', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass30', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass35', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass35', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass35', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass40', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass40', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass40', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass45', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass45', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass45', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass50', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass50', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass50', 'jetMassHT', 0, 100 ],
#			['PFTrimHT750TrimMass55', 'HT', 20, 50 ],
#			['PFTrimHT750TrimMass55', 'jetMass', 0, 100 ],
#			['PFTrimHT750TrimMass55', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass00', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass00', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass00', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass05', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass05', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass05', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass10', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass10', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass10', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass15', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass15', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass15', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass20', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass20', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass20', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass25', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass25', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass25', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass30', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass30', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass30', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass35', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass35', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass35', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass40', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass40', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass40', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass45', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass45', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass45', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass50', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass50', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass50', 'jetMassHT', 0, 100 ],
#			['PFTrimHT850TrimMass55', 'HT', 20, 50 ],
#			['PFTrimHT850TrimMass55', 'jetMass', 0, 100 ],
#			['PFTrimHT850TrimMass55', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass00', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass00', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass00', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass05', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass05', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass05', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass10', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass10', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass10', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass15', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass15', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass15', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass20', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass20', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass20', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass25', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass25', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass25', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass30', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass30', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass30', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass35', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass35', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass35', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass40', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass40', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass40', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass45', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass45', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass45', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass50', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass50', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass50', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT450TrimMass55', 'HT', 20, 50 ],
#			['AK8PFTrimHT450TrimMass55', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT450TrimMass55', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass00', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass00', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass00', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass05', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass05', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass05', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass10', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass10', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass10', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass15', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass15', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass15', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass20', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass20', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass20', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass25', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass25', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass25', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass30', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass30', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass30', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass35', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass35', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass35', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass40', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass40', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass40', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass45', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass45', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass45', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass50', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass50', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass50', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT550TrimMass55', 'HT', 20, 50 ],
#			['AK8PFTrimHT550TrimMass55', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT550TrimMass55', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass00', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass00', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass00', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass05', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass05', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass05', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass10', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass10', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass10', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass15', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass15', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass15', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass20', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass20', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass20', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass25', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass25', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass25', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass30', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass30', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass30', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass35', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass35', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass35', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass40', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass40', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass40', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass45', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass45', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass45', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass50', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass50', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass50', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT650TrimMass55', 'HT', 20, 50 ],
#			['AK8PFTrimHT650TrimMass55', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT650TrimMass55', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass00', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass00', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass00', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass05', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass05', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass05', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass10', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass10', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass10', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass15', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass15', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass15', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass20', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass20', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass20', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass25', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass25', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass25', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass30', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass30', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass30', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass35', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass35', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass35', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass40', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass40', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass40', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass45', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass45', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass45', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass50', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass50', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass50', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT750TrimMass55', 'HT', 20, 50 ],
#			['AK8PFTrimHT750TrimMass55', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT750TrimMass55', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass00', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass00', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass00', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass05', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass05', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass05', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass10', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass10', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass10', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass15', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass15', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass15', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass20', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass20', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass20', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass25', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass25', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass25', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass30', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass30', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass30', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass35', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass35', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass35', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass40', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass40', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass40', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass45', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass45', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass45', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass50', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass50', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass50', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass50TrimMod', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass50TrimMod', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass50TrimMod', 'jetMassHT', 0, 100 ],
		#	['AK8PFTrimHT850TrimMass40AK4CaloHT', 'HT', 20, 50 ],
		#	['AK8PFTrimHT850TrimMass40AK4CaloHT', 'jetMass', 0, 100 ],
		#	['AK8PFTrimHT850TrimMass40AK4CaloHT', 'jetMassHT', 0, 100 ],
#			['AK8PFTrimHT850TrimMass55', 'HT', 20, 50 ],
#			['AK8PFTrimHT850TrimMass55', 'jetMass', 0, 100 ],
#			['AK8PFTrimHT850TrimMass55', 'jetMassHT', 0, 100 ],
			]
	for i in plotsList: 
		if 'jetMassHT' in i[1]: plot2D( inputFile, Signal, i[0], i[1], i[2], i[3], PU )
		else: plot( inputFile, Signal, i[0], i[1], i[2], i[3], PU )
