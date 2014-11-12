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
#print [ i.replace('\n', '') for i in open("../lumiBoostedEvents.txt").readlines()]
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
		fileName=cms.string('simpleAnalyzer_'+NAME+'_'+PU+'.root'))
#		fileName=cms.string('simpleAnalyzer_'+NAME+'_'+PU+'_boosted.root'))

if 'QCD' in NAME: SF = 10000
elif 'RPVSt100': SF = 10000 * 559.757/98404

#############   User analyzer (PF jets) ##
process.histosUngroomedJets = cms.EDAnalyzer("SimpleAnalyzer",
		jets = cms.InputTag( "hltAK8PFJetsCorrected" ),
		scale = cms.double( SF )
		)

process.histosTrimmedJets = cms.EDAnalyzer("SimpleAnalyzer",
		jets = cms.InputTag( "hltAK8PFJetsTrimR0p1PT0p03" ),
		scale = cms.double( SF )
		)

#############   Path       ###########################
process.p = cms.Path(
	process.histosUngroomedJets
	* process.histosTrimmedJets
)
#############   Format MessageLogger #################
process.MessageLogger.cerr.FwkReport.reportEvery = 100

