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
process.load(NAME+'_'+PU+'_v721patch2_Filt_cfi')
#process.source.eventsToProcess = cms.untracked.VEventRange([ i.replace('\n','') for i in open("../lumiBoostedEvents.txt").readlines()])
#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('/store/user/algomez/FiltFiles/RPVSt100tojj_13TeV_pythia8_PU20bx25_allAK8_100k_Filt.root'))

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PLS170_V7AN1::All')

process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_'+NAME+'_'+PU+'.root'))
#process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_QCD_Pt-'+ptBin+'.root'))
#process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_RPVSt100tojj_13TeV_pythia8_PU20bx25.root'))


process.AK8PFHT850TrimModMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_HT850_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT850TrimModMass50Pt100 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt100_HT850_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT800TrimModMass50Pt100 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt100_HT800_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT750TrimModMass50Pt100 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt100_HT750_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT850TrimModMass50Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT850_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT800TrimModMass50Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT800_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT750TrimModMass50Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT750TrimModMass40Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass40_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT750TrimModMass30Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT750_Mass30_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT700TrimModMass40Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT700_Mass40_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT700TrimModMass50Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt150_HT700_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT850TrimModMass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt200_HT850_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT800TrimModMass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt200_HT800_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT750TrimModMass30Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt200_HT750_Mass30_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT750TrimModMass40Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt200_HT750_Mass40_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT750TrimModMass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt200_HT750_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT700TrimModMass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt200_HT700_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT650TrimModMass40Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt200_HT650_Mass40_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFHT650TrimModMass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFHT450_TrimR0p1PT0p03Mass00_Pt200_HT650_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT650Mass00Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt150_HT650_Mass00_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT850Mass50Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt150_HT850_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT800Mass50Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt150_HT800_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT750Mass50Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt150_HT750_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT700Mass50Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt150_HT700_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT650Mass50Pt150 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt150_HT650_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT850Mass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt200_HT850_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT800Mass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt200_HT800_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT750Mass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt200_HT750_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT700Mass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt200_HT700_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT650Mass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt200_HT650_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT600Mass50Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt200_HT600_Mass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)

process.AK8PFTrimHT600Mass00Pt200 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFNOJECTrimR0p1PT0p03_HT450_Mass00_Pt200_HT600_Mass00_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		oneHLTPFJetsTrim = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		trigger3 = cms.string( "HLT_AK8PFJet360TrimMod_Mass30_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJetsTrim" ),
		trigger4 = cms.string( "HLT_PFHT750_4Jet_v1" ),
		)



#############   Path       ###########################
process.p = cms.Path(
	process.AK8PFHT850TrimModMass50
	* process.AK8PFHT850TrimModMass50Pt100
	* process.AK8PFHT800TrimModMass50Pt100
	* process.AK8PFHT750TrimModMass50Pt100
	* process.AK8PFHT700TrimModMass40Pt150
	* process.AK8PFHT850TrimModMass50Pt150
	* process.AK8PFHT800TrimModMass50Pt150
	* process.AK8PFHT750TrimModMass50Pt150
	* process.AK8PFHT750TrimModMass40Pt150
	* process.AK8PFHT750TrimModMass30Pt150
	* process.AK8PFHT700TrimModMass50Pt150
	* process.AK8PFHT650TrimModMass40Pt200
	* process.AK8PFHT850TrimModMass50Pt200
	* process.AK8PFHT800TrimModMass50Pt200
	* process.AK8PFHT750TrimModMass30Pt200
	* process.AK8PFHT750TrimModMass40Pt200
	* process.AK8PFHT750TrimModMass50Pt200
	* process.AK8PFHT700TrimModMass50Pt200
	* process.AK8PFHT650TrimModMass50Pt200
	* process.AK8PFTrimHT650Mass00Pt150
	* process.AK8PFTrimHT850Mass50Pt150
	* process.AK8PFTrimHT800Mass50Pt150
	* process.AK8PFTrimHT750Mass50Pt150
	* process.AK8PFTrimHT700Mass50Pt150
	* process.AK8PFTrimHT650Mass50Pt150
	* process.AK8PFTrimHT600Mass00Pt200
	* process.AK8PFTrimHT850Mass50Pt200
	* process.AK8PFTrimHT800Mass50Pt200
	* process.AK8PFTrimHT750Mass50Pt200
	* process.AK8PFTrimHT700Mass50Pt200
	* process.AK8PFTrimHT650Mass50Pt200
	* process.AK8PFTrimHT600Mass50Pt200
	)

#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

