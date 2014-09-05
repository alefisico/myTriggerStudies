import FWCore.ParameterSet.Config as cms
import sys

NAME = sys.argv[1]
if 'bx25' in NAME: myGT = 'PRE_LS171_V5A::All'
else: myGT = 'PRE_LS171_V6A::All'

process = cms.Process("HLT3")

process.source = cms.Source("PoolSource",
    eventsToProcess = cms.untracked.VEventRange(),
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('/store/mc/Fall13dr/QCD_Pt-600to800_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU20bx25_POSTLS162_V2-v1/00000/022573C3-AE6D-E311-9144-002618943930.root')
)
process.hltAK4CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(True),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('CaloJet'),
    radiusPU = cms.double(0.4),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(5),
    minSeed = cms.uint32(14327),
    voronoiRfact = cms.double(0.9),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(-1.0),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(False),
    MaxVtxZ = cms.double(15.0),
    rParam = cms.double(0.4),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(False),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.0),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltTowerMakerForAll"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(1.0),
    puPtMin = cms.double(10.0),
    srcPVs = cms.InputTag("NotUsed"),
    inputEtMin = cms.double(0.3),
    trimPtFracMin = cms.double(-1.0),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.0),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltAK4CaloJetsCorrected = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("hltAK4CaloJets"),
    correctors = cms.vstring('hltESPAK4CaloCorrection')
)


process.hltAK4CaloJetsCorrectedIDPassed = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("hltAK4CaloJetsIDPassed"),
    correctors = cms.vstring('hltESPAK4CaloCorrection')
)


process.hltAK4CaloJetsIDPassed = cms.EDProducer("HLTCaloJetIDProducer",
    min_N90 = cms.int32(-2),
    min_N90hits = cms.int32(2),
    min_EMF = cms.double(1e-06),
    jetsInput = cms.InputTag("hltAK4CaloJets"),
    JetIDParams = cms.PSet(
        eeRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        hbheRecHitsColl = cms.InputTag("hltHbhereco"),
        hoRecHitsColl = cms.InputTag("hltHoreco"),
        ebRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        hfRecHitsColl = cms.InputTag("hltHfreco"),
        useRecHits = cms.bool(True)
    ),
    max_EMF = cms.double(999.0)
)


process.hltAK4CaloJetsPF = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('CaloJet'),
    radiusPU = cms.double(0.4),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(5),
    minSeed = cms.uint32(0),
    voronoiRfact = cms.double(-9.0),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(-1.0),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(False),
    MaxVtxZ = cms.double(15.0),
    rParam = cms.double(0.4),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(False),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.0),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltTowerMakerForPF"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(1.0),
    puPtMin = cms.double(10.0),
    srcPVs = cms.InputTag("NotUsed"),
    inputEtMin = cms.double(0.3),
    trimPtFracMin = cms.double(-1.0),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.0),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltAK4Iter0TrackJets4Iter1 = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('TrackJet'),
    radiusPU = cms.double(0.4),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(0),
    minSeed = cms.uint32(14327),
    voronoiRfact = cms.double(0.9),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(-1.0),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(False),
    MaxVtxZ = cms.double(30.0),
    rParam = cms.double(0.4),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(True),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.5),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltTrackIter0RefsForJets4Iter1"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(1.0),
    puPtMin = cms.double(0.0),
    srcPVs = cms.InputTag("hltTrimmedPixelVertices"),
    inputEtMin = cms.double(0.1),
    trimPtFracMin = cms.double(-1.0),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.2),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltAK4Iter1TrackJets4Iter2 = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('TrackJet'),
    radiusPU = cms.double(0.4),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(0),
    minSeed = cms.uint32(14327),
    voronoiRfact = cms.double(0.9),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(-1.0),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(False),
    MaxVtxZ = cms.double(30.0),
    rParam = cms.double(0.4),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(True),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.5),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltIter1TrackRefsForJets4Iter2"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(7.5),
    puPtMin = cms.double(0.0),
    srcPVs = cms.InputTag("hltTrimmedPixelVertices"),
    inputEtMin = cms.double(0.1),
    trimPtFracMin = cms.double(-1.0),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.2),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltAK4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(True),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    radiusPU = cms.double(0.4),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(0),
    minSeed = cms.uint32(0),
    voronoiRfact = cms.double(-9.0),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(-1.0),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(False),
    MaxVtxZ = cms.double(15.0),
    rParam = cms.double(0.4),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(False),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.0),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltParticleFlow"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(0.0),
    puPtMin = cms.double(10.0),
    srcPVs = cms.InputTag("hltPixelVertices"),
    inputEtMin = cms.double(0.0),
    trimPtFracMin = cms.double(-1.0),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.0),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltAK4PFJetsCorrected = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("hltAK4PFJets"),
    correctors = cms.vstring('hltESPAK4PFCorrection')
)


process.hltAK4PFJetsTrim = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(True),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    radiusPU = cms.double(0.4),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(0),
    minSeed = cms.uint32(0),
    voronoiRfact = cms.double(-9.0),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(0.2),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(True),
    MaxVtxZ = cms.double(15.0),
    rParam = cms.double(0.4),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(False),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.0),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltParticleFlow"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(0.0),
    puPtMin = cms.double(10.0),
    srcPVs = cms.InputTag("hltPixelVertices"),
    inputEtMin = cms.double(0.0),
    trimPtFracMin = cms.double(0.03),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.0),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltAK8CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(True),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('CaloJet'),
    radiusPU = cms.double(0.8),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(5),
    minSeed = cms.uint32(14327),
    voronoiRfact = cms.double(0.9),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(-1.0),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(False),
    MaxVtxZ = cms.double(15.0),
    rParam = cms.double(0.8),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(False),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.0),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltTowerMakerForAll"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(1.0),
    puPtMin = cms.double(10.0),
    srcPVs = cms.InputTag("NotUsed"),
    inputEtMin = cms.double(0.3),
    trimPtFracMin = cms.double(-1.0),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.0),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltAK8CaloJetsCorrected = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("hltAK8CaloJets"),
    correctors = cms.vstring('hltESPAK4CaloCorrection')
)


process.hltAK8CaloJetsCorrectedIDPassed = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("hltAK8CaloJetsIDPassed"),
    correctors = cms.vstring('hltESPAK4CaloCorrection')
)


process.hltAK8CaloJetsIDPassed = cms.EDProducer("HLTCaloJetIDProducer",
    min_N90 = cms.int32(-2),
    min_N90hits = cms.int32(2),
    min_EMF = cms.double(1e-06),
    jetsInput = cms.InputTag("hltAK8CaloJets"),
    JetIDParams = cms.PSet(
        eeRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        hbheRecHitsColl = cms.InputTag("hltHbhereco"),
        hoRecHitsColl = cms.InputTag("hltHoreco"),
        ebRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        hfRecHitsColl = cms.InputTag("hltHfreco"),
        useRecHits = cms.bool(True)
    ),
    max_EMF = cms.double(999.0)
)


process.hltAK8HtMht = cms.EDProducer("HLTHtMhtProducer",
    usePt = cms.bool(False),
    minPtJetHt = cms.double(40.0),
    maxEtaJetMht = cms.double(5.0),
    minNJetMht = cms.int32(0),
    jetsLabel = cms.InputTag("hltAK8CaloJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    minPtJetMht = cms.double(30.0),
    excludePFMuons = cms.bool(False),
    pfCandidatesLabel = cms.InputTag(""),
    minNJetHt = cms.int32(0)
)


process.hltAK8PFHT = cms.EDProducer("HLTHtMhtProducer",
    usePt = cms.bool(True),
    minPtJetHt = cms.double(40.0),
    maxEtaJetMht = cms.double(999.0),
    minNJetMht = cms.int32(0),
    jetsLabel = cms.InputTag("hltAK8PFJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    minPtJetMht = cms.double(0.0),
    excludePFMuons = cms.bool(False),
    pfCandidatesLabel = cms.InputTag("hltParticleFlow"),
    minNJetHt = cms.int32(0)
)


process.hltAK8PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(True),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    radiusPU = cms.double(0.8),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(0),
    minSeed = cms.uint32(0),
    voronoiRfact = cms.double(-9.0),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(-1.0),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(False),
    MaxVtxZ = cms.double(15.0),
    rParam = cms.double(0.8),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(False),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.0),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltParticleFlow"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(0.0),
    puPtMin = cms.double(10.0),
    srcPVs = cms.InputTag("hltPixelVertices"),
    inputEtMin = cms.double(0.0),
    trimPtFracMin = cms.double(-1.0),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.0),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltAK8PFJetsCorrected = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("hltAK8PFJets"),
    correctors = cms.vstring('hltESPAK4PFCorrection')
)


process.hltAK8PFJetsCorrectedMatchedToCaloJets260 = cms.EDProducer("PFJetsMatchedToFilteredCaloJetsProducer",
    DeltaR = cms.double(0.5),
    CaloJetFilter = cms.InputTag("hltAK8SingleCaloJet260"),
    TriggerType = cms.int32(85),
    PFJetSrc = cms.InputTag("hltAK8PFJetsCorrected")
)


process.hltAK8PFJetsTrim = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(True),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    radiusPU = cms.double(0.8),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(0),
    minSeed = cms.uint32(0),
    voronoiRfact = cms.double(-9.0),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(0.2),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(True),
    MaxVtxZ = cms.double(15.0),
    rParam = cms.double(0.8),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(False),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.0),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltParticleFlow"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(0.0),
    puPtMin = cms.double(10.0),
    srcPVs = cms.InputTag("hltPixelVertices"),
    inputEtMin = cms.double(0.0),
    trimPtFracMin = cms.double(0.03),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.0),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltAK8PFTrimHT = cms.EDProducer("HLTHtMhtProducer",
    usePt = cms.bool(True),
    minPtJetHt = cms.double(40.0),
    maxEtaJetMht = cms.double(999.0),
    minNJetMht = cms.int32(0),
    jetsLabel = cms.InputTag("hltAK8PFJetsTrim"),
    maxEtaJetHt = cms.double(3.0),
    minPtJetMht = cms.double(0.0),
    excludePFMuons = cms.bool(False),
    pfCandidatesLabel = cms.InputTag("hltParticleFlow"),
    minNJetHt = cms.int32(0)
)


process.hltAK8TrimJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    useMassDropTagger = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    muMin = cms.double(-1.0),
    Ghost_EtaMax = cms.double(5.0),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    subtractorName = cms.string(''),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    radiusPU = cms.double(0.5),
    subjetPtMin = cms.double(-1.0),
    MinVtxNdof = cms.int32(5),
    minSeed = cms.uint32(14327),
    voronoiRfact = cms.double(-0.9),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    muMax = cms.double(-1.0),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    yMin = cms.double(-1.0),
    useFiltering = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    rFilt = cms.double(0.2),
    yMax = cms.double(-1.0),
    zcut = cms.double(-1.0),
    useTrimming = cms.bool(True),
    MaxVtxZ = cms.double(15.0),
    rParam = cms.double(0.8),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(False),
    nFilt = cms.int32(-1),
    usePruning = cms.bool(False),
    maxDepth = cms.int32(-1),
    yCut = cms.double(-1.0),
    DzTrVtxMax = cms.double(0.0),
    dRMin = cms.double(-1.0),
    maxProblematicHcalCells = cms.uint32(9999999),
    rcut_factor = cms.double(-1.0),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("hltParticleFlow"),
    sumRecHits = cms.bool(False),
    jetPtMin = cms.double(20.0),
    puPtMin = cms.double(10.0),
    srcPVs = cms.InputTag("hltPixelVertices"),
    inputEtMin = cms.double(0.0),
    trimPtFracMin = cms.double(0.03),
    muCut = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    DxyTrVtxMax = cms.double(0.0),
    maxProblematicEcalCells = cms.uint32(9999999),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hltCsc2DRecHits = cms.EDProducer("CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double(0.0),
    XTasymmetry_ME1a = cms.double(0.0),
    XTasymmetry_ME41 = cms.double(0.0),
    ConstSyst_ME41 = cms.double(0.0),
    CSCStripxtalksOffset = cms.double(0.03),
    CSCUseCalibrations = cms.bool(True),
    CSCUseTimingCorrections = cms.bool(True),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
    XTasymmetry_ME22 = cms.double(0.0),
    UseFivePoleFit = cms.bool(True),
    XTasymmetry_ME21 = cms.double(0.0),
    ConstSyst_ME21 = cms.double(0.0),
    CSCDebug = cms.untracked.bool(False),
    XTasymmetry_ME32 = cms.double(0.0),
    ConstSyst_ME22 = cms.double(0.0),
    CSCUseGasGainCorrections = cms.bool(False),
    XTasymmetry_ME31 = cms.double(0.0),
    ConstSyst_ME1a = cms.double(0.022),
    readBadChambers = cms.bool(True),
    NoiseLevel_ME13 = cms.double(8.0),
    NoiseLevel_ME12 = cms.double(9.0),
    NoiseLevel_ME32 = cms.double(9.0),
    NoiseLevel_ME31 = cms.double(9.0),
    CSCStripClusterChargeCut = cms.double(25.0),
    ConstSyst_ME1b = cms.double(0.007),
    CSCStripClusterSize = cms.untracked.int32(3),
    CSCStripPeakThreshold = cms.double(10.0),
    readBadChannels = cms.bool(False),
    UseParabolaFit = cms.bool(False),
    XTasymmetry_ME13 = cms.double(0.0),
    XTasymmetry_ME12 = cms.double(0.0),
    wireDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi"),
    ConstSyst_ME12 = cms.double(0.0),
    ConstSyst_ME13 = cms.double(0.0),
    ConstSyst_ME32 = cms.double(0.0),
    ConstSyst_ME31 = cms.double(0.0),
    UseAverageTime = cms.bool(False),
    NoiseLevel_ME1a = cms.double(7.0),
    NoiseLevel_ME1b = cms.double(8.0),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCUseStaticPedestals = cms.bool(False),
    stripDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCStripDigi"),
    CSCstripWireDeltaTime = cms.int32(8),
    NoiseLevel_ME21 = cms.double(9.0),
    NoiseLevel_ME22 = cms.double(9.0),
    NoiseLevel_ME41 = cms.double(9.0)
)


process.hltCscSegments = cms.EDProducer("CSCSegmentProducer",
    inputObjects = cms.InputTag("hltCsc2DRecHits"),
    algo_type = cms.int32(1),
    algo_psets = cms.VPSet(cms.PSet(
        chamber_types = cms.vstring('ME1/a', 
            'ME1/b', 
            'ME1/2', 
            'ME1/3', 
            'ME2/1', 
            'ME2/2', 
            'ME3/1', 
            'ME3/2', 
            'ME4/1', 
            'ME4/2'),
        algo_name = cms.string('CSCSegAlgoST'),
        algo_psets = cms.VPSet(cms.PSet(
            maxRatioResidualPrune = cms.double(3.0),
            yweightPenalty = cms.double(1.5),
            maxRecHitsInCluster = cms.int32(20),
            dPhiFineMax = cms.double(0.025),
            preClusteringUseChaining = cms.bool(True),
            ForceCovariance = cms.bool(False),
            hitDropLimit6Hits = cms.double(0.3333),
            NormChi2Cut2D = cms.double(20.0),
            BPMinImprovement = cms.double(10000.0),
            Covariance = cms.double(0.0),
            tanPhiMax = cms.double(0.5),
            onlyBestSegment = cms.bool(False),
            SeedBig = cms.double(0.0015),
            dRPhiFineMax = cms.double(8.0),
            SeedSmall = cms.double(0.0002),
            curvePenalty = cms.double(2.0),
            dXclusBoxMax = cms.double(4.0),
            BrutePruning = cms.bool(True),
            tanThetaMax = cms.double(1.2),
            CorrectTheErrors = cms.bool(True),
            hitDropLimit4Hits = cms.double(0.6),
            useShowering = cms.bool(False),
            CSCDebug = cms.untracked.bool(False),
            curvePenaltyThreshold = cms.double(0.85),
            NormChi2Cut3D = cms.double(10.0),
            minHitsPerSegment = cms.int32(3),
            ForceCovarianceAll = cms.bool(False),
            yweightPenaltyThreshold = cms.double(1.0),
            prePrunLimit = cms.double(3.17),
            hitDropLimit5Hits = cms.double(0.8),
            preClustering = cms.bool(True),
            prePrun = cms.bool(True),
            maxDPhi = cms.double(999.0),
            maxDTheta = cms.double(999.0),
            Pruning = cms.bool(True),
            dYclusBoxMax = cms.double(8.0)
        ), 
            cms.PSet(
                maxRatioResidualPrune = cms.double(3.0),
                yweightPenalty = cms.double(1.5),
                maxRecHitsInCluster = cms.int32(24),
                dPhiFineMax = cms.double(0.025),
                preClusteringUseChaining = cms.bool(True),
                ForceCovariance = cms.bool(False),
                hitDropLimit6Hits = cms.double(0.3333),
                NormChi2Cut2D = cms.double(20.0),
                BPMinImprovement = cms.double(10000.0),
                Covariance = cms.double(0.0),
                tanPhiMax = cms.double(0.5),
                onlyBestSegment = cms.bool(False),
                SeedBig = cms.double(0.0015),
                dRPhiFineMax = cms.double(8.0),
                SeedSmall = cms.double(0.0002),
                curvePenalty = cms.double(2.0),
                dXclusBoxMax = cms.double(4.0),
                BrutePruning = cms.bool(True),
                tanThetaMax = cms.double(1.2),
                CorrectTheErrors = cms.bool(True),
                hitDropLimit4Hits = cms.double(0.6),
                useShowering = cms.bool(False),
                CSCDebug = cms.untracked.bool(False),
                curvePenaltyThreshold = cms.double(0.85),
                NormChi2Cut3D = cms.double(10.0),
                minHitsPerSegment = cms.int32(3),
                ForceCovarianceAll = cms.bool(False),
                yweightPenaltyThreshold = cms.double(1.0),
                prePrunLimit = cms.double(3.17),
                hitDropLimit5Hits = cms.double(0.8),
                preClustering = cms.bool(True),
                prePrun = cms.bool(True),
                maxDPhi = cms.double(999.0),
                maxDTheta = cms.double(999.0),
                Pruning = cms.bool(True),
                dYclusBoxMax = cms.double(8.0)
            )),
        parameters_per_chamber_type = cms.vint32(2, 1, 1, 1, 1, 
            1, 1, 1, 1, 1)
    ))
)


process.hltDt1DRecHits = cms.EDProducer("DTRecHitProducer",
    debug = cms.untracked.bool(False),
    recAlgoConfig = cms.PSet(
        tTrigMode = cms.string('DTTTrigSyncFromDB'),
        minTime = cms.double(-3.0),
        stepTwoFromDigi = cms.bool(False),
        doVdriftCorr = cms.bool(False),
        debug = cms.untracked.bool(False),
        tTrigModeConfig = cms.PSet(
            vPropWire = cms.double(24.4),
            doTOFCorrection = cms.bool(True),
            tofCorrType = cms.int32(0),
            wirePropCorrType = cms.int32(0),
            tTrigLabel = cms.string(''),
            doWirePropCorrection = cms.bool(True),
            doT0Correction = cms.bool(True),
            debug = cms.untracked.bool(False)
        ),
        maxTime = cms.double(420.0),
        useUncertDB = cms.bool(True)
    ),
    dtDigiLabel = cms.InputTag("hltMuonDTDigis"),
    recAlgo = cms.string('DTLinearDriftFromDBAlgo')
)


process.hltDt4DSegments = cms.EDProducer("DTRecSegment4DProducer",
    debug = cms.untracked.bool(False),
    Reco4DAlgoName = cms.string('DTCombinatorialPatternReco4D'),
    recHits2DLabel = cms.InputTag("dt2DSegments"),
    recHits1DLabel = cms.InputTag("hltDt1DRecHits"),
    Reco4DAlgoConfig = cms.PSet(
        segmCleanerMode = cms.int32(2),
        perform_delta_rejecting = cms.bool(False),
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        nSharedHitsMax = cms.int32(2),
        hit_afterT0_resolution = cms.double(0.03),
        Reco2DAlgoConfig = cms.PSet(
            segmCleanerMode = cms.int32(2),
            perform_delta_rejecting = cms.bool(False),
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            nSharedHitsMax = cms.int32(2),
            AlphaMaxPhi = cms.double(1.0),
            hit_afterT0_resolution = cms.double(0.03),
            MaxAllowedHits = cms.uint32(50),
            performT0_vdriftSegCorrection = cms.bool(False),
            AlphaMaxTheta = cms.double(0.9),
            debug = cms.untracked.bool(False),
            recAlgoConfig = cms.PSet(
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                minTime = cms.double(-3.0),
                stepTwoFromDigi = cms.bool(False),
                doVdriftCorr = cms.bool(False),
                debug = cms.untracked.bool(False),
                tTrigModeConfig = cms.PSet(
                    vPropWire = cms.double(24.4),
                    doTOFCorrection = cms.bool(True),
                    tofCorrType = cms.int32(0),
                    wirePropCorrType = cms.int32(0),
                    tTrigLabel = cms.string(''),
                    doWirePropCorrection = cms.bool(True),
                    doT0Correction = cms.bool(True),
                    debug = cms.untracked.bool(False)
                ),
                maxTime = cms.double(420.0),
                useUncertDB = cms.bool(True)
            ),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False)
        ),
        performT0_vdriftSegCorrection = cms.bool(False),
        debug = cms.untracked.bool(False),
        recAlgoConfig = cms.PSet(
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            minTime = cms.double(-3.0),
            stepTwoFromDigi = cms.bool(False),
            doVdriftCorr = cms.bool(False),
            debug = cms.untracked.bool(False),
            tTrigModeConfig = cms.PSet(
                vPropWire = cms.double(24.4),
                doTOFCorrection = cms.bool(True),
                tofCorrType = cms.int32(0),
                wirePropCorrType = cms.int32(0),
                tTrigLabel = cms.string(''),
                doWirePropCorrection = cms.bool(True),
                doT0Correction = cms.bool(True),
                debug = cms.untracked.bool(False)
            ),
            maxTime = cms.double(420.0),
            useUncertDB = cms.bool(True)
        ),
        nUnSharedHitsMin = cms.int32(2),
        AllDTRecHits = cms.bool(True),
        performT0SegCorrection = cms.bool(False),
        Reco2DAlgoName = cms.string('DTCombinatorialPatternReco')
    )
)


process.hltEcalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    integrityTTIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityTTIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    eeIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("hltEcalDigis"),
    eeFEToBeRecovered = cms.string('eeFE'),
    integrityBlockSizeErrors = cms.InputTag("hltEcalDigis","EcalIntegrityBlockSizeErrors"),
    eeSrFlagCollection = cms.InputTag("hltEcalDigis")
)


process.hltEcalDigis = cms.EDProducer("EcalRawToDigi",
    orderedDCCIdList = cms.vint32(1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 
        16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 
        26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 
        36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 
        46, 47, 48, 49, 50, 
        51, 52, 53, 54),
    FedLabel = cms.InputTag("listfeds"),
    tccUnpacking = cms.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    headerUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    orderedFedList = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    eventPut = cms.bool(True),
    feUnpacking = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    numbXtalTSamples = cms.int32(10),
    feIdCheck = cms.bool(True),
    FEDs = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    silentMode = cms.untracked.bool(True),
    DoRegional = cms.bool(False),
    forceToKeepFRData = cms.bool(False),
    memUnpacking = cms.bool(True)
)


process.hltEcalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    sourceTag = cms.InputTag("rawDataCollector"),
    debugMode = cms.untracked.bool(False),
    InstanceES = cms.string(''),
    ESdigiCollection = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat')
)


process.hltEcalPreshowerRecHit = cms.EDProducer("ESRecHitProducer",
    ESRecoAlgo = cms.int32(0),
    ESrechitCollection = cms.string('EcalRecHitsES'),
    ESdigiCollection = cms.InputTag("hltEcalPreshowerDigis"),
    algo = cms.string('ESRecHitWorker')
)


process.hltEcalRecHit = cms.EDProducer("EcalRecHitProducer",
    recoverEEVFE = cms.bool(False),
    EErechitCollection = cms.string('EcalRecHitsEE'),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    laserCorrection = cms.bool(True),
    EBLaserMIN = cms.double(0.5),
    killDeadChannels = cms.bool(True),
    dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
    EEuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEE"),
    EBLaserMAX = cms.double(3.0),
    EELaserMIN = cms.double(0.5),
    ebFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebFE"),
    EELaserMAX = cms.double(8.0),
    recoverEEIsolatedChannels = cms.bool(False),
    eeDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeDetId"),
    recoverEBFE = cms.bool(True),
    eeFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeFE"),
    ebDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebDetId"),
    singleChannelRecoveryThreshold = cms.double(8.0),
    ChannelStatusToBeExcluded = cms.vstring(),
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    triggerPrimitiveDigiCollection = cms.InputTag("hltEcalDigis","EcalTriggerPrimitives"),
    recoverEEFE = cms.bool(True),
    singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
    dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
    flagsMapDBReco = cms.PSet(
        kGood = cms.vstring('kOk', 
            'kDAC', 
            'kNoLaser', 
            'kNoisy'),
        kNeighboursRecovered = cms.vstring('kFixedG0', 
            'kNonRespondingIsolated', 
            'kDeadVFE'),
        kDead = cms.vstring('kNoDataNoTP'),
        kNoisy = cms.vstring('kNNoisy', 
            'kFixedG6', 
            'kFixedG1'),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    EBuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEB"),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    algo = cms.string('EcalRecHitWorkerSimple'),
    cleaningConfig = cms.PSet(
        tightenCrack_e1_double = cms.double(2.0),
        tightenCrack_e6e2_double = cms.double(3.0),
        e4e1Threshold_endcap = cms.double(0.3),
        tightenCrack_e4e1_single = cms.double(3.0),
        cThreshold_barrel = cms.double(4.0),
        e4e1Threshold_barrel = cms.double(0.08),
        tightenCrack_e1_single = cms.double(2.0),
        e4e1_b_barrel = cms.double(-0.024),
        e4e1_a_barrel = cms.double(0.04),
        ignoreOutOfTimeThresh = cms.double(1000000000.0),
        cThreshold_endcap = cms.double(15.0),
        e4e1_b_endcap = cms.double(-0.0125),
        e4e1_a_endcap = cms.double(0.02),
        e6e2thresh = cms.double(0.04),
        cThreshold_double = cms.double(10.0)
    ),
    logWarningEtThreshold_EB_FE = cms.double(50.0),
    logWarningEtThreshold_EE_FE = cms.double(50.0)
)


process.hltEcalUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag("hltEcalDigis","eeDigis"),
    alphaEB = cms.double(1.138),
    alphaEE = cms.double(1.89),
    EBdigiCollection = cms.InputTag("hltEcalDigis","ebDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    AlphaBetaFilename = cms.untracked.string('NOFILE'),
    betaEB = cms.double(1.655),
    MinAmplEndcap = cms.double(14.0),
    MinAmplBarrel = cms.double(8.0),
    algo = cms.string('EcalUncalibRecHitWorkerWeights'),
    betaEE = cms.double(1.4),
    UseDynamicPedestal = cms.bool(True),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB')
)


process.hltFEDSelector = cms.EDProducer("EvFFEDSelector",
    inputTag = cms.InputTag("rawDataCollector"),
    fedList = cms.vuint32(1023)
)


process.hltFixedGridRhoFastjetAll = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(5.0),
    pfCandidatesTag = cms.InputTag("hltParticleFlow")
)


process.hltFixedGridRhoFastjetAllCalo = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(5.0),
    pfCandidatesTag = cms.InputTag("hltTowerMakerForAll")
)


process.hltGctDigis = cms.EDProducer("GctRawToDigi",
    unpackSharedRegions = cms.bool(False),
    numberOfGctSamplesToUnpack = cms.uint32(1),
    verbose = cms.untracked.bool(False),
    numberOfRctSamplesToUnpack = cms.uint32(1),
    inputLabel = cms.InputTag("rawDataCollector"),
    unpackerVersion = cms.uint32(0),
    gctFedId = cms.untracked.int32(745),
    hltMode = cms.bool(True)
)


process.hltGtDigis = cms.EDProducer("L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32(813),
    DaqGtInputTag = cms.InputTag("rawDataCollector"),
    UnpackBxInEvent = cms.int32(5),
    ActiveBoardsMask = cms.uint32(65535)
)


process.hltHbhereco = cms.EDProducer("HcalHitReconstructor",
    digiTimeFromDB = cms.bool(True),
    mcOOTCorrectionName = cms.string(''),
    setTimingShapedCutsFlags = cms.bool(False),
    S9S1stat = cms.PSet(

    ),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    tsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    mcOOTCorrectionCategory = cms.string('MC'),
    dataOOTCorrectionName = cms.string(''),
    correctionPhaseNS = cms.double(13.0),
    HFInWindowStat = cms.PSet(

    ),
    pulseShapeParameters = cms.PSet(

    ),
    digiLabel = cms.InputTag("hltHcalDigis"),
    timingshapedcutsParameters = cms.PSet(
        ignorelowest = cms.bool(True),
        win_offset = cms.double(0.0),
        ignorehighest = cms.bool(False),
        win_gain = cms.double(1.0),
        tfilterEnvelope = cms.vdouble(4.0, 12.04, 13.0, 10.56, 23.5, 
            8.82, 37.0, 7.38, 56.0, 6.3, 
            81.0, 5.64, 114.5, 5.44, 175.5, 
            5.38, 350.5, 5.14)
    ),
    setHSCPFlags = cms.bool(False),
    firstAuxTS = cms.int32(4),
    setSaturationFlags = cms.bool(False),
    hfTimingTrustParameters = cms.PSet(

    ),
    PETstat = cms.PSet(

    ),
    digistat = cms.PSet(

    ),
    useLeakCorrection = cms.bool(False),
    flagParameters = cms.PSet(
        nominalPedestal = cms.double(3.0),
        hitMultiplicityThreshold = cms.int32(17),
        hitEnergyMinimum = cms.double(1.0),
        pulseShapeParameterSets = cms.VPSet(cms.PSet(
            pulseShapeParameters = cms.vdouble(0.0, 100.0, -50.0, 0.0, -15.0, 
                0.15)
        ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(100.0, 2000.0, -50.0, 0.0, -5.0, 
                    0.05)
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(2000.0, 1000000.0, -50.0, 0.0, 95.0, 
                    0.0)
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(-1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 
                    0.0)
            ))
    ),
    setTimingTrustFlags = cms.bool(False),
    S8S1stat = cms.PSet(

    ),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    setNoiseFlags = cms.bool(False),
    correctTiming = cms.bool(False),
    setPulseShapeFlags = cms.bool(False),
    Subdetector = cms.string('HBHE'),
    hscpParameters = cms.PSet(
        slopeMax = cms.double(-0.6),
        r1Max = cms.double(1.0),
        r1Min = cms.double(0.15),
        fracLeaderMax = cms.double(0.7),
        slopeMin = cms.double(-1.5),
        outerMin = cms.double(0.0),
        outerMax = cms.double(0.1),
        fracLeaderMin = cms.double(0.4),
        r2Min = cms.double(0.1),
        r2Max = cms.double(0.5),
        TimingEnergyThreshold = cms.double(30.0)
    ),
    firstSample = cms.int32(4),
    dropZSmarkedPassed = cms.bool(True),
    recoParamsFromDB = cms.bool(True),
    dataOOTCorrectionCategory = cms.string('Data')
)


process.hltHcalDigis = cms.EDProducer("HcalRawToDigi",
    UnpackZDC = cms.untracked.bool(True),
    FilterDataQuality = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    ComplainEmptyData = cms.untracked.bool(False),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(False),
    lastSample = cms.int32(9),
    firstSample = cms.int32(0)
)


process.hltHfreco = cms.EDProducer("HcalHitReconstructor",
    digiTimeFromDB = cms.bool(True),
    mcOOTCorrectionName = cms.string(''),
    setTimingShapedCutsFlags = cms.bool(False),
    S9S1stat = cms.PSet(
        longETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        HcalAcceptSeverityLevel = cms.int32(9),
        shortEnergyParams = cms.vdouble(35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093),
        flagsToSkip = cms.int32(24),
        shortETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        short_optimumSlope = cms.vdouble(-99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927),
        longEnergyParams = cms.vdouble(43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62),
        long_optimumSlope = cms.vdouble(-99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927),
        isS8S1 = cms.bool(False)
    ),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    tsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(2),
    mcOOTCorrectionCategory = cms.string('MC'),
    dataOOTCorrectionName = cms.string(''),
    correctionPhaseNS = cms.double(13.0),
    HFInWindowStat = cms.PSet(
        hflongEthresh = cms.double(40.0),
        hflongMinWindowTime = cms.vdouble(-10.0),
        hfshortEthresh = cms.double(40.0),
        hflongMaxWindowTime = cms.vdouble(10.0),
        hfshortMaxWindowTime = cms.vdouble(10.0),
        hfshortMinWindowTime = cms.vdouble(-12.0)
    ),
    pulseShapeParameters = cms.PSet(

    ),
    digiLabel = cms.InputTag("hltHcalDigis"),
    timingshapedcutsParameters = cms.PSet(

    ),
    setHSCPFlags = cms.bool(False),
    firstAuxTS = cms.int32(1),
    setSaturationFlags = cms.bool(False),
    hfTimingTrustParameters = cms.PSet(
        hfTimingTrustLevel2 = cms.int32(4),
        hfTimingTrustLevel1 = cms.int32(1)
    ),
    PETstat = cms.PSet(
        longETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        short_R_29 = cms.vdouble(0.8),
        HcalAcceptSeverityLevel = cms.int32(9),
        shortEnergyParams = cms.vdouble(35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093),
        flagsToSkip = cms.int32(0),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        short_R = cms.vdouble(0.8),
        longEnergyParams = cms.vdouble(43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62),
        long_R = cms.vdouble(0.98)
    ),
    digistat = cms.PSet(
        HFdigiflagCoef = cms.vdouble(0.93, -0.012667, -0.38275),
        HFdigiflagExpectedPeak = cms.int32(2),
        HFdigiflagSamplesToAdd = cms.int32(3),
        HFdigiflagFirstSample = cms.int32(1),
        HFdigiflagMinEthreshold = cms.double(40.0)
    ),
    useLeakCorrection = cms.bool(False),
    flagParameters = cms.PSet(

    ),
    setTimingTrustFlags = cms.bool(False),
    S8S1stat = cms.PSet(
        longETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        HcalAcceptSeverityLevel = cms.int32(9),
        shortEnergyParams = cms.vdouble(40.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0),
        flagsToSkip = cms.int32(16),
        shortETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        short_optimumSlope = cms.vdouble(0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1),
        longEnergyParams = cms.vdouble(40.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0),
        long_optimumSlope = cms.vdouble(0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1),
        isS8S1 = cms.bool(True)
    ),
    correctForPhaseContainment = cms.bool(False),
    correctForTimeslew = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    correctTiming = cms.bool(False),
    setPulseShapeFlags = cms.bool(False),
    Subdetector = cms.string('HF'),
    hscpParameters = cms.PSet(

    ),
    firstSample = cms.int32(2),
    dropZSmarkedPassed = cms.bool(True),
    recoParamsFromDB = cms.bool(True),
    dataOOTCorrectionCategory = cms.string('Data')
)


process.hltHoreco = cms.EDProducer("HcalHitReconstructor",
    digiTimeFromDB = cms.bool(True),
    mcOOTCorrectionName = cms.string(''),
    setTimingShapedCutsFlags = cms.bool(False),
    S9S1stat = cms.PSet(

    ),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    tsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    mcOOTCorrectionCategory = cms.string('MC'),
    dataOOTCorrectionName = cms.string(''),
    correctionPhaseNS = cms.double(13.0),
    HFInWindowStat = cms.PSet(

    ),
    pulseShapeParameters = cms.PSet(

    ),
    digiLabel = cms.InputTag("hltHcalDigis"),
    timingshapedcutsParameters = cms.PSet(

    ),
    setHSCPFlags = cms.bool(False),
    firstAuxTS = cms.int32(4),
    setSaturationFlags = cms.bool(False),
    hfTimingTrustParameters = cms.PSet(

    ),
    PETstat = cms.PSet(

    ),
    digistat = cms.PSet(

    ),
    useLeakCorrection = cms.bool(False),
    flagParameters = cms.PSet(

    ),
    setTimingTrustFlags = cms.bool(False),
    S8S1stat = cms.PSet(

    ),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    setNoiseFlags = cms.bool(False),
    correctTiming = cms.bool(False),
    setPulseShapeFlags = cms.bool(False),
    Subdetector = cms.string('HO'),
    hscpParameters = cms.PSet(

    ),
    firstSample = cms.int32(4),
    dropZSmarkedPassed = cms.bool(True),
    recoParamsFromDB = cms.bool(True),
    dataOOTCorrectionCategory = cms.string('Data')
)


process.hltHtMht = cms.EDProducer("HLTHtMhtProducer",
    usePt = cms.bool(False),
    minPtJetHt = cms.double(40.0),
    maxEtaJetMht = cms.double(5.0),
    minNJetMht = cms.int32(0),
    jetsLabel = cms.InputTag("hltAK4CaloJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    minPtJetMht = cms.double(30.0),
    excludePFMuons = cms.bool(False),
    pfCandidatesLabel = cms.InputTag(""),
    minNJetHt = cms.int32(0)
)


process.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool(True),
    originHalfLength = cms.double(0.3),
    useProtoTrackKinematics = cms.bool(False),
    usePV = cms.bool(False),
    InputVertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    InputCollection = cms.InputTag("hltPixelTracks"),
    originRadius = cms.double(0.1)
)


process.hltIter0PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("hltIter0PFLowPixelSeedsFromPixelTracks"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    cleanTrajectoryAfterInOut = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryBuilderIT')
    ),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string(''),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    )
)


process.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("hltIter0PFlowCkfTrackCandidates"),
    SimpleMagneticField = cms.string('ParabolicMf'),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    AlgorithmName = cms.string('iter0'),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    GeometricInnerState = cms.bool(True),
    useSimpleMF = cms.bool(True),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator')
)


process.hltIter0PFlowTrackSelectionHighPurity = cms.EDProducer("AnalyticalTrackSelector",
    max_d0 = cms.double(100.0),
    minNumber3DLayers = cms.uint32(0),
    max_lostHitFraction = cms.double(1.0),
    applyAbsCutsIfNoPV = cms.bool(False),
    qualityBit = cms.string('highPurity'),
    minNumberLayers = cms.uint32(3),
    chi2n_par = cms.double(0.7),
    useVtxError = cms.bool(False),
    dz_par1 = cms.vdouble(0.35, 4.0),
    dz_par2 = cms.vdouble(0.4, 4.0),
    applyAdaptedPVCuts = cms.bool(True),
    min_eta = cms.double(-9999.0),
    nSigmaZ = cms.double(3.0),
    copyTrajectories = cms.untracked.bool(True),
    vtxNumber = cms.int32(-1),
    max_d0NoPV = cms.double(100.0),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(1),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    max_relpterr = cms.double(9999.0),
    copyExtras = cms.untracked.bool(True),
    max_z0NoPV = cms.double(100.0),
    vertexCut = cms.string('tracksSize>=3'),
    max_z0 = cms.double(100.0),
    useVertices = cms.bool(True),
    min_nhits = cms.uint32(0),
    src = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks"),
    max_minMissHitOutOrIn = cms.int32(99),
    chi2n_no1Dmod_par = cms.double(9999.0),
    vertices = cms.InputTag("hltTrimmedPixelVertices"),
    max_eta = cms.double(9999.0),
    d0_par2 = cms.vdouble(0.4, 4.0),
    d0_par1 = cms.vdouble(0.3, 4.0),
    res_par = cms.vdouble(0.003, 0.001),
    minHitsToBypassChecks = cms.uint32(20)
)


process.hltIter0TrackAndTauJets4Iter1 = cms.EDProducer("TauJetSelectorForHLTTrackSeeding",
    fractionMinCaloInTauCone = cms.double(0.7),
    fractionMaxChargedPUInCaloCone = cms.double(0.3),
    etaMinCaloJet = cms.double(-2.7),
    ptTrkMaxInCaloCone = cms.double(1.0),
    isolationConeSize = cms.double(0.5),
    inputTrackJetTag = cms.InputTag("hltAK4Iter0TrackJets4Iter1"),
    nTrkMaxInCaloCone = cms.int32(0),
    inputCaloJetTag = cms.InputTag("hltAK4CaloJetsPFEt5"),
    etaMaxCaloJet = cms.double(2.7),
    ptMinCaloJet = cms.double(5.0),
    inputTrackTag = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity"),
    tauConeSize = cms.double(0.2)
)


process.hltIter1ClustersRefRemoval = cms.EDProducer("HLTTrackClusterRemoverNew",
    doStrip = cms.bool(True),
    doStripChargeCheck = cms.bool(True),
    trajectories = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity"),
    oldClusterRemovalInfo = cms.InputTag(""),
    stripClusters = cms.InputTag("hltSiStripRawToClustersFacility"),
    pixelClusters = cms.InputTag("hltSiPixelClusters"),
    Common = cms.PSet(
        minGoodStripCharge = cms.double(50.0),
        maxChi2 = cms.double(9.0)
    ),
    doPixel = cms.bool(True)
)


process.hltIter1MaskedMeasurementTrackerEvent = cms.EDProducer("MaskedMeasurementTrackerEventProducer",
    src = cms.InputTag("hltSiStripClusters"),
    OnDemand = cms.bool(False),
    clustersToSkip = cms.InputTag("hltIter1ClustersRefRemoval")
)


process.hltIter1Merged = cms.EDProducer("SimpleTrackListMerger",
    ShareFrac = cms.double(0.19),
    promoteTrackQuality = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    allowFirstHitShare = cms.bool(True),
    newQuality = cms.string('confirmed'),
    MaxNormalizedChisq = cms.double(1000.0),
    FoundHitBonus = cms.double(5.0),
    MinFound = cms.int32(3),
    LostHitPenalty = cms.double(20.0),
    TrackProducer2 = cms.string('hltIter1PFlowTrackSelectionHighPurity'),
    TrackProducer1 = cms.string('hltIter0PFlowTrackSelectionHighPurity')
)


process.hltIter1PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("hltIter1PFlowPixelSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    MeasurementTrackerEvent = cms.InputTag("hltIter1MaskedMeasurementTrackerEvent"),
    cleanTrajectoryAfterInOut = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryBuilderIT')
    ),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string(''),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    )
)


process.hltIter1PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("hltIter1PFlowCkfTrackCandidates"),
    SimpleMagneticField = cms.string('ParabolicMf'),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    MeasurementTrackerEvent = cms.InputTag("hltIter1MaskedMeasurementTrackerEvent"),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    AlgorithmName = cms.string('iter1'),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    GeometricInnerState = cms.bool(True),
    useSimpleMF = cms.bool(True),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator')
)


process.hltIter1PFlowPixelSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("hltSiPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(50000),
        doClusterCheck = cms.bool(False),
        ClusterCollectionLabel = cms.InputTag("hltSiStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(10000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('CandidateSeededTrackingRegionsProducer'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            zErrorVetex = cms.double(0.1),
            zErrorBeamSpot = cms.double(15.0),
            maxNRegions = cms.int32(100),
            nSigmaZBeamSpot = cms.double(3.0),
            deltaEta = cms.double(1.0),
            deltaPhi = cms.double(1.0),
            vertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
            mode = cms.string('VerticesFixed'),
            searchOpt = cms.bool(True),
            maxNVertices = cms.int32(10),
            input = cms.InputTag("hltIter0TrackAndTauJets4Iter1"),
            measurementTrackerName = cms.string('hltIter1MaskedMeasurementTrackerEvent'),
            originRadius = cms.double(0.05),
            ptMin = cms.double(0.5)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
        propagator = cms.string('PropagatorWithMaterialParabolicMf')
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(0),
        ComponentName = cms.string('StandardHitTripletGenerator'),
        SeedingLayers = cms.InputTag("hltIter1PixelLayerTriplets"),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            phiPreFiltering = cms.double(0.3),
            extraHitRPhitolerance = cms.double(0.032),
            useMultScattering = cms.bool(True),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            extraHitRZtolerance = cms.double(0.037),
            ComponentName = cms.string('PixelTripletHLTGenerator')
        )
    ),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
)


process.hltIter1PFlowTrackSelectionHighPurity = cms.EDProducer("SimpleTrackListMerger",
    ShareFrac = cms.double(0.19),
    promoteTrackQuality = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    allowFirstHitShare = cms.bool(True),
    newQuality = cms.string('confirmed'),
    MaxNormalizedChisq = cms.double(1000.0),
    FoundHitBonus = cms.double(5.0),
    MinFound = cms.int32(3),
    LostHitPenalty = cms.double(20.0),
    TrackProducer2 = cms.string('hltIter1PFlowTrackSelectionHighPurityTight'),
    TrackProducer1 = cms.string('hltIter1PFlowTrackSelectionHighPurityLoose')
)


process.hltIter1PFlowTrackSelectionHighPurityLoose = cms.EDProducer("AnalyticalTrackSelector",
    max_d0 = cms.double(100.0),
    minNumber3DLayers = cms.uint32(0),
    max_lostHitFraction = cms.double(1.0),
    applyAbsCutsIfNoPV = cms.bool(False),
    qualityBit = cms.string('highPurity'),
    minNumberLayers = cms.uint32(3),
    chi2n_par = cms.double(0.7),
    useVtxError = cms.bool(False),
    dz_par1 = cms.vdouble(0.8, 3.0),
    dz_par2 = cms.vdouble(0.9, 3.0),
    applyAdaptedPVCuts = cms.bool(True),
    min_eta = cms.double(-9999.0),
    nSigmaZ = cms.double(3.0),
    copyTrajectories = cms.untracked.bool(True),
    vtxNumber = cms.int32(-1),
    max_d0NoPV = cms.double(100.0),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(1),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    max_relpterr = cms.double(9999.0),
    copyExtras = cms.untracked.bool(True),
    max_z0NoPV = cms.double(100.0),
    vertexCut = cms.string('tracksSize>=3'),
    max_z0 = cms.double(100.0),
    useVertices = cms.bool(True),
    min_nhits = cms.uint32(0),
    src = cms.InputTag("hltIter1PFlowCtfWithMaterialTracks"),
    max_minMissHitOutOrIn = cms.int32(99),
    chi2n_no1Dmod_par = cms.double(9999.0),
    vertices = cms.InputTag("hltTrimmedPixelVertices"),
    max_eta = cms.double(9999.0),
    d0_par2 = cms.vdouble(0.9, 3.0),
    d0_par1 = cms.vdouble(0.85, 3.0),
    res_par = cms.vdouble(0.003, 0.001),
    minHitsToBypassChecks = cms.uint32(20)
)


process.hltIter1PFlowTrackSelectionHighPurityTight = cms.EDProducer("AnalyticalTrackSelector",
    max_d0 = cms.double(100.0),
    minNumber3DLayers = cms.uint32(0),
    max_lostHitFraction = cms.double(1.0),
    applyAbsCutsIfNoPV = cms.bool(False),
    qualityBit = cms.string('highPurity'),
    minNumberLayers = cms.uint32(5),
    chi2n_par = cms.double(0.4),
    useVtxError = cms.bool(False),
    dz_par1 = cms.vdouble(1.0, 4.0),
    dz_par2 = cms.vdouble(1.0, 4.0),
    applyAdaptedPVCuts = cms.bool(True),
    min_eta = cms.double(-9999.0),
    nSigmaZ = cms.double(3.0),
    copyTrajectories = cms.untracked.bool(True),
    vtxNumber = cms.int32(-1),
    max_d0NoPV = cms.double(100.0),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(1),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    max_relpterr = cms.double(9999.0),
    copyExtras = cms.untracked.bool(True),
    max_z0NoPV = cms.double(100.0),
    vertexCut = cms.string('tracksSize>=3'),
    max_z0 = cms.double(100.0),
    useVertices = cms.bool(True),
    min_nhits = cms.uint32(0),
    src = cms.InputTag("hltIter1PFlowCtfWithMaterialTracks"),
    max_minMissHitOutOrIn = cms.int32(99),
    chi2n_no1Dmod_par = cms.double(9999.0),
    vertices = cms.InputTag("hltTrimmedPixelVertices"),
    max_eta = cms.double(9999.0),
    d0_par2 = cms.vdouble(1.0, 4.0),
    d0_par1 = cms.vdouble(1.0, 4.0),
    res_par = cms.vdouble(0.003, 0.001),
    minHitsToBypassChecks = cms.uint32(20)
)


process.hltIter1PixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltIter1TrackAndTauJets4Iter2 = cms.EDProducer("TauJetSelectorForHLTTrackSeeding",
    fractionMinCaloInTauCone = cms.double(0.7),
    fractionMaxChargedPUInCaloCone = cms.double(0.3),
    etaMinCaloJet = cms.double(-2.7),
    ptTrkMaxInCaloCone = cms.double(1.4),
    isolationConeSize = cms.double(0.5),
    inputTrackJetTag = cms.InputTag("hltAK4Iter1TrackJets4Iter2"),
    nTrkMaxInCaloCone = cms.int32(0),
    inputCaloJetTag = cms.InputTag("hltAK4CaloJetsPFEt5"),
    etaMaxCaloJet = cms.double(2.7),
    ptMinCaloJet = cms.double(5.0),
    inputTrackTag = cms.InputTag("hltIter1Merged"),
    tauConeSize = cms.double(0.2)
)


process.hltIter1TrackRefsForJets4Iter2 = cms.EDProducer("ChargedRefCandidateProducer",
    src = cms.InputTag("hltIter1Merged"),
    particleType = cms.string('pi+')
)


process.hltIter2ClustersRefRemoval = cms.EDProducer("HLTTrackClusterRemoverNew",
    doStrip = cms.bool(True),
    doStripChargeCheck = cms.bool(True),
    trajectories = cms.InputTag("hltIter1PFlowTrackSelectionHighPurity"),
    oldClusterRemovalInfo = cms.InputTag("hltIter1ClustersRefRemoval"),
    stripClusters = cms.InputTag("hltSiStripRawToClustersFacility"),
    pixelClusters = cms.InputTag("hltSiPixelClusters"),
    Common = cms.PSet(
        minGoodStripCharge = cms.double(60.0),
        maxChi2 = cms.double(16.0)
    ),
    doPixel = cms.bool(True)
)


process.hltIter2MaskedMeasurementTrackerEvent = cms.EDProducer("MaskedMeasurementTrackerEventProducer",
    src = cms.InputTag("hltSiStripClusters"),
    OnDemand = cms.bool(False),
    clustersToSkip = cms.InputTag("hltIter2ClustersRefRemoval")
)


process.hltIter2Merged = cms.EDProducer("SimpleTrackListMerger",
    ShareFrac = cms.double(0.19),
    promoteTrackQuality = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    allowFirstHitShare = cms.bool(True),
    newQuality = cms.string('confirmed'),
    MaxNormalizedChisq = cms.double(1000.0),
    FoundHitBonus = cms.double(5.0),
    MinFound = cms.int32(3),
    LostHitPenalty = cms.double(20.0),
    TrackProducer2 = cms.string('hltIter2PFlowTrackSelectionHighPurity'),
    TrackProducer1 = cms.string('hltIter1Merged')
)


process.hltIter2PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("hltIter2PFlowPixelSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    MeasurementTrackerEvent = cms.InputTag("hltIter2MaskedMeasurementTrackerEvent"),
    cleanTrajectoryAfterInOut = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryBuilderIT')
    ),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string(''),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    )
)


process.hltIter2PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("hltIter2PFlowCkfTrackCandidates"),
    SimpleMagneticField = cms.string('ParabolicMf'),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    MeasurementTrackerEvent = cms.InputTag("hltIter2MaskedMeasurementTrackerEvent"),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    AlgorithmName = cms.string('iter2'),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    GeometricInnerState = cms.bool(True),
    useSimpleMF = cms.bool(True),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator')
)


process.hltIter2PFlowPixelSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("hltSiPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(50000),
        doClusterCheck = cms.bool(False),
        ClusterCollectionLabel = cms.InputTag("hltSiStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(10000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('CandidateSeededTrackingRegionsProducer'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            zErrorVetex = cms.double(0.05),
            zErrorBeamSpot = cms.double(15.0),
            maxNRegions = cms.int32(100),
            nSigmaZBeamSpot = cms.double(3.0),
            deltaEta = cms.double(0.8),
            deltaPhi = cms.double(0.8),
            ptMin = cms.double(1.2),
            vertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
            mode = cms.string('VerticesFixed'),
            searchOpt = cms.bool(True),
            maxNVertices = cms.int32(10),
            input = cms.InputTag("hltIter1TrackAndTauJets4Iter2"),
            measurementTrackerName = cms.string('hltIter2MaskedMeasurementTrackerEvent'),
            originZPos = cms.double(0.0),
            originRadius = cms.double(0.025)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        propagator = cms.string('PropagatorWithMaterialParabolicMf')
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(0),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.InputTag("hltIter2PixelLayerPairs"),
        GeneratorPSet = cms.PSet(
            maxElement = cms.uint32(100000),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            )
        )
    ),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
)


process.hltIter2PFlowTrackSelectionHighPurity = cms.EDProducer("AnalyticalTrackSelector",
    max_d0 = cms.double(100.0),
    minNumber3DLayers = cms.uint32(0),
    max_lostHitFraction = cms.double(1.0),
    applyAbsCutsIfNoPV = cms.bool(False),
    qualityBit = cms.string('highPurity'),
    minNumberLayers = cms.uint32(3),
    chi2n_par = cms.double(0.7),
    useVtxError = cms.bool(False),
    dz_par1 = cms.vdouble(0.35, 4.0),
    dz_par2 = cms.vdouble(0.4, 4.0),
    applyAdaptedPVCuts = cms.bool(True),
    min_eta = cms.double(-9999.0),
    nSigmaZ = cms.double(3.0),
    copyTrajectories = cms.untracked.bool(True),
    vtxNumber = cms.int32(-1),
    max_d0NoPV = cms.double(100.0),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(1),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    max_relpterr = cms.double(9999.0),
    copyExtras = cms.untracked.bool(True),
    max_z0NoPV = cms.double(100.0),
    vertexCut = cms.string('tracksSize>=3'),
    max_z0 = cms.double(100.0),
    useVertices = cms.bool(True),
    min_nhits = cms.uint32(0),
    src = cms.InputTag("hltIter2PFlowCtfWithMaterialTracks"),
    max_minMissHitOutOrIn = cms.int32(99),
    chi2n_no1Dmod_par = cms.double(9999.0),
    vertices = cms.InputTag("hltTrimmedPixelVertices"),
    max_eta = cms.double(9999.0),
    d0_par2 = cms.vdouble(0.4, 4.0),
    d0_par1 = cms.vdouble(0.3, 4.0),
    res_par = cms.vdouble(0.003, 0.001),
    minHitsToBypassChecks = cms.uint32(20)
)


process.hltIter2PixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltL1GtObjectMap = cms.EDProducer("L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool(True),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    AlgorithmTriggersUnmasked = cms.bool(False),
    EmulateBxInEvent = cms.int32(1),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    ProduceL1GtDaqRecord = cms.bool(False),
    ReadTechnicalTriggerRecords = cms.bool(True),
    RecordLength = cms.vint32(3, 0),
    TechnicalTriggersUnmasked = cms.bool(False),
    ProduceL1GtEvmRecord = cms.bool(False),
    GmtInputTag = cms.InputTag("hltGtDigis"),
    TechnicalTriggersVetoUnmasked = cms.bool(True),
    AlternativeNrBxBoardEvm = cms.uint32(0),
    TechnicalTriggersInputTags = cms.VInputTag("simBscDigis"),
    CastorInputTag = cms.InputTag("castorL1Digis"),
    GctInputTag = cms.InputTag("hltGctDigis"),
    AlternativeNrBxBoardDaq = cms.uint32(0),
    WritePsbL1GtDaqRecord = cms.bool(False),
    BstLengthBytes = cms.int32(-1)
)


process.hltL1extraParticles = cms.EDProducer("L1ExtraParticlesProd",
    centralBxOnly = cms.bool(True),
    muonSource = cms.InputTag("hltGtDigis"),
    etTotalSource = cms.InputTag("hltGctDigis"),
    etHadSource = cms.InputTag("hltGctDigis"),
    centralJetSource = cms.InputTag("hltGctDigis","cenJets"),
    etMissSource = cms.InputTag("hltGctDigis"),
    hfRingEtSumsSource = cms.InputTag("hltGctDigis"),
    produceMuonParticles = cms.bool(True),
    forwardJetSource = cms.InputTag("hltGctDigis","forJets"),
    ignoreHtMiss = cms.bool(False),
    htMissSource = cms.InputTag("hltGctDigis"),
    produceCaloParticles = cms.bool(True),
    tauJetSource = cms.InputTag("hltGctDigis","tauJets"),
    isolatedEmSource = cms.InputTag("hltGctDigis","isoEm"),
    nonIsolatedEmSource = cms.InputTag("hltGctDigis","nonIsoEm"),
    hfRingBitCountsSource = cms.InputTag("hltGctDigis")
)


process.hltL2MuonCandidates = cms.EDProducer("L2MuonCandidateProducer",
    InputObjects = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL2MuonSeeds = cms.EDProducer("L2MuonSeedGenerator",
    L1MinPt = cms.double(0.0),
    InputObjects = cms.InputTag("hltL1extraParticles"),
    L1MaxEta = cms.double(2.5),
    OfflineSeedLabel = cms.untracked.InputTag("hltL2OfflineMuonSeeds"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    L1MinQuality = cms.uint32(1),
    GMTReadoutCollection = cms.InputTag("hltGtDigis"),
    UseUnassociatedL1 = cms.bool(False),
    UseOfflineSeed = cms.untracked.bool(True),
    Propagator = cms.string('SteppingHelixPropagatorAny')
)


process.hltL2Muons = cms.EDProducer("L2MuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny', 
            'hltESPFastSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    InputObjects = cms.InputTag("hltL2MuonSeeds"),
    SeedTransformerParameters = cms.PSet(
        Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        UseSubRecHits = cms.bool(False),
        NMinRecHits = cms.uint32(2),
        RescaleError = cms.double(100.0)
    ),
    L2TrajBuilderParameters = cms.PSet(
        DoRefit = cms.bool(False),
        SeedPropagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        FilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            FitDirection = cms.string('insideOut'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits"),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        NavigationType = cms.string('Standard'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            UseSubRecHits = cms.bool(False),
            NMinRecHits = cms.uint32(2),
            RescaleError = cms.double(100.0)
        ),
        DoBackwardFilter = cms.bool(True),
        SeedPosition = cms.string('in'),
        BWFilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            FitDirection = cms.string('outsideIn'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            BWSeedType = cms.string('fromGenerator'),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits"),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        DoSeedRefit = cms.bool(False)
    ),
    DoSeedRefit = cms.bool(False),
    TrackLoaderParameters = cms.PSet(
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            BeamSpotPosition = cms.vdouble(0.0, 0.0, 0.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        VertexConstraint = cms.bool(True)
    ),
    MuonTrajectoryBuilder = cms.string('Exhaustive')
)


process.hltL2OfflineMuonSeeds = cms.EDProducer("MuonSeedGenerator",
    SMB_21 = cms.vdouble(1.043, -0.124, 0.0, 0.183, 0.0, 
        0.0),
    SMB_20 = cms.vdouble(1.011, -0.052, 0.0, 0.188, 0.0, 
        0.0),
    SMB_22 = cms.vdouble(1.474, -0.758, 0.0, 0.185, 0.0, 
        0.0),
    OL_2213 = cms.vdouble(0.117, 0.0, 0.0, 0.044, 0.0, 
        0.0),
    SME_11 = cms.vdouble(3.295, -1.527, 0.112, 0.378, 0.02, 
        0.0),
    SME_13 = cms.vdouble(-1.286, 1.711, 0.0, 0.356, 0.0, 
        0.0),
    SME_12 = cms.vdouble(0.102, 0.599, 0.0, 0.38, 0.0, 
        0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    DT_13 = cms.vdouble(0.315, 0.068, -0.127, 0.051, -0.002, 
        0.0),
    DT_12 = cms.vdouble(0.183, 0.054, -0.087, 0.028, 0.002, 
        0.0),
    DT_14 = cms.vdouble(0.359, 0.052, -0.107, 0.072, -0.004, 
        0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    CSC_23 = cms.vdouble(-0.081, 0.113, -0.029, 0.015, 0.008, 
        0.0),
    CSC_24 = cms.vdouble(0.004, 0.021, -0.002, 0.053, 0.0, 
        0.0),
    OL_2222 = cms.vdouble(0.107, 0.0, 0.0, 0.04, 0.0, 
        0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    SMB_10 = cms.vdouble(1.387, -0.038, 0.0, 0.19, 0.0, 
        0.0),
    SMB_11 = cms.vdouble(1.247, 0.72, -0.802, 0.229, -0.075, 
        0.0),
    SMB_12 = cms.vdouble(2.128, -0.956, 0.0, 0.199, 0.0, 
        0.0),
    SME_21 = cms.vdouble(-0.529, 1.194, -0.358, 0.472, 0.086, 
        0.0),
    SME_22 = cms.vdouble(-1.207, 1.491, -0.251, 0.189, 0.243, 
        0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    CSC_34 = cms.vdouble(0.062, -0.067, 0.019, 0.021, 0.003, 
        0.0),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    SMB_32 = cms.vdouble(0.67, -0.327, 0.0, 0.22, 0.0, 
        0.0),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    DT_34 = cms.vdouble(0.044, 0.004, -0.013, 0.029, 0.003, 
        0.0),
    SME_32 = cms.vdouble(-0.901, 1.333, -0.47, 0.41, 0.073, 
        0.0),
    SME_31 = cms.vdouble(-1.594, 1.482, -0.317, 0.487, 0.097, 
        0.0),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    crackEtas = cms.vdouble(0.2, 1.6, 1.7),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    DT_23 = cms.vdouble(0.13, 0.023, -0.057, 0.028, 0.004, 
        0.0),
    DT_24 = cms.vdouble(0.176, 0.014, -0.051, 0.051, 0.003, 
        0.0),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    SME_42 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    SME_41 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    OL_1232 = cms.vdouble(0.184, 0.0, 0.0, 0.066, 0.0, 
        0.0),
    DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    EnableDTMeasurement = cms.bool(True),
    CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    scaleDT = cms.bool(True),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    OL_1222 = cms.vdouble(0.848, -0.591, 0.0, 0.062, 0.0, 
        0.0),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    OL_1213 = cms.vdouble(0.96, -0.737, 0.0, 0.052, 0.0, 
        0.0),
    CSC_02 = cms.vdouble(0.612, -0.207, 0.0, 0.067, -0.001, 
        0.0),
    CSC_03 = cms.vdouble(0.787, -0.338, 0.029, 0.101, -0.008, 
        0.0),
    CSC_01 = cms.vdouble(0.166, 0.0, 0.0, 0.031, 0.0, 
        0.0),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    SMB_30 = cms.vdouble(0.505, -0.022, 0.0, 0.215, 0.0, 
        0.0),
    SMB_31 = cms.vdouble(0.549, -0.145, 0.0, 0.207, 0.0, 
        0.0),
    crackWindow = cms.double(0.04),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    beamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    CSC_13 = cms.vdouble(0.901, -1.302, 0.533, 0.045, 0.005, 
        0.0),
    CSC_14 = cms.vdouble(0.606, -0.181, -0.002, 0.111, -0.003, 
        0.0),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    EnableCSCMeasurement = cms.bool(True),
    CSC_12 = cms.vdouble(-0.161, 0.254, -0.047, 0.042, -0.007, 
        0.0)
)


process.hltL3MuonCandidates = cms.EDProducer("L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag("hltL3MuonsLinksCombination"),
    InputObjects = cms.InputTag("hltL3Muons"),
    MuonPtOption = cms.string('Tracker')
)


process.hltL3Muons = cms.EDProducer("L3TrackCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit")
)


process.hltL3MuonsIOHit = cms.EDProducer("L3MuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    L3TrajBuilderParameters = cms.PSet(
        ScaleTECyFactor = cms.double(-1.0),
        tkTrajUseVertex = cms.bool(False),
        GlbRefitterParameters = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            TrackerSkipSection = cms.int32(-1),
            Chi2CutCSC = cms.double(150.0),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            Chi2CutRPC = cms.double(1.0),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DYTthrs = cms.vint32(30, 15),
            PropDirForCosmics = cms.bool(False),
            Chi2CutDT = cms.double(10.0),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            TrackerSkipSystem = cms.int32(-1)
        ),
        tkTrajMaxChi2 = cms.double(9999.0),
        ScaleTECxFactor = cms.double(-1.0),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(0.001),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('hltESPSmartPropagator'),
            Quality_1 = cms.double(20.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2IOHit"),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        MuonTrackingRegionBuilder = cms.PSet(
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            DeltaR = cms.double(0.2),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            OnDemand = cms.double(-1.0),
            vertexCollection = cms.InputTag("pixelVertices"),
            Rescale_phi = cms.double(3.0),
            Eta_fixed = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            Rescale_eta = cms.double(3.0),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Eta_min = cms.double(0.05),
            Phi_fixed = cms.double(0.2),
            Phi_min = cms.double(0.05),
            EscapePt = cms.double(1.5),
            UseFixedRegion = cms.bool(False),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            UseVertex = cms.bool(False),
            Rescale_Dz = cms.double(3.0)
        ),
        RefitRPCHits = cms.bool(True),
        PCut = cms.double(2.5),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Propagator = cms.string('hltESPSmartPropagatorAny')
        ),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        PtCut = cms.double(1.0),
        tkTrajVertex = cms.InputTag("pixelVertices"),
        tkTrajMaxDXYBeamSpot = cms.double(0.2)
    ),
    TrackLoaderParameters = cms.PSet(
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        SmoothTkTrack = cms.untracked.bool(False),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        VertexConstraint = cms.bool(False),
        DoSmoothing = cms.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL3MuonsLinksCombination = cms.EDProducer("L3TrackLinksCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit")
)


process.hltL3MuonsOIHit = cms.EDProducer("L3MuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    L3TrajBuilderParameters = cms.PSet(
        ScaleTECyFactor = cms.double(-1.0),
        tkTrajUseVertex = cms.bool(False),
        GlbRefitterParameters = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            TrackerSkipSection = cms.int32(-1),
            Chi2CutCSC = cms.double(150.0),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            Chi2CutRPC = cms.double(1.0),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DYTthrs = cms.vint32(30, 15),
            PropDirForCosmics = cms.bool(False),
            Chi2CutDT = cms.double(10.0),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            TrackerSkipSystem = cms.int32(-1)
        ),
        tkTrajMaxChi2 = cms.double(9999.0),
        ScaleTECxFactor = cms.double(-1.0),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(0.001),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('hltESPSmartPropagator'),
            Quality_1 = cms.double(20.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2OIHit"),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        MuonTrackingRegionBuilder = cms.PSet(
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            DeltaR = cms.double(0.2),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            OnDemand = cms.double(-1.0),
            vertexCollection = cms.InputTag("pixelVertices"),
            Rescale_phi = cms.double(3.0),
            Eta_fixed = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            Rescale_eta = cms.double(3.0),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Eta_min = cms.double(0.05),
            Phi_fixed = cms.double(0.2),
            Phi_min = cms.double(0.05),
            EscapePt = cms.double(1.5),
            UseFixedRegion = cms.bool(False),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            UseVertex = cms.bool(False),
            Rescale_Dz = cms.double(3.0)
        ),
        RefitRPCHits = cms.bool(True),
        PCut = cms.double(2.5),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Propagator = cms.string('hltESPSmartPropagatorAny')
        ),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        PtCut = cms.double(1.0),
        tkTrajVertex = cms.InputTag("pixelVertices"),
        tkTrajMaxDXYBeamSpot = cms.double(0.2)
    ),
    TrackLoaderParameters = cms.PSet(
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        SmoothTkTrack = cms.untracked.bool(False),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        VertexConstraint = cms.bool(False),
        DoSmoothing = cms.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL3MuonsOIState = cms.EDProducer("L3MuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    L3TrajBuilderParameters = cms.PSet(
        ScaleTECyFactor = cms.double(-1.0),
        tkTrajUseVertex = cms.bool(False),
        GlbRefitterParameters = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            TrackerSkipSection = cms.int32(-1),
            Chi2CutCSC = cms.double(150.0),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            Chi2CutRPC = cms.double(1.0),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DYTthrs = cms.vint32(30, 15),
            PropDirForCosmics = cms.bool(False),
            Chi2CutDT = cms.double(10.0),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            TrackerSkipSystem = cms.int32(-1)
        ),
        tkTrajMaxChi2 = cms.double(9999.0),
        ScaleTECxFactor = cms.double(-1.0),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(0.001),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('hltESPSmartPropagator'),
            Quality_1 = cms.double(20.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2OIState"),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        MuonTrackingRegionBuilder = cms.PSet(
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            DeltaR = cms.double(0.2),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            OnDemand = cms.double(-1.0),
            vertexCollection = cms.InputTag("pixelVertices"),
            Rescale_phi = cms.double(3.0),
            Eta_fixed = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            Rescale_eta = cms.double(3.0),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Eta_min = cms.double(0.05),
            Phi_fixed = cms.double(0.2),
            Phi_min = cms.double(0.05),
            EscapePt = cms.double(1.5),
            UseFixedRegion = cms.bool(False),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            UseVertex = cms.bool(False),
            Rescale_Dz = cms.double(3.0)
        ),
        RefitRPCHits = cms.bool(True),
        PCut = cms.double(2.5),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Propagator = cms.string('hltESPSmartPropagatorAny')
        ),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        PtCut = cms.double(1.0),
        tkTrajVertex = cms.InputTag("pixelVertices"),
        tkTrajMaxDXYBeamSpot = cms.double(0.2)
    ),
    TrackLoaderParameters = cms.PSet(
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        SmoothTkTrack = cms.untracked.bool(False),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        VertexConstraint = cms.bool(False),
        DoSmoothing = cms.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL3TkFromL2OICombination = cms.EDProducer("L3TrackCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit")
)


process.hltL3TkTracksFromL2 = cms.EDProducer("SimpleTrackListMerger",
    ShareFrac = cms.double(0.19),
    promoteTrackQuality = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    allowFirstHitShare = cms.bool(True),
    newQuality = cms.string('confirmed'),
    MaxNormalizedChisq = cms.double(1000.0),
    FoundHitBonus = cms.double(100.0),
    MinFound = cms.int32(3),
    LostHitPenalty = cms.double(0.0),
    TrackProducer2 = cms.string('hltL3TkTracksFromL2IOHit'),
    TrackProducer1 = cms.string('hltL3TkTracksMergeStep1')
)


process.hltL3TkTracksFromL2IOHit = cms.EDProducer("TrackProducer",
    src = cms.InputTag("hltL3TrackCandidateFromL2IOHit"),
    SimpleMagneticField = cms.string(''),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    AlgorithmName = cms.string('undefAlgorithm'),
    alias = cms.untracked.string(''),
    NavigationSchool = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    GeometricInnerState = cms.bool(True),
    useSimpleMF = cms.bool(False),
    Propagator = cms.string('PropagatorWithMaterial')
)


process.hltL3TkTracksFromL2OIHit = cms.EDProducer("TrackProducer",
    src = cms.InputTag("hltL3TrackCandidateFromL2OIHit"),
    SimpleMagneticField = cms.string(''),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    AlgorithmName = cms.string('undefAlgorithm'),
    alias = cms.untracked.string(''),
    NavigationSchool = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    GeometricInnerState = cms.bool(True),
    useSimpleMF = cms.bool(False),
    Propagator = cms.string('PropagatorWithMaterial')
)


process.hltL3TkTracksFromL2OIState = cms.EDProducer("TrackProducer",
    src = cms.InputTag("hltL3TrackCandidateFromL2OIState"),
    SimpleMagneticField = cms.string(''),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    AlgorithmName = cms.string('undefAlgorithm'),
    alias = cms.untracked.string(''),
    NavigationSchool = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    GeometricInnerState = cms.bool(True),
    useSimpleMF = cms.bool(False),
    Propagator = cms.string('PropagatorWithMaterial')
)


process.hltL3TkTracksMergeStep1 = cms.EDProducer("SimpleTrackListMerger",
    ShareFrac = cms.double(0.19),
    promoteTrackQuality = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    allowFirstHitShare = cms.bool(True),
    newQuality = cms.string('confirmed'),
    MaxNormalizedChisq = cms.double(1000.0),
    FoundHitBonus = cms.double(100.0),
    MinFound = cms.int32(3),
    LostHitPenalty = cms.double(0.0),
    TrackProducer2 = cms.string('hltL3TkTracksFromL2OIHit'),
    TrackProducer1 = cms.string('hltL3TkTracksFromL2OIState')
)


process.hltL3TrackCandidateFromL2 = cms.EDProducer("L3TrackCandCombiner",
    labels = cms.VInputTag("hltL3TrackCandidateFromL2IOHit", "hltL3TrackCandidateFromL2OIHit", "hltL3TrackCandidateFromL2OIState")
)


process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer("CkfTrajectoryMaker",
    src = cms.InputTag("hltL3TrajSeedIOHit"),
    reverseTrajectories = cms.bool(False),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    cleanTrajectoryAfterInOut = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    trackCandidateAlso = cms.bool(True),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('hltESPMuonCkfTrajectoryBuilder'),
    maxNSeeds = cms.uint32(100000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    )
)


process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer("CkfTrajectoryMaker",
    src = cms.InputTag("hltL3TrajSeedOIHit"),
    reverseTrajectories = cms.bool(True),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    cleanTrajectoryAfterInOut = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    trackCandidateAlso = cms.bool(True),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('hltESPMuonCkfTrajectoryBuilder'),
    maxNSeeds = cms.uint32(100000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    )
)


process.hltL3TrackCandidateFromL2OIState = cms.EDProducer("CkfTrajectoryMaker",
    src = cms.InputTag("hltL3TrajSeedOIState"),
    reverseTrajectories = cms.bool(True),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    cleanTrajectoryAfterInOut = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    trackCandidateAlso = cms.bool(True),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilderSeedHit')
    ),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('hltESPMuonCkfTrajectoryBuilderSeedHit'),
    maxNSeeds = cms.uint32(100000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    )
)


process.hltL3TrajSeedIOHit = cms.EDProducer("TSGFromL2Muon",
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('DualByL2TSG'),
        L3TkCollectionA = cms.InputTag("hltL3TkFromL2OICombination"),
        iterativeTSG = cms.PSet(
            firstTSG = cms.PSet(
                ComponentName = cms.string('TSGFromOrderedHits'),
                OrderedHitsFactoryPSet = cms.PSet(
                    ComponentName = cms.string('StandardHitTripletGenerator'),
                    SeedingLayers = cms.InputTag("hltPixelLayerTriplets"),
                    GeneratorPSet = cms.PSet(
                        useBending = cms.bool(True),
                        useFixedPreFiltering = cms.bool(False),
                        maxElement = cms.uint32(0),
                        phiPreFiltering = cms.double(0.3),
                        extraHitRPhitolerance = cms.double(0.06),
                        useMultScattering = cms.bool(True),
                        SeedComparitorPSet = cms.PSet(
                            ComponentName = cms.string('none')
                        ),
                        extraHitRZtolerance = cms.double(0.06),
                        ComponentName = cms.string('PixelTripletHLTGenerator')
                    )
                ),
                TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
            ),
            PSetNames = cms.vstring('firstTSG', 
                'secondTSG'),
            ComponentName = cms.string('CombinedTSG'),
            thirdTSG = cms.PSet(
                PSetNames = cms.vstring('endcapTSG', 
                    'barrelTSG'),
                ComponentName = cms.string('DualByEtaTSG'),
                endcapTSG = cms.PSet(
                    ComponentName = cms.string('TSGFromOrderedHits'),
                    OrderedHitsFactoryPSet = cms.PSet(
                        maxElement = cms.uint32(0),
                        ComponentName = cms.string('StandardHitPairGenerator'),
                        SeedingLayers = cms.InputTag("hltMixedLayerPairs"),
                        useOnDemandTracker = cms.untracked.int32(0)
                    ),
                    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
                ),
                etaSeparation = cms.double(2.0),
                barrelTSG = cms.PSet(

                )
            ),
            secondTSG = cms.PSet(
                ComponentName = cms.string('TSGFromOrderedHits'),
                OrderedHitsFactoryPSet = cms.PSet(
                    maxElement = cms.uint32(0),
                    ComponentName = cms.string('StandardHitPairGenerator'),
                    SeedingLayers = cms.InputTag("hltPixelLayerPairs"),
                    useOnDemandTracker = cms.untracked.int32(0)
                ),
                TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
            )
        ),
        skipTSG = cms.PSet(

        ),
        PSetNames = cms.vstring('skipTSG', 
            'iterativeTSG')
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('PropagatorWithMaterial'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double(0.25),
        DeltaR = cms.double(0.2),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        OnDemand = cms.double(-1.0),
        vertexCollection = cms.InputTag("pixelVertices"),
        Rescale_phi = cms.double(3.0),
        Eta_fixed = cms.double(0.2),
        DeltaZ_Region = cms.double(15.9),
        Rescale_eta = cms.double(3.0),
        PhiR_UpperLimit_Par2 = cms.double(0.2),
        Eta_min = cms.double(0.1),
        Phi_fixed = cms.double(0.2),
        Phi_min = cms.double(0.1),
        EscapePt = cms.double(1.5),
        UseFixedRegion = cms.bool(False),
        PhiR_UpperLimit_Par1 = cms.double(0.6),
        EtaR_UpperLimit_Par2 = cms.double(0.15),
        MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
        UseVertex = cms.bool(False),
        Rescale_Dz = cms.double(3.0)
    ),
    PCut = cms.double(2.5),
    TrackerSeedCleaner = cms.PSet(
        cleanerFromSharedHits = cms.bool(True),
        ptCleaner = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        directionCleaner = cms.bool(True)
    ),
    PtCut = cms.double(1.0)
)


process.hltL3TrajSeedOIHit = cms.EDProducer("TSGFromL2Muon",
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('DualByL2TSG'),
        L3TkCollectionA = cms.InputTag("hltL3MuonsOIState"),
        iterativeTSG = cms.PSet(
            ErrorRescaling = cms.double(3.0),
            beamSpot = cms.InputTag("unused"),
            MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
            ComponentName = cms.string('TSGFromPropagation'),
            errorMatrixPset = cms.PSet(
                action = cms.string('use'),
                atIP = cms.bool(True),
                errorMatrixValuesPSet = cms.PSet(
                    pf3_V12 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V13 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V11 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V45 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V14 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V15 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    yAxis = cms.vdouble(0.0, 1.0, 1.4, 10.0),
                    pf3_V35 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    zAxis = cms.vdouble(-3.14159, 3.14159),
                    pf3_V44 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    xAxis = cms.vdouble(0.0, 13.0, 30.0, 70.0, 1000.0),
                    pf3_V23 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V22 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V55 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V34 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V33 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V25 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V24 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    )
                )
            ),
            UpdateState = cms.bool(True),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            SelectState = cms.bool(False),
            SigmaZ = cms.double(25.0),
            ResetMethod = cms.string('matrix'),
            MaxChi2 = cms.double(40.0),
            UseVertexState = cms.bool(True),
            Propagator = cms.string('hltESPSmartPropagatorAnyOpposite')
        ),
        skipTSG = cms.PSet(

        ),
        PSetNames = cms.vstring('skipTSG', 
            'iterativeTSG')
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('PropagatorWithMaterial', 
            'hltESPSmartPropagatorAnyOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(

    ),
    PCut = cms.double(2.5),
    TrackerSeedCleaner = cms.PSet(
        cleanerFromSharedHits = cms.bool(True),
        ptCleaner = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        directionCleaner = cms.bool(True)
    ),
    PtCut = cms.double(1.0)
)


process.hltL3TrajSeedOIState = cms.EDProducer("TSGFromL2Muon",
    TkSeedGenerator = cms.PSet(
        propagatorCompatibleName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
        option = cms.uint32(3),
        MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
        ComponentName = cms.string('TSGForRoadSearch'),
        errorMatrixPset = cms.PSet(
            action = cms.string('use'),
            atIP = cms.bool(True),
            errorMatrixValuesPSet = cms.PSet(
                pf3_V12 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V13 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V11 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V45 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V14 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V15 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                yAxis = cms.vdouble(0.0, 1.0, 1.4, 10.0),
                pf3_V35 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                zAxis = cms.vdouble(-3.14159, 3.14159),
                pf3_V44 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                xAxis = cms.vdouble(0.0, 13.0, 30.0, 70.0, 1000.0),
                pf3_V23 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V22 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V55 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V34 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V33 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V25 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V24 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                )
            )
        ),
        propagatorName = cms.string('hltESPSteppingHelixPropagatorAlong'),
        manySeeds = cms.bool(False),
        copyMuonRecHit = cms.bool(False),
        maxChi2 = cms.double(40.0)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSteppingHelixPropagatorOpposite', 
            'hltESPSteppingHelixPropagatorAlong'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(

    ),
    PCut = cms.double(2.5),
    TrackerSeedCleaner = cms.PSet(

    ),
    PtCut = cms.double(1.0)
)


process.hltL3TrajectorySeed = cms.EDProducer("L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag("hltL3TrajSeedIOHit", "hltL3TrajSeedOIState", "hltL3TrajSeedOIHit")
)


process.hltLightPFTracks = cms.EDProducer("LightPFTrackProducer",
    TrackQuality = cms.string('none'),
    UseQuality = cms.bool(False),
    TkColList = cms.VInputTag("hltPFMuonMerging")
)


process.hltMixedLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix2_pos+TEC1_pos', 
        'FPix2_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC1_neg', 
        'FPix2_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg'),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        minRing = cms.int32(1),
        maxRing = cms.int32(1)
    ),
    MTID = cms.PSet(

    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltMuonCSCDigis = cms.EDProducer("CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool(False),
    UseExaminer = cms.bool(True),
    Debug = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    InputObjects = cms.InputTag("rawDataCollector"),
    ExaminerMask = cms.uint32(535557110),
    UseFormatStatus = cms.bool(True),
    UnpackStatusDigis = cms.bool(False),
    VisualFEDInspect = cms.untracked.bool(False),
    FormatedEventDump = cms.untracked.bool(False),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDShort = cms.untracked.bool(False)
)


process.hltMuonDTDigis = cms.EDProducer("DTUnpackingModule",
    dataType = cms.string('DDU'),
    inputLabel = cms.InputTag("rawDataCollector"),
    useStandardFEDid = cms.bool(True),
    fedbyType = cms.bool(False),
    readOutParameters = cms.PSet(
        debug = cms.untracked.bool(False),
        rosParameters = cms.PSet(
            writeSC = cms.untracked.bool(True),
            readingDDU = cms.untracked.bool(True),
            performDataIntegrityMonitor = cms.untracked.bool(False),
            readDDUIDfromDDU = cms.untracked.bool(True),
            debug = cms.untracked.bool(False),
            localDAQ = cms.untracked.bool(False)
        ),
        performDataIntegrityMonitor = cms.untracked.bool(False),
        localDAQ = cms.untracked.bool(False)
    ),
    dqmOnly = cms.bool(False)
)


process.hltMuonLinks = cms.EDProducer("MuonLinksProducerForHLT",
    InclusiveTrackerTrackCollection = cms.InputTag("hltPFMuonMerging"),
    pMin = cms.double(2.5),
    LinkCollection = cms.InputTag("hltL3MuonsLinksCombination"),
    shareHitFraction = cms.double(0.8),
    ptMin = cms.double(2.5)
)


process.hltMuonRPCDigis = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    doSynchro = cms.bool(False)
)


process.hltMuons = cms.EDProducer("MuonIdProducer",
    TrackExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        inputTrackCollection = cms.InputTag("hltPFMuonMerging"),
        BeamSpotLabel = cms.InputTag("hltOnlineBeamSpot"),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.01),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent')
    ),
    maxAbsEta = cms.double(3.0),
    fillGlobalTrackRefits = cms.bool(False),
    arbitrationCleanerOptions = cms.PSet(
        ME1a = cms.bool(True),
        Clustering = cms.bool(True),
        ClusterDPhi = cms.double(0.6),
        OverlapDTheta = cms.double(0.02),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        ClusterDTheta = cms.double(0.02)
    ),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    addExtraSoftMuons = cms.bool(False),
    debugWithTruthMatching = cms.bool(False),
    CaloExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        DR_Max = cms.double(1.0),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        Noise_HE = cms.double(0.2),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_HB = cms.double(0.2),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        DepositLabel = cms.untracked.string('Cal'),
        UseRecHitsFlag = cms.bool(False),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            dRHcal = cms.double(1.0),
            dREcal = cms.double(1.0),
            CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForPF"),
            useEcal = cms.bool(False),
            dRPreshowerPreselection = cms.double(0.2),
            dREcalPreselection = cms.double(1.0),
            HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(1.0),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
            useHcal = cms.bool(False)
        ),
        Threshold_HO = cms.double(0.5),
        Noise_EE = cms.double(0.1),
        Noise_EB = cms.double(0.025),
        DR_Veto_H = cms.double(0.1),
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        Threshold_H = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_HO = cms.double(0.1),
        Noise_HO = cms.double(0.2)
    ),
    runArbitrationCleaner = cms.bool(False),
    fillEnergy = cms.bool(True),
    TrackerKinkFinderParameters = cms.PSet(
        usePosition = cms.bool(False),
        diagonalOnly = cms.bool(False)
    ),
    TimingFillerParameters = cms.PSet(
        DTTimingParameters = cms.PSet(
            HitError = cms.double(6.0),
            DoWireCorr = cms.bool(False),
            MatchParameters = cms.PSet(
                DTsegments = cms.InputTag("hltDt4DSegments"),
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            debug = cms.bool(False),
            DTsegments = cms.InputTag("hltDt4DSegments"),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            RequireBothProjections = cms.bool(False),
            HitsMin = cms.int32(5),
            DTTimeOffset = cms.double(2.7),
            DropTheta = cms.bool(True),
            UseSegmentT0 = cms.bool(False),
            PruneCut = cms.double(10000.0)
        ),
        ErrorDT = cms.double(6.0),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorCSC = cms.double(7.4),
        CSCTimingParameters = cms.PSet(
            CSCsegments = cms.InputTag("hltCscSegments"),
            CSCTimeOffset = cms.double(0.0),
            CSCStripTimeOffset = cms.double(0.0),
            MatchParameters = cms.PSet(
                DTsegments = cms.InputTag("hltDt4DSegments"),
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                TightMatchDT = cms.bool(False),
                TightMatchCSC = cms.bool(True)
            ),
            debug = cms.bool(False),
            UseStripTime = cms.bool(True),
            CSCStripError = cms.double(7.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            PruneCut = cms.double(100.0),
            UseWireTime = cms.bool(True)
        ),
        UseDT = cms.bool(True),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    fillCaloCompatibility = cms.bool(True),
    minCaloCompatibility = cms.double(0.6),
    ecalDepositName = cms.string('ecal'),
    minP = cms.double(10.0),
    fillIsolation = cms.bool(True),
    jetDepositName = cms.string('jets'),
    hoDepositName = cms.string('ho'),
    writeIsoDeposits = cms.bool(False),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minPt = cms.double(10.0),
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
        dRHcal = cms.double(9999.0),
        dREcal = cms.double(9999.0),
        CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForPF"),
        useEcal = cms.bool(True),
        dRPreshowerPreselection = cms.double(0.2),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
        useHcal = cms.bool(True)
    ),
    JetExtractorPSet = cms.PSet(
        PrintTimeReport = cms.untracked.bool(False),
        ExcludeMuonVeto = cms.bool(True),
        TrackAssociatorParameters = cms.PSet(
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            dRHcal = cms.double(0.5),
            dREcal = cms.double(0.5),
            CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForPF"),
            useEcal = cms.bool(False),
            dRPreshowerPreselection = cms.double(0.2),
            dREcalPreselection = cms.double(0.5),
            HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
            dRMuon = cms.double(9999.0),
            propagateAllDirections = cms.bool(True),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            useHO = cms.bool(False),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            usePreshower = cms.bool(False),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
            dRHcalPreselection = cms.double(0.5),
            useMuon = cms.bool(False),
            useCalo = cms.bool(True),
            accountForTrajectoryChangeCalo = cms.bool(False),
            EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
            dRMuonPreselection = cms.double(0.2),
            truthMatch = cms.bool(False),
            HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
            useHcal = cms.bool(False)
        ),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        JetCollectionLabel = cms.InputTag("hltAK4CaloJetsPFEt5"),
        DR_Veto = cms.double(0.1),
        Threshold = cms.double(5.0)
    ),
    trackDepositName = cms.string('tracker'),
    minPCaloMuon = cms.double(1000000000.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    fillMatching = cms.bool(True),
    MuonCaloCompatibility = cms.PSet(
        delta_eta = cms.double(0.02),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_phi = cms.double(0.02)
    ),
    fillTrackerKink = cms.bool(False),
    inputCollectionTypes = cms.vstring('inner tracks', 
        'links', 
        'outer tracks'),
    hcalDepositName = cms.string('hcal'),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    inputCollectionLabels = cms.VInputTag("hltPFMuonMerging", "hltMuonLinks", "hltL2Muons"),
    fillGlobalTrackQuality = cms.bool(False),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    minNumberOfMatches = cms.int32(1)
)


process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotOnlineProducer",
    maxZ = cms.double(40.0),
    src = cms.InputTag("hltScalersRawToDigi"),
    gtEvmLabel = cms.InputTag(""),
    changeToCMSCoordinates = cms.bool(False),
    setSigmaZ = cms.double(0.0),
    maxRadius = cms.double(2.0)
)


process.hltPFHT = cms.EDProducer("HLTHtMhtProducer",
    usePt = cms.bool(True),
    minPtJetHt = cms.double(40.0),
    maxEtaJetMht = cms.double(999.0),
    minNJetMht = cms.int32(0),
    jetsLabel = cms.InputTag("hltAK4PFJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    minPtJetMht = cms.double(0.0),
    excludePFMuons = cms.bool(False),
    pfCandidatesLabel = cms.InputTag("hltParticleFlow"),
    minNJetHt = cms.int32(0)
)


process.hltPFMuonMerging = cms.EDProducer("SimpleTrackListMerger",
    ShareFrac = cms.double(0.19),
    promoteTrackQuality = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    allowFirstHitShare = cms.bool(True),
    newQuality = cms.string('confirmed'),
    MaxNormalizedChisq = cms.double(1000.0),
    FoundHitBonus = cms.double(5.0),
    MinFound = cms.int32(3),
    LostHitPenalty = cms.double(20.0),
    TrackProducer2 = cms.string('hltIter2Merged'),
    TrackProducer1 = cms.string('hltL3TkTracksFromL2')
)


process.hltParticleFlow = cms.EDProducer("PFProducer",
    photon_SigmaiEtaiEta_endcap = cms.double(0.034),
    minPtForPostCleaning = cms.double(20.0),
    pf_nsigma_ECAL = cms.double(0.0),
    GedPhotonValueMap = cms.InputTag("tmpGedPhotons","valMapPFEgammaCandToPhoton"),
    sumPtTrackIsoForPhoton = cms.double(-1.0),
    metFactorForFakes = cms.double(4.0),
    muon_HO = cms.vdouble(0.9, 0.9),
    electron_missinghits = cms.uint32(1),
    metSignificanceForCleaning = cms.double(3.0),
    usePFPhotons = cms.bool(False),
    dptRel_DispVtx = cms.double(10.0),
    nTrackIsoForEgammaSC = cms.uint32(2),
    pf_nsigma_HCAL = cms.double(1.0),
    cosmicRejectionDistance = cms.double(1.0),
    useEGammaFilters = cms.bool(False),
    useEGammaElectrons = cms.bool(False),
    nsigma_TRACK = cms.double(1.0),
    useEGammaSupercluster = cms.bool(False),
    sumPtTrackIsoForEgammaSC_barrel = cms.double(4.0),
    eventFractionForCleaning = cms.double(0.8),
    usePFDecays = cms.bool(False),
    rejectTracks_Step45 = cms.bool(False),
    eventFractionForRejection = cms.double(0.8),
    photon_MinEt = cms.double(10.0),
    usePFNuclearInteractions = cms.bool(False),
    maxSignificance = cms.double(2.5),
    electron_iso_mva_endcap = cms.double(-0.1075),
    debug = cms.untracked.bool(False),
    pf_convID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt'),
    calibHF_eta_step = cms.vdouble(0.0, 2.9, 3.0, 3.2, 4.2, 
        4.4, 4.6, 4.8, 5.2, 5.4),
    ptErrorScale = cms.double(8.0),
    minSignificance = cms.double(2.5),
    minMomentumForPunchThrough = cms.double(100.0),
    pf_conv_mvaCut = cms.double(0.0),
    useCalibrationsFromDB = cms.bool(True),
    usePFElectrons = cms.bool(False),
    blocks = cms.InputTag("hltParticleFlowBlock"),
    photon_combIso = cms.double(10.0),
    electron_iso_mva_barrel = cms.double(-0.1875),
    postHFCleaning = cms.bool(False),
    dzPV = cms.double(0.2),
    cleanedHF = cms.VInputTag("hltParticleFlowRecHitHCAL:Cleaned", "hltParticleFlowClusterHFHAD:Cleaned", "hltParticleFlowClusterHFEM:Cleaned"),
    coneEcalIsoForEgammaSC = cms.double(0.3),
    minSignificanceReduction = cms.double(1.4),
    photon_SigmaiEtaiEta_barrel = cms.double(0.0125),
    calibHF_b_HADonly = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    minPixelHits = cms.int32(1),
    maxDPtOPt = cms.double(1.0),
    useHO = cms.bool(False),
    pf_electron_output_col = cms.string('electrons'),
    electron_noniso_mvaCut = cms.double(-0.1),
    GedElectronValueMap = cms.InputTag("gedGsfElectronsTmp"),
    useVerticesForNeutral = cms.bool(True),
    pf_Res_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFRes.root'),
    PFEGammaCandidates = cms.InputTag("particleFlowEGamma"),
    sumPtTrackIsoSlopeForPhoton = cms.double(-1.0),
    coneTrackIsoForEgammaSC = cms.double(0.3),
    minDeltaMet = cms.double(0.4),
    pt_Error = cms.double(1.0),
    useProtectionsForJetMET = cms.bool(True),
    metFactorForRejection = cms.double(4.0),
    sumPtTrackIsoForEgammaSC_endcap = cms.double(4.0),
    calibHF_use = cms.bool(False),
    verbose = cms.untracked.bool(False),
    usePFConversions = cms.bool(False),
    trackQuality = cms.string('highPurity'),
    calibPFSCEle_endcap = cms.vdouble(1.153, -16.5975, 5.668, -0.1772, 16.22, 
        7.326, 0.0483, -4.068, 9.406),
    metFactorForCleaning = cms.double(4.0),
    eventFactorForCosmics = cms.double(10.0),
    egammaElectrons = cms.InputTag(""),
    minEnergyForPunchThrough = cms.double(100.0),
    minTrackerHits = cms.int32(8),
    iCfgCandConnector = cms.PSet(
        bCalibSecondary = cms.bool(False),
        bCalibPrimary = cms.bool(False),
        bCorrect = cms.bool(False),
        nuclCalibFactors = cms.vdouble(0.8, 0.15, 0.5, 0.5, 0.05)
    ),
    rejectTracks_Bad = cms.bool(False),
    pf_electronID_crackCorrection = cms.bool(False),
    pf_locC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFClusterCorr.root'),
    calibHF_a_EMonly = cms.vdouble(0.96945, 0.96701, 0.76309, 0.82268, 0.87583, 
        0.89718, 0.98674, 1.4681, 1.458, 1.458),
    muons = cms.InputTag("hltMuons"),
    metFactorForHighEta = cms.double(25.0),
    minHFCleaningPt = cms.double(5.0),
    muon_HCAL = cms.vdouble(3.0, 3.0),
    pf_electron_mvaCut = cms.double(-0.1),
    ptFactorForHighEta = cms.double(2.0),
    maxDeltaPhiPt = cms.double(7.0),
    pf_electronID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt'),
    sumEtEcalIsoForEgammaSC_endcap = cms.double(2.0),
    calibHF_b_EMHAD = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    pf_GlobC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFGlobalCorr.root'),
    photon_HoE = cms.double(0.1),
    sumEtEcalIsoForEgammaSC_barrel = cms.double(1.0),
    calibPFSCEle_Fbrem_endcap = cms.vdouble(0.9, 6.5, -0.0692932, 0.101776, 0.995338, 
        -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 
        0.923165, 0.000474665, 1.10782),
    punchThroughFactor = cms.double(3.0),
    algoType = cms.uint32(0),
    electron_iso_combIso_barrel = cms.double(10.0),
    postMuonCleaning = cms.bool(True),
    calibPFSCEle_barrel = cms.vdouble(1.004, -1.536, 22.88, -1.467, 0.3555, 
        0.6227, 14.65, 2051.0, 25.0, 0.9932, 
        -0.5444, 0.0, 0.5438, 0.7109, 7.645, 
        0.2904, 0.0),
    electron_protectionsForJetMET = cms.PSet(
        maxE = cms.double(50.0),
        maxTrackPOverEele = cms.double(1.0),
        maxEcalEOverP_2 = cms.double(0.2),
        maxHcalEOverEcalE = cms.double(0.1),
        maxEcalEOverP_1 = cms.double(0.5),
        maxNtracks = cms.double(3.0),
        maxEcalEOverPRes = cms.double(0.2),
        maxHcalE = cms.double(10.0),
        maxEeleOverPout = cms.double(0.2),
        maxHcalEOverP = cms.double(1.0),
        maxEleHcalEOverEcalE = cms.double(0.1),
        maxDPhiIN = cms.double(0.1),
        maxEeleOverPoutRes = cms.double(0.5)
    ),
    electron_iso_pt = cms.double(10.0),
    isolatedElectronID_mvaWeightFile = cms.string('RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml'),
    vertexCollection = cms.InputTag("hltPixelVertices"),
    X0_Map = cms.string('RecoParticleFlow/PFProducer/data/allX0histos.root'),
    calibPFSCEle_Fbrem_barrel = cms.vdouble(0.6, 6.0, -0.0255975, 0.0576727, 0.975442, 
        -0.000546394, 1.26147, 25.0, -0.02025, 0.04537, 
        0.9728, -0.0008962, 1.172),
    electron_iso_combIso_endcap = cms.double(10.0),
    punchThroughMETFactor = cms.double(4.0),
    metSignificanceForRejection = cms.double(4.0),
    photon_protectionsForJetMET = cms.PSet(
        sumPtTrackIso = cms.double(2.0),
        sumPtTrackIsoSlope = cms.double(0.001)
    ),
    usePhotonReg = cms.bool(False),
    factors_45 = cms.vdouble(10.0, 100.0),
    calibHF_a_EMHAD = cms.vdouble(1.42215, 1.00496, 0.68961, 0.81656, 0.98504, 
        0.98504, 1.00802, 1.0593, 1.4576, 1.4576),
    useRegressionFromDB = cms.bool(False),
    muon_ECAL = cms.vdouble(0.5, 0.5),
    usePFSCEleCalib = cms.bool(True)
)


process.hltParticleFlowBlock = cms.EDProducer("PFBlockProducer",
    debug = cms.untracked.bool(False),
    elementImporters = cms.VPSet(cms.PSet(
        useIterativeTracking = cms.bool(False),
        importerName = cms.string('GeneralTracksImporter'),
        muonSrc = cms.InputTag("hltMuons"),
        source = cms.InputTag("hltLightPFTracks"),
        NHitCuts_byTrackAlgo = cms.vuint32(3, 3, 3, 3, 3),
        DPtOverPtCuts_byTrackAlgo = cms.vdouble(0.5, 0.5, 0.5, 0.5, 0.5)
    ), 
        cms.PSet(
            source = cms.InputTag("hltParticleFlowClusterECALUnseeded"),
            importerName = cms.string('ECALClusterImporter'),
            BCtoPFCMap = cms.InputTag("")
        ), 
        cms.PSet(
            source = cms.InputTag("hltParticleFlowClusterHCAL"),
            importerName = cms.string('GenericClusterImporter')
        ), 
        cms.PSet(
            source = cms.InputTag("hltParticleFlowClusterHFEM"),
            importerName = cms.string('GenericClusterImporter')
        ), 
        cms.PSet(
            source = cms.InputTag("hltParticleFlowClusterHFHAD"),
            importerName = cms.string('GenericClusterImporter')
        ), 
        cms.PSet(
            source = cms.InputTag("hltParticleFlowClusterPSUnseeded"),
            importerName = cms.string('GenericClusterImporter')
        )),
    linkDefinitions = cms.VPSet(cms.PSet(
        linkType = cms.string('PS1:ECAL'),
        useKDTree = cms.bool(True),
        linkerName = cms.string('PreshowerAndECALLinker')
    ), 
        cms.PSet(
            linkType = cms.string('PS2:ECAL'),
            useKDTree = cms.bool(True),
            linkerName = cms.string('PreshowerAndECALLinker')
        ), 
        cms.PSet(
            linkType = cms.string('TRACK:ECAL'),
            useKDTree = cms.bool(True),
            linkerName = cms.string('TrackAndECALLinker')
        ), 
        cms.PSet(
            linkType = cms.string('TRACK:HCAL'),
            useKDTree = cms.bool(True),
            linkerName = cms.string('TrackAndHCALLinker')
        ), 
        cms.PSet(
            linkType = cms.string('ECAL:HCAL'),
            useKDTree = cms.bool(False),
            linkerName = cms.string('ECALAndHCALLinker')
        ), 
        cms.PSet(
            linkType = cms.string('HFEM:HFHAD'),
            useKDTree = cms.bool(False),
            linkerName = cms.string('HFEMAndHFHADLinker')
        )),
    verbose = cms.untracked.bool(False)
)


process.hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer("PFClusterProducer",
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minAllowedNormalization = cms.double(1e-09),
            logWeightDenominator = cms.double(0.08),
            posCalcNCrystals = cms.int32(-1),
            minFractionInCalc = cms.double(1e-09)
        ),
        showerSigma = cms.double(1.5),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minAllowedNormalization = cms.double(1e-09),
            logWeightDenominator = cms.double(0.08),
            posCalcNCrystals = cms.int32(9),
            minFractionInCalc = cms.double(1e-09)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            recHitEnergyNorm = cms.double(0.08)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )),
        stoppingTolerance = cms.double(1e-08),
        positionCalcForConvergence = cms.PSet(
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minFractionInCalc = cms.double(0.0),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            minAllowedNormalization = cms.double(0.0),
            X0 = cms.double(0.89),
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1)
        ),
        excludeOtherSeeds = cms.bool(True),
        minFractionToKeep = cms.double(1e-07)
    ),
    positionReCalc = cms.PSet(
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minFractionInCalc = cms.double(0.0),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        minAllowedNormalization = cms.double(0.0),
        X0 = cms.double(0.89),
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1)
    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            gatheringThresholdPt = cms.double(0.0),
            gatheringThreshold = cms.double(0.08)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThresholdPt = cms.double(0.0),
                gatheringThreshold = cms.double(0.3)
            )),
        useCornerCells = cms.bool(True)
    ),
    energyCorrector = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            minS4S1_a = cms.double(0.04),
            minS4S1_b = cms.double(-0.024),
            singleSpikeThresh = cms.double(4.0),
            energyThresholdModifier = cms.double(2.0),
            doubleSpikeThresh = cms.double(10.0),
            fractionThresholdModifier = cms.double(3.0),
            doubleSpikeS6S2 = cms.double(0.04),
            detector = cms.string('ECAL_BARREL')
        ), 
            cms.PSet(
                minS4S1_a = cms.double(0.02),
                minS4S1_b = cms.double(-0.0125),
                singleSpikeThresh = cms.double(15.0),
                energyThresholdModifier = cms.double(2.0),
                doubleSpikeThresh = cms.double(1000000000.0),
                fractionThresholdModifier = cms.double(3.0),
                doubleSpikeS6S2 = cms.double(-1.0),
                detector = cms.string('ECAL_ENDCAP')
            ))
    )),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_ENDCAP'),
            seedingThresholdPt = cms.double(0.15),
            seedingThreshold = cms.double(0.6)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThresholdPt = cms.double(0.0),
                seedingThreshold = cms.double(0.23)
            )),
        nNeighbours = cms.int32(8)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECALUnseeded")
)


process.hltParticleFlowClusterECALUnseeded = cms.EDProducer("CorrectedECALPFClusterProducer",
    inputPS = cms.InputTag("hltParticleFlowClusterPSUnseeded"),
    minimumPSEnergy = cms.double(0.0),
    energyCorrector = cms.PSet(
        algoName = cms.string('PFClusterEMEnergyCorrector'),
        applyCrackCorrections = cms.bool(False)
    ),
    inputECAL = cms.InputTag("hltParticleFlowClusterECALUncorrectedUnseeded")
)


process.hltParticleFlowClusterHCAL = cms.EDProducer("PFClusterProducer",
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minAllowedNormalization = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(-1),
            minFractionInCalc = cms.double(1e-09)
        ),
        showerSigma = cms.double(10.0),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minAllowedNormalization = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(5),
            minFractionInCalc = cms.double(1e-09)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            recHitEnergyNorm = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.8)
            )),
        stoppingTolerance = cms.double(1e-08),
        excludeOtherSeeds = cms.bool(True),
        minFractionToKeep = cms.double(1e-07)
    ),
    positionReCalc = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            gatheringThresholdPt = cms.double(0.0),
            gatheringThreshold = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThresholdPt = cms.double(0.0),
                gatheringThreshold = cms.double(0.8)
            )),
        useCornerCells = cms.bool(True)
    ),
    energyCorrector = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('RBXAndHPDCleaner')
    )),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            seedingThresholdPt = cms.double(0.0),
            seedingThreshold = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                seedingThresholdPt = cms.double(0.0),
                seedingThreshold = cms.double(1.1)
            )),
        nNeighbours = cms.int32(4)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHCAL")
)


process.hltParticleFlowClusterHFEM = cms.EDProducer("PFClusterProducer",
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minAllowedNormalization = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(-1),
            minFractionInCalc = cms.double(1e-09)
        ),
        showerSigma = cms.double(10.0),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minAllowedNormalization = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(5),
            minFractionInCalc = cms.double(1e-09)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            recHitEnergyNorm = cms.double(0.8)
        )),
        stoppingTolerance = cms.double(1e-08),
        excludeOtherSeeds = cms.bool(True),
        minFractionToKeep = cms.double(1e-07)
    ),
    positionReCalc = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            gatheringThresholdPt = cms.double(0.0),
            gatheringThreshold = cms.double(0.8)
        )),
        useCornerCells = cms.bool(False)
    ),
    energyCorrector = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            minS4S1_a = cms.double(0.11),
            minS4S1_b = cms.double(-0.19),
            singleSpikeThresh = cms.double(80.0),
            energyThresholdModifier = cms.double(1.0),
            doubleSpikeThresh = cms.double(1000000000.0),
            fractionThresholdModifier = cms.double(1.0),
            doubleSpikeS6S2 = cms.double(-1.0),
            detector = cms.string('HF_EM')
        ))
    )),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            seedingThresholdPt = cms.double(0.0),
            seedingThreshold = cms.double(1.4)
        )),
        nNeighbours = cms.int32(0)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHCAL","HFEM")
)


process.hltParticleFlowClusterHFHAD = cms.EDProducer("PFClusterProducer",
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minAllowedNormalization = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(-1),
            minFractionInCalc = cms.double(1e-09)
        ),
        showerSigma = cms.double(10.0),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minAllowedNormalization = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(5),
            minFractionInCalc = cms.double(1e-09)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HF_HAD'),
            recHitEnergyNorm = cms.double(0.8)
        )),
        stoppingTolerance = cms.double(1e-08),
        excludeOtherSeeds = cms.bool(True),
        minFractionToKeep = cms.double(1e-07)
    ),
    positionReCalc = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_HAD'),
            gatheringThresholdPt = cms.double(0.0),
            gatheringThreshold = cms.double(0.8)
        )),
        useCornerCells = cms.bool(False)
    ),
    energyCorrector = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            minS4S1_a = cms.double(0.045),
            minS4S1_b = cms.double(-0.08),
            singleSpikeThresh = cms.double(120.0),
            energyThresholdModifier = cms.double(1.0),
            doubleSpikeThresh = cms.double(1000000000.0),
            fractionThresholdModifier = cms.double(1.0),
            doubleSpikeS6S2 = cms.double(-1.0),
            detector = cms.string('HF_HAD')
        ))
    )),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_HAD'),
            seedingThresholdPt = cms.double(0.0),
            seedingThreshold = cms.double(1.4)
        )),
        nNeighbours = cms.int32(0)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHCAL","HFHAD")
)


process.hltParticleFlowClusterPSUnseeded = cms.EDProducer("PFClusterProducer",
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        maxIterations = cms.uint32(50),
        showerSigma = cms.double(0.3),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            recHitEnergyNorm = cms.double(6e-05)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minAllowedNormalization = cms.double(1e-09),
            logWeightDenominator = cms.double(6e-05),
            posCalcNCrystals = cms.int32(-1),
            minFractionInCalc = cms.double(1e-09)
        ),
        minFracTot = cms.double(1e-20),
        stoppingTolerance = cms.double(1e-08),
        excludeOtherSeeds = cms.bool(True),
        minFractionToKeep = cms.double(1e-07)
    ),
    positionReCalc = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            gatheringThresholdPt = cms.double(0.0),
            gatheringThreshold = cms.double(6e-05)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThresholdPt = cms.double(0.0),
                gatheringThreshold = cms.double(6e-05)
            )),
        useCornerCells = cms.bool(False)
    ),
    energyCorrector = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            seedingThresholdPt = cms.double(0.0),
            seedingThreshold = cms.double(0.00012)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThresholdPt = cms.double(0.0),
                seedingThreshold = cms.double(0.00012)
            )),
        nNeighbours = cms.int32(4)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitPSUnseeded")
)


process.hltParticleFlowRecHitECALUnseeded = cms.EDProducer("PFRecHitProducer",
    producers = cms.VPSet(cms.PSet(
        src = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        name = cms.string('PFEBRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            threshold = cms.double(0.08),
            name = cms.string('PFRecHitQTestThreshold')
        ), 
            cms.PSet(
                skipTTRecoveredHits = cms.bool(True),
                topologicalCleaning = cms.bool(True),
                name = cms.string('PFRecHitQTestECAL'),
                timingCleaning = cms.bool(True),
                cleaningThreshold = cms.double(2.0)
            ))
    ), 
        cms.PSet(
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                threshold = cms.double(0.3),
                name = cms.string('PFRecHitQTestThreshold')
            ), 
                cms.PSet(
                    skipTTRecoveredHits = cms.bool(True),
                    topologicalCleaning = cms.bool(True),
                    name = cms.string('PFRecHitQTestECAL'),
                    timingCleaning = cms.bool(True),
                    cleaningThreshold = cms.double(2.0)
                ))
        )),
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator'),
        endcap = cms.PSet(

        )
    )
)


process.hltParticleFlowRecHitHCAL = cms.EDProducer("PFCTRecHitProducer",
    ECAL_Compensate = cms.bool(False),
    ECAL_Dead_Code = cms.uint32(10),
    MinLongTiming_Cut = cms.double(-5.0),
    ECAL_Compensation = cms.double(0.5),
    HCAL_Calib = cms.bool(True),
    weight_HFhad = cms.double(1.0),
    ApplyPulseDPG = cms.bool(False),
    navigator = cms.PSet(
        name = cms.string('PFRecHitCaloTowerNavigator')
    ),
    ECAL_Threshold = cms.double(10.0),
    ApplyTimeDPG = cms.bool(False),
    caloTowers = cms.InputTag("hltTowerMakerForPF"),
    hcalRecHitsHBHE = cms.InputTag("hltHbhereco"),
    LongFibre_Fraction = cms.double(0.1),
    MaxShortTiming_Cut = cms.double(5.0),
    HcalMaxAllowedHFLongShortSev = cms.int32(9),
    thresh_Barrel = cms.double(0.4),
    navigation_HF = cms.bool(True),
    HcalMaxAllowedHFInTimeWindowSev = cms.int32(9),
    HF_Calib_29 = cms.double(1.07),
    LongFibre_Cut = cms.double(120.0),
    EM_Depth = cms.double(22.0),
    weight_HFem = cms.double(1.0),
    LongShortFibre_Cut = cms.double(1000000000.0),
    MinShortTiming_Cut = cms.double(-5.0),
    MaxLongTiming_Cut = cms.double(5.0),
    thresh_HF = cms.double(0.4),
    HcalMaxAllowedHFDigiTimeSev = cms.int32(9),
    thresh_Endcap = cms.double(0.4),
    HcalMaxAllowedChannelStatusSev = cms.int32(9),
    hcalRecHitsHF = cms.InputTag("hltHfreco"),
    ShortFibre_Cut = cms.double(60.0),
    ApplyLongShortDPG = cms.bool(True),
    HF_Calib = cms.bool(True),
    HAD_Depth = cms.double(47.0),
    ShortFibre_Fraction = cms.double(0.01),
    HCAL_Calib_29 = cms.double(1.35)
)


process.hltParticleFlowRecHitPSUnseeded = cms.EDProducer("PFRecHitProducer",
    producers = cms.VPSet(cms.PSet(
        src = cms.InputTag("hltEcalPreshowerRecHit","EcalRecHitsES"),
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            threshold = cms.double(7e-06),
            name = cms.string('PFRecHitQTestThreshold')
        ))
    )),
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    )
)


process.hltPixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltPixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltPixelTracks = cms.EDProducer("PixelTrackProducer",
    useFilterWithES = cms.bool(False),
    FilterPSet = cms.PSet(
        nSigmaTipMaxTolerance = cms.double(0.0),
        chi2 = cms.double(1000.0),
        ComponentName = cms.string('PixelTrackFilterByKinematics'),
        nSigmaInvPtTolerance = cms.double(0.0),
        ptMin = cms.double(0.1),
        tipMax = cms.double(1.0)
    ),
    passLabel = cms.string('Pixel triplet primary tracks with vertex constraint'),
    FitterPSet = cms.PSet(
        ComponentName = cms.string('PixelFitterByHelixProjections'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        fixImpactParameter = cms.double(0.0)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            originRadius = cms.double(0.2),
            ptMin = cms.double(0.9),
            originHalfLength = cms.double(24.0)
        )
    ),
    CleanerPSet = cms.PSet(
        ComponentName = cms.string('PixelTrackCleanerBySharedHits')
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        SeedingLayers = cms.InputTag("hltPixelLayerTriplets"),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            phiPreFiltering = cms.double(0.3),
            extraHitRPhitolerance = cms.double(0.06),
            useMultScattering = cms.bool(True),
            ComponentName = cms.string('PixelTripletHLTGenerator'),
            extraHitRZtolerance = cms.double(0.06),
            SeedComparitorPSet = cms.PSet(
                clusterShapeCacheSrc = cms.InputTag("hltSiPixelClustersCache"),
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor')
            )
        )
    )
)


process.hltPixelVertices = cms.EDProducer("PixelVertexProducer",
    WtAverage = cms.bool(True),
    ZOffset = cms.double(5.0),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    ),
    Verbosity = cms.int32(0),
    UseError = cms.bool(True),
    TrackCollection = cms.InputTag("hltPixelTracks"),
    ZSeparation = cms.double(0.05),
    NTrkMin = cms.int32(2),
    Method2 = cms.bool(True),
    Finder = cms.string('DivisiveVertexFinder'),
    PtMin = cms.double(1.0)
)


process.hltRpcRecHits = cms.EDProducer("RPCRecHitProducer",
    recAlgo = cms.string('RPCRecHitStandardAlgo'),
    deadvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat'),
    rpcDigiLabel = cms.InputTag("hltMuonRPCDigis"),
    maskvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat'),
    recAlgoConfig = cms.PSet(

    ),
    deadSource = cms.string('File'),
    maskSource = cms.string('File')
)


process.hltScalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    scalersInputTag = cms.InputTag("rawDataCollector")
)


process.hltSiPixelClusters = cms.EDProducer("SiPixelClusterProducer",
    src = cms.InputTag("hltSiPixelDigis"),
    ChannelThreshold = cms.int32(1000),
    maxNumberOfClusters = cms.int32(20000),
    VCaltoElectronGain = cms.int32(65),
    MissCalibrate = cms.untracked.bool(True),
    SplitClusters = cms.bool(False),
    VCaltoElectronOffset = cms.int32(-414),
    payloadType = cms.string('HLT'),
    SeedThreshold = cms.int32(1000),
    ClusterThreshold = cms.double(4000.0)
)


process.hltSiPixelClustersCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    src = cms.InputTag("hltSiPixelClusters"),
    onDemand = cms.bool(False)
)


process.hltSiPixelDigis = cms.EDProducer("SiPixelRawToDigi",
    UseQualityInfo = cms.bool(False),
    CheckPixelOrder = cms.bool(False),
    InputLabel = cms.InputTag("rawDataCollector"),
    IncludeErrors = cms.bool(False),
    ErrorList = cms.vint32(),
    Regions = cms.PSet(

    ),
    Timing = cms.untracked.bool(False),
    UserErrorList = cms.vint32()
)


process.hltSiPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("hltSiPixelClusters"),
    CPE = cms.string('hltESPPixelCPEGeneric')
)


process.hltSiStripClusters = cms.EDProducer("MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(),
    measurementTracker = cms.string('hltESPMeasurementTracker'),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string('hltSiStripRawToClustersFacility')
)


process.hltSiStripExcludedFEDListProducer = cms.EDProducer("SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag("rawDataCollector")
)


process.hltSiStripRawToClustersFacility = cms.EDProducer("SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag("rawDataCollector"),
    DoAPVEmulatorCheck = cms.bool(False),
    Algorithms = cms.PSet(
        CommonModeNoiseSubtractionMode = cms.string('Median'),
        doAPVRestore = cms.bool(False),
        TruncateInSuppressor = cms.bool(True),
        useCMMeanMap = cms.bool(False),
        PedestalSubtractionFedMode = cms.bool(True),
        SiStripFedZeroSuppressionMode = cms.uint32(4)
    ),
    Clusterizer = cms.PSet(
        setDetId = cms.bool(True),
        ChannelThreshold = cms.double(2.0),
        MaxSequentialBad = cms.uint32(1),
        MaxSequentialHoles = cms.uint32(0),
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        MaxAdjacentBad = cms.uint32(0),
        QualityLabel = cms.string(''),
        SeedThreshold = cms.double(3.0),
        RemoveApvShots = cms.bool(True),
        ClusterThreshold = cms.double(5.0)
    ),
    onDemand = cms.bool(True)
)


process.hltTowerMakerForAll = cms.EDProducer("CaloTowersCreator",
    EBSumThreshold = cms.double(0.2),
    MomHBDepth = cms.double(0.2),
    EBWeight = cms.double(1.0),
    hfInput = cms.InputTag("hltHfreco"),
    AllowMissingInputs = cms.bool(False),
    UseSymEBTreshold = cms.bool(False),
    MomEEDepth = cms.double(0.0),
    EESumThreshold = cms.double(0.45),
    HBGrid = cms.vdouble(),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HBThreshold = cms.double(0.7),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    UseEcalRecoveredHits = cms.bool(False),
    MomConstrMethod = cms.int32(1),
    MomHEDepth = cms.double(0.4),
    HcalThreshold = cms.double(-1000.0),
    HF2Weights = cms.vdouble(),
    HOWeights = cms.vdouble(),
    EEGrid = cms.vdouble(),
    HEDWeight = cms.double(1.0),
    EEWeights = cms.vdouble(),
    EEWeight = cms.double(1.0),
    UseHO = cms.bool(False),
    HBWeights = cms.vdouble(),
    HESWeight = cms.double(1.0),
    HF1Weight = cms.double(1.0),
    HF2Grid = cms.vdouble(),
    HEDWeights = cms.vdouble(),
    HEDGrid = cms.vdouble(),
    HOThresholdPlus1 = cms.double(3.5),
    HF1Grid = cms.vdouble(),
    EBWeights = cms.vdouble(),
    HOWeight = cms.double(1e-99),
    EBThreshold = cms.double(0.07),
    hbheInput = cms.InputTag("hltHbhereco"),
    HF2Weight = cms.double(1.0),
    HF2Threshold = cms.double(0.85),
    HcalAcceptSeverityLevel = cms.uint32(9),
    EEThreshold = cms.double(0.3),
    HESThreshold = cms.double(0.8),
    HOThresholdPlus2 = cms.double(3.5),
    HF1Weights = cms.vdouble(),
    hoInput = cms.InputTag("hltHoreco"),
    HF1Threshold = cms.double(0.5),
    HOThresholdMinus1 = cms.double(3.5),
    HESGrid = cms.vdouble(),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring('kTime', 
        'kWeird', 
        'kBad'),
    HESWeights = cms.vdouble(),
    UseSymEETreshold = cms.bool(False),
    HEDThreshold = cms.double(0.8),
    UseEtEBTreshold = cms.bool(False),
    EcutTower = cms.double(-1000.0),
    UseRejectedHitsOnly = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(False),
    HOThresholdMinus2 = cms.double(3.5),
    HOThreshold0 = cms.double(3.5),
    ecalInputs = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE"),
    UseRejectedRecoveredHcalHits = cms.bool(False),
    MomEBDepth = cms.double(0.3),
    HBWeight = cms.double(1.0),
    HOGrid = cms.vdouble(),
    EBGrid = cms.vdouble()
)


process.hltTowerMakerForPF = cms.EDProducer("CaloTowersCreator",
    EBSumThreshold = cms.double(0.2),
    MomHBDepth = cms.double(0.2),
    EBWeight = cms.double(1.0),
    hfInput = cms.InputTag("hltHfreco"),
    AllowMissingInputs = cms.bool(False),
    UseSymEBTreshold = cms.bool(False),
    MomEEDepth = cms.double(0.0),
    EESumThreshold = cms.double(0.45),
    HBGrid = cms.vdouble(),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HBThreshold = cms.double(0.4),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    UseEcalRecoveredHits = cms.bool(False),
    MomConstrMethod = cms.int32(1),
    MomHEDepth = cms.double(0.4),
    HcalThreshold = cms.double(-1000.0),
    HF2Weights = cms.vdouble(),
    HOWeights = cms.vdouble(),
    EEGrid = cms.vdouble(),
    HEDWeight = cms.double(1.0),
    EEWeights = cms.vdouble(),
    EEWeight = cms.double(1.0),
    UseHO = cms.bool(False),
    HBWeights = cms.vdouble(),
    HESWeight = cms.double(1.0),
    HF1Weight = cms.double(1.0),
    HF2Grid = cms.vdouble(),
    HEDWeights = cms.vdouble(),
    HEDGrid = cms.vdouble(),
    HOThresholdPlus1 = cms.double(1.1),
    HF1Grid = cms.vdouble(),
    EBWeights = cms.vdouble(),
    HOWeight = cms.double(1.0),
    EBThreshold = cms.double(0.07),
    hbheInput = cms.InputTag("hltHbhereco"),
    HF2Weight = cms.double(1.0),
    HF2Threshold = cms.double(1.8),
    HcalAcceptSeverityLevel = cms.uint32(11),
    EEThreshold = cms.double(0.3),
    HESThreshold = cms.double(0.4),
    HOThresholdPlus2 = cms.double(1.1),
    HF1Weights = cms.vdouble(),
    hoInput = cms.InputTag("hltHoreco"),
    HF1Threshold = cms.double(1.2),
    HOThresholdMinus1 = cms.double(1.1),
    HESGrid = cms.vdouble(),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring('kTime', 
        'kWeird', 
        'kBad'),
    HESWeights = cms.vdouble(),
    UseSymEETreshold = cms.bool(False),
    HEDThreshold = cms.double(0.4),
    UseEtEBTreshold = cms.bool(False),
    EcutTower = cms.double(-1000.0),
    UseRejectedHitsOnly = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(True),
    HOThresholdMinus2 = cms.double(1.1),
    HOThreshold0 = cms.double(1.1),
    ecalInputs = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE"),
    UseRejectedRecoveredHcalHits = cms.bool(False),
    MomEBDepth = cms.double(0.3),
    HBWeight = cms.double(1.0),
    HOGrid = cms.vdouble(),
    EBGrid = cms.vdouble()
)


process.hltTrackIter0RefsForJets4Iter1 = cms.EDProducer("ChargedRefCandidateProducer",
    src = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity"),
    particleType = cms.string('pi+')
)


process.hltTriggerSummaryAOD = cms.EDProducer("TriggerSummaryProducerAOD",
    processName = cms.string('@')
)


process.hltTriggerSummaryRAW = cms.EDProducer("TriggerSummaryProducerRAW",
    processName = cms.string('@')
)


process.hltTrimmedPixelVertices = cms.EDProducer("PixelVertexCollectionTrimmer",
    minSumPt2 = cms.double(0.0),
    src = cms.InputTag("hltPixelVertices"),
    maxVtx = cms.uint32(100),
    fractionSumPt2 = cms.double(0.3),
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    )
)


process.hlt1AK4PFJetsMass00 = cms.EDFilter("HLT1PFJet",
    saveTags = cms.bool(False),
    MinPt = cms.double(40.0),
    MinN = cms.int32(1),
    MaxEta = cms.double(3.0),
    MinMass = cms.double(0.0),
    inputTag = cms.InputTag("hltAK4PFJetsCorrected"),
    MinE = cms.double(-1.0),
    triggerType = cms.int32(85)
)


process.hlt1AK4PFJetsNOJECMass00 = cms.EDFilter("HLT1PFJet",
    saveTags = cms.bool(False),
    MinPt = cms.double(40.0),
    MinN = cms.int32(1),
    MaxEta = cms.double(3.0),
    MinMass = cms.double(0.0),
    inputTag = cms.InputTag("hltAK4PFJets"),
    MinE = cms.double(-1.0),
    triggerType = cms.int32(85)
)


process.hlt1AK4PFJetsTrimMass00 = cms.EDFilter("HLT1PFJet",
    saveTags = cms.bool(False),
    MinPt = cms.double(40.0),
    MinN = cms.int32(1),
    MaxEta = cms.double(3.0),
    MinMass = cms.double(0.0),
    inputTag = cms.InputTag("hltAK4PFJetsTrim"),
    MinE = cms.double(-1.0),
    triggerType = cms.int32(85)
)


process.hlt1AK8PFJetsMass00 = cms.EDFilter("HLT1PFJet",
    saveTags = cms.bool(False),
    MinPt = cms.double(40.0),
    MinN = cms.int32(1),
    MaxEta = cms.double(3.0),
    MinMass = cms.double(0.0),
    inputTag = cms.InputTag("hltAK8PFJetsCorrected"),
    MinE = cms.double(-1.0),
    triggerType = cms.int32(85)
)


process.hlt1AK8PFJetsNOJECMass00 = cms.EDFilter("HLT1PFJet",
    saveTags = cms.bool(False),
    MinPt = cms.double(40.0),
    MinN = cms.int32(1),
    MaxEta = cms.double(3.0),
    MinMass = cms.double(0.0),
    inputTag = cms.InputTag("hltAK8PFJets"),
    MinE = cms.double(-1.0),
    triggerType = cms.int32(85)
)


process.hlt1AK8PFJetsTrimMass00 = cms.EDFilter("HLT1PFJet",
    saveTags = cms.bool(False),
    MinPt = cms.double(40.0),
    MinN = cms.int32(1),
    MaxEta = cms.double(3.0),
    MinMass = cms.double(0.0),
    inputTag = cms.InputTag("hltAK8PFJetsTrim"),
    MinE = cms.double(-1.0),
    triggerType = cms.int32(85)
)


process.hltAK4CaloJetsPFEt5 = cms.EDFilter("EtMinCaloJetSelector",
    filter = cms.bool(False),
    src = cms.InputTag("hltAK4CaloJetsPF"),
    etMin = cms.double(5.0)
)


process.hltAK8Ht350 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltAK8HtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8HtMht"),
    minHt = cms.vdouble(350.0)
)


process.hltAK8Ht450 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltAK8HtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8HtMht"),
    minHt = cms.vdouble(450.0)
)


process.hltAK8Ht550 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltAK8HtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8HtMht"),
    minHt = cms.vdouble(550.0)
)


process.hltAK8Ht650 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltAK8HtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8HtMht"),
    minHt = cms.vdouble(650.0)
)


process.hltAK8Ht750 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltAK8HtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8HtMht"),
    minHt = cms.vdouble(750.0)
)


process.hltAK8PFHT450 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFHT"),
    minHt = cms.vdouble(450.0)
)


process.hltAK8PFHT550 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFHT"),
    minHt = cms.vdouble(550.0)
)


process.hltAK8PFHT650 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFHT"),
    minHt = cms.vdouble(650.0)
)


process.hltAK8PFHT750 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFHT"),
    minHt = cms.vdouble(750.0)
)


process.hltAK8PFHT850 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFHT"),
    minHt = cms.vdouble(850.0)
)


process.hltAK8PFTrimHT450 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFTrimHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFTrimHT"),
    minHt = cms.vdouble(450.0)
)


process.hltAK8PFTrimHT550 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFTrimHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFTrimHT"),
    minHt = cms.vdouble(550.0)
)


process.hltAK8PFTrimHT650 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFTrimHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFTrimHT"),
    minHt = cms.vdouble(650.0)
)


process.hltAK8PFTrimHT750 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFTrimHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFTrimHT"),
    minHt = cms.vdouble(750.0)
)


process.hltAK8PFTrimHT850 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltAK8PFTrimHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltAK8PFTrimHT"),
    minHt = cms.vdouble(850.0)
)


process.hltAK8SingleCaloJet260 = cms.EDFilter("HLT1CaloJet",
    saveTags = cms.bool(True),
    MinPt = cms.double(260.0),
    MinN = cms.int32(1),
    MaxEta = cms.double(5.0),
    MinMass = cms.double(-1.0),
    inputTag = cms.InputTag("hltAK8CaloJetsCorrectedIDPassed"),
    MinE = cms.double(-1.0),
    triggerType = cms.int32(85)
)


process.hltAK8SinglePFJet360TrimMass30 = cms.EDFilter("HLT1PFJet",
    saveTags = cms.bool(True),
    MinPt = cms.double(360.0),
    MinN = cms.int32(1),
    MaxEta = cms.double(5.0),
    MinMass = cms.double(30.0),
    inputTag = cms.InputTag("hltAK8TrimJets"),
    MinE = cms.double(-1.0),
    triggerType = cms.int32(85)
)


process.hltBoolEnd = cms.EDFilter("HLTBool",
    result = cms.bool(True)
)


process.hltBoolFalse = cms.EDFilter("HLTBool",
    result = cms.bool(False)
)


process.hltHt350 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltHtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltHtMht"),
    minHt = cms.vdouble(350.0)
)


process.hltHt450 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltHtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltHtMht"),
    minHt = cms.vdouble(450.0)
)


process.hltHt550 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltHtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltHtMht"),
    minHt = cms.vdouble(550.0)
)


process.hltHt650 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltHtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltHtMht"),
    minHt = cms.vdouble(650.0)
)


process.hltHt700 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltHtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltHtMht"),
    minHt = cms.vdouble(700.0)
)


process.hltHt750 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(False),
    mhtLabels = cms.VInputTag("hltHtMht"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltHtMht"),
    minHt = cms.vdouble(750.0)
)


process.hltL1sL1HTT150OrHTT175 = cms.EDFilter("HLTLevel1GTSeed",
    saveTags = cms.bool(True),
    L1SeedsLogicalExpression = cms.string('L1_HTT150 OR L1_HTT175'),
    L1MuonCollectionTag = cms.InputTag("hltL1extraParticles"),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    L1UseAliasesForSeeding = cms.bool(True),
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    L1CollectionsTag = cms.InputTag("hltL1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1GtObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
    L1TechTriggerSeeding = cms.bool(False)
)


process.hltL1sL1SingleJet128 = cms.EDFilter("HLTLevel1GTSeed",
    saveTags = cms.bool(True),
    L1SeedsLogicalExpression = cms.string('L1_SingleJet128'),
    L1MuonCollectionTag = cms.InputTag("hltL1extraParticles"),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    L1UseAliasesForSeeding = cms.bool(True),
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    L1CollectionsTag = cms.InputTag("hltL1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1GtObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
    L1TechTriggerSeeding = cms.bool(False)
)


process.hltPFHT450 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltPFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltPFHT"),
    minHt = cms.vdouble(450.0)
)


process.hltPFHT550 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltPFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltPFHT"),
    minHt = cms.vdouble(550.0)
)


process.hltPFHT650 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltPFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltPFHT"),
    minHt = cms.vdouble(650.0)
)


process.hltPFHT750 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltPFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltPFHT"),
    minHt = cms.vdouble(750.0)
)


process.hltPFHT850 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltPFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltPFHT"),
    minHt = cms.vdouble(850.0)
)


process.hltPFHT900 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltPFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltPFHT"),
    minHt = cms.vdouble(900.0)
)


process.hltPFHT950 = cms.EDFilter("HLTHtMhtFilter",
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag("hltPFHT"),
    meffSlope = cms.vdouble(1.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    htLabels = cms.VInputTag("hltPFHT"),
    minHt = cms.vdouble(950.0)
)


process.hltPreAK8PFHT450 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFHT550 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFHT650 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFHT750 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFHT850 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFJet360TrimMass30 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFNOJECTrimHT450 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFNOJECTrimHT550 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFNOJECTrimHT650 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFNOJECTrimHT750 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFNOJECTrimHT850 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFTrimHT550 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFTrimHT650 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFTrimHT750 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAK8PFTrimHT850 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreHLTAK8PFTrimHT450 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT450 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT550 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT650 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT750 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT850 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT900 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT950 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFTrimHT450 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFTrimHT650 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFTrimHT750 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFTrimHT850 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltTriggerType = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)


process.hltGetConditions = cms.EDAnalyzer("EventSetupRecordDataGetter",
    toGet = cms.VPSet(),
    verbose = cms.untracked.bool(False)
)


process.hltGetRaw = cms.EDAnalyzer("HLTGetRaw",
    RawDataCollection = cms.InputTag("rawDataCollector")
)


process.output = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltAntiKT5CaloJets_*_*', 
        'keep *_hltAK8HtMht_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltGtDigis_*_*', 
        'keep *_hltAK8PFHT_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK8PFJetsCorrected_*_*', 
        'keep *_hltAK8PFTrimHT_*_*', 
        'keep *_hltAK8PFJets_*_*', 
        'keep *_hltAK8CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4PFJetsTrim_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltAK4CaloJetsPF_*_*', 
        'keep *_hltAntiKT5PFJetsNoPU_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltAntiKT5PFJets_*_*', 
        'keep *_hltPFHT_*_*', 
        'keep *_hltAK8TrimJets_*_*', 
        'keep *_hltAK8PFJetsTrim_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltLightPFTracks_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltHtMht_*_*'),
    fileName = cms.untracked.string(NAME+'_Prod.root'),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('HLTDEBUG')
    )
)


process.HLTDoLocalPixelSequence = cms.Sequence(process.hltSiPixelDigis+process.hltSiPixelClusters+process.hltSiPixelClustersCache+process.hltSiPixelRecHits)


process.HLTPreshowerSequence = cms.Sequence(process.hltEcalPreshowerDigis+process.hltEcalPreshowerRecHit)


process.HLTParticleFlowSequence = cms.Sequence(process.HLTPreshowerSequence+process.hltParticleFlowRecHitECALUnseeded+process.hltParticleFlowRecHitHCAL+process.hltParticleFlowRecHitPSUnseeded+process.hltParticleFlowClusterECALUncorrectedUnseeded+process.hltParticleFlowClusterPSUnseeded+process.hltParticleFlowClusterECALUnseeded+process.hltParticleFlowClusterHCAL+process.hltParticleFlowClusterHFEM+process.hltParticleFlowClusterHFHAD+process.hltLightPFTracks+process.hltParticleFlowBlock+process.hltParticleFlow)


process.HLTL1UnpackerSequence = cms.Sequence(process.hltGtDigis+process.hltGctDigis+process.hltL1GtObjectMap+process.hltL1extraParticles)


process.HLTMuonLocalRecoSequence = cms.Sequence(process.hltMuonDTDigis+process.hltDt1DRecHits+process.hltDt4DSegments+process.hltMuonCSCDigis+process.hltCsc2DRecHits+process.hltCscSegments+process.hltMuonRPCDigis+process.hltRpcRecHits)


process.HLTAK4CaloJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAllCalo+process.hltAK4CaloJetsCorrected+process.hltAK4CaloJetsCorrectedIDPassed)


process.HLTAK8PFJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAll+process.hltAK8PFJetsCorrected)


process.HLTDoLocalHcalSequence = cms.Sequence(process.hltHcalDigis+process.hltHbhereco+process.hltHfreco+process.hltHoreco)


process.HLTIter0TrackAndTauJet4Iter1Sequence = cms.Sequence(process.hltTrackIter0RefsForJets4Iter1+process.hltAK4Iter0TrackJets4Iter1+process.hltIter0TrackAndTauJets4Iter1)


process.HLTAK4PFJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAll+process.hltAK4PFJetsCorrected)


process.HLTL2muonrecoNocandSequence = cms.Sequence(process.HLTMuonLocalRecoSequence+process.hltL2OfflineMuonSeeds+process.hltL2MuonSeeds+process.hltL2Muons)


process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence(process.hltEcalDigis+process.hltEcalUncalibRecHit+process.hltEcalDetIdToBeRecovered+process.hltEcalRecHit)


process.HLTAK8CaloJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAllCalo+process.hltAK8CaloJetsCorrected+process.hltAK8CaloJetsCorrectedIDPassed)


process.HLTIter1TrackAndTauJets4Iter2Sequence = cms.Sequence(process.hltIter1TrackRefsForJets4Iter2+process.hltAK4Iter1TrackJets4Iter2+process.hltIter1TrackAndTauJets4Iter2)


process.HLTBeamSpot = cms.Sequence(process.hltScalersRawToDigi+process.hltOnlineBeamSpot)


process.HLTEndSequence = cms.Sequence(process.hltBoolEnd)


process.HLTIterativeTrackingIteration2 = cms.Sequence(process.hltIter2ClustersRefRemoval+process.hltIter2MaskedMeasurementTrackerEvent+process.hltIter2PixelLayerPairs+process.hltIter2PFlowPixelSeeds+process.hltIter2PFlowCkfTrackCandidates+process.hltIter2PFlowCtfWithMaterialTracks+process.hltIter2PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIteration1 = cms.Sequence(process.hltIter1ClustersRefRemoval+process.hltIter1MaskedMeasurementTrackerEvent+process.hltIter1PixelLayerTriplets+process.hltIter1PFlowPixelSeeds+process.hltIter1PFlowCkfTrackCandidates+process.hltIter1PFlowCtfWithMaterialTracks+process.hltIter1PFlowTrackSelectionHighPurityLoose+process.hltIter1PFlowTrackSelectionHighPurityTight+process.hltIter1PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIteration0 = cms.Sequence(process.hltIter0PFLowPixelSeedsFromPixelTracks+process.hltIter0PFlowCkfTrackCandidates+process.hltIter0PFlowCtfWithMaterialTracks+process.hltIter0PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIter02 = cms.Sequence(process.HLTIterativeTrackingIteration0+process.HLTIter0TrackAndTauJet4Iter1Sequence+process.HLTIterativeTrackingIteration1+process.hltIter1Merged+process.HLTIter1TrackAndTauJets4Iter2Sequence+process.HLTIterativeTrackingIteration2+process.hltIter2Merged)


process.HLTRecopixelvertexingSequence = cms.Sequence(process.hltPixelLayerTriplets+process.hltPixelTracks+process.hltPixelVertices+process.hltTrimmedPixelVertices)


process.HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)


process.HLTDoLocalStripSequence = cms.Sequence(process.hltSiStripExcludedFEDListProducer+process.hltSiStripRawToClustersFacility+process.hltSiStripClusters)


process.HLTDoCaloSequencePF = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence+process.HLTDoLocalHcalSequence+process.hltTowerMakerForPF)


process.HLTTrackReconstructionForPF = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTRecopixelvertexingSequence+process.HLTDoLocalStripSequence+process.HLTIterativeTrackingIter02+process.hltPFMuonMerging+process.hltMuonLinks+process.hltMuons)


process.HLTL3muonTkCandidateSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.hltL3TrajSeedOIState+process.hltL3TrackCandidateFromL2OIState+process.hltL3TkTracksFromL2OIState+process.hltL3MuonsOIState+process.hltL3TrajSeedOIHit+process.hltL3TrackCandidateFromL2OIHit+process.hltL3TkTracksFromL2OIHit+process.hltL3MuonsOIHit+process.hltL3TkFromL2OICombination+process.hltPixelLayerTriplets+process.hltPixelLayerPairs+process.hltMixedLayerPairs+process.hltL3TrajSeedIOHit+process.hltL3TrackCandidateFromL2IOHit+process.hltL3TkTracksFromL2IOHit+process.hltL3MuonsIOHit+process.hltL3TrajectorySeed+process.hltL3TrackCandidateFromL2)


process.HLTL2muonrecoSequence = cms.Sequence(process.HLTL2muonrecoNocandSequence+process.hltL2MuonCandidates)


process.HLTDoCaloSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence+process.HLTDoLocalHcalSequence+process.hltTowerMakerForAll)


process.HLTL3muonrecoNocandSequence = cms.Sequence(process.HLTL3muonTkCandidateSequence+process.hltL3TkTracksMergeStep1+process.hltL3TkTracksFromL2+process.hltL3MuonsLinksCombination+process.hltL3Muons)


process.HLTAK4CaloJetsPrePFRecoSequence = cms.Sequence(process.HLTDoCaloSequencePF+process.hltAK4CaloJetsPF)


process.HLTPreAK4PFJetsRecoSequence = cms.Sequence(process.HLTAK4CaloJetsPrePFRecoSequence+process.hltAK4CaloJetsPFEt5)


process.HLTAK4CaloJetsReconstructionSequence = cms.Sequence(process.HLTDoCaloSequence+process.hltAK4CaloJets+process.hltAK4CaloJetsIDPassed)


process.HLTAK8CaloJetsReconstructionSequence = cms.Sequence(process.HLTDoCaloSequence+process.hltAK8CaloJets+process.hltAK8CaloJetsIDPassed)


process.HLTL3muonrecoSequence = cms.Sequence(process.HLTL3muonrecoNocandSequence+process.hltL3MuonCandidates)


process.HLTAK8PFJetsReconstructionSequence = cms.Sequence(process.HLTL2muonrecoSequence+process.HLTL3muonrecoSequence+process.HLTTrackReconstructionForPF+process.HLTParticleFlowSequence+process.hltAK8PFJets)


process.HLTAK8CaloJetsSequence = cms.Sequence(process.HLTAK8CaloJetsReconstructionSequence+process.HLTAK8CaloJetsCorrectionSequence)


process.HLTAK8PFJetsReconstructionSequenceNOJEC = cms.Sequence(process.HLTL2muonrecoSequence+process.HLTL3muonrecoSequence+process.HLTTrackReconstructionForPF+process.HLTParticleFlowSequence+process.hltAK8PFJetsTrim)


process.HLTAK4PFJetsReconstructionSequence = cms.Sequence(process.HLTL2muonrecoSequence+process.HLTL3muonrecoSequence+process.HLTTrackReconstructionForPF+process.HLTParticleFlowSequence+process.hltAK4PFJets)


process.HLTAK8PFJetsSequence = cms.Sequence(process.HLTPreAK4PFJetsRecoSequence+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence)


process.HLTAK8PFJetsNOJECSequence = cms.Sequence(process.HLTPreAK4PFJetsRecoSequence+process.HLTAK8PFJetsReconstructionSequenceNOJEC)


process.HLTAK4CaloJetsSequence = cms.Sequence(process.HLTAK4CaloJetsReconstructionSequence+process.HLTAK4CaloJetsCorrectionSequence)


process.HLTAK4PFJetsSequence = cms.Sequence(process.HLTPreAK4PFJetsRecoSequence+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence)


process.HLT_PFHT450_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt350)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+cms.ignore(process.hltPFHT450)+cms.ignore(process.hlt1AK4PFJetsMass00)+cms.ignore(process.hlt1AK4PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT550_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt450)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+cms.ignore(process.hltPFHT550)+cms.ignore(process.hlt1AK4PFJetsMass00)+cms.ignore(process.hlt1AK4PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT650_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt550)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+cms.ignore(process.hltPFHT650)+cms.ignore(process.hlt1AK4PFJetsMass00)+cms.ignore(process.hlt1AK4PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT750_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt650)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+cms.ignore(process.hltPFHT750)+cms.ignore(process.hlt1AK4PFJetsMass00)+cms.ignore(process.hlt1AK4PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT850_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt550)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+cms.ignore(process.hltPFHT850)+cms.ignore(process.hlt1AK4PFJetsMass00)+cms.ignore(process.hlt1AK4PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT900_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt700)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+cms.ignore(process.hltPFHT900)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT950_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt750)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+cms.ignore(process.hltPFHT950)+cms.ignore(process.hltBoolEnd))


process.HLT_PFTrimHT450_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt350)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+process.hltAK4PFJetsTrim+cms.ignore(process.hlt1AK4PFJetsTrimMass00)+cms.ignore(process.hltPFHT450)+cms.ignore(process.hltBoolEnd))


process.HLT_PFTrimHT550_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt450)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+process.hltAK4PFJetsTrim+cms.ignore(process.hlt1AK4PFJetsTrimMass00)+cms.ignore(process.hltPFHT550)+cms.ignore(process.hltBoolEnd))


process.HLT_PFTrimHT650_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt550)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+process.hltAK4PFJetsTrim+cms.ignore(process.hlt1AK4PFJetsTrimMass00)+cms.ignore(process.hltPFHT650)+cms.ignore(process.hltBoolEnd))


process.HLT_PFTrimHT750_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt650)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+process.hltAK4PFJetsTrim+cms.ignore(process.hlt1AK4PFJetsTrimMass00)+cms.ignore(process.hltPFHT750)+cms.ignore(process.hltBoolEnd))


process.HLT_PFTrimHT850_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt750)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+process.hltAK4PFJetsTrim+cms.ignore(process.hlt1AK4PFJetsTrimMass00)+cms.ignore(process.hltPFHT850)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFHT450_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht350)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+cms.ignore(process.hltAK8PFHT450)+cms.ignore(process.hlt1AK8PFJetsMass00)+cms.ignore(process.hlt1AK8PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFHT550_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht450)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+cms.ignore(process.hltAK8PFHT550)+cms.ignore(process.hlt1AK8PFJetsMass00)+cms.ignore(process.hlt1AK8PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFHT650_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht550)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+cms.ignore(process.hltAK8PFHT650)+cms.ignore(process.hlt1AK8PFJetsMass00)+cms.ignore(process.hlt1AK8PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFHT750_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht650)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+cms.ignore(process.hltAK8PFHT750)+cms.ignore(process.hlt1AK8PFJetsMass00)+cms.ignore(process.hlt1AK8PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFHT850_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht750)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+cms.ignore(process.hltAK8PFHT850)+cms.ignore(process.hlt1AK8PFJetsMass00)+cms.ignore(process.hlt1AK8PFJetsNOJECMass00)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFTrimHT450_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht350)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+process.hltAK8PFJetsTrim+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFHT450)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFTrimHT550_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht450)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+process.hltAK8PFJetsTrim+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFHT550)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFTrimHT650_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht550)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+process.hltAK8PFJetsTrim+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFHT650)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFTrimHT750_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht650)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+process.hltAK8PFJetsTrim+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFHT750)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFTrimHT850_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht750)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+process.hltAK8PFJetsTrim+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFHT850)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFNOJECTrimHT450_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht350)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequenceNOJEC+process.hltAK8PFTrimHT+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFTrimHT450)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFNOJECTrimHT550_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht450)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequenceNOJEC+process.hltAK8PFTrimHT+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFTrimHT550)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFNOJECTrimHT650_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht550)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequenceNOJEC+process.hltAK8PFTrimHT+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFTrimHT650)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFNOJECTrimHT750_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht650)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequenceNOJEC+process.hltAK8PFTrimHT+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFTrimHT750)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFNOJECTrimHT850_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150OrHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht750)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequenceNOJEC+process.hltAK8PFTrimHT+cms.ignore(process.hlt1AK8PFJetsTrimMass00)+cms.ignore(process.hltAK8PFTrimHT850)+cms.ignore(process.hltBoolEnd))


process.HLT_AK8PFJet360Trim_Mass30_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1SingleJet128)+process.HLTAK8CaloJetsSequence+cms.ignore(process.hltAK8SingleCaloJet260)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets260+process.hltAK8TrimJets+cms.ignore(process.hltAK8SinglePFJet360TrimMass30)+cms.ignore(process.hltBoolEnd))


process.HLTOutput_openhlt = cms.EndPath(process.output)


process.DQMStore = cms.Service("DQMStore",
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(True),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    LSbasedMode = cms.untracked.bool(True),
    verboseQT = cms.untracked.int32(0)
)


process.EvFDaqDirector = cms.Service("EvFDaqDirector",
    buBaseDir = cms.untracked.string('.'),
    runNumber = cms.untracked.uint32(0),
    baseDir = cms.untracked.string('.')
)


process.FastMonitoringService = cms.Service("FastMonitoringService",
    slowName = cms.untracked.string('slowmoni'),
    fastName = cms.untracked.string('fastmoni'),
    fastMonIntervals = cms.untracked.uint32(2),
    sleepTime = cms.untracked.int32(1)
)


process.FastTimerService = cms.Service("FastTimerService",
    dqmPath = cms.untracked.string('HLT/TimerService'),
    dqmModuleTimeRange = cms.untracked.double(40.0),
    enableTimingPaths = cms.untracked.bool(True),
    enableTimingModules = cms.untracked.bool(True),
    enableDQM = cms.untracked.bool(True),
    enableDQMbyModule = cms.untracked.bool(False),
    enableTimingExclusive = cms.untracked.bool(True),
    skipFirstPath = cms.untracked.bool(False),
    enableDQMbyLumiSection = cms.untracked.bool(True),
    dqmPathTimeResolution = cms.untracked.double(0.5),
    dqmPathTimeRange = cms.untracked.double(100.0),
    dqmTimeRange = cms.untracked.double(1000.0),
    dqmLumiSectionsRange = cms.untracked.uint32(2500),
    enableDQMbyProcesses = cms.untracked.bool(True),
    enableDQMSummary = cms.untracked.bool(True),
    enableTimingSummary = cms.untracked.bool(True),
    enableDQMbyPathTotal = cms.untracked.bool(True),
    useRealTimeClock = cms.untracked.bool(True),
    enableDQMbyPathExclusive = cms.untracked.bool(True),
    dqmTimeResolution = cms.untracked.double(5.0),
    dqmModuleTimeResolution = cms.untracked.double(0.2),
    enableDQMbyPathActive = cms.untracked.bool(True),
    enableDQMbyPathDetails = cms.untracked.bool(True),
    enableDQMbyPathOverhead = cms.untracked.bool(False),
    enableDQMbyPathCounters = cms.untracked.bool(True),
    enableDQMbyModuleType = cms.untracked.bool(False)
)


process.MessageLogger = cms.Service("MessageLogger",
    suppressInfo = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        suppressInfo = cms.untracked.vstring(),
        suppressDebug = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO'),
        placeholder = cms.untracked.bool(True)
    ),
    suppressDebug = cms.untracked.vstring(),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    warnings = cms.untracked.PSet(
        suppressInfo = cms.untracked.vstring(),
        suppressDebug = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO'),
        placeholder = cms.untracked.bool(True)
    ),
    threshold = cms.untracked.string('INFO'),
    statistics = cms.untracked.vstring('cerr'),
    cerr = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        suppressInfo = cms.untracked.vstring(),
        noTimeStamps = cms.untracked.bool(False),
        suppressDebug = cms.untracked.vstring(),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        suppressWarning = cms.untracked.vstring(),
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        suppressError = cms.untracked.vstring(),
        FwkSummary = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1),
            limit = cms.untracked.int32(10000000)
        ),
        threshold = cms.untracked.string('INFO'),
        FwkReport = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(500),
            limit = cms.untracked.int32(10000000)
        )
    ),
    FrameworkJobReport = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        )
    ),
    suppressWarning = cms.untracked.vstring('hltOnlineBeamSpot', 
        'hltCtf3HitL1SeededWithMaterialTracks', 
        'hltL3MuonsOIState', 
        'hltPixelTracksForHighMult', 
        'hltHITPixelTracksHE', 
        'hltHITPixelTracksHB', 
        'hltCtfL1SeededWithMaterialTracks', 
        'hltRegionalTracksForL3MuonIsolation', 
        'hltSiPixelClusters', 
        'hltActivityStartUpElectronPixelSeeds', 
        'hltLightPFTracks', 
        'hltPixelVertices3DbbPhi', 
        'hltL3MuonsIOHit', 
        'hltPixelTracks', 
        'hltSiPixelDigis', 
        'hltL3MuonsOIHit', 
        'hltL1SeededElectronGsfTracks', 
        'hltL1SeededStartUpElectronPixelSeeds', 
        'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV', 
        'hltCtfActivityWithMaterialTracks'),
    suppressError = cms.untracked.vstring('hltOnlineBeamSpot', 
        'hltL3MuonCandidates', 
        'hltL3TkTracksFromL2OIState', 
        'hltPFJetCtfWithMaterialTracks', 
        'hltL3TkTracksFromL2IOHit', 
        'hltL3TkTracksFromL2OIHit'),
    errors = cms.untracked.PSet(
        suppressInfo = cms.untracked.vstring(),
        suppressDebug = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO'),
        placeholder = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    debugModules = cms.untracked.vstring(),
    infos = cms.untracked.PSet(
        suppressInfo = cms.untracked.vstring(),
        suppressDebug = cms.untracked.vstring(),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        suppressWarning = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO'),
        placeholder = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary', 
        'TriggerSummaryProducerAOD', 
        'L1GtTrigReport', 
        'HLTrigReport', 
        'FastReport'),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport')
)


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    PropagationDirection = cms.string('anyDirection')
)


process.AutoMagneticFieldESProducer = cms.ESProducer("AutoMagneticFieldESProducer",
    label = cms.untracked.string(''),
    nominalCurrents = cms.untracked.vint32(-1, 0, 9558, 14416, 16819, 
        18268, 19262),
    valueOverride = cms.int32(-1),
    mapLabels = cms.untracked.vstring('090322_3_8t', 
        '0t', 
        '071212_2t', 
        '071212_3t', 
        '071212_3_5t', 
        '090322_3_8t', 
        '071212_4t')
)


process.CSCChannelMapperESProducer = cms.ESProducer("CSCChannelMapperESProducer",
    AlgoName = cms.string('CSCChannelMapperPostls1')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string(''),
    useDDD = cms.bool(False),
    alignmentsLabel = cms.string(''),
    useGangedStripsInME1a = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(True)
)


process.CSCIndexerESProducer = cms.ESProducer("CSCIndexerESProducer",
    AlgoName = cms.string('CSCIndexerPostls1')
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    appendToDataLabel = cms.string(''),
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC'),
        maxDepthHB = cms.int32(2)
    )
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par')
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC'),
        maxDepthHB = cms.int32(2)
    )
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string(''),
    hcalTopologyConstants = cms.PSet(
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC'),
        maxDepthHB = cms.int32(2)
    )
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    SimpleMagneticField = cms.string(''),
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    SimpleMagneticField = cms.string('ParabolicMf'),
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    SimpleMagneticField = cms.string(''),
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    SimpleMagneticField = cms.string('ParabolicMf'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('Parabolic'),
    parameters = cms.PSet(
        BValue = cms.string('')
    ),
    label = cms.untracked.string('ParabolicMf')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    useDDD = cms.untracked.bool(False),
    compatibiltyWith11 = cms.untracked.bool(True)
)


process.SiStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    printDebug = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    APVGain = cms.VPSet(cms.PSet(
        Record = cms.string('SiStripApvGainRcd'),
        NormalizationFactor = cms.untracked.double(1.0),
        Label = cms.untracked.string('')
    ), 
        cms.PSet(
            Record = cms.string('SiStripApvGain2Rcd'),
            NormalizationFactor = cms.untracked.double(1.0),
            Label = cms.untracked.string('')
        )),
    AutomaticNormalization = cms.bool(False)
)


process.SiStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    appendToDataLabel = cms.string(''),
    PrintDebugOutput = cms.bool(False),
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        )),
    UseEmptyRunInfo = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    PreFilter = cms.bool(False),
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0)
)


process.SlaveField0 = cms.ESProducer("UniformMagneticFieldESProducer",
    ZFieldInTesla = cms.double(0.0),
    label = cms.untracked.string('slave_0')
)


process.SlaveField20 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('2_0T')
    ),
    label = cms.untracked.string('slave_20')
)


process.SlaveField30 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_0T')
    ),
    label = cms.untracked.string('slave_30')
)


process.SlaveField35 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_5T')
    ),
    label = cms.untracked.string('slave_35')
)


process.SlaveField38 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_8T')
    ),
    label = cms.untracked.string('slave_38')
)


process.SlaveField40 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('4_0T')
    ),
    label = cms.untracked.string('slave_40')
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False),
    trackerGeometryConstants = cms.PSet(
        ROCS_X = cms.int32(0),
        ROCS_Y = cms.int32(0),
        upgradeGeometry = cms.bool(False),
        BIG_PIX_PER_ROC_Y = cms.int32(2),
        BIG_PIX_PER_ROC_X = cms.int32(1),
        ROWS_PER_ROC = cms.int32(80),
        COLS_PER_ROC = cms.int32(52)
    ),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False),
    layerNumberPXB = cms.uint32(16),
    totalBlade = cms.uint32(24)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VBF0 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('0t'),
    version = cms.string('grid_1103l_071212_2t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_0'),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        path = cms.string('grid.[v].bin'),
        master = cms.int32(1),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF20 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('071212_2t'),
    version = cms.string('grid_1103l_071212_2t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_20'),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        path = cms.string('grid.[v].bin'),
        master = cms.int32(1),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF30 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('071212_3t'),
    version = cms.string('grid_1103l_071212_3t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_30'),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        path = cms.string('grid.[v].bin'),
        master = cms.int32(1),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF35 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('071212_3_5t'),
    version = cms.string('grid_1103l_071212_3_5t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_35'),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        path = cms.string('grid.[v].bin'),
        master = cms.int32(1),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF38 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(1.0, 1.0, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991),
    label = cms.untracked.string('090322_3_8t'),
    version = cms.string('grid_1103l_090322_3_8t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_38'),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        path = cms.string('grid.[v].bin'),
        master = cms.int32(1),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    ), 
        cms.PSet(
            path = cms.string('S3/grid.[v].bin'),
            master = cms.int32(3),
            sectors = cms.string('3'),
            volumes = cms.string('176-186,231-241,286-296')
        ), 
        cms.PSet(
            path = cms.string('S4/grid.[v].bin'),
            master = cms.int32(4),
            sectors = cms.string('4'),
            volumes = cms.string('176-186,231-241,286-296')
        ), 
        cms.PSet(
            path = cms.string('S9/grid.[v].bin'),
            master = cms.int32(9),
            sectors = cms.string('9'),
            volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296')
        ), 
        cms.PSet(
            path = cms.string('S10/grid.[v].bin'),
            master = cms.int32(10),
            sectors = cms.string('10'),
            volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296')
        ), 
        cms.PSet(
            path = cms.string('S11/grid.[v].bin'),
            master = cms.int32(11),
            sectors = cms.string('11'),
            volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296')
        )),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF40 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('071212_4t'),
    version = cms.string('grid_1103l_071212_4t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_40'),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        path = cms.string('grid.[v].bin'),
        master = cms.int32(1),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    cacheLastVolume = cms.untracked.bool(True)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.02),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kRecovered = cms.vstring(),
        kGood = cms.vstring('kOk'),
        kTime = cms.vstring(),
        kWeird = cms.vstring(),
        kBad = cms.vstring('kNonRespondingIsolated', 
            'kDeadVFE', 
            'kDeadFE', 
            'kNoDataNoTP'),
        kProblematic = cms.vstring('kDAC', 
            'kNoLaser', 
            'kNoisy', 
            'kNNoisy', 
            'kNNNoisy', 
            'kNNNNoisy', 
            'kNNNNNoisy', 
            'kFixedG6', 
            'kFixedG1', 
            'kFixedG0')
    ),
    timeThresh = cms.double(2.0),
    flagMask = cms.PSet(
        kRecovered = cms.vstring('kLeadingEdgeRecovered', 
            'kTowerRecovered'),
        kGood = cms.vstring('kGood'),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring('kWeird', 
            'kDiWeird'),
        kBad = cms.vstring('kFaultyHardware', 
            'kDead', 
            'kKilled'),
        kProblematic = cms.vstring('kPoorReco', 
            'kPoorCalib', 
            'kNoisy', 
            'kSaturated')
    )
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    RecoveredRecHitBits = cms.vstring('TimingAddedBit', 
        'TimingSubtractedBit'),
    SeverityLevels = cms.VPSet(cms.PSet(
        RecHitFlags = cms.vstring(),
        ChannelStatus = cms.vstring(),
        Level = cms.int32(0)
    ), 
        cms.PSet(
            RecHitFlags = cms.vstring(),
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HSCP_R1R2', 
                'HSCP_FracLeader', 
                'HSCP_OuterEnergy', 
                'HSCP_ExpFit', 
                'ADCSaturationBit', 
                'HBHEIsolatedNoise', 
                'AddedSimHcalNoise'),
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HBHEHpdHitMultiplicity', 
                'HBHEPulseShape', 
                'HOBit', 
                'HFInTimeWindow', 
                'ZDCBit', 
                'CalibrationBit', 
                'TimingErrorBit', 
                'HBHETriangleNoise', 
                'HBHETS4TS5Noise'),
            ChannelStatus = cms.vstring(),
            Level = cms.int32(8)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HFLongShort', 
                'HFPET', 
                'HFS8S1Ratio', 
                'HFDigiTime'),
            ChannelStatus = cms.vstring(),
            Level = cms.int32(11)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HBHEFlatNoise', 
                'HBHESpikeNoise'),
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring(),
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring(),
            ChannelStatus = cms.vstring('HcalCellOff', 
                'HcalCellDead'),
            Level = cms.int32(20)
        )),
    DropChannelStatusBits = cms.vstring('HcalCellMask', 
        'HcalCellOff', 
        'HcalCellDead')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer")


process.hltCombinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    useTrackWeights = cms.bool(True),
    useCategories = cms.bool(True),
    pseudoMultiplicityMin = cms.uint32(2),
    correctVertexMass = cms.bool(True),
    categoryVariableName = cms.string('vertexCategory'),
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    charmCut = cms.double(1.5),
    trackFlip = cms.bool(False),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('any'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        normChi2Max = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5.0),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dValMin = cms.double(-99999.9)
    ),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackMultiplicityMin = cms.uint32(3),
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('any'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        normChi2Max = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5.0),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dValMin = cms.double(-99999.9)
    ),
    trackSort = cms.string('sip2dSig'),
    vertexFlip = cms.bool(False)
)


process.hltESPAK4CaloAbsoluteCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK4CaloHLT'),
    level = cms.string('L3Absolute')
)


process.hltESPAK4CaloCorrection = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPAK4CaloFastJetCorrectionESProducer', 
        'hltESPAK4CaloRelativeCorrectionESProducer', 
        'hltESPAK4CaloAbsoluteCorrectionESProducer')
)


process.hltESPAK4CaloFastJetCorrectionESProducer = cms.ESProducer("L1FastjetCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAllCalo"),
    algorithm = cms.string('AK4CaloHLT'),
    level = cms.string('L1FastJet')
)


process.hltESPAK4CaloRelativeCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK4CaloHLT'),
    level = cms.string('L2Relative')
)


process.hltESPAK4PFAbsoluteCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK4PFHLT'),
    level = cms.string('L3Absolute')
)


process.hltESPAK4PFCorrection = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPAK4PFFastJetCorrectionESProducer', 
        'hltESPAK4PFRelativeCorrectionESProducer', 
        'hltESPAK4PFAbsoluteCorrectionESProducer')
)


process.hltESPAK4PFFastJetCorrectionESProducer = cms.ESProducer("L1FastjetCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAll"),
    algorithm = cms.string('AK4PFHLT'),
    level = cms.string('L1FastJet')
)


process.hltESPAK4PFRelativeCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK4PFHLT'),
    level = cms.string('L2Relative')
)


process.hltESPAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('hltESPAnalyticalPropagator'),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPBwdAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('hltESPBwdAnalyticalPropagator'),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.hltESPBwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    SimpleMagneticField = cms.string(''),
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('hltESPBwdElectronPropagator'),
    Mass = cms.double(0.000511),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.hltESPChi2EstimatorForRefit = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2EstimatorForRefit'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(100000.0)
)


process.hltESPChi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(30.0)
)


process.hltESPChi2MeasurementEstimator16 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator16'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(16.0)
)


process.hltESPChi2MeasurementEstimator30 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator30'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(30.0)
)


process.hltESPChi2MeasurementEstimator9 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator9'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(9.0)
)


process.hltESPCloseComponentsMerger5D = cms.ESProducer("CloseComponentsMergerESProducer5D",
    ComponentName = cms.string('hltESPCloseComponentsMerger5D'),
    MaxComponents = cms.int32(12),
    DistanceMeasure = cms.string('hltESPKullbackLeiblerDistance5D')
)


process.hltESPDummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPEcalRegionCablingESProducer = cms.ESProducer("EcalRegionCablingESProducer",
    esMapping = cms.PSet(
        LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat')
    )
)


process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.hltESPElectronChi2 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPElectronChi2'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(2000.0)
)


process.hltESPElectronMaterialEffects = cms.ESProducer("GsfMaterialEffectsESProducer",
    BetheHeitlerParametrization = cms.string('BetheHeitler_cdfmom_nC6_O5.par'),
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    ComponentName = cms.string('hltESPElectronMaterialEffects'),
    MultipleScatteringUpdator = cms.string('MultipleScatteringUpdator'),
    Mass = cms.double(0.000511),
    BetheHeitlerCorrection = cms.int32(2)
)


process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useTuningForL2Speed = cms.bool(True),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useTuningForL2Speed = cms.bool(True),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.hltESPFittingSmootherIT = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPFittingSmootherIT'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.hltESPFittingSmootherRK = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPFittingSmootherRK'),
    NoInvalidHitsBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True)
)


process.hltESPFwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    SimpleMagneticField = cms.string(''),
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('hltESPFwdElectronPropagator'),
    Mass = cms.double(0.000511),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.hltESPGlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.hltESPGsfElectronFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPGsfTrajectoryFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('hltESPGsfTrajectorySmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPGsfElectronFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.hltESPGsfTrajectoryFitter = cms.ESProducer("GsfTrajectoryFitterESProducer",
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    ComponentName = cms.string('hltESPGsfTrajectoryFitter'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    GeometricalPropagator = cms.string('hltESPAnalyticalPropagator')
)


process.hltESPGsfTrajectorySmoother = cms.ESProducer("GsfTrajectorySmootherESProducer",
    ErrorRescaling = cms.double(100.0),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    ComponentName = cms.string('hltESPGsfTrajectorySmoother'),
    GeometricalPropagator = cms.string('hltESPBwdAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects')
)


process.hltESPKFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPKFTrajectoryFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('hltESPKFTrajectorySmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True)
)


process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    NoInvalidHitsBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True)
)


process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(20.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('hltESPRKFitter'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('hltESPRKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.hltESPKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    ComponentName = cms.string('hltESPKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPKFTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPKFUpdator = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('hltESPKFUpdator')
)


process.hltESPKullbackLeiblerDistance5D = cms.ESProducer("DistanceBetweenComponentsESProducer5D",
    ComponentName = cms.string('hltESPKullbackLeiblerDistance5D'),
    DistanceMeasure = cms.string('KullbackLeibler')
)


process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    minHits = cms.int32(3)
)


process.hltESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    UsePixelModuleQualityDB = cms.bool(True),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    UseStripModuleQualityDB = cms.bool(True),
    SiStripQualityLabel = cms.string(''),
    MaskBadAPVFibers = cms.bool(True),
    PixelCPE = cms.string('hltESPPixelCPEGeneric')
)


process.hltESPMeasurementTrackerReg = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltESPMeasurementTrackerReg'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    UsePixelModuleQualityDB = cms.bool(True),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    UseStripModuleQualityDB = cms.bool(True),
    SiStripQualityLabel = cms.string(''),
    MaskBadAPVFibers = cms.bool(True),
    PixelCPE = cms.string('hltESPPixelCPEGeneric')
)


process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPMuonTransientTrackingRecHitBuilder')
)


process.hltESPPixelCPEGeneric = cms.ESProducer("PixelCPEGenericESProducer",
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    useLAAlignmentOffsets = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    eff_charge_cut_highX = cms.double(1.0),
    ComponentName = cms.string('hltESPPixelCPEGeneric'),
    size_cutY = cms.double(3.0),
    size_cutX = cms.double(3.0),
    eff_charge_cut_highY = cms.double(1.0),
    useLAWidthFromDB = cms.bool(False),
    IrradiationBiasCorrection = cms.bool(False),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    eff_charge_cut_lowX = cms.double(0.0),
    TruncatePixelCharge = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    eff_charge_cut_lowY = cms.double(0.0),
    PixelErrorParametrization = cms.string('NOTcmsim'),
    DoCosmics = cms.bool(False),
    Alpha2Order = cms.bool(True)
)


process.hltESPPixelCPETemplateReco = cms.ESProducer("PixelCPETemplateRecoESProducer",
    DoLorentz = cms.bool(False),
    DoCosmics = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    ComponentName = cms.string('hltESPPixelCPETemplateReco'),
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    speed = cms.int32(-2),
    UseClusterSplitter = cms.bool(False)
)


process.hltESPPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    maxImpactParameterSig = cms.double(999999.0),
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    deltaRmin = cms.double(0.0),
    maxImpactParameter = cms.double(0.03),
    maximumDecayLength = cms.double(999999.0),
    nthTrack = cms.int32(-1)
)


process.hltESPRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    ComponentName = cms.string('hltESPRKFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    minHits = cms.int32(3)
)


process.hltESPRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPRKSmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    SimpleMagneticField = cms.string(''),
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('hltESPRungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(True)
)


process.hltESPSiStripRegionConnectivity = cms.ESProducer("SiStripRegionConnectivity",
    EtaMax = cms.untracked.double(2.5),
    PhiDivisions = cms.untracked.uint32(20),
    EtaDivisions = cms.untracked.uint32(20)
)


process.hltESPSmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagator'),
    TrackerPropagator = cms.string('PropagatorWithMaterial'),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    Epsilon = cms.double(5.0)
)


process.hltESPSmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    TrackerPropagator = cms.string('PropagatorWithMaterial'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    Epsilon = cms.double(5.0)
)


process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    Epsilon = cms.double(5.0)
)


process.hltESPSmartPropagatorOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorOpposite'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite'),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    Epsilon = cms.double(5.0)
)


process.hltESPSoftLeptonByDistance = cms.ESProducer("LeptonTaggerByDistanceESProducer",
    distance = cms.double(0.5)
)


process.hltESPSoftLeptonByPt = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('hltESPSteppingHelixPropagatorAlong'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.hltESPStraightLinePropagator = cms.ESProducer("StraightLinePropagatorESProducer",
    ComponentName = cms.string('hltESPStraightLinePropagator'),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPStripCPEfromTrackAngle = cms.ESProducer("StripCPEESProducer",
    TanDiffusionAngle = cms.double(0.01),
    UncertaintyScaling = cms.double(1.42),
    ThicknessRelativeUncertainty = cms.double(0.02),
    MaybeNoiseThreshold = cms.double(3.5),
    ComponentName = cms.string('hltESPStripCPEfromTrackAngle'),
    MinimumUncertainty = cms.double(0.01),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    NoiseThreshold = cms.double(2.3)
)


process.hltESPTTRHBWithTrackAngle = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    ComponentName = cms.string('hltESPTTRHBWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    Matcher = cms.string('StandardMatcher')
)


process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    ComponentName = cms.string('hltESPTTRHBuilderAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPETemplateReco'),
    Matcher = cms.string('StandardMatcher')
)


process.hltESPTTRHBuilderPixelOnly = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    Matcher = cms.string('StandardMatcher')
)


process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    ComponentName = cms.string('hltESPTTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    Matcher = cms.string('StandardMatcher')
)


process.hltESPTrackCounting3D1st = cms.ESProducer("TrackCountingESProducer",
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    a_dR = cms.double(-0.001053),
    min_pT = cms.double(120.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    max_pT = cms.double(500.0),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False),
    min_pT_dRcut = cms.double(0.5),
    max_pT_trackPTcut = cms.double(3.0),
    max_pT_dRcut = cms.double(0.1),
    b_dR = cms.double(0.6263),
    a_pT = cms.double(0.005263),
    maximumDecayLength = cms.double(5.0),
    nthTrack = cms.int32(1)
)


process.hltESPTrackCounting3D2nd = cms.ESProducer("TrackCountingESProducer",
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    a_dR = cms.double(-0.001053),
    min_pT = cms.double(120.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    max_pT = cms.double(500.0),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False),
    min_pT_dRcut = cms.double(0.5),
    max_pT_trackPTcut = cms.double(3.0),
    max_pT_dRcut = cms.double(0.1),
    b_dR = cms.double(0.6263),
    a_pT = cms.double(0.005263),
    maximumDecayLength = cms.double(5.0),
    nthTrack = cms.int32(2)
)


process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    trackerGeometryLabel = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
)


process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    fractionShared = cms.double(0.5),
    ValidHitBonus = cms.double(100.0),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(0.0),
    allowSharedFirstHit = cms.bool(False)
)


process.hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedSeeds'),
    fractionShared = cms.double(0.5),
    ValidHitBonus = cms.double(100.0),
    ComponentType = cms.string('TrajectoryCleanerBySharedSeeds'),
    MissingHitPenalty = cms.double(0.0),
    allowSharedFirstHit = cms.bool(True)
)


process.hltESPTrajectoryFitterRK = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    ComponentName = cms.string('hltESPTrajectoryFitterRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    minHits = cms.int32(3)
)


process.hltESPTrajectorySmootherRK = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPTrajectorySmootherRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.125),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.1),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    LatencyRecord = cms.PSet(
        record = cms.string('SiStripLatencyRcd'),
        label = cms.untracked.string('')
    ),
    BackPlaneCorrectionDeconvMode = cms.PSet(
        record = cms.string('SiStripBackPlaneCorrectionRcd'),
        label = cms.untracked.string('deconvolution')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        record = cms.string('SiStripBackPlaneCorrectionRcd'),
        label = cms.untracked.string('peak')
    )
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        record = cms.string('SiStripLatencyRcd'),
        label = cms.untracked.string('')
    ),
    LorentzAnglePeakMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('peak')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('deconvolution')
    )
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.trackerTopologyConstants = cms.ESProducer("TrackerTopologyEP",
    tob_rodStartBit = cms.uint32(5),
    tib_str_int_extStartBit = cms.uint32(10),
    tib_layerMask = cms.uint32(7),
    pxf_bladeMask = cms.uint32(63),
    appendToDataLabel = cms.string(''),
    pxb_ladderStartBit = cms.uint32(8),
    pxb_layerStartBit = cms.uint32(16),
    tec_wheelStartBit = cms.uint32(14),
    tib_str_int_extMask = cms.uint32(3),
    tec_ringStartBit = cms.uint32(5),
    tib_moduleStartBit = cms.uint32(2),
    pxf_sideMask = cms.uint32(3),
    tid_sideStartBit = cms.uint32(13),
    tid_module_fw_bwStartBit = cms.uint32(7),
    tid_ringMask = cms.uint32(3),
    tob_rod_fw_bwStartBit = cms.uint32(12),
    tec_petal_fw_bwStartBit = cms.uint32(12),
    tec_ringMask = cms.uint32(7),
    tib_strMask = cms.uint32(63),
    tec_sterMask = cms.uint32(3),
    tec_wheelMask = cms.uint32(15),
    tec_sideStartBit = cms.uint32(18),
    pxb_moduleMask = cms.uint32(63),
    pxf_panelStartBit = cms.uint32(8),
    tid_sideMask = cms.uint32(3),
    tob_moduleMask = cms.uint32(7),
    pxf_bladeStartBit = cms.uint32(10),
    tib_sterMask = cms.uint32(3),
    pxb_moduleStartBit = cms.uint32(2),
    pxf_diskStartBit = cms.uint32(16),
    tib_str_fw_bwMask = cms.uint32(3),
    tec_moduleMask = cms.uint32(7),
    tid_sterMask = cms.uint32(3),
    tob_rod_fw_bwMask = cms.uint32(3),
    tob_layerStartBit = cms.uint32(14),
    tec_petal_fw_bwMask = cms.uint32(3),
    tob_sterMask = cms.uint32(3),
    tib_strStartBit = cms.uint32(4),
    pxf_moduleStartBit = cms.uint32(2),
    tid_moduleMask = cms.uint32(31),
    tib_sterStartBit = cms.uint32(0),
    tob_sterStartBit = cms.uint32(0),
    tec_sterStartBit = cms.uint32(0),
    pxf_diskMask = cms.uint32(15),
    tob_moduleStartBit = cms.uint32(2),
    tid_wheelStartBit = cms.uint32(11),
    tob_layerMask = cms.uint32(7),
    tid_module_fw_bwMask = cms.uint32(3),
    tec_petalMask = cms.uint32(15),
    pxb_ladderMask = cms.uint32(255),
    tec_moduleStartBit = cms.uint32(2),
    tob_rodMask = cms.uint32(127),
    tec_sideMask = cms.uint32(3),
    pxf_sideStartBit = cms.uint32(23),
    pxb_layerMask = cms.uint32(15),
    tib_layerStartBit = cms.uint32(14),
    pxf_panelMask = cms.uint32(3),
    tib_moduleMask = cms.uint32(3),
    tid_ringStartBit = cms.uint32(9),
    tid_wheelMask = cms.uint32(3),
    tid_sterStartBit = cms.uint32(0),
    tid_moduleStartBit = cms.uint32(2),
    tec_petalStartBit = cms.uint32(8),
    tib_str_fw_bwStartBit = cms.uint32(12),
    pxf_moduleMask = cms.uint32(63)
)


process.CSCChannelMapperESSource = cms.ESSource("EmptyESSource",
    recordName = cms.string('CSCChannelMapperRecord'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.CSCINdexerESSource = cms.ESSource("EmptyESSource",
    recordName = cms.string('CSCIndexerRecord'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    globaltag = cms.string(myGT),
    RefreshEachRun = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('JetCorrectionsRecord'),
        tag = cms.string('JetCorrectorParametersCollection_HLT_V1_AK4Calo'),
        connect = cms.untracked.string('frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS'),
        label = cms.untracked.string('AK4CaloHLT')
    ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HLT_trk0_V1_AK4PF'),
            connect = cms.untracked.string('frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS'),
            label = cms.untracked.string('AK4PFHLT')
        )),
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        connectionRetrialPeriod = cms.untracked.int32(10),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        connectionTimeOut = cms.untracked.int32(0),
        connectionRetrialTimeOut = cms.untracked.int32(60)
    ),
    RefreshAlways = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
    RefreshOpenIOVs = cms.untracked.bool(False),
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    recordName = cms.string('EcalMappingRcd'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.hltESSBTagRecord = cms.ESSource("EmptyESSource",
    recordName = cms.string('JetTagComputerRecord'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.hltESSEcalSeverityLevel = cms.ESSource("EmptyESSource",
    recordName = cms.string('EcalSeverityLevelAlgoRcd'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.hltESSHcalSeverityLevel = cms.ESSource("EmptyESSource",
    recordName = cms.string('HcalSeverityLevelComputerRcd'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.magfield = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMagneticField.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml', 
        'Geometry/CMSCommonData/data/materials.xml'),
    rootNodeName = cms.string('cmsMagneticField:MAGF')
)


process.ALCARECOEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'keep edmTriggerResults_*_*_*', 
        'keep *_ALCARECOTkAlZMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_ALCARECOTkAlCosmicsInCollisions_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*', 
        'keep *_ALCARECOTkAlCosmicsCTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsCosmicTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsRegional_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*', 
        'keep *_ALCARECOTkAlCosmicsCTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsCosmicTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsRegional_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*', 
        'keep *_ALCARECOTkAlCosmics*0T_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*', 
        'keep *_ALCARECOTkAlCosmics*0T_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*', 
        'keep *_ALCARECOTkAlLAST0Producer_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_ALCARECOTkAlMuonIsolated_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_ALCARECOTkAlMuonIsolatedPA_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_ALCARECOTkAlJpsiMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_ALCARECOTkAlUpsilonMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_ALCARECOTkAlMinBias_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_ALCARECOTkAlBeamHalo_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_ALCARECOSiStripCalZeroBias_*_*', 
        'keep *_calZeroBiasClusters_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_ALCARECOSiStripCalMinBias_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_ecalPhiSymCorrected_phiSymEcalRecHitsEB_*', 
        'keep *_ecalPhiSymCorrected_phiSymEcalRecHitsEE_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectron*_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep *_*_*_HLT', 
        'keep recoTracks_generalTracks_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop *EcalrecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsE*_*_*', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep *EcalRecHit*_reducedEcalRecHitsES_alCaRecHitsES_*', 
        'keep *_ecalPi0Corrected_pi0EcalRecHitsEB_*', 
        'keep *_ecalPi0Corrected_pi0EcalRecHitsEE_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_pi0EcalRecHitsES_*', 
        'keep *_ecalEtaCorrected_etaEcalRecHitsEB_*', 
        'keep *_ecalEtaCorrected_etaEcalRecHitsEE_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_etaEcalRecHitsES_*', 
        'keep *_DiJProd_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_GammaJetProd_*_*', 
        'keep *_IsoProd_*_*', 
        'keep *_TkAlIsoProd_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_IsoProd_*_*', 
        'keep *_gtDigisAlCaMB_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMBspecial_*_*', 
        'keep HBHERecHitsSorted_hbherecoNoise_*_*', 
        'keep HORecHitsSorted_horecoNoise_*_*', 
        'keep HFRecHitsSorted_hfrecoNoise_*_*', 
        'keep *_hoCalibProducer_*_*', 
        'keep HOCalibVariabless_*_*_*', 
        'keep *_HcalNoiseProd_*_*', 
        'keep edmTriggerResults_*_*_HLT', 
        'keep *_ALCARECOMuAlStandAloneCosmics_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_ALCARECOMuAlGlobalCosmicsInCollisions_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_ALCARECOMuAlGlobalCosmics_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_ALCARECOMuAlCalIsolatedMu_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_ALCARECOMuAlZMuMu_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_ALCARECOMuAlOverlaps_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_ALCARECOMuAlBeamHaloOverlaps_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_ALCARECOMuAlBeamHalo_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep CSCDetIdCSCWireDigiMuonDigiCollection_*_*_*', 
        'keep CSCDetIdCSCStripDigiMuonDigiCollection_*_*_*', 
        'keep DTLayerIdDTDigiMuonDigiCollection_*_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep RPCDetIdRPCDigiMuonDigiCollection_*_*_*', 
        'keep recoMuons_muonsNoRPC_*_*', 
        'keep L1MuRegionalCands_*_RPCb_*', 
        'keep L1MuRegionalCands_*_RPCf_*', 
        'keep L1MuGMTCands_*_*_*', 
        'keep L1MuGMTReadoutCollection_*_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt4DSegmentsNoWire_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep recoMuons_muons_*_*', 
        'keep booledmValueMap_muid*_*_*', 
        'keep *_MEtoEDMConvertSiStrip_*_*', 
        'keep *_siPixelClustersForLumi_*_*', 
        'keep *_TriggerResults_*_HLT', 
        'drop *_MEtoEDMConverter_*_*' ) )
)

process.AODEventContent = cms.PSet(
    compressionLevel = cms.untracked.int32(4),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_castorreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep recoCaloClusters_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoTracks_GsfGlobalElectronTest_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'drop recoHcalNoiseRBXs_*_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *GlobalHaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep recoPhotonCores_gedPhotonCore_*_*', 
        'keep recoPhotons_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'drop *_gedPhotons_valMapPFEgammaCandToPhoton_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'drop *_pfElectronTranslator_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep recoCaloClusters_pfElectronTranslator_*_*', 
        'keep recoPreshowerClusters_pfElectronTranslator_*_*', 
        'keep recoSuperClusters_pfElectronTranslator_*_*', 
        'keep recoCaloClusters_pfPhotonTranslator_*_*', 
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*', 
        'keep recoSuperClusters_pfPhotonTranslator_*_*', 
        'keep recoPhotons_pfPhotonTranslator_*_*', 
        'keep recoPhotonCores_pfPhotonTranslator_*_*', 
        'keep recoConversions_pfPhotonTranslator_*_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'drop L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640)
)

process.AODSIMEventContent = cms.PSet(
    compressionLevel = cms.untracked.int32(4),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_castorreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep recoCaloClusters_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoTracks_GsfGlobalElectronTest_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'drop recoHcalNoiseRBXs_*_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *GlobalHaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep recoPhotonCores_gedPhotonCore_*_*', 
        'keep recoPhotons_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'drop *_gedPhotons_valMapPFEgammaCandToPhoton_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'drop *_pfElectronTranslator_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep recoCaloClusters_pfElectronTranslator_*_*', 
        'keep recoPreshowerClusters_pfElectronTranslator_*_*', 
        'keep recoSuperClusters_pfElectronTranslator_*_*', 
        'keep recoCaloClusters_pfPhotonTranslator_*_*', 
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*', 
        'keep recoSuperClusters_pfPhotonTranslator_*_*', 
        'keep recoPhotons_pfPhotonTranslator_*_*', 
        'keep recoPhotonCores_pfPhotonTranslator_*_*', 
        'keep recoConversions_pfPhotonTranslator_*_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'drop L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep PileupSummaryInfos_*_*_*'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640)
)

process.BeamSpotAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_offlineBeamSpot_*_*')
)

process.BeamSpotFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_offlineBeamSpot_*_*')
)

process.BeamSpotRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_offlineBeamSpot_*_*')
)

process.CommonEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_logErrorHarvester_*_*')
)

process.DATAMIXEREventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep CaloTowersSorted_calotoweroptmaker_*_*', 
        'keep CSCDetIdCSCALCTDigiMuonDigiCollection_muonCSCDigis_MuonCSCALCTDigi_*', 
        'keep CSCDetIdCSCCLCTDigiMuonDigiCollection_muonCSCDigis_MuonCSCCLCTDigi_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_muonCSCDigis_MuonCSCComparatorDigi_*', 
        'keep CSCDetIdCSCCorrelatedLCTDigiMuonDigiCollection_csctfDigis_*_*', 
        'keep CSCDetIdCSCCorrelatedLCTDigiMuonDigiCollection_muonCSCDigis_MuonCSCCorrelatedLCTDigi_*', 
        'keep CSCDetIdCSCRPCDigiMuonDigiCollection_muonCSCDigis_MuonCSCRPCDigi_*', 
        'keep CSCDetIdCSCStripDigiMuonDigiCollection_muonCSCDigis_MuonCSCStripDigi_*', 
        'keep CSCDetIdCSCWireDigiMuonDigiCollection_muonCSCDigis_MuonCSCWireDigi_*', 
        'keep DTLayerIdDTDigiMuonDigiCollection_muonDTDigis_*_*', 
        'keep PixelDigiedmDetSetVector_siPixelDigis_*_*', 
        'keep SiStripDigiedmDetSetVector_siStripDigis_*_*', 
        'keep RPCDetIdRPCDigiMuonDigiCollection_muonRPCDigis_*_*', 
        'keep HBHEDataFramesSorted_hcalDigis_*_*', 
        'keep HFDataFramesSorted_hcalDigis_*_*', 
        'keep HODataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep CastorDataFramesSorted_castorDigis_*_*', 
        'keep EBDigiCollection_ecalDigis_*_*', 
        'keep EEDigiCollection_ecalDigis_*_*', 
        'keep ESDigiCollection_ecalPreshowerDigis_*_*')
)

process.DQMEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_MEtoEDMConverter_*_*')
)

process.DigiToRawFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*')
)

process.EITopPAGEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*')
)

process.EvtScalersAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*')
)

process.EvtScalersRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*')
)

process.FEVTDEBUGEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak7GenJets_*_*', 
        'keep *_iterativeCone5GenJets_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep *_simCscTriggerPrimitiveDigis_*_*', 
        'keep *_simDtTriggerPrimitiveDigis_*_*', 
        'keep *_simRpcTriggerDigis_*_*', 
        'keep *_simRctDigis_*_*', 
        'keep *_simCsctfDigis_*_*', 
        'keep *_simCsctfTrackDigis_*_*', 
        'keep *_simDttfDigis_*_*', 
        'keep *_simGctDigis_*_*', 
        'keep *_simGmtDigis_*_*', 
        'keep *_simGtDigis_*_*', 
        'keep *_cscTriggerPrimitiveDigis_*_*', 
        'keep *_dtTriggerPrimitiveDigis_*_*', 
        'keep *_rpcTriggerDigis_*_*', 
        'keep *_rctDigis_*_*', 
        'keep *_csctfDigis_*_*', 
        'keep *_csctfTrackDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gctDigis_*_*', 
        'keep *_gmtDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_gtEvmDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep *_simSiPixelDigis_*_*', 
        'keep *_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_trackingParticleRecoTrackAsssociation_*_*', 
        'keep *_assoc2secStepTk_*_*', 
        'keep *_assoc2thStepTk_*_*', 
        'keep *_assoc2GsfTracks_*_*', 
        'keep *_assocOutInConversionTracks_*_*', 
        'keep *_assocInOutConversionTracks_*_*', 
        'keep *_simMuonCSCDigis_*_*', 
        'keep *_simMuonDTDigis_*_*', 
        'keep *_simMuonRPCDigis_*_*', 
        'keep *_simEcalDigis_*_*', 
        'keep *_simEcalPreshowerDigis_*_*', 
        'keep *_simEcalTriggerPrimitiveDigis_*_*', 
        'keep *_simHcalDigis_*_*', 
        'keep ZDCDataFramesSorted_simHcalUnsuppressedDigis_*_*', 
        'drop ZDCDataFramesSorted_mix_simHcalUnsuppressedDigis*_*', 
        'keep *_simHcalTriggerPrimitiveDigis_*_*' ) )
)

process.FEVTDEBUGHLTEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(1048576),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak7GenJets_*_*', 
        'keep *_iterativeCone5GenJets_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep *_simCscTriggerPrimitiveDigis_*_*', 
        'keep *_simDtTriggerPrimitiveDigis_*_*', 
        'keep *_simRpcTriggerDigis_*_*', 
        'keep *_simRctDigis_*_*', 
        'keep *_simCsctfDigis_*_*', 
        'keep *_simCsctfTrackDigis_*_*', 
        'keep *_simDttfDigis_*_*', 
        'keep *_simGctDigis_*_*', 
        'keep *_simGmtDigis_*_*', 
        'keep *_simGtDigis_*_*', 
        'keep *_cscTriggerPrimitiveDigis_*_*', 
        'keep *_dtTriggerPrimitiveDigis_*_*', 
        'keep *_rpcTriggerDigis_*_*', 
        'keep *_rctDigis_*_*', 
        'keep *_csctfDigis_*_*', 
        'keep *_csctfTrackDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gctDigis_*_*', 
        'keep *_gmtDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_gtEvmDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep *_simSiPixelDigis_*_*', 
        'keep *_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_trackingParticleRecoTrackAsssociation_*_*', 
        'keep *_assoc2secStepTk_*_*', 
        'keep *_assoc2thStepTk_*_*', 
        'keep *_assoc2GsfTracks_*_*', 
        'keep *_assocOutInConversionTracks_*_*', 
        'keep *_assocInOutConversionTracks_*_*', 
        'keep *_simMuonCSCDigis_*_*', 
        'keep *_simMuonDTDigis_*_*', 
        'keep *_simMuonRPCDigis_*_*', 
        'keep *_simEcalDigis_*_*', 
        'keep *_simEcalPreshowerDigis_*_*', 
        'keep *_simEcalTriggerPrimitiveDigis_*_*', 
        'keep *_simHcalDigis_*_*', 
        'keep ZDCDataFramesSorted_simHcalUnsuppressedDigis_*_*', 
        'drop ZDCDataFramesSorted_mix_simHcalUnsuppressedDigis*_*', 
        'keep *_simHcalTriggerPrimitiveDigis_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBUncalibrator_*_*', 
        'keep *_hltAlCaEtaEEUncalibrator_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPhiSymUncalibrator_*_*', 
        'keep *_hltAlCaPi0EBUncalibrator_*_*', 
        'keep *_hltAlCaPi0EEUncalibrator_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltEle32WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1extraParticlesCentral_*_*', 
        'keep *_hltL1extraParticlesNonIsolated_*_*', 
        'keep *_hltL1extraParticlesTau_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidatesNoVtx_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltMetForHf_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4JetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTCands_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) )
)

process.FEVTEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*' ) )
)

process.FEVTHLTALLEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep *_*_*_HLT' ) )
)

process.FEVTSIMEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak7GenJets_*_*', 
        'keep *_iterativeCone5GenJets_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*' ) )
)

process.GENRAWEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_logErrorHarvester_*_*')
)

process.GeneratorInterfaceAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.GeneratorInterfaceLHE = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep *_externalLHEProducer_LHEScriptOutput_*')
)

process.GeneratorInterfaceRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.GeneratorInterfaceRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.HLTConfigVersion = cms.PSet(
    tableName = cms.string('/users/algomez/HTBoostedTriggers/V11')
)

process.HLTDEBUGEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'keep *_logErrorHarvester_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBUncalibrator_*_*', 
        'keep *_hltAlCaEtaEEUncalibrator_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPhiSymUncalibrator_*_*', 
        'keep *_hltAlCaPi0EBUncalibrator_*_*', 
        'keep *_hltAlCaPi0EEUncalibrator_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltEle32WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1extraParticlesCentral_*_*', 
        'keep *_hltL1extraParticlesNonIsolated_*_*', 
        'keep *_hltL1extraParticlesTau_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidatesNoVtx_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltMetForHf_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4JetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTCands_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) )
)

process.HLTDebugFEVT = cms.PSet(
    outputCommands = cms.vstring( ('drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBUncalibrator_*_*', 
        'keep *_hltAlCaEtaEEUncalibrator_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPhiSymUncalibrator_*_*', 
        'keep *_hltAlCaPi0EBUncalibrator_*_*', 
        'keep *_hltAlCaPi0EEUncalibrator_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltEle32WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1extraParticlesCentral_*_*', 
        'keep *_hltL1extraParticlesNonIsolated_*_*', 
        'keep *_hltL1extraParticlesTau_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidatesNoVtx_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltMetForHf_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4JetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTCands_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) )
)

process.HLTDebugRAW = cms.PSet(
    outputCommands = cms.vstring( ('drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBUncalibrator_*_*', 
        'keep *_hltAlCaEtaEEUncalibrator_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPhiSymUncalibrator_*_*', 
        'keep *_hltAlCaPi0EBUncalibrator_*_*', 
        'keep *_hltAlCaPi0EEUncalibrator_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltEle32WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1extraParticlesCentral_*_*', 
        'keep *_hltL1extraParticlesNonIsolated_*_*', 
        'keep *_hltL1extraParticlesTau_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidatesNoVtx_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltMetForHf_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4JetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTCands_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) )
)

process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    maxCand = cms.int32(4),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    maxCand = cms.int32(2),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.3),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3)
)

process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    maxCand = cms.int32(2),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter1ESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.2),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3)
)

process.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    maxCand = cms.int32(2),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2HighPtTkMuPSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter2HighPtTkMuESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.3),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    maxConsecLostHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5)
)

process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    maxCand = cms.int32(2),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter2ESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.3),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3)
)

process.HLTIter3PSetTrajectoryBuilderIT = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    maxCand = cms.int32(1),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter3PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter3ESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTIter3PSetTrajectoryFilterIT = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.3),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(0),
    maxNumberOfHits = cms.int32(100),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3)
)

process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    maxCand = cms.int32(1),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter4PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter4ESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    minNrOfHitsForRebuild = cms.untracked.int32(4),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.3),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(0),
    maxNumberOfHits = cms.int32(100),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(6)
)

process.HLTPSetCkf3HitTrajectoryBuilder = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    maxCand = cms.int32(5),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkf3HitTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTPSetCkf3HitTrajectoryFilter = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.9),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(-1),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3)
)

process.HLTPSetCkfTrajectoryBuilder = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    maxCand = cms.int32(5),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTPSetCkfTrajectoryFilter = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.9),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(-1),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5)
)

process.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    maxCand = cms.int32(1),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiEffTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(1.0),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(9),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5)
)

process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    maxCand = cms.int32(1),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(10.0),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(8),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5)
)

process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    maxCand = cms.int32(5),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(False),
    useSeedLayer = cms.bool(False),
    deltaEta = cms.double(-1.0),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    rescaleErrorIfFail = cms.double(1.0),
    deltaPhi = cms.double(-1.0),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTPSetMuonCkfTrajectoryBuilderSeedHit = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    maxCand = cms.int32(5),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(False),
    useSeedLayer = cms.bool(True),
    deltaEta = cms.double(-1.0),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    rescaleErrorIfFail = cms.double(1.0),
    deltaPhi = cms.double(-1.0),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
    minimumNumberOfHits = cms.int32(5),
    minPt = cms.double(0.9),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(-1),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    chargeSignificance = cms.double(-1.0)
)

process.HLTPSetPvClusterComparer = cms.PSet(
    track_chi2_max = cms.double(9999999.0),
    track_pt_max = cms.double(10.0),
    track_pt_min = cms.double(2.5),
    track_prob_min = cms.double(-1.0)
)

process.HLTPSetPvClusterComparerForBTag = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(0.1),
    track_prob_min = cms.double(-1.0)
)

process.HLTPSetPvClusterComparerForIT = cms.PSet(
    track_chi2_max = cms.double(9999999.0),
    track_pt_max = cms.double(10.0),
    track_pt_min = cms.double(2.5),
    track_prob_min = cms.double(-1.0)
)

process.HLTPSetTrajectoryBuilderForElectrons = cms.PSet(
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    maxCand = cms.int32(5),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    intermediateCleaning = cms.bool(False),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    lostHitPenalty = cms.double(90.0)
)

process.HLTPSetTrajectoryBuilderIT = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    maxCand = cms.int32(2),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTPSetTrajectoryBuilderL3 = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    maxCand = cms.int32(5),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterL3')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTPSetTrajectoryFilterForElectrons = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(2.0),
    minHitsMinPt = cms.int32(-1),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(-1),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5)
)

process.HLTPSetTrajectoryFilterIT = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.3),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3)
)

process.HLTPSetTrajectoryFilterL3 = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(0.5),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(1000000000),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5)
)

process.HLTPSetbJetRegionalTrajectoryBuilder = cms.PSet(
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    maxCand = cms.int32(1),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetbJetRegionalTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)

process.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet(
    chargeSignificance = cms.double(-1.0),
    minPt = cms.double(1.0),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(8),
    maxConsecLostHits = cms.int32(1),
    nSigmaMinPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5)
)

process.HLTSeedFromConsecutiveHitsCreator = cms.PSet(
    SimpleMagneticField = cms.string('ParabolicMf'),
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    SeedMomentumForBOFF = cms.double(5.0),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0)
)

process.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTriggerAOD = cms.PSet(
    outputCommands = cms.vstring('drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'drop L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.HLTriggerRAW = cms.PSet(
    outputCommands = cms.vstring('drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.HLTriggerRECO = cms.PSet(
    outputCommands = cms.vstring('drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.IOMCRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_randomEngineStateProducer_*_*')
)

process.L1TriggerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiSummary_lumiProducer_*_*')
)

process.L1TriggerFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simCscTriggerPrimitiveDigis_*_*', 
        'keep *_simDtTriggerPrimitiveDigis_*_*', 
        'keep *_simRpcTriggerDigis_*_*', 
        'keep *_simRctDigis_*_*', 
        'keep *_simCsctfDigis_*_*', 
        'keep *_simCsctfTrackDigis_*_*', 
        'keep *_simDttfDigis_*_*', 
        'keep *_simGctDigis_*_*', 
        'keep *_simGmtDigis_*_*', 
        'keep *_simGtDigis_*_*', 
        'keep *_cscTriggerPrimitiveDigis_*_*', 
        'keep *_dtTriggerPrimitiveDigis_*_*', 
        'keep *_rpcTriggerDigis_*_*', 
        'keep *_rctDigis_*_*', 
        'keep *_csctfDigis_*_*', 
        'keep *_csctfTrackDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gctDigis_*_*', 
        'keep *_gmtDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_gtEvmDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*')
)

process.L1TriggerRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*')
)

process.L1TriggerRAWDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*')
)

process.L1TriggerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*')
)

process.LHEEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep *_externalLHEProducer_LHEScriptOutput_*')
)

process.MEtoEDMConverterAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.MEtoEDMConverterFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_MEtoEDMConverter_*_*')
)

process.MEtoEDMConverterRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.MINIAODEventContent = cms.PSet(
    compressionLevel = cms.untracked.int32(4),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep *_slimmedPhotons*_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons*_*_*', 
        'keep *_slimmedTaus*_*_*', 
        'keep *_slimmedJets*_*_*', 
        'keep *_slimmedMETs*_*_*', 
        'keep *_slimmedSecondaryVertices*_*_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep double_fixedGridRho*__*', 
        'keep *_selectedPatTrigger_*_PAT', 
        'keep patPackedTriggerPrescales_patTrigger__PAT', 
        'keep *_l1extraParticles_*_HLT', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_HLT', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_PAT', 
        'keep patPackedCandidates_lostTracks_*_PAT', 
        'keep HcalNoiseSummary_hcalnoise__*'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640)
)

process.MINIAODSIMEventContent = cms.PSet(
    compressionLevel = cms.untracked.int32(4),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep *_slimmedPhotons*_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons*_*_*', 
        'keep *_slimmedTaus*_*_*', 
        'keep *_slimmedJets*_*_*', 
        'keep *_slimmedMETs*_*_*', 
        'keep *_slimmedSecondaryVertices*_*_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep double_fixedGridRho*__*', 
        'keep *_selectedPatTrigger_*_PAT', 
        'keep patPackedTriggerPrescales_patTrigger__PAT', 
        'keep *_l1extraParticles_*_HLT', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_HLT', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_PAT', 
        'keep patPackedCandidates_lostTracks_*_PAT', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep *_slimmedGenJets_*_*', 
        'keep *_packedGenParticles_*_*', 
        'keep recoGenParticles_prunedGenParticles_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep GenRunInfoProduct_*_*_*', 
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640)
)

process.MIXINGMODULEEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_cfWriter_*_*')
)

process.MicroEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_slimmedPhotons*_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons*_*_*', 
        'keep *_slimmedTaus*_*_*', 
        'keep *_slimmedJets*_*_*', 
        'keep *_slimmedMETs*_*_*', 
        'keep *_slimmedSecondaryVertices*_*_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep double_fixedGridRho*__*', 
        'keep *_selectedPatTrigger_*_PAT', 
        'keep patPackedTriggerPrescales_patTrigger__PAT', 
        'keep *_l1extraParticles_*_HLT', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_HLT', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_PAT', 
        'keep patPackedCandidates_lostTracks_*_PAT', 
        'keep HcalNoiseSummary_hcalnoise__*')
)

process.MicroEventContentMC = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_slimmedPhotons*_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons*_*_*', 
        'keep *_slimmedTaus*_*_*', 
        'keep *_slimmedJets*_*_*', 
        'keep *_slimmedMETs*_*_*', 
        'keep *_slimmedSecondaryVertices*_*_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep double_fixedGridRho*__*', 
        'keep *_selectedPatTrigger_*_PAT', 
        'keep patPackedTriggerPrescales_patTrigger__PAT', 
        'keep *_l1extraParticles_*_HLT', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_HLT', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_PAT', 
        'keep patPackedCandidates_lostTracks_*_PAT', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep *_slimmedGenJets_*_*', 
        'keep *_packedGenParticles_*_*', 
        'keep recoGenParticles_prunedGenParticles_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep GenRunInfoProduct_*_*_*', 
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*')
)

process.OutALCARECODtCalib = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECODtCalib')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt4DSegmentsNoWire_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep recoMuons_muons_*_*', 
        'keep booledmValueMap_muid*_*_*')
)

process.OutALCARECODtCalibCosmics = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECODtCalibCosmics')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt4DSegmentsNoWire_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muons_*_*', 
        'keep booledmValueMap_muid*_*_*')
)

process.OutALCARECODtCalibCosmics_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECODtCalibCosmics')
    ),
    outputCommands = cms.untracked.vstring('keep *_dt4DSegments_*_*', 
        'keep *_dt4DSegmentsNoWire_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muons_*_*', 
        'keep booledmValueMap_muid*_*_*')
)

process.OutALCARECODtCalibHI = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECODtCalibHI')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt4DSegmentsNoWire_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muons_*_*', 
        'keep booledmValueMap_muid*_*_*', 
        'keep *_hiSelectedVertex_*_*')
)

process.OutALCARECODtCalibHI_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECODtCalibHI')
    ),
    outputCommands = cms.untracked.vstring('keep *_dt4DSegments_*_*', 
        'keep *_dt4DSegmentsNoWire_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muons_*_*', 
        'keep booledmValueMap_muid*_*_*', 
        'keep *_hiSelectedVertex_*_*')
)

process.OutALCARECODtCalib_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECODtCalib')
    ),
    outputCommands = cms.untracked.vstring('keep *_dt4DSegments_*_*', 
        'keep *_dt4DSegmentsNoWire_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep recoMuons_muons_*_*', 
        'keep booledmValueMap_muid*_*_*')
)

process.OutALCARECOEcalCalElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectron*_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep *_*_*_HLT', 
        'keep recoTracks_generalTracks_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop *EcalrecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsE*_*_*', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep *EcalRecHit*_reducedEcalRecHitsES_alCaRecHitsES_*')
)

process.OutALCARECOEcalCalElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron')
    ),
    outputCommands = cms.untracked.vstring('keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectron*_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep *_*_*_HLT', 
        'keep recoTracks_generalTracks_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop *EcalrecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsE*_*_*', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep *EcalRecHit*_reducedEcalRecHitsES_alCaRecHitsES_*')
)

process.OutALCARECOEcalCalEtaCalib = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalEtaCalib')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ecalEtaCorrected_etaEcalRecHitsEB_*', 
        'keep *_ecalEtaCorrected_etaEcalRecHitsEE_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_etaEcalRecHitsES_*')
)

process.OutALCARECOEcalCalEtaCalib_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalEtaCalib')
    ),
    outputCommands = cms.untracked.vstring('keep *_ecalEtaCorrected_etaEcalRecHitsEB_*', 
        'keep *_ecalEtaCorrected_etaEcalRecHitsEE_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_etaEcalRecHitsES_*')
)

process.OutALCARECOEcalCalPhiSym = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalPhiSym')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ecalPhiSymCorrected_phiSymEcalRecHitsEB_*', 
        'keep *_ecalPhiSymCorrected_phiSymEcalRecHitsEE_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*')
)

process.OutALCARECOEcalCalPhiSym_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalPhiSym')
    ),
    outputCommands = cms.untracked.vstring('keep *_ecalPhiSymCorrected_phiSymEcalRecHitsEB_*', 
        'keep *_ecalPhiSymCorrected_phiSymEcalRecHitsEE_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*')
)

process.OutALCARECOEcalCalPi0Calib = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalPi0Calib')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ecalPi0Corrected_pi0EcalRecHitsEB_*', 
        'keep *_ecalPi0Corrected_pi0EcalRecHitsEE_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_pi0EcalRecHitsES_*')
)

process.OutALCARECOEcalCalPi0Calib_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalPi0Calib')
    ),
    outputCommands = cms.untracked.vstring('keep *_ecalPi0Corrected_pi0EcalRecHitsEB_*', 
        'keep *_ecalPi0Corrected_pi0EcalRecHitsEE_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_pi0EcalRecHitsES_*')
)

process.OutALCARECOHcalCalDijets = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalDijets')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_DiJProd_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.OutALCARECOHcalCalDijets_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalDijets')
    ),
    outputCommands = cms.untracked.vstring('keep *_DiJProd_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.OutALCARECOHcalCalGammaJet = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalGammaJet')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_GammaJetProd_*_*')
)

process.OutALCARECOHcalCalGammaJet_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalGammaJet')
    ),
    outputCommands = cms.untracked.vstring('keep *_GammaJetProd_*_*')
)

process.OutALCARECOHcalCalHO = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalHO')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hoCalibProducer_*_*')
)

process.OutALCARECOHcalCalHOCosmics = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalHOCosmics')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep HOCalibVariabless_*_*_*')
)

process.OutALCARECOHcalCalHOCosmics_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalHOCosmics')
    ),
    outputCommands = cms.untracked.vstring('keep HOCalibVariabless_*_*_*')
)

process.OutALCARECOHcalCalHO_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalHO')
    ),
    outputCommands = cms.untracked.vstring('keep *_hoCalibProducer_*_*')
)

process.OutALCARECOHcalCalIsoTrk = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalIsoTrk')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_IsoProd_*_*', 
        'keep *_TkAlIsoProd_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.OutALCARECOHcalCalIsoTrkNoHLT = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalIsoTrkNoHLT')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_IsoProd_*_*')
)

process.OutALCARECOHcalCalIsoTrkNoHLT_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalIsoTrkNoHLT')
    ),
    outputCommands = cms.untracked.vstring('keep *_IsoProd_*_*')
)

process.OutALCARECOHcalCalIsoTrk_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalIsoTrk')
    ),
    outputCommands = cms.untracked.vstring('keep *_IsoProd_*_*', 
        'keep *_TkAlIsoProd_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.OutALCARECOHcalCalMinBias = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalMinBias')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_gtDigisAlCaMB_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMBspecial_*_*', 
        'keep HBHERecHitsSorted_hbherecoNoise_*_*', 
        'keep HORecHitsSorted_horecoNoise_*_*', 
        'keep HFRecHitsSorted_hfrecoNoise_*_*')
)

process.OutALCARECOHcalCalMinBiasHI = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalMinBias')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_gtDigisAlCaMB_*_*', 
        'keep HBHERecHitsSorted_hbhereco_*_*', 
        'keep HORecHitsSorted_horeco_*_*', 
        'keep HFRecHitsSorted_hfreco_*_*', 
        'keep HFRecHitsSorted_hfrecoMBspecial_*_*', 
        'keep HBHERecHitsSorted_hbherecoNoise_*_*', 
        'keep HORecHitsSorted_horecoNoise_*_*', 
        'keep HFRecHitsSorted_hfrecoNoise_*_*')
)

process.OutALCARECOHcalCalMinBiasHI_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalMinBias')
    ),
    outputCommands = cms.untracked.vstring('keep *_gtDigisAlCaMB_*_*', 
        'keep HBHERecHitsSorted_hbhereco_*_*', 
        'keep HORecHitsSorted_horeco_*_*', 
        'keep HFRecHitsSorted_hfreco_*_*', 
        'keep HFRecHitsSorted_hfrecoMBspecial_*_*', 
        'keep HBHERecHitsSorted_hbherecoNoise_*_*', 
        'keep HORecHitsSorted_horecoNoise_*_*', 
        'keep HFRecHitsSorted_hfrecoNoise_*_*')
)

process.OutALCARECOHcalCalMinBias_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalMinBias')
    ),
    outputCommands = cms.untracked.vstring('keep *_gtDigisAlCaMB_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMBspecial_*_*', 
        'keep HBHERecHitsSorted_hbherecoNoise_*_*', 
        'keep HORecHitsSorted_horecoNoise_*_*', 
        'keep HFRecHitsSorted_hfrecoNoise_*_*')
)

process.OutALCARECOHcalCalNoise = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalNoise')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_HcalNoiseProd_*_*', 
        'keep edmTriggerResults_*_*_HLT')
)

process.OutALCARECOHcalCalNoise_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalNoise')
    ),
    outputCommands = cms.untracked.vstring('keep *_HcalNoiseProd_*_*', 
        'keep edmTriggerResults_*_*_HLT')
)

process.OutALCARECOLumiPixels = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOLumiPixels')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_siPixelClustersForLumi_*_*', 
        'keep *_TriggerResults_*_HLT')
)

process.OutALCARECOLumiPixels_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOLumiPixels')
    ),
    outputCommands = cms.untracked.vstring('keep *_siPixelClustersForLumi_*_*', 
        'keep *_TriggerResults_*_HLT')
)

process.OutALCARECOMuAlBeamHalo = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlBeamHalo')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOMuAlBeamHalo_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlBeamHaloOverlaps = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlBeamHaloOverlaps')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOMuAlBeamHaloOverlaps_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlBeamHaloOverlaps_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlBeamHaloOverlaps')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOMuAlBeamHaloOverlaps_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlBeamHalo_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlBeamHalo')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOMuAlBeamHalo_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlCalIsolatedMu = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlCalIsolatedMu')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOMuAlCalIsolatedMu_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlCalIsolatedMu_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlCalIsolatedMu')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOMuAlCalIsolatedMu_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlGlobalCosmics = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlGlobalCosmics')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOMuAlGlobalCosmics_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlGlobalCosmicsInCollisions = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlGlobalCosmicsInCollisions')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOMuAlGlobalCosmicsInCollisions_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlGlobalCosmicsInCollisions_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlGlobalCosmicsInCollisions')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOMuAlGlobalCosmicsInCollisions_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlGlobalCosmics_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlGlobalCosmics')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOMuAlGlobalCosmics_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlOverlaps = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlOverlaps')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOMuAlOverlaps_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlOverlaps_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlOverlaps')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOMuAlOverlaps_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlStandAloneCosmics = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlStandAloneCosmics')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOMuAlStandAloneCosmics_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlStandAloneCosmics_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlStandAloneCosmics')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOMuAlStandAloneCosmics_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlZMuMu = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlZMuMu')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOMuAlZMuMu_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOMuAlZMuMu_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlZMuMu')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOMuAlZMuMu_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOPromptCalibProd = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOPromptCalibProd')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_alcaBeamSpotProducer_*_*', 
        'keep *_MEtoEDMConvertSiStrip_*_*')
)

process.OutALCARECOPromptCalibProdSiStrip = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOPromptCalibProdSiStrip')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_MEtoEDMConvertSiStrip_*_*')
)

process.OutALCARECOPromptCalibProdSiStripGains = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOPromptCalibProdSiStripGains')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_alcaBeamSpotProducer_*_*', 
        'keep *_MEtoEDMConvertSiStripGains_*_*')
)

process.OutALCARECOPromptCalibProdSiStripGains_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOPromptCalibProdSiStripGains')
    ),
    outputCommands = cms.untracked.vstring('keep *_alcaBeamSpotProducer_*_*', 
        'keep *_MEtoEDMConvertSiStripGains_*_*')
)

process.OutALCARECOPromptCalibProdSiStrip_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOPromptCalibProdSiStrip')
    ),
    outputCommands = cms.untracked.vstring('keep *_MEtoEDMConvertSiStrip_*_*')
)

process.OutALCARECOPromptCalibProd_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOPromptCalibProd')
    ),
    outputCommands = cms.untracked.vstring('keep *_alcaBeamSpotProducer_*_*', 
        'keep *_MEtoEDMConvertSiStrip_*_*')
)

process.OutALCARECORpcCalHLT = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECORpcCalHLT')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_muonDTDigis_*_*', 
        'keep CSCDetIdCSCWireDigiMuonDigiCollection_*_*_*', 
        'keep CSCDetIdCSCStripDigiMuonDigiCollection_*_*_*', 
        'keep DTLayerIdDTDigiMuonDigiCollection_*_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep RPCDetIdRPCDigiMuonDigiCollection_*_*_*', 
        'keep recoMuons_muonsNoRPC_*_*', 
        'keep L1MuRegionalCands_*_RPCb_*', 
        'keep L1MuRegionalCands_*_RPCf_*', 
        'keep L1MuGMTCands_*_*_*', 
        'keep L1MuGMTReadoutCollection_*_*_*')
)

process.OutALCARECORpcCalHLT_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECORpcCalHLT')
    ),
    outputCommands = cms.untracked.vstring('keep *_muonDTDigis_*_*', 
        'keep CSCDetIdCSCWireDigiMuonDigiCollection_*_*_*', 
        'keep CSCDetIdCSCStripDigiMuonDigiCollection_*_*_*', 
        'keep DTLayerIdDTDigiMuonDigiCollection_*_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep RPCDetIdRPCDigiMuonDigiCollection_*_*_*', 
        'keep recoMuons_muonsNoRPC_*_*', 
        'keep L1MuRegionalCands_*_RPCb_*', 
        'keep L1MuRegionalCands_*_RPCf_*', 
        'keep L1MuGMTCands_*_*_*', 
        'keep L1MuGMTReadoutCollection_*_*_*')
)

process.OutALCARECOSiPixelLorentzAngle = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiPixelLorentzAngle')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_globalMuons_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_siPixelClusters_*_*', 
        'drop *_*_*_HLT')
)

process.OutALCARECOSiPixelLorentzAngle_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiPixelLorentzAngle')
    ),
    outputCommands = cms.untracked.vstring('keep *_globalMuons_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_siPixelClusters_*_*', 
        'drop *_*_*_HLT')
)

process.OutALCARECOSiStripCalMinBias = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripCalMinBias')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOSiStripCalMinBias_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*')
)

process.OutALCARECOSiStripCalMinBias_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripCalMinBias')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOSiStripCalMinBias_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*')
)

process.OutALCARECOSiStripCalZeroBias = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripCalZeroBias')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOSiStripCalZeroBias_*_*', 
        'keep *_calZeroBiasClusters_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep *_TriggerResults_*_*')
)

process.OutALCARECOSiStripCalZeroBias_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripCalZeroBias')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOSiStripCalZeroBias_*_*', 
        'keep *_calZeroBiasClusters_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep *_TriggerResults_*_*')
)

process.OutALCARECOSiStripPCLHistos = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripPCLHistos')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_MEtoEDMConvertSiStrip_*_*')
)

process.OutALCARECOSiStripPCLHistos_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripPCLHistos')
    ),
    outputCommands = cms.untracked.vstring('keep *_MEtoEDMConvertSiStrip_*_*')
)

process.OutALCARECOTkAlBeamHalo = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlBeamHalo')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlBeamHalo_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOTkAlBeamHalo_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlBeamHalo')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlBeamHalo_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOTkAlCosmics = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsCTF', 
            'pathALCARECOTkAlCosmicsCosmicTF', 
            'pathALCARECOTkAlCosmicsRegional')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlCosmicsCTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsCosmicTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsRegional_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlCosmics0T = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsCTF0T', 
            'pathALCARECOTkAlCosmicsCosmicTF0T', 
            'pathALCARECOTkAlCosmicsRegional0T')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlCosmics*0T_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlCosmics0THLT = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsCTF0THLT', 
            'pathALCARECOTkAlCosmicsCosmicTF0THLT', 
            'pathALCARECOTkAlCosmicsRegional0THLT')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlCosmics*0T_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlCosmics0THLT_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsCTF0THLT', 
            'pathALCARECOTkAlCosmicsCosmicTF0THLT', 
            'pathALCARECOTkAlCosmicsRegional0THLT')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlCosmics*0T_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlCosmics0T_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsCTF0T', 
            'pathALCARECOTkAlCosmicsCosmicTF0T', 
            'pathALCARECOTkAlCosmicsRegional0T')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlCosmics*0T_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlCosmicsHLT = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsCTFHLT', 
            'pathALCARECOTkAlCosmicsCosmicTFHLT', 
            'pathALCARECOTkAlCosmicsRegionalHLT')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlCosmicsCTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsCosmicTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsRegional_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlCosmicsHLT_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsCTFHLT', 
            'pathALCARECOTkAlCosmicsCosmicTFHLT', 
            'pathALCARECOTkAlCosmicsRegionalHLT')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlCosmicsCTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsCosmicTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsRegional_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlCosmicsInCollisions = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsInCollisions')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlCosmicsInCollisions_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlCosmicsInCollisions_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsInCollisions')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlCosmicsInCollisions_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlCosmics_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsCTF', 
            'pathALCARECOTkAlCosmicsCosmicTF', 
            'pathALCARECOTkAlCosmicsRegional')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlCosmicsCTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsCosmicTF_*_*', 
        'keep *_ALCARECOTkAlCosmicsRegional_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep Si*Cluster*_si*Clusters_*_*', 
        'keep recoMuons_muons1Leg_*_*')
)

process.OutALCARECOTkAlJpsiMuMu = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlJpsiMuMu')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlJpsiMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.OutALCARECOTkAlJpsiMuMu_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlJpsiMuMu')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlJpsiMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.OutALCARECOTkAlLAS = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlLAS')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlLAST0Producer_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOTkAlLAS_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlLAS')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlLAST0Producer_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.OutALCARECOTkAlMinBias = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMinBias')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlMinBias_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_offlineBeamSpot_*_*')
)

process.OutALCARECOTkAlMinBiasHI = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMinBiasHI')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlMinBiasHI_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_hiSelectedVertex_*_*', 
        'keep *_offlineBeamSpot_*_*')
)

process.OutALCARECOTkAlMinBiasHI_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMinBiasHI')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlMinBiasHI_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_hiSelectedVertex_*_*', 
        'keep *_offlineBeamSpot_*_*')
)

process.OutALCARECOTkAlMinBias_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMinBias')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlMinBias_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_offlineBeamSpot_*_*')
)

process.OutALCARECOTkAlMuonIsolated = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMuonIsolated')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlMuonIsolated_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.OutALCARECOTkAlMuonIsolatedPA = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMuonIsolatedPA')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlMuonIsolatedPA_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.OutALCARECOTkAlMuonIsolatedPA_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMuonIsolatedPA')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlMuonIsolatedPA_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.OutALCARECOTkAlMuonIsolated_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMuonIsolated')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlMuonIsolated_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.OutALCARECOTkAlUpsilonMuMu = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlUpsilonMuMu')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlUpsilonMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.OutALCARECOTkAlUpsilonMuMu_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlUpsilonMuMu')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlUpsilonMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.OutALCARECOTkAlZMuMu = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlZMuMu')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlZMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.OutALCARECOTkAlZMuMu_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlZMuMu')
    ),
    outputCommands = cms.untracked.vstring('keep *_ALCARECOTkAlZMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

process.PREMIXEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep RPCDetIdRPCDigiMuonDigiCollection_simMuonRPCDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*')
)

process.PREMIXRAWEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'drop CrossingFramePlaybackInfoExtended_mix_*_*', 
        'drop PileupSummaryInfos_addPileupInfo_*_*')
)

process.RAWDEBUGEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*')
)

process.RAWDEBUGHLTEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBUncalibrator_*_*', 
        'keep *_hltAlCaEtaEEUncalibrator_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPhiSymUncalibrator_*_*', 
        'keep *_hltAlCaPi0EBUncalibrator_*_*', 
        'keep *_hltAlCaPi0EEUncalibrator_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltEle32WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1extraParticlesCentral_*_*', 
        'keep *_hltL1extraParticlesNonIsolated_*_*', 
        'keep *_hltL1extraParticlesTau_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidatesNoVtx_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltMetForHf_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4JetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTCands_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) )
)

process.RAWEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.RAWRECODEBUGHLTEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak7GenJets_*_*', 
        'keep *_iterativeCone5GenJets_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBUncalibrator_*_*', 
        'keep *_hltAlCaEtaEEUncalibrator_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPhiSymUncalibrator_*_*', 
        'keep *_hltAlCaPi0EBUncalibrator_*_*', 
        'keep *_hltAlCaPi0EEUncalibrator_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltEle32WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1extraParticlesCentral_*_*', 
        'keep *_hltL1extraParticlesNonIsolated_*_*', 
        'keep *_hltL1extraParticlesTau_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidatesNoVtx_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltMetForHf_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4JetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTCands_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*' ) )
)

process.RAWRECOEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*' ) )
)

process.RAWRECOSIMHLTEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak7GenJets_*_*', 
        'keep *_iterativeCone5GenJets_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBUncalibrator_*_*', 
        'keep *_hltAlCaEtaEEUncalibrator_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPhiSymUncalibrator_*_*', 
        'keep *_hltAlCaPi0EBUncalibrator_*_*', 
        'keep *_hltAlCaPi0EEUncalibrator_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltEle32WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1extraParticlesCentral_*_*', 
        'keep *_hltL1extraParticlesNonIsolated_*_*', 
        'keep *_hltL1extraParticlesTau_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidatesNoVtx_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltMetForHf_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4JetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTCands_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) )
)

process.RAWSIMEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*')
)

process.RAWSIMHLTEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBUncalibrator_*_*', 
        'keep *_hltAlCaEtaEEUncalibrator_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPhiSymUncalibrator_*_*', 
        'keep *_hltAlCaPi0EBUncalibrator_*_*', 
        'keep *_hltAlCaPi0EEUncalibrator_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltEle32WP80PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1extraParticlesCentral_*_*', 
        'keep *_hltL1extraParticlesNonIsolated_*_*', 
        'keep *_hltL1extraParticlesTau_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidatesNoVtx_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltMetForHf_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4JetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTCands_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) )
)

process.RECODEBUGEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak7GenJets_*_*', 
        'keep *_iterativeCone5GenJets_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*' ) )
)

process.RECOEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*' ) )
)

process.RECOSIMEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*', 
        'keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak7GenJets_*_*', 
        'keep *_iterativeCone5GenJets_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*' ) )
)

process.REDIGIEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring('drop *', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'drop *_randomEngineStateProducer_*_*')
)

process.REGENEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*')
)

process.REPACKRAWEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop FEDRawDataCollection_*_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'drop FEDRawDataCollection_source_*_*', 
        'drop FEDRawDataCollection_rawDataCollector_*_*')
)

process.REPACKRAWSIMEventContent = cms.PSet(
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop FEDRawDataCollection_*_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'drop FEDRawDataCollection_source_*_*', 
        'drop FEDRawDataCollection_rawDataCollector_*_*')
)

process.RESIMEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring('drop *', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.RecoBTagAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*')
)

process.RecoBTagFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*')
)

process.RecoBTagRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedSecondaryVertexMVABJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*')
)

process.RecoBTauAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoBTauFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoBTauRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoEcalAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep recoCaloClusters_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*')
)

process.RecoEcalFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_selectDigi_*_*', 
        'keep *_reducedEcalRecHitsEB_*_*', 
        'keep *_reducedEcalRecHitsEE_*_*', 
        'keep *_reducedEcalRecHitsES_*_*', 
        'keep *_interestingEcalDetId*_*_*', 
        'keep *_ecalWeightUncalibRecHit_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep *_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5*_*_*', 
        'keep *_correctedMulti5x5*_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*')
)

process.RecoEcalRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*')
)

process.RecoEgammaAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep recoPhotonCores_gedPhotonCore_*_*', 
        'keep recoPhotons_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'drop *_gedPhotons_valMapPFEgammaCandToPhoton_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*')
)

process.RecoEgammaFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_gsfElectronCores_*_*', 
        'keep *_gsfElectrons_*_*', 
        'keep *_uncleanedOnlyGsfElectronCores_*_*', 
        'keep *_uncleanedOnlyGsfElectrons_*_*', 
        'keep *_eidRobustLoose_*_*', 
        'keep *_eidRobustTight_*_*', 
        'keep *_eidRobustHighEnergy_*_*', 
        'keep *_eidLoose_*_*', 
        'keep *_eidTight_*_*', 
        'keep *_conversions_*_*', 
        'keep *_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotonsTmp_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep *_photonCore_*_*', 
        'keep *_photons_*_*', 
        'keep *_mustachePhotonCore_*_*', 
        'keep *_mustachePhotons_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_allConversionsOldEG_*_*', 
        'keep *_ckfOutInTracksFrom*Conversions_*_*', 
        'keep *_ckfInOutTracksFrom*Conversions_*_*', 
        'keep *_uncleanedOnlyAllConversions_*_*', 
        'keep *_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep *_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*')
)

process.RecoEgammaRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*')
)

process.RecoGenJetsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_genParticle_*_*')
)

process.RecoGenJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*')
)

process.RecoGenJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_kt4GenJets_*_*', 
        'keep *_kt6GenJets_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak5GenJets_*_*', 
        'keep *_ak7GenJets_*_*', 
        'keep *_iterativeCone5GenJets_*_*', 
        'keep *_genParticle_*_*')
)

process.RecoGenMETAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenMETs_*_*_*')
)

process.RecoGenMETFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenMETs_*_*_*')
)

process.RecoGenMETRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenMETs_*_*_*')
)

process.RecoHcalNoiseAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('drop recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*')
)

process.RecoHcalNoiseFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*')
)

process.RecoHcalNoiseRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*')
)

process.RecoJetsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*')
)

process.RecoJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloJets_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoTrackJets_*_*_*', 
        'keep recoJPTJets_*_*_*', 
        'keep recoBasicJets_*_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_*JetID_*_*', 
        'keep *_kt4CaloJets_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep *_ak7CaloJets_*_*', 
        'keep *_kt4PFJets_*_*', 
        'keep *_kt6PFJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak7PFJets_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep *_kt4TrackJets_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca*Links_*_*', 
        'keep *_ak*Links_*_*')
)

process.RecoJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep double_kt6PFJets_rho_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak8PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak5PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHS_*_*', 
        'keep *_ca8PFJetsCHSPruned_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5JetID_*_*', 
        'keep *_ak7JetID_*_*', 
        'keep *_ic5JetID_*_*', 
        'keep *_kt4JetID_*_*', 
        'keep *_kt6JetID_*_*', 
        'keep *_ak7BasicJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep double_kt6CaloJetsCentral_*_*', 
        'keep double_kt6PFJetsCentralChargedPileUp_*_*', 
        'keep double_kt6PFJetsCentralNeutral_*_*', 
        'keep double_kt6PFJetsCentralNeutralTight_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca8PFJetsCHSPrunedLinks_*_*')
)

process.RecoLocalCaloAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_castorreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep HcalUnpackerReport_*_*_*')
)

process.RecoLocalCaloFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HBHERecHitsSorted_hbheprerecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalGlobalUncalibRecHit_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*')
)

process.RecoLocalCaloRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_hbhereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*')
)

process.RecoLocalMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoLocalMuonFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*')
)

process.RecoLocalMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*')
)

process.RecoLocalTrackerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_clusterSummaryProducer_*_*')
)

process.RecoLocalTrackerFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*')
)

process.RecoLocalTrackerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*')
)

process.RecoMETAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'drop recoHcalNoiseRBXs_*_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *GlobalHaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*')
)

process.RecoMETFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*')
)

process.RecoMETRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloMETs_met_*_*', 
        'keep recoCaloMETs_metNoHF_*_*', 
        'keep recoCaloMETs_metHO_*_*', 
        'keep recoCaloMETs_corMetGlobalMuons_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*')
)

process.RecoMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*')
)

process.RecoMuonFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*')
)

process.RecoMuonIsolationAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoMuonIsolationFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*')
)

process.RecoMuonIsolationParamGlobal = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_muParamGlobalIsoDepositGsTk_*_*', 
        'keep *_muParamGlobalIsoDepositCalEcal_*_*', 
        'keep *_muParamGlobalIsoDepositCalHcal_*_*', 
        'keep *_muParamGlobalIsoDepositCtfTk_*_*', 
        'keep *_muParamGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muParamGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muParamGlobalIsoDepositJets_*_*')
)

process.RecoMuonIsolationRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*')
)

process.RecoMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_globalCosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTrackExtras_globalCosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_globalCosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoTracks_globalCosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoTracks_globalCosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*')
)

process.RecoParticleFlowAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('drop CaloTowersSorted_towerMakerPF_*_*', 
        'drop *_pfElectronTranslator_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep recoCaloClusters_pfElectronTranslator_*_*', 
        'keep recoPreshowerClusters_pfElectronTranslator_*_*', 
        'keep recoSuperClusters_pfElectronTranslator_*_*', 
        'keep recoCaloClusters_pfPhotonTranslator_*_*', 
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*', 
        'keep recoSuperClusters_pfPhotonTranslator_*_*', 
        'keep recoPhotons_pfPhotonTranslator_*_*', 
        'keep recoPhotonCores_pfPhotonTranslator_*_*', 
        'keep recoConversions_pfPhotonTranslator_*_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*')
)

process.RecoParticleFlowFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHFEM_*_*', 
        'keep recoPFClusters_particleFlowClusterHFHAD_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*')
)

process.RecoParticleFlowRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*')
)

process.RecoPixelVertexingFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*')
)

process.RecoPixelVertexingRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*')
)

process.RecoTauTagAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*')
)

process.RecoTauTagFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*')
)

process.RecoTauTagRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*')
)

process.RecoTrackerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*')
)

process.RecoTrackerFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*')
)

process.RecoTrackerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_regionalCosmicTracks_*_*', 
        'keep recoTrackExtras_regionalCosmicTracks_*_*', 
        'keep TrackingRecHitsOwned_regionalCosmicTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxDiscrimASmi_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*')
)

process.RecoVertexAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*')
)

process.RecoVertexFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*')
)

process.RecoVertexRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*')
)

process.SimCalorimetryAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimCalorimetryFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simEcalDigis_*_*', 
        'keep *_simEcalPreshowerDigis_*_*', 
        'keep *_simEcalTriggerPrimitiveDigis_*_*', 
        'keep *_simHcalDigis_*_*', 
        'keep ZDCDataFramesSorted_simHcalUnsuppressedDigis_*_*', 
        'drop ZDCDataFramesSorted_mix_simHcalUnsuppressedDigis*_*', 
        'keep *_simHcalTriggerPrimitiveDigis_*_*')
)

process.SimCalorimetryRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*')
)

process.SimCalorimetryRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimG4CoreAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimG4CoreRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*')
)

process.SimG4CoreRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*')
)

process.SimGeneralAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep PileupSummaryInfos_*_*_*')
)

process.SimGeneralFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoExtended_*_*_*')
)

process.SimGeneralRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep CrossingFramePlaybackInfoExtended_*_*_*', 
        'keep PileupSummaryInfos_*_*_*')
)

process.SimGeneralRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep PileupSummaryInfos_*_*_*')
)

process.SimMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimMuonFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simMuonCSCDigis_*_*', 
        'keep *_simMuonDTDigis_*_*', 
        'keep *_simMuonRPCDigis_*_*')
)

process.SimMuonRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*')
)

process.SimMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*')
)

process.SimTrackerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_allTrackMCMatch_*_*')
)

process.SimTrackerDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*')
)

process.SimTrackerFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simSiPixelDigis_*_*', 
        'keep *_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_trackingParticleRecoTrackAsssociation_*_*', 
        'keep *_assoc2secStepTk_*_*', 
        'keep *_assoc2thStepTk_*_*', 
        'keep *_assoc2GsfTracks_*_*', 
        'keep *_assocOutInConversionTracks_*_*', 
        'keep *_assocInOutConversionTracks_*_*')
)

process.SimTrackerRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_allTrackMCMatch_*_*')
)

process.SimTrackerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_allTrackMCMatch_*_*')
)

process.TrackingToolsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoTracks_GsfGlobalElectronTest_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*')
)

process.TrackingToolsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep *_electronGsfTracks_*_*')
)

process.TrackingToolsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*')
)

process.datasets = cms.PSet(
    InitialPD = cms.vstring('HLT_BTagCSV07_v1', 
        'HLT_CaloJet260_v1', 
        'HLT_Dimuon13_PsiPrime_v1', 
        'HLT_Dimuon13_Upsilon_v1', 
        'HLT_Dimuon20_Jpsi_v1', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1', 
        'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_v1', 
        'HLT_DoubleMu4_3_Bs_v1', 
        'HLT_DoubleMu4_3_Jpsi_Displaced_v1', 
        'HLT_DoubleMu4_JpsiTrk_Displaced_v1', 
        'HLT_DoubleMu4_Jpsi_Displaced_v1', 
        'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v1', 
        'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v1', 
        'HLT_Ele17_Ele12_Ele10_CaloId_TrackId_v1', 
        'HLT_Ele17_Ele8_Gsf_v1', 
        'HLT_Ele22_eta2p1_WP90Rho_Gsf_LooseIsoPFTau20_v1', 
        'HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1', 
        'HLT_Ele27_WP80_Gsf_CentralPFJet30_BTagCSV_v1', 
        'HLT_Ele27_WP80_Gsf_TriCentralPFJet40_v1', 
        'HLT_Ele27_WP80_Gsf_TriCentralPFJet60_50_35_v1', 
        'HLT_Ele27_WP80_Gsf_v1', 
        'HLT_HT650_v1', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1', 
        'HLT_IsoMu24_IterTrk02_CentralPFJet30_BTagCSV_v1', 
        'HLT_IsoMu24_IterTrk02_TriCentralPFJet40_v1', 
        'HLT_IsoMu24_IterTrk02_TriCentralPFJet60_50_35_v1', 
        'HLT_IsoMu24_IterTrk02_v1', 
        'HLT_IsoTkMu24_IterTrk02_v1', 
        'HLT_IterativeTracking_v1', 
        'HLT_JetE50_NoBPTX3BX_NoHalo_v1', 
        'HLT_LooseIsoPFTau40_Trk25_Prong1_eta2p1_PFMET65_v1', 
        'HLT_Mu17_Mu8_v1', 
        'HLT_Mu17_NoFilters_v1', 
        'HLT_Mu17_TkMu8_v1', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1', 
        'HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1', 
        'HLT_Mu25_TkMu0_dEta18_Onia_v1', 
        'HLT_Mu30_TkMu11_v1', 
        'HLT_Mu40_v1', 
        'HLT_Mu8_TrkIsoVVL_Ele23_Gsf_CaloId_TrackId_Iso_MediumWP_v1', 
        'HLT_PFHT650_v1', 
        'HLT_PFJet260_v1', 
        'HLT_PFJet40_v1', 
        'HLT_PFMET180_NoiseCleaned_v1', 
        'HLT_PFchMET90_NoiseCleaned_v1', 
        'HLT_Photon135_PFMET40_v1', 
        'HLT_Photon135_VBF_v1', 
        'HLT_Photon150_PFMET40_v1', 
        'HLT_Photon150_VBF_v1', 
        'HLT_Photon160_PFMET40_v1', 
        'HLT_Photon160_VBF_v1', 
        'HLT_Photon20_CaloIdVL_IsoL_v1', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon250_NoHE_PFMET40_v1', 
        'HLT_Photon250_NoHE_VBF_v1', 
        'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v1', 
        'HLT_Photon300_NoHE_PFMET40_v1', 
        'HLT_Photon300_NoHE_VBF_v1', 
        'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon18_AND_HE10_R9Id65_Mass95_v1', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_v1', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Physics_v1', 
        'HLT_ReducedIterativeTracking_v1')
)

process.ecalLocalRecoAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.ecalLocalRecoFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ecalGlobalUncalibRecHit_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*')
)

process.ecalLocalRecoRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.streams = cms.PSet(
    A = cms.vstring('InitialPD')
)

