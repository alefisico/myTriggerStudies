import FWCore.ParameterSet.Config as cms
import sys

#ptBin = sys.argv[2]
NAME = sys.argv[2]
PU = sys.argv[3]

process = cms.Process("Ana")
process.load("FWCore.MessageService.MessageLogger_cfi")
#############   Set the number of events #############
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
#############   Define the source file ###############
#process.load('QCD_Pt-'+ptBin+'_Tune4C_13TeV_pythia8_PU20bx25_allAK8_Trk1B_30k_ProdFiles_cfi')
process.load(NAME+'_'+PU+'_v721_Filt_v3_cfi')
#process.source.eventsToProcess = cms.untracked.VEventRange([ i.replace('\n','') for i in open("../lumiBoostedEvents.txt").readlines()])
#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('/store/user/algomez/FiltFiles/RPVSt100tojj_13TeV_pythia8_PU20bx25_allAK8_100k_Filt.root'))

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PLS170_V7AN1::All')

process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_'+NAME+'_'+PU+'_v3.root'))
#process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_QCD_Pt-'+ptBin+'.root'))
#process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_RPVSt100tojj_13TeV_pythia8_PU20bx25.root'))


process.AK8PFHT850TrimMass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT850_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT800TrimMass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT800_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT800TrimMass00TrimModvsPFHT900vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT800_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass00_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT750TrimMass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT750_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT850TrimMass50TrimModvsPFHT850vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT850_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT850_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)
#
#process.AK8PFHT850TrimMass40TrimModvsPFHT850vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
#		trigger2 = cms.string( "HLT_PFHT850_v1" ),
#		twoHLTHT = cms.InputTag( "hltPFHT" ),
#		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
#		trigger1 = cms.string( "HLT_AK8PFHT850_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass40_v1" ),
#		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
#		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
#		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
#		threeHLTHT = cms.InputTag( "hltPFHT" ),
#		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
#		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
#		)
#
#process.AK8PFHT800TrimMass50TrimModvsPFHT850vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
#		trigger2 = cms.string( "HLT_PFHT850_v1" ),
#		twoHLTHT = cms.InputTag( "hltPFHT" ),
#		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
#		trigger1 = cms.string( "HLT_AK8PFHT800_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass50_v1" ),
#		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
#		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
#		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
#		threeHLTHT = cms.InputTag( "hltPFHT" ),
#		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
#		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
#		)
#
process.AK8PFHT850TrimMass50TrimModvsPFHT800vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT800_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT850_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)
#
#process.AK8PFHT850TrimMass40TrimModvsPFHT800vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
#		trigger2 = cms.string( "HLT_PFHT800_v1" ),
#		twoHLTHT = cms.InputTag( "hltPFHT" ),
#		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
#		trigger1 = cms.string( "HLT_AK8PFHT850_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass40_v1" ),
#		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
#		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
#		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
#		threeHLTHT = cms.InputTag( "hltPFHT" ),
#		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
#		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
#		)
#
#process.AK8PFHT800TrimMass50TrimModvsPFHT800vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
#		trigger2 = cms.string( "HLT_PFHT800_v1" ),
#		twoHLTHT = cms.InputTag( "hltPFHT" ),
#		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
#		trigger1 = cms.string( "HLT_AK8PFHT800_TrimR0p1PT0p03Mass00_TrimR0p1PT0p03Mass50_v1" ),
#		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
#		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
#		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
#		threeHLTHT = cms.InputTag( "hltPFHT" ),
#		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
#		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
#		)
process.AK8PFTrimHT750Mass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT750_Mass00_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFTrimR0p1PT0p03HT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT800Mass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT800_Mass00_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFTrimR0p1PT0p03HT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT850Mass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT850_Mass00_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFTrimR0p1PT0p03HT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT800Mass00TrimModvsPFHT900vsAK8PFJet360TrimModMass30 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT800_Mass00_Mass00_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFTrimR0p1PT0p03HT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)



#############   Path       ###########################
process.p = cms.Path(
	process.AK8PFHT850TrimMass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 *
	process.AK8PFHT800TrimMass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 *
	process.AK8PFHT800TrimMass00TrimModvsPFHT900vsAK8PFJet360TrimModMass30 *
	process.AK8PFHT750TrimMass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 *
	process.AK8PFHT850TrimMass50TrimModvsPFHT850vsAK8PFJet360TrimModMass30 *
	process.AK8PFTrimHT850Mass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 *
	process.AK8PFTrimHT800Mass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 *
	process.AK8PFTrimHT750Mass50TrimModvsPFHT900vsAK8PFJet360TrimModMass30 *
	process.AK8PFTrimHT800Mass00TrimModvsPFHT900vsAK8PFJet360TrimModMass30 *
#	process.AK8PFHT850TrimMass40TrimModvsPFHT850vsAK8PFJet360TrimModMass30 *
#	process.AK8PFHT800TrimMass50TrimModvsPFHT850vsAK8PFJet360TrimModMass30 *
	process.AK8PFHT850TrimMass50TrimModvsPFHT800vsAK8PFJet360TrimModMass30 
#	process.AK8PFHT850TrimMass40TrimModvsPFHT800vsAK8PFJet360TrimModMass30 *
#	process.AK8PFHT800TrimMass50TrimModvsPFHT800vsAK8PFJet360TrimModMass30 
	)

#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

