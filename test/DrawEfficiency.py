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

		histo.GetYaxis().SetTitle( 'HT [GeV]' )
		histo.GetXaxis().SetTitle( 'Leading Jet Trimmed Mass [GeV]')
		
		if 'Efficiency' in plot:
			histo.GetXaxis().SetRange( 1, 10 )
			#histo.GetYaxis().SetRange( 0, 15 )
			gStyle.SetPaintTextFormat("4.2f")
			can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
			histo.Draw('colz')
			histo.Draw('same text')
			setSelectionTrigger2D( signal + ' 13 TeV '+ PU, trigger, '' )
			can.SaveAs( 'Plots/'+outputFileName )
			del can
		else:
			histo.GetXaxis().SetRange( 1, 10 )
			#histo.GetYaxis().SetRange( 0, 15 )
			can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
			can.SetLogz()
			histo.Draw('colz')
			setSelectionTrigger2D( signal + ' 13 TeV '+ PU, trigger, plot )
			can.SaveAs( 'Plots/'+trigger+'_'+plot+'_'+signal+'_'+PU+'_TriggerEfficiency.pdf' )
			del can


def plotDiffPU( inFile, signal, trigger, name1, xmin, xmax, PU ):
	"""docstring for plot"""

	name = name1.replace('Efficiency','')
	outputFileName = trigger+'_'+name+'Efficiency_DiffPU_'+signal+'_'+PU+'_TriggerEfficiency.pdf' 
	print 'Processing.......', outputFileName

	histos = {}
	histos[ 'lowPU'+name+'Denom' ] = inFile.Get( trigger+'/lowPU'+name+'Denom')
	histos[ 'lowPU'+name+'Passing' ] = inFile.Get( trigger+'/lowPU'+name+'Passing')
	histos[ 'midPU'+name+'Denom' ] = inFile.Get( trigger+'/midPU'+name+'Denom')
	histos[ 'midPU'+name+'Passing' ] = inFile.Get( trigger+'/midPU'+name+'Passing')
	histos[ 'highPU'+name+'Denom' ] = inFile.Get( trigger+'/highPU'+name+'Denom')
	histos[ 'highPU'+name+'Passing' ] = inFile.Get( trigger+'/highPU'+name+'Passing')

	binWidth = histos[ 'lowPU'+name+'Denom' ].GetBinWidth(1)
	lowEffHisto = TGraphAsymmErrors( histos[ 'lowPU'+name+'Passing'], histos[ 'lowPU'+name+'Denom' ], "B" )
	lowEffHisto.GetYaxis().SetTitle( 'Efficiency / '+str(binWidth) )
	lowEffHisto.GetXaxis().SetTitle( histos['lowPU'+name+'Denom'].GetXaxis().GetTitle() )
	lowEffHisto.GetXaxis().SetRange( xmin, xmax )
	lowEffHisto.SetMaximum( 1.1 ) 
	lowEffHisto.SetMinimum( -0.1 ) 
	lowEffHisto.SetLineColor(1)

	midEffHisto = TGraphAsymmErrors( histos[ 'midPU'+name+'Passing'], histos[ 'midPU'+name+'Denom' ], "B" )
	midEffHisto.SetLineColor(2)
	highEffHisto = TGraphAsymmErrors( histos[ 'highPU'+name+'Passing'], histos[ 'highPU'+name+'Denom' ], "B" )
	highEffHisto.SetLineColor(3)
		
	legend=TLegend(0.65,0.20,0.90,0.40)
	legend.SetFillStyle(0)
	legend.SetTextSize(0.03)
	legend.AddEntry( lowEffHisto, 'NPV < 25', 'l' )
	legend.AddEntry( midEffHisto, '25 < NPV < 35', 'l' )
	legend.AddEntry( highEffHisto, 'NPV > 35', 'l' )

	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	lowEffHisto.Draw('AP')
	midEffHisto.Draw('P')
	highEffHisto.Draw('P')
	legend.Draw()
	setOverlap( signal + ' 13 TeV '+ PU )
	can.SaveAs( 'Plots/'+outputFileName )
	del can

def plotSimple2D( inFile, signal, trigger, name, xmax, xmax2, PU ):
	"""docstring for plot"""

	outputFileName = trigger+'_'+name+'_'+signal+'_'+PU+'_TriggerEfficiency.pdf' 
	print 'Processing.......', outputFileName

	histo = inFile.Get( trigger+'/'+name )

	#histo.GetYaxis().SetTitle( histo.GetXaxis().GetTitle( ) )
	histo.GetXaxis().SetTitle( 'Online Jet TrimMod Mass [GeV]' )
#	histo.GetXaxis().SetRange( 20, 50 )
#	histo.GetYaxis().SetRange( 5, 25 )
#	gStyle.SetPaintTextFormat("4.1f")
	can = TCanvas('c1', 'c1',  10, 10, 800, 500 )
	histo.Draw('colz')
	setEfficiencyTrigger( signal + PU, '')
	can.SaveAs( 'Plots/'+outputFileName )
	del can



if __name__ == '__main__':

	PU = sys.argv[2]
	Signal = sys.argv[1] #'RPVSt100tojj'	
	inputFile = TFile.Open('filesWithHistos_'+Signal+'_'+PU+'.root')
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
#			['PFHT900', 'HT', 50, 100 ],
#			['PFHT900', 'jetMass', 0, 100 ],
#			['PFHT950', 'HT', 20, 50 ],
#			['PFHT950', 'jetMass', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'HT', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'pt', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'jetMass', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'jetMassTrim', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'jetMassTrimMod', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'jetMassPruned', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'jetMassHT', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'jetMassEfficiency', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'jetMassTrimEfficiency', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'jetMassTrimModEfficiency', 0, 200 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'jetMassPrunedEfficiency', 0, 200 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'hltVsPatJetMass', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'hltVsPatJetMassTrim', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'hltVsPatJetMassTrimMod', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'hltVsPatJetMassPruned', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'passedHltVsPatJetMass', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'passedHltVsPatJetMassTrim', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'passedHltVsPatJetMassTrimMod', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutMass', 'passedHltVsPatJetMassPruned', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'HT', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'pt', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMass', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassTrim', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassTrimMod', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassPruned', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassHT', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassEfficiency', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassTrimEfficiency', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassTrimModEfficiency', 0, 200 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassPrunedEfficiency', 0, 200 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'hltVsPatJetMass', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'hltVsPatJetMassTrim', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'hltVsPatJetMassTrimMod', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'hltVsPatJetMassPruned', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'passedHltVsPatJetMass', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'passedHltVsPatJetMassTrim', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'passedHltVsPatJetMassTrimMod', 0, 100 ],
#			['AK8PFHT850TrimMass50TrimModCutHT', 'passedHltVsPatJetMassPruned', 0, 100 ],
			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassHT', 0, 100 ],
			['AK8PFHT850TrimMass50TrimModCutHT', 'HT', 0, 100 ],
			['AK8PFHT850TrimMass50TrimModCutHT', 'jetMassTrimMod', 0, 100 ],
			['AK8PFHT800TrimMass50TrimModCutHT', 'jetMassHT', 0, 100 ],
			['AK8PFHT800TrimMass50TrimModCutHT', 'HT', 0, 100 ],
			['AK8PFHT800TrimMass50TrimModCutHT', 'jetMassTrimMod', 0, 100 ],
			['AK8PFHT750TrimMass50TrimModCutHT', 'jetMassHT', 0, 100 ],
			['AK8PFHT750TrimMass50TrimModCutHT', 'HT', 0, 100 ],
			['AK8PFHT750TrimMass50TrimModCutHT', 'jetMassTrimMod', 0, 100 ],
			]
	for i in plotsList: 
		if 'jetMassHT' in i[1]: plot2D( inputFile, Signal, i[0], i[1], i[2], i[3], PU )
		elif 'ltVs' in i[1]: plotSimple2D( inputFile, Signal, i[0], i[1], i[2], i[3], PU )
		elif 'Efficiency' in i[1] : plotDiffPU( inputFile, Signal, i[0], i[1], i[2], i[3], PU )
		else: plot( inputFile, Signal, i[0], i[1], i[2], i[3], PU )
