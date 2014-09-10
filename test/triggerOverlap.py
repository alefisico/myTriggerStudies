import FWCore.ParameterSet.Config as cms
import sys

ptBin = sys.argv[2]

process = cms.Process("Ana")
process.load("FWCore.MessageService.MessageLogger_cfi")
#############   Set the number of events #############
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
#############   Define the source file ###############
#process.load('QCD_Pt-'+ptBin+'_Tune4C_13TeV_pythia8_PU20bx25_allAK8_Trk1B_30k_ProdFiles_cfi')
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('/store/user/algomez/FiltFiles/RPVSt100tojj_13TeV_pythia8_PU20bx25_allAK8_100k_Filt.root'))

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PLS170_V7AN1::All')

#process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_QCD_Pt-'+ptBin+'.root'))
process.TFileService=cms.Service("TFileService", fileName=cms.string('overlapStudies_RPVSt100tojj_13TeV_pythia8_PU20bx25.root'))

process.PFHT900 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_PFHT900_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.AK8PFTrimHT450_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT450_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.AK8PFTrimHT550_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT550_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.AK8PFTrimHT650_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT650_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.AK8PFTrimHT750_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT750_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.AK8PFTrimHT850_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT850_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.PFTrimHT450_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_PFTrimHT450_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.PFTrimHT550_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_PFTrimHT550_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.PFTrimHT650_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_PFTrimHT650_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.PFTrimHT750_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_PFTrimHT750_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.PFTrimHT850_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_PFTrimHT850_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		)

process.AK4vsAK8PFTrimHT450_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT450_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_PFTrimHT450_TrimMass50_v1" ),
		)

process.AK4vsAK8PFTrimHT550_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT550_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_PFTrimHT550_TrimMass50_v1" ),
		)

process.AK4vsAK8PFTrimHT650_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT650_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_PFTrimHT650_TrimMass50_v1" ),
		)

process.AK4vsAK8PFTrimHT750_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT750_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_PFTrimHT750_TrimMass50_v1" ),
		)

process.AK4vsAK8PFTrimHT850_TrimMass50 = cms.EDAnalyzer("OverlapTriggers",
		trigger1 = cms.string( "HLT_AK8PFTrimHT850_TrimMass50_v1" ),
		trigger2 = cms.string( "HLT_PFTrimHT850_TrimMass50_v1" ),
		)

#############   Path       ###########################
process.p = cms.Path(
	process.PFHT900  *
	process.AK8PFTrimHT450_TrimMass50  *
	process.AK8PFTrimHT550_TrimMass50  *
	process.AK8PFTrimHT650_TrimMass50  *
	process.AK8PFTrimHT750_TrimMass50  *
	process.AK8PFTrimHT850_TrimMass50  *
	process.PFTrimHT450_TrimMass50  *
	process.PFTrimHT550_TrimMass50  *
	process.PFTrimHT650_TrimMass50  *
	process.PFTrimHT750_TrimMass50  *
	process.PFTrimHT850_TrimMass50  *
	process.AK4vsAK8PFTrimHT450_TrimMass50  *
	process.AK4vsAK8PFTrimHT550_TrimMass50  *
	process.AK4vsAK8PFTrimHT650_TrimMass50  *
	process.AK4vsAK8PFTrimHT750_TrimMass50  *
	process.AK4vsAK8PFTrimHT850_TrimMass50  
	)

#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

