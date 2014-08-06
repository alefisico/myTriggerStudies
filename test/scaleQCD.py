#!/usr/bin/env python
'''
File: scaleQCD.py
Author: Alejandro Gomez Espinosa
Email: gomez@physics.rutgers.edu
Description: simple script to scale QCD Files
'''

from ROOT import TFile, TH1, TH2, TMath, gROOT, gPad, TTree
#from ROOT import *

gROOT.Reset()
gROOT.SetBatch()

scaleFactors = [
		[ 'QCD_Pt-30to50', 161500000. * 0.9481 ],
		[ 'QCD_Pt-50to80', 22110000. *0.8820 ],
		[ 'QCD_Pt-80to120', 3000114.3 * 0.8456 ],
		[ 'QCD_Pt-120to170', 493200. * 0.8355 ],
		[ 'QCD_Pt-170to300', 120300. ],
		[ 'QCD_Pt-300to470', 7475. ],
		[ 'QCD_Pt-470to600', 587.1 ],
		[ 'QCD_Pt-600to800', 167. ],
		[ 'QCD_Pt-800to1000', 28.25 ],
		[ 'QCD_Pt-1000to1400', 8.195 ],
		[ 'QCD_Pt-1400to1800', 0.7346 ],
		[ 'QCD_Pt-1800', 0.1091 ]
		]

listDir = []

def scaleQCD( inFileName, treeName ):
	"""docstring for scaleQCD"""

	infile = TFile( inFileName+'.root', "READ")
	outfile = TFile( inFileName+'_Scaled.root', "RECREATE")

	tree = infile.Get( treeName )
	numEvents = tree.GetEntries()

	scale = 0
	for i in range( len( scaleFactors ) ):
		if str(scaleFactors[i][0]) in inFileName: 
			scale = scaleFactors[i][1] / numEvents
			continue

	listDir = []
	for k in infile.GetListOfKeys(): 
		name = k.GetName()
		listDir.append( name )
	#print listDir
	for j in listDir:
		outfile.mkdir(j)
		outfile.cd(j)
		dir = infile.GetDirectory(j)
		for q in dir.GetListOfKeys():
			name = q.GetName()
			h = infile.Get( j+'/'+name)
			if isinstance(h, TTree): continue
			hOut = h.Clone()
			if not isinstance(h,TH2) and not "numJets" in name : hOut.Scale( scale )
			hOut.Write()
		outfile.cd('/')
	
	outfile.Write()
	outfile.Close()
	infile.Close()

if __name__ == '__main__':
	scaleQCD( 'hlt_jetmass_QCD_Pt-30to50_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-50to80_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-80to120_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-120to170_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-170to300_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-300to470_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-470to600_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-600to800_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-800to1000_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-1000to1400_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-1400to1800_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
	scaleQCD( 'hlt_jetmass_QCD_Pt-1800_TuneZ2star_13TeV_pythia8_PU20bx25', 'triggerPlotterHT/JetVariables' )
