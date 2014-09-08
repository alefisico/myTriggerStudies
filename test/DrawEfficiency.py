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
			setSelectionTrigger( signal + ' 13 TeV '+ PU, trigger+' '+plot )
			can.SaveAs( 'Plots/'+trigger+'_'+plot+'_'+signal+'_'+PU+'_TriggerEfficiency.pdf' )
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

	PU = sys.argv[1]
	Signal = sys.argv[2] #'RPVSt100tojj'	
	inputFile = TFile.Open('filesWithHistos_'+Signal+'_13TeV_pythia8_'+PU+'.root')
	plotsList = [
			['PFHT450', 'HT', 20, 50 ],
			['PFHT450', 'jetMass', 0, 100 ],
			['PFHT550', 'HT', 20, 50 ],
			['PFHT550', 'jetMass', 0, 100 ],
			['PFHT650', 'HT', 20, 50 ],
			['PFHT650', 'jetMass', 0, 100 ],
			['PFHT750', 'HT', 20, 50 ],
			['PFHT750', 'jetMass', 0, 100 ],
			['PFHT850', 'HT', 20, 50 ],
			['PFHT850', 'jetMass', 0, 100 ],
			['PFHT900', 'HT', 20, 50 ],
			['PFHT900', 'jetMass', 0, 100 ],
			['PFHT950', 'HT', 20, 50 ],
			['PFHT950', 'jetMass', 0, 100 ],
			['PFTrimHT450', 'HT', 20, 50 ],
			['PFTrimHT450', 'jetMass', 0, 100 ],
			['PFTrimHT550', 'HT', 20, 50 ],
			['PFTrimHT550', 'jetMass', 0, 100 ],
			['PFTrimHT650', 'HT', 20, 50 ],
			['PFTrimHT650', 'jetMass', 0, 100 ],
			['PFTrimHT750', 'HT', 20, 50 ],
			['PFTrimHT750', 'jetMass', 0, 100 ],
			['PFTrimHT850', 'HT', 20, 50 ],
			['PFTrimHT850', 'jetMass', 0, 100 ],
			['AK8PFHT450', 'HT', 20, 50 ],
			['AK8PFHT450', 'jetMass', 0, 100 ],
			['AK8PFHT550', 'HT', 20, 50 ],
			['AK8PFHT550', 'jetMass', 0, 100 ],
			['AK8PFHT650', 'HT', 20, 50 ],
			['AK8PFHT650', 'jetMass', 0, 100 ],
			['AK8PFHT750', 'HT', 20, 50 ],
			['AK8PFHT750', 'jetMass', 0, 100 ],
			['AK8PFHT850', 'HT', 20, 50 ],
			['AK8PFHT850', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450', 'HT', 20, 50 ],
			['AK8PFTrimHT450', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550', 'HT', 20, 50 ],
			['AK8PFTrimHT550', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650', 'HT', 20, 50 ],
			['AK8PFTrimHT650', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750', 'HT', 20, 50 ],
			['AK8PFTrimHT750', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850', 'HT', 20, 50 ],
			['AK8PFTrimHT850', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass00', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass00', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass05', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass05', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass10', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass10', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass15', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass15', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass20', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass20', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass25', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass25', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass30', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass30', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass35', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass35', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass40', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass40', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass45', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass45', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass50', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass50', 'jetMass', 0, 100 ],
			['PFTrimHT450TrimMass55', 'HT', 20, 50 ],
			['PFTrimHT450TrimMass55', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass00', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass00', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass05', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass05', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass10', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass10', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass15', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass15', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass20', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass20', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass25', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass25', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass30', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass30', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass35', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass35', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass40', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass40', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass45', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass45', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass50', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass50', 'jetMass', 0, 100 ],
			['PFTrimHT550TrimMass55', 'HT', 20, 50 ],
			['PFTrimHT550TrimMass55', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass00', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass00', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass05', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass05', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass10', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass10', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass15', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass15', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass20', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass20', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass25', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass25', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass30', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass30', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass35', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass35', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass40', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass40', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass45', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass45', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass50', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass50', 'jetMass', 0, 100 ],
			['PFTrimHT650TrimMass55', 'HT', 20, 50 ],
			['PFTrimHT650TrimMass55', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass00', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass00', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass05', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass05', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass10', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass10', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass15', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass15', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass20', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass20', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass25', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass25', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass30', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass30', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass35', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass35', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass40', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass40', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass45', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass45', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass50', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass50', 'jetMass', 0, 100 ],
			['PFTrimHT750TrimMass55', 'HT', 20, 50 ],
			['PFTrimHT750TrimMass55', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass00', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass00', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass05', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass05', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass10', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass10', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass15', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass15', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass20', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass20', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass25', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass25', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass30', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass30', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass35', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass35', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass40', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass40', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass45', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass45', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass50', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass50', 'jetMass', 0, 100 ],
			['PFTrimHT850TrimMass55', 'HT', 20, 50 ],
			['PFTrimHT850TrimMass55', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass00', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass00', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass05', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass05', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass10', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass10', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass15', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass15', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass20', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass20', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass25', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass25', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass30', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass30', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass35', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass35', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass40', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass40', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass45', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass45', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass50', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass50', 'jetMass', 0, 100 ],
			['AK8PFTrimHT450TrimMass55', 'HT', 20, 50 ],
			['AK8PFTrimHT450TrimMass55', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass00', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass00', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass05', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass05', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass10', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass10', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass15', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass15', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass20', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass20', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass25', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass25', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass30', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass30', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass35', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass35', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass40', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass40', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass45', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass45', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass50', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass50', 'jetMass', 0, 100 ],
			['AK8PFTrimHT550TrimMass55', 'HT', 20, 50 ],
			['AK8PFTrimHT550TrimMass55', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass00', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass00', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass05', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass05', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass10', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass10', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass15', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass15', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass20', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass20', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass25', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass25', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass30', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass30', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass35', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass35', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass40', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass40', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass45', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass45', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass50', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass50', 'jetMass', 0, 100 ],
			['AK8PFTrimHT650TrimMass55', 'HT', 20, 50 ],
			['AK8PFTrimHT650TrimMass55', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass00', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass00', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass05', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass05', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass10', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass10', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass15', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass15', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass20', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass20', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass25', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass25', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass30', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass30', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass35', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass35', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass40', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass40', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass45', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass45', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass50', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass50', 'jetMass', 0, 100 ],
			['AK8PFTrimHT750TrimMass55', 'HT', 20, 50 ],
			['AK8PFTrimHT750TrimMass55', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass00', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass00', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass05', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass05', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass10', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass10', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass15', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass15', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass20', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass20', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass25', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass25', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass30', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass30', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass35', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass35', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass40', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass40', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass45', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass45', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass50', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass50', 'jetMass', 0, 100 ],
			['AK8PFTrimHT850TrimMass55', 'HT', 20, 50 ],
			['AK8PFTrimHT850TrimMass55', 'jetMass', 0, 100 ],
			]
	for i in plotsList: plot( inputFile, Signal, i[0], i[1], i[2], i[3], PU )

	sys.exit(0)
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
