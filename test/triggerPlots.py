# PYTHON configuration file.
# Description:  Example of dijet mass plot
#               with corrected and uncorrected jets
#               for various jet algorithms
# Author: Kalanand Mishra
# Date:  22 - November - 2009 

import FWCore.ParameterSet.Config as cms

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
			'file:Filt_QCD.root'
    #'/store/mc/Summer09/QCDFlat_Pt15to3000/GEN-SIM-RECO/MC_31X_V9_7TeV-v1/0000/FABD2A94-C0D3-DE11-B6FD-00237DA13C2E.root'
    )
)
#process.source.inputCommands = cms.untracked.vstring("keep *","drop *_MEtoEDMConverter_*_*")

process.TFileService=cms.Service("TFileService",
		fileName=cms.string('TriggerPlotter.root'))

#############   User analyzer (PF jets) ##
process.TriggerPlots = cms.EDAnalyzer("hltTriggerPlots",
    # Uncorrected PFJets
    hltFilter           = cms.string('hltCambridgeAachen8PFJetsTrim'),
    # Name of the output ROOT file containing the histograms 
    #HistoFileName = cms.untracked.string('TriggerPlots.root')
)


#############   Path       ###########################
process.p = cms.Path(process.TriggerPlots)

#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 100

