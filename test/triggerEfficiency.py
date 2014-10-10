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
process.load(NAME+'_13TeV_pythia8_'+PU+'_v718_FiltFiles_cfi')
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
		hltJets = cms.InputTag( "hltAK8PFJets" ),
		hltJetsTrim = cms.InputTag( "hltAK8PFJetsTrim" ),
		hltJetsTrimMod = cms.InputTag( "hltAK8PFJetsTrimMod" ),
		hltJetsPruned = cms.InputTag( "hltAK8PFJetsPruned" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		patJetsTrim = cms.InputTag( "patJetsAK8CHSTrim" ),
		patJetsTrimMod = cms.InputTag( "patJetsAK8CHSTrimMod" ),
		patJetsPruned = cms.InputTag( "patJetsAK8CHSPruned" ),
		primaryVertex = cms.InputTag( 'goodOfflinePrimaryVertices' ),
		jetsForEff = cms.InputTag( "patJetsAK8CHSTrim" ),
		minHT= cms.double( 700. ),
		minMass= cms.double( 50. ),
		)
process.AK8PFHT850TrimMass50 = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFHT850_TrimMass00_TrimMass50_v1" ),
		hltJets = cms.InputTag( "hltAK8PFJets" ),
		hltJetsTrim = cms.InputTag( "hltAK8PFJetsTrim" ),
		hltJetsTrimMod = cms.InputTag( "hltAK8PFJetsTrimMod" ),
		hltJetsPruned = cms.InputTag( "hltAK8PFJetsPruned" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		patJetsTrim = cms.InputTag( "patJetsAK8CHSTrim" ),
		patJetsTrimMod = cms.InputTag( "patJetsAK8CHSTrimMod" ),
		patJetsPruned = cms.InputTag( "patJetsAK8CHSPruned" ),
		primaryVertex = cms.InputTag( 'goodOfflinePrimaryVertices' ),
		jetsForEff = cms.InputTag( "patJetsAK8CHSTrim" ),
		minHT= cms.double( 700. ),
		minMass= cms.double( 50. ),
		)
process.AK8PFHT850TrimMass50TrimMod = cms.EDAnalyzer("TriggerEfficiency",
		triggerPath = cms.string( "HLT_AK8PFHT850_TrimModMass00_TrimModMass50_v1" ),
		hltJets = cms.InputTag( "hltAK8PFJets" ),
		hltJetsTrim = cms.InputTag( "hltAK8PFJetsTrim" ),
		hltJetsTrimMod = cms.InputTag( "hltAK8PFJetsTrimMod" ),
		hltJetsPruned = cms.InputTag( "hltAK8PFJetsPruned" ),
		patJets = cms.InputTag( "patJetsAK8CHS" ),
		patJetsTrim = cms.InputTag( "patJetsAK8CHSTrim" ),
		patJetsTrimMod = cms.InputTag( "patJetsAK8CHSTrimMod" ),
		patJetsPruned = cms.InputTag( "patJetsAK8CHSPruned" ),
		jetsForEff = cms.InputTag( "patJetsAK8CHSTrimMod" ),
		primaryVertex = cms.InputTag( 'goodOfflinePrimaryVertices' ),
		minHT= cms.double( 0. ),
		minMass= cms.double( 0. ),
		)

#############   Path       ###########################
process.p = cms.Path(
	process.PFHT900 *
	process.AK8PFHT850TrimMass50 * 
	process.AK8PFHT850TrimMass50TrimMod 
)
#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 100

