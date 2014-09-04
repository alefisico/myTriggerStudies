import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("Ana")
process.load("FWCore.MessageService.MessageLogger_cfi")
#############   Set the number of events #############
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)
#############   Define the source file ###############
process.source = cms.Source("PoolSource",
		fileNames = cms.untracked.vstring(
			#'file:Filt_RSGllsuon.root'
			'file:/uscms/home/algomez/EOS/FiltFiles/QCD_Pt-300to470_Tune4C_13TeV_pythia8_PU40bx50_AK8JEC_Filt.root'
    )
)

process.TFileService=cms.Service("TFileService", fileName=cms.string('filesWithHistos_QCD_Pt-1000to1400_Tune4C_13TeV_pythia8_PU20bx25'+NAME+'.root'))

#############   User analyzer (PF jets) ##
process.HT750 = cms.EDAnalyzer("TriggerEfficiency",
		patJets = cms.InputTag( "patJetsAK4PFchs" ),
		triggerPath = cms.string( "HLT_HT750_v1" ),
		scale = cms.double( 1 ) 
		)

process.HT850 = cms.EDAnalyzer("TriggerEfficiency",
		patJets = cms.InputTag( "patJetsAK4PFchs" ),
		triggerPath = cms.string( "HLT_HT850_v1" ),
		scale = cms.double( 1 ) 
		)

process.PFHT750 = cms.EDAnalyzer("TriggerEfficiency",
		patJets = cms.InputTag( "patJetsAK4PFchs" ),
		triggerPath = cms.string( "HLT_PFHT750_v1" ),
		scale = cms.double( 1 ) 
		)

process.PFHT850 = cms.EDAnalyzer("TriggerEfficiency",
		patJets = cms.InputTag( "patJetsAK4PFchs" ),
		triggerPath = cms.string( "HLT_PFHT850_v1" ),
		scale = cms.double( 1 ) 
		)


#############   Path       ###########################
process.p = cms.Path(
		process.HT750 * process.HT850 *
		process.PFHT750 * process.PFHT850 
		)

#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 100

