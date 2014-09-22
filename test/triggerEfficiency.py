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
process.load(NAME+'_13TeV_pythia8_'+PU+'_allAK8_100k_FiltFiles_cfi')
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
		fileName=cms.string('filesWithHistos_'+NAME+'_13TeV_pythia8_'+PU+'.root'))

#############   User analyzer (PF jets) ##
process.PFHT900 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_PFHT900_v1" ),
		patJets = cms.InputTag( "patJetsAK4CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass50TrimMod = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_TrimMod_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)
process.AK8PFTrimHT850TrimMass50AK4CaloHT = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFTrimHT850_AK4CaloHT_TrimMass50_v1" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		sf = cms.double( 1 )
		)

#############   Path       ###########################
process.p = cms.Path(
	process.PFHT900 *
	process.AK8PFTrimHT850TrimMass50 * 
	process.AK8PFTrimHT850TrimMass50TrimMod *
	process.AK8PFTrimHT850TrimMass50AK4CaloHT  
)
#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 100

