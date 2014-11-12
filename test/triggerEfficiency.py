import FWCore.ParameterSet.Config as cms
import sys

PU = sys.argv[3]
NAME = sys.argv[2]

process = cms.Process("Ana")
process.load("FWCore.MessageService.MessageLogger_cfi")
#############   Set the number of events #############
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
#############   Define the source file ###############
process.load(NAME+'_'+PU+'_v721patch2_Filt_cfi')
#process.source.eventsToProcess = cms.untracked.VEventRange([ i.replace('\n','') for i in open("../lumiBoostedEvents.txt").readlines()])
#process.source = cms.Source("PoolSource",
#		fileNames = cms.untracked.vstring(
			#'file:Filt_RSGllsuon.root'
			#'file:/uscms/home/algomez/EOS/FiltFiles/QCD_Pt-300to470_Tune4C_13TeV_pythia8_PU40bx50_AK8JEC_Filt.root'
#			'file:/uscms/home/algomez/EOS/FiltFiles/'+NAME+'_13TeV_pythia8_'+PU+'_Filt.root'
#    )
#)
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PLS170_V7AN1::All')

process.TFileService=cms.Service("TFileService", 
		fileName=cms.string('filesWithHistos_'+NAME+'_'+PU+'.root'))

#############   User analyzer (PF jets) ##
process.AK8PFPt150HT750TrimMass50H750P40M50AK8NG = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom	= cms.InputTag( "patJetsAK8CHS" ),
		minHT		= cms.double( 750. ),
		minPt   	= cms.double( 40. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H750P40M50AK8Trim = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSTrimMod" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 40. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H750P40M50AK8Prun = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSPruned" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 40. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H750P100M50AK8NG = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom	= cms.InputTag( "patJetsAK8CHS" ),
		minHT		= cms.double( 750. ),
		minPt   	= cms.double( 100. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H750P100M50AK8Trim = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSTrimMod" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 100. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H750P100M50AK8Prun = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSPruned" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 100. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H750P150M50AK8NG = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom	= cms.InputTag( "patJetsAK8CHS" ),
		minHT		= cms.double( 750. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H750P150M50AK8Trim = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSTrimMod" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H750P150M50AK8Prun = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSPruned" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H750P150M0AK8NG = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom	= cms.InputTag( "patJetsAK8CHS" ),
		minHT		= cms.double( 750. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 0. ),
		)

process.AK8PFPt150HT750TrimMass50H750P150M0AK8Trim = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSTrimMod" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 0. ),
		)

process.AK8PFPt150HT750TrimMass50H750P150M0AK8Prun = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSPruned" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 0. ),
		)


process.PFHT900H750P150M50AK8NG = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_PFHT900_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom	= cms.InputTag( "patJetsAK8CHS" ),
		minHT		= cms.double( 750. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H900P150M50AK8NG = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom	= cms.InputTag( "patJetsAK8CHS" ),
		minHT		= cms.double( 900. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H900P150M50AK8Trim = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSTrimMod" ),
		minHT   	= cms.double( 900. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 50. ),
		)

process.AK8PFPt150HT750TrimMass50H900P150M50AK8Prun = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSPruned" ),
		minHT   	= cms.double( 900. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 50. ),
		)

process.PFHT900H750P150M50AK8Trim = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_PFHT900_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSTrimMod" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 50. ),
		)

process.PFHT900H750P150M50AK8Prun = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath 	= cms.string( "HLT_PFHT900_v1" ),
		patJets     	= cms.InputTag( "patJetsAK8CHS" ),
		patJetsGrom 	= cms.InputTag( "patJetsAK8CHSPruned" ),
		minHT   	= cms.double( 750. ),
		minPt   	= cms.double( 150. ),
		minMass 	= cms.double( 50. ),
		)

#############   Path       ###########################
process.p = cms.Path(
	process.AK8PFPt150HT750TrimMass50H750P40M50AK8NG
	* process.AK8PFPt150HT750TrimMass50H750P40M50AK8Trim
	* process.AK8PFPt150HT750TrimMass50H750P40M50AK8Prun
	* process.AK8PFPt150HT750TrimMass50H750P150M50AK8NG
	* process.AK8PFPt150HT750TrimMass50H750P150M50AK8Trim
	* process.AK8PFPt150HT750TrimMass50H750P150M50AK8Prun
	* process.AK8PFPt150HT750TrimMass50H750P150M0AK8NG
	* process.AK8PFPt150HT750TrimMass50H750P150M0AK8Trim
	* process.AK8PFPt150HT750TrimMass50H750P150M0AK8Prun
	* process.AK8PFPt150HT750TrimMass50H900P150M50AK8NG
	* process.AK8PFPt150HT750TrimMass50H900P150M50AK8Trim
	* process.AK8PFPt150HT750TrimMass50H900P150M50AK8Prun
	* process.PFHT900H750P150M50AK8NG
	* process.PFHT900H750P150M50AK8Trim
	* process.PFHT900H750P150M50AK8Prun
)
#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 100

