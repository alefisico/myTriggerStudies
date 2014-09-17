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
process.load(NAME+'_13TeV_pythia8_'+PU+'_allAK8_100k_FiltFiles_cfi')
#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('/store/user/algomez/FiltFiles/RPVSt100tojj_13TeV_pythia8_PU20bx25_allAK8_100k_Filt.root'))

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PLS170_V7AN1::All')

process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_'+NAME+'_'+PU+'.root'))
#process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_QCD_Pt-'+ptBin+'.root'))
#process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_RPVSt100tojj_13TeV_pythia8_PU20bx25.root'))

process.AK8PFTrimHT850TrimMass50vsPFHT900 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
		trigger1 = cms.string( "HLT_AK8PFTrimHT850_TrimMass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrim" ),
		trigger3 = cms.string( "HLT_AK8PFTrimHT850_TrimMass50_v1" ),
		threeHLTHT = cms.InputTag( "hltAK8PFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK8PFJetsTrim" ),
		)

process.AK8PFTrimHT850TrimMass50TrimModvsPFHT900 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_PFHT900_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
		trigger1 = cms.string( "HLT_AK8PFTrimHT850_TrimMod_TrimMass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrimMod" ),
		trigger3 = cms.string( "HLT_AK8PFJet360Trim_Mass30_TrimMod_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
		)

process.AK8PFTrimHT850TrimMass50TrimModvsAK8PFTrimHT850TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_AK8PFTrimHT850_TrimMass50_v1" ),
		twoHLTHT = cms.InputTag( "hltAK8PFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK8PFJetsTrim" ),
		trigger1 = cms.string( "HLT_AK8PFTrimHT850_TrimMod_TrimMass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrimMod" ),
		trigger3 = cms.string( "HLT_AK8PFJet360Trim_Mass30_TrimMod_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
		)

#process.AK8PFTrimHT850TrimMass50AK4CaloHTvsPFHT900 = cms.EDAnalyzer("OverlapTriggers",
#		trigger2 = cms.string( "HLT_PFHT900_v1" ),
#		twoHLTHT = cms.InputTag( "hltPFHT" ),
#		twoHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
#		trigger1 = cms.string( "HLT_AK8PFTrimHT850_AK4CaloHT_TrimMass50_v1" ),
#		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
#		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrim" ),
#		)

process.AK8PFTrimHT850TrimMass50vsAK8PFJet360TrimMass30TrimMod = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_TrimMod_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
		trigger1 = cms.string( "HLT_AK8PFTrimHT850_TrimMass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrim" ),
		trigger3 = cms.string( "HLT_AK8PFJet360Trim_Mass30_TrimMod_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
		)

process.AK8PFTrimHT850TrimMass50TrimModvsAK8PFJet360TrimMass30TrimMod = cms.EDAnalyzer("OverlapTriggers",
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_TrimMod_v1" ),
		twoHLTHT = cms.InputTag( "hltPFHT" ),
		twoHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
		trigger1 = cms.string( "HLT_AK8PFTrimHT850_TrimMod_TrimMass50_v1" ),
		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrimMod" ),
		trigger3 = cms.string( "HLT_AK8PFJet360Trim_Mass30_TrimMod_v1" ),
		threeHLTHT = cms.InputTag( "hltPFHT" ),
		threeHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
		)

#process.AK8PFTrimHT850TrimMass50AK4CaloHTvsAK8PFJet360TrimMass30TrimMod = cms.EDAnalyzer("OverlapTriggers",
#		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_TrimMod_v1" ),
#		twoHLTHT = cms.InputTag( "hltPFHT" ),
#		twoHLTPFJets = cms.InputTag( "hltAK4PFJets" ),
#		trigger1 = cms.string( "HLT_AK8PFTrimHT850_AK4CaloHT_TrimMass50_v1" ),
#		oneHLTHT = cms.InputTag( "hltAK8PFHT" ),
#		oneHLTPFJets = cms.InputTag( "hltAK8PFJetsTrim" ),
#		)
#

#############   Path       ###########################
process.p = cms.Path(
	process.AK8PFTrimHT850TrimMass50vsPFHT900 *
	process.AK8PFTrimHT850TrimMass50TrimModvsPFHT900 *
#	process.AK8PFTrimHT850TrimMass50AK4CaloHTvsPFHT900 *
	process.AK8PFTrimHT850TrimMass50vsAK8PFJet360TrimMass30TrimMod *
	process.AK8PFTrimHT850TrimMass50TrimModvsAK8PFTrimHT850TrimMass50 *
	process.AK8PFTrimHT850TrimMass50TrimModvsAK8PFJet360TrimMass30TrimMod 
#	process.AK8PFTrimHT850TrimMass50AK4CaloHTvsAK8PFJet360TrimMass30TrimMod 
	)

#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

