import FWCore.ParameterSet.Config as cms
import sys

PU = sys.argv[2]
NAME = sys.argv[3]

process = cms.Process("Ana")
process.load("FWCore.MessageService.MessageLogger_cfi")
#############   Set the number of events #############
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
#############   Define the source file ###############
process.source = cms.Source("PoolSource",
		fileNames = cms.untracked.vstring(
			#'file:Filt_RSGllsuon.root'
			#'file:/uscms/home/algomez/EOS/FiltFiles/QCD_Pt-300to470_Tune4C_13TeV_pythia8_PU40bx50_AK8JEC_Filt.root'
			'file:/uscms/home/algomez/EOS/FiltFiles/'+NAME+'_13TeV_pythia8_'+PU+'_Filt.root'
    )
)
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PLS170_V7AN1::All')

process.TFileService=cms.Service("TFileService", 
		fileName=cms.string('filesWithHistos_'+NAME+'_13TeV_pythia8_'+PU+'.root'))

#############   User analyzer (PF jets) ##
process.PFHT450 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFHT450_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFHT550 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFHT550_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFHT650 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFHT650_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFHT750 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFHT750_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFHT850 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFHT850_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFHT900 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFHT900_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFHT950 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFHT950_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFHT450 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFHT450_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFHT550 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFHT550_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFHT650 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFHT650_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFHT750 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFHT750_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFHT850 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFHT850_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFNOJECTrimHT450 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFNOJECTrimHT550 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFNOJECTrimHT650 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFNOJECTrimHT750 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFNOJECTrimHT850 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFJet360TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFJet360Trim_Mass30_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT450TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT450_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT550TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT550_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT650TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT650_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT750TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT750_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT450_TrimMass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT550_TrimMass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT650_TrimMass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT750_TrimMass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFNOJECTrimHT850_TrimMass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
process.PFTrimHT450TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT450TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT450_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT550TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT550_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT650TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT650_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT750TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT750_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass00 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass00_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass05 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass05_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass10 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass10_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass15 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass15_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass20 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass20_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass25 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass25_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass30 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass30_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass35 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass35_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass40 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass40_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass45 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass45_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.PFTrimHT850TrimMass55 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFTrimHT850_TrimMass55_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT450_Mass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT550_Mass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT650_Mass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT750_Mass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass00_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass05_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass10_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass15_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass20_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass25_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass30_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass35_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass40_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass45_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass50_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_PFHT850_Mass55_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT450_CaloHT250_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT450_CaloHT300_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT450_CaloHT350_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT450_CaloHT400_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT450_CaloHT450_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT850_CaloHT550_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT850_CaloHT600_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT850_CaloHT650_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT850_CaloHT700_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)
#process.PFHT = cms.EDAnalyzer("TriggerEfficiency",
#		triggerPath = cms.string( "HLT_AK8PFTrimHT850_CaloHT750_v1" ),
#		patJets = cms.InputTag( "patJetsAK4CHS" ),
#		sf = cms.double( 1 )
#		)

#############   Path       ###########################
process.p = cms.Path(
		process.PFHT450 *
		process.PFHT550 *
		process.PFHT650 *
		process.PFHT750 *
		process.PFHT850 *
		process.PFHT900 *
		process.PFHT950 *
		process.PFTrimHT450 *
		process.PFTrimHT550 *
		process.PFTrimHT650 *
		process.PFTrimHT750 *
		process.PFTrimHT850 *
		process.AK8PFHT450 *
		process.AK8PFHT550 *
		process.AK8PFHT650 *
		process.AK8PFHT750 *
		process.AK8PFHT850 *
		process.AK8PFTrimHT450 *
		process.AK8PFTrimHT550 *
		process.AK8PFTrimHT650 *
		process.AK8PFTrimHT750 *
		process.AK8PFTrimHT850 *
		process.AK8PFNOJECTrimHT450 *
		process.AK8PFNOJECTrimHT550 *
		process.AK8PFNOJECTrimHT650 *
		process.AK8PFNOJECTrimHT750 *
		process.AK8PFNOJECTrimHT850 *
		process.AK8PFJet360TrimMass30 *
		process.AK8PFTrimHT450TrimMass00 *
		process.AK8PFTrimHT450TrimMass05 *
		process.AK8PFTrimHT450TrimMass10 *
		process.AK8PFTrimHT450TrimMass15 *
		process.AK8PFTrimHT450TrimMass20 *
		process.AK8PFTrimHT450TrimMass25 *
		process.AK8PFTrimHT450TrimMass30 *
		process.AK8PFTrimHT450TrimMass35 *
		process.AK8PFTrimHT450TrimMass40 *
		process.AK8PFTrimHT450TrimMass45 *
		process.AK8PFTrimHT450TrimMass50 *
		process.AK8PFTrimHT450TrimMass55 *
		process.AK8PFTrimHT550TrimMass00 *
		process.AK8PFTrimHT550TrimMass05 *
		process.AK8PFTrimHT550TrimMass10 *
		process.AK8PFTrimHT550TrimMass15 *
		process.AK8PFTrimHT550TrimMass20 *
		process.AK8PFTrimHT550TrimMass25 *
		process.AK8PFTrimHT550TrimMass30 *
		process.AK8PFTrimHT550TrimMass35 *
		process.AK8PFTrimHT550TrimMass40 *
		process.AK8PFTrimHT550TrimMass45 *
		process.AK8PFTrimHT550TrimMass50 *
		process.AK8PFTrimHT550TrimMass55 *
		process.AK8PFTrimHT650TrimMass00 *
		process.AK8PFTrimHT650TrimMass05 *
		process.AK8PFTrimHT650TrimMass10 *
		process.AK8PFTrimHT650TrimMass15 *
		process.AK8PFTrimHT650TrimMass20 *
		process.AK8PFTrimHT650TrimMass25 *
		process.AK8PFTrimHT650TrimMass30 *
		process.AK8PFTrimHT650TrimMass35 *
		process.AK8PFTrimHT650TrimMass40 *
		process.AK8PFTrimHT650TrimMass45 *
		process.AK8PFTrimHT650TrimMass50 *
		process.AK8PFTrimHT650TrimMass55 *
		process.AK8PFTrimHT750TrimMass00 *
		process.AK8PFTrimHT750TrimMass05 *
		process.AK8PFTrimHT750TrimMass10 *
		process.AK8PFTrimHT750TrimMass15 *
		process.AK8PFTrimHT750TrimMass20 *
		process.AK8PFTrimHT750TrimMass25 *
		process.AK8PFTrimHT750TrimMass30 *
		process.AK8PFTrimHT750TrimMass35 *
		process.AK8PFTrimHT750TrimMass40 *
		process.AK8PFTrimHT750TrimMass45 *
		process.AK8PFTrimHT750TrimMass50 *
		process.AK8PFTrimHT750TrimMass55 *
		process.AK8PFTrimHT850TrimMass00 *
		process.AK8PFTrimHT850TrimMass05 *
		process.AK8PFTrimHT850TrimMass10 *
		process.AK8PFTrimHT850TrimMass15 *
		process.AK8PFTrimHT850TrimMass20 *
		process.AK8PFTrimHT850TrimMass25 *
		process.AK8PFTrimHT850TrimMass30 *
		process.AK8PFTrimHT850TrimMass35 *
		process.AK8PFTrimHT850TrimMass40 *
		process.AK8PFTrimHT850TrimMass45 *
		process.AK8PFTrimHT850TrimMass50 *
		process.AK8PFTrimHT850TrimMass55 *
#		process.AK8PFNOJECTrimHT450TrimMass00 *
#		process.AK8PFNOJECTrimHT450TrimMass05 *
#		process.AK8PFNOJECTrimHT450TrimMass10 *
#		process.AK8PFNOJECTrimHT450TrimMass15 *
#		process.AK8PFNOJECTrimHT450TrimMass20 *
#		process.AK8PFNOJECTrimHT450TrimMass25 *
#		process.AK8PFNOJECTrimHT450TrimMass30 *
#		process.AK8PFNOJECTrimHT450TrimMass35 *
#		process.AK8PFNOJECTrimHT450TrimMass40 *
#		process.AK8PFNOJECTrimHT450TrimMass45 *
#		process.AK8PFNOJECTrimHT450TrimMass50 *
#		process.AK8PFNOJECTrimHT450TrimMass55 *
#		process.AK8PFNOJECTrimHT550TrimMass00 *
#		process.AK8PFNOJECTrimHT550TrimMass05 *
#		process.AK8PFNOJECTrimHT550TrimMass10 *
#		process.AK8PFNOJECTrimHT550TrimMass15 *
#		process.AK8PFNOJECTrimHT550TrimMass20 *
#		process.AK8PFNOJECTrimHT550TrimMass25 *
#		process.AK8PFNOJECTrimHT550TrimMass30 *
#		process.AK8PFNOJECTrimHT550TrimMass35 *
#		process.AK8PFNOJECTrimHT550TrimMass40 *
#		process.AK8PFNOJECTrimHT550TrimMass45 *
#		process.AK8PFNOJECTrimHT550TrimMass50 *
#		process.AK8PFNOJECTrimHT550TrimMass55 *
#		process.AK8PFNOJECTrimHT650TrimMass00 *
#		process.AK8PFNOJECTrimHT650TrimMass05 *
#		process.AK8PFNOJECTrimHT650TrimMass10 *
#		process.AK8PFNOJECTrimHT650TrimMass15 *
#		process.AK8PFNOJECTrimHT650TrimMass20 *
#		process.AK8PFNOJECTrimHT650TrimMass25 *
#		process.AK8PFNOJECTrimHT650TrimMass30 *
#		process.AK8PFNOJECTrimHT650TrimMass35 *
#		process.AK8PFNOJECTrimHT650TrimMass40 *
#		process.AK8PFNOJECTrimHT650TrimMass45 *
#		process.AK8PFNOJECTrimHT650TrimMass50 *
#		process.AK8PFNOJECTrimHT650TrimMass55 *
#		process.AK8PFNOJECTrimHT750TrimMass00 *
#		process.AK8PFNOJECTrimHT750TrimMass05 *
#		process.AK8PFNOJECTrimHT750TrimMass10 *
#		process.AK8PFNOJECTrimHT750TrimMass15 *
#		process.AK8PFNOJECTrimHT750TrimMass20 *
#		process.AK8PFNOJECTrimHT750TrimMass25 *
#		process.AK8PFNOJECTrimHT750TrimMass30 *
#		process.AK8PFNOJECTrimHT750TrimMass35 *
#		process.AK8PFNOJECTrimHT750TrimMass40 *
#		process.AK8PFNOJECTrimHT750TrimMass45 *
#		process.AK8PFNOJECTrimHT750TrimMass50 *
#		process.AK8PFNOJECTrimHT750TrimMass55 *
#		process.AK8PFNOJECTrimHT850TrimMass00 *
#		process.AK8PFNOJECTrimHT850TrimMass05 *
#		process.AK8PFNOJECTrimHT850TrimMass10 *
#		process.AK8PFNOJECTrimHT850TrimMass15 *
#		process.AK8PFNOJECTrimHT850TrimMass20 *
#		process.AK8PFNOJECTrimHT850TrimMass25 *
#		process.AK8PFNOJECTrimHT850TrimMass30 *
#		process.AK8PFNOJECTrimHT850TrimMass35 *
#		process.AK8PFNOJECTrimHT850TrimMass40 *
#		process.AK8PFNOJECTrimHT850TrimMass45 *
#		process.AK8PFNOJECTrimHT850TrimMass50 *
#		process.AK8PFNOJECTrimHT850TrimMass55 *
		process.PFTrimHT450TrimMass00 *
		process.PFTrimHT450TrimMass05 *
		process.PFTrimHT450TrimMass10 *
		process.PFTrimHT450TrimMass15 *
		process.PFTrimHT450TrimMass20 *
		process.PFTrimHT450TrimMass25 *
		process.PFTrimHT450TrimMass30 *
		process.PFTrimHT450TrimMass35 *
		process.PFTrimHT450TrimMass40 *
		process.PFTrimHT450TrimMass45 *
		process.PFTrimHT450TrimMass50 *
		process.PFTrimHT450TrimMass55 *
		process.PFTrimHT550TrimMass00 *
		process.PFTrimHT550TrimMass05 *
		process.PFTrimHT550TrimMass10 *
		process.PFTrimHT550TrimMass15 *
		process.PFTrimHT550TrimMass20 *
		process.PFTrimHT550TrimMass25 *
		process.PFTrimHT550TrimMass30 *
		process.PFTrimHT550TrimMass35 *
		process.PFTrimHT550TrimMass40 *
		process.PFTrimHT550TrimMass45 *
		process.PFTrimHT550TrimMass50 *
		process.PFTrimHT550TrimMass55 *
		process.PFTrimHT650TrimMass00 *
		process.PFTrimHT650TrimMass05 *
		process.PFTrimHT650TrimMass10 *
		process.PFTrimHT650TrimMass15 *
		process.PFTrimHT650TrimMass20 *
		process.PFTrimHT650TrimMass25 *
		process.PFTrimHT650TrimMass30 *
		process.PFTrimHT650TrimMass35 *
		process.PFTrimHT650TrimMass40 *
		process.PFTrimHT650TrimMass45 *
		process.PFTrimHT650TrimMass50 *
		process.PFTrimHT650TrimMass55 *
		process.PFTrimHT750TrimMass00 *
		process.PFTrimHT750TrimMass05 *
		process.PFTrimHT750TrimMass10 *
		process.PFTrimHT750TrimMass15 *
		process.PFTrimHT750TrimMass20 *
		process.PFTrimHT750TrimMass25 *
		process.PFTrimHT750TrimMass30 *
		process.PFTrimHT750TrimMass35 *
		process.PFTrimHT750TrimMass40 *
		process.PFTrimHT750TrimMass45 *
		process.PFTrimHT750TrimMass50 *
		process.PFTrimHT750TrimMass55 *
		process.PFTrimHT850TrimMass00 *
		process.PFTrimHT850TrimMass05 *
		process.PFTrimHT850TrimMass10 *
		process.PFTrimHT850TrimMass15 *
		process.PFTrimHT850TrimMass20 *
		process.PFTrimHT850TrimMass25 *
		process.PFTrimHT850TrimMass30 *
		process.PFTrimHT850TrimMass35 *
		process.PFTrimHT850TrimMass40 *
		process.PFTrimHT850TrimMass45 *
		process.PFTrimHT850TrimMass50 *
		process.PFTrimHT850TrimMass55 
#		process.PFHT450Mass00 *
#		process.PFHT450Mass05 *
#		process.PFHT450Mass10 *
#		process.PFHT450Mass15 *
#		process.PFHT450Mass20 *
#		process.PFHT450Mass25 *
#		process.PFHT450Mass30 *
#		process.PFHT450Mass35 *
#		process.PFHT450Mass40 *
#		process.PFHT450Mass45 *
#		process.PFHT450Mass50 *
#		process.PFHT450Mass55 *
#		process.PFHT550Mass00 *
#		process.PFHT550Mass05 *
#		process.PFHT550Mass10 *
#		process.PFHT550Mass15 *
#		process.PFHT550Mass20 *
#		process.PFHT550Mass25 *
#		process.PFHT550Mass30 *
#		process.PFHT550Mass35 *
#		process.PFHT550Mass40 *
#		process.PFHT550Mass45 *
#		process.PFHT550Mass50 *
#		process.PFHT550Mass55 *
#		process.PFHT650Mass00 *
#		process.PFHT650Mass05 *
#		process.PFHT650Mass10 *
#		process.PFHT650Mass15 *
#		process.PFHT650Mass20 *
#		process.PFHT650Mass25 *
#		process.PFHT650Mass30 *
#		process.PFHT650Mass35 *
#		process.PFHT650Mass40 *
#		process.PFHT650Mass45 *
#		process.PFHT650Mass50 *
#		process.PFHT650Mass55 *
#		process.PFHT750Mass00 *
#		process.PFHT750Mass05 *
#		process.PFHT750Mass10 *
#		process.PFHT750Mass15 *
#		process.PFHT750Mass20 *
#		process.PFHT750Mass25 *
#		process.PFHT750Mass30 *
#		process.PFHT750Mass35 *
#		process.PFHT750Mass40 *
#		process.PFHT750Mass45 *
#		process.PFHT750Mass50 *
#		process.PFHT750Mass55 *
#		process.PFHT850Mass00 *
#		process.PFHT850Mass05 *
#		process.PFHT850Mass10 *
#		process.PFHT850Mass15 *
#		process.PFHT850Mass20 *
#		process.PFHT850Mass25 *
#		process.PFHT850Mass30 *
#		process.PFHT850Mass35 *
#		process.PFHT850Mass40 *
#		process.PFHT850Mass45 *
#		process.PFHT850Mass50 *
#		process.PFHT850Mass55 *
#		process.AK8PFTrimHT450CaloHT250 *
#		process.AK8PFTrimHT450CaloHT300 *
#		process.AK8PFTrimHT450CaloHT350 *
#		process.AK8PFTrimHT450CaloHT400 *
#		process.AK8PFTrimHT450CaloHT450 *
#		process.AK8PFTrimHT850CaloHT550 *
#		process.AK8PFTrimHT850CaloHT600 *
#		process.AK8PFTrimHT850CaloHT650 *
#		process.AK8PFTrimHT850CaloHT700 *
#		process.AK8PFTrimHT850CaloHT750 *
		)

#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 100

