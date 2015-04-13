import FWCore.ParameterSet.Config as cms

process = cms.Process("HLT3")

process.source = cms.Source("PoolSource",
    eventsToProcess = cms.untracked.VEventRange(),
    fileNames = cms.untracked.vstring('/store/user/algomez/RPVSt350tojj_13TeV_pythia8/AODSIM_PHYS14_v720_PU20bx25/150321_122931/0000/RPVSt350tojj_13TeV_pythia8_AODSIM_PU20bx25_1.root'),
    secondaryFileNames = cms.untracked.vstring('/store/user/algomez/RPVSt350tojj_13TeV_pythia8/RAWSIM_PHYS14_v720_PU20bx25/150320_034026/0000/RPVSt350tojj_13TeV_pythia8_RAWSIM_PU20bx25_307.root')
)
parentProcess8759233674377 = process
import FWCore.ParameterSet.Config as cms

process = cms.Process("PAT")

process.ak4PFJetsCHS = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(20.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("pfNoPileUp"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PFJetsCHS = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(20.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("pfNoPileUp"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PFJetsCHSPruned = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(20.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nFilt = cms.int32(2),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    rcut_factor = cms.double(0.5),
    src = cms.InputTag("pfNoPileUp"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    usePruning = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8PFJetsCHSTrim = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(20.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rFilt = cms.double(0.2),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("pfNoPileUp"),
    srcPVs = cms.InputTag(""),
    trimPtFracMin = cms.double(0.03),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useTrimming = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PFJetsCHSTrimMod = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(20.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rFilt = cms.double(0.1),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("pfNoPileUp"),
    srcPVs = cms.InputTag(""),
    trimPtFracMin = cms.double(0.03),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useTrimming = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.patJetCorrFactorsAK4CHS = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAK8CHS = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK8PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAK8CHSPruned = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK8PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PFJetsCHSPruned"),
    useNPV = cms.bool(True),
    useRho = cms.bool(False)
)


process.patJetCorrFactorsAK8CHSTrim = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK8PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PFJetsCHSTrim"),
    useNPV = cms.bool(True),
    useRho = cms.bool(False)
)


process.patJetCorrFactorsAK8CHSTrimMod = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK8PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PFJetsCHSTrimMod"),
    useNPV = cms.bool(True),
    useRho = cms.bool(False)
)


process.patJetsAK4CHS = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(False),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexBJetTags"), cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighPurBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), 
        cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedSecondaryVertexSoftLeptonBJetTags"), 
        cms.InputTag("pfCombinedMVABJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK4CHS")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsCHS"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAK8CHS = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(False),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexBJetTags"), cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighPurBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), 
        cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedSecondaryVertexSoftLeptonBJetTags"), 
        cms.InputTag("pfCombinedMVABJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK8CHS")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PFJetsCHS"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAK8CHSPruned = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(False),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexBJetTags"), cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighPurBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), 
        cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedSecondaryVertexSoftLeptonBJetTags"), 
        cms.InputTag("pfCombinedMVABJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK8CHSPruned")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PFJetsCHSPruned"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAK8CHSTrim = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(False),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexBJetTags"), cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighPurBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), 
        cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedSecondaryVertexSoftLeptonBJetTags"), 
        cms.InputTag("pfCombinedMVABJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK8CHSTrim")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PFJetsCHSTrim"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAK8CHSTrimMod = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(False),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexBJetTags"), cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighPurBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), 
        cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedSecondaryVertexSoftLeptonBJetTags"), 
        cms.InputTag("pfCombinedMVABJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK8CHSTrimMod")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PFJetsCHSTrimMod"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.pfAllElectronsClones = cms.EDProducer("PFCandidateProductFromFwdPtrProducer",
    src = cms.InputTag("pfAllElectrons")
)


process.pfAllMuonsClones = cms.EDProducer("PFCandidateProductFromFwdPtrProducer",
    src = cms.InputTag("pfAllMuons")
)


process.pfNoPileUp = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUp"),
    verbose = cms.untracked.bool(False)
)


process.pfNoPileUpIso = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowTmpPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIso"),
    verbose = cms.untracked.bool(False)
)


process.pfNoPileUpJME = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpJME"),
    verbose = cms.untracked.bool(False)
)


process.pfPileUp = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices"),
    checkClosestZVertex = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.pfPileUpIso = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowTmpPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.pfPileUpJME = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices"),
    checkClosestZVertex = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.pfAllChargedHadrons = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfAllChargedParticles = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfAllElectrons = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(11, -11),
    src = cms.InputTag("pfNoMuon")
)


process.pfAllMuons = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(-13, 13),
    src = cms.InputTag("pfNoPileUp")
)


process.pfAllNeutralHadrons = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfAllNeutralHadronsAndPhotons = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfAllPhotons = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfPileUpAllChargedParticles = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfPileUpIso")
)


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myHLT2PAT_prod.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_patJets*_*_*', 
        'keep *_goodOfflinePrimaryVertices_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_patJets*_*_*', 
        'keep *_hltOnlinePrimaryVertices*_*_*', 
        'keep *_goodOfflinePrimaryVertices*_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltPFHT_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltAntiKT5CaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltPFHT4Jet_*_*', 
        'keep *_hltAK8HtMht_*_*', 
        'keep *_hltAK8PFJetsTrimR0p1PT0p03_*_*', 
        'keep *_hltAntiKT5PFJets_*_*', 
        'keep *_hltGtDigis_*_*', 
        'keep *_hltHtMht4Jet_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltLightPFTracks_*_*', 
        'keep *_hltAK8PFHT_*_*', 
        'keep *_hltAK4CaloJetsPF_*_*', 
        'keep *_hltAntiKT5PFJetsNoPU_*_*', 
        'keep *_hltHtMht_*_*', 
        'keep *_hltAK8CaloJetsPF_*_*')
)


process.pfNoPileUpIsoSequence = cms.Sequence(process.pfPileUpIso+process.pfNoPileUpIso)


process.pfNoPileUpSequence = cms.Sequence(process.goodOfflinePrimaryVertices+process.pfPileUp+process.pfNoPileUp)


process.pfSortByTypeSequence = cms.Sequence(process.pfAllNeutralHadrons+process.pfAllChargedHadrons+process.pfAllPhotons+process.pfAllChargedParticles+process.pfPileUpAllChargedParticles+process.pfAllNeutralHadronsAndPhotons)


process.pfNoPileUpJMESequence = cms.Sequence(process.goodOfflinePrimaryVertices+process.pfPileUpJME+process.pfNoPileUpJME)


process.pfParticleSelectionSequence = cms.Sequence(process.pfNoPileUpIsoSequence+process.pfNoPileUpSequence+process.pfSortByTypeSequence)


process.pileUpSubtractionSequence = cms.Sequence(process.pfNoPileUpSequence+process.pfParticleSelectionSequence)


process.outpath = cms.EndPath(process.out)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
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


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    parameters = cms.PSet(

    ),
    version = cms.string('Parabolic')
)


process.ParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
    label = cms.untracked.string('parametrizedField'),
    parameters = cms.PSet(
        BValue = cms.string('3_8T')
    ),
    version = cms.string('OAE_1103l_071212')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    cacheLastVolume = cms.untracked.bool(True),
    debugBuilder = cms.untracked.bool(False),
    geometryVersion = cms.int32(90322),
    gridFiles = cms.VPSet(cms.PSet(
        master = cms.int32(1),
        path = cms.string('grid.[v].bin'),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    ), 
        cms.PSet(
            master = cms.int32(3),
            path = cms.string('S3/grid.[v].bin'),
            sectors = cms.string('3'),
            volumes = cms.string('176-186,231-241,286-296')
        ), 
        cms.PSet(
            master = cms.int32(4),
            path = cms.string('S4/grid.[v].bin'),
            sectors = cms.string('4'),
            volumes = cms.string('176-186,231-241,286-296')
        ), 
        cms.PSet(
            master = cms.int32(9),
            path = cms.string('S9/grid.[v].bin'),
            sectors = cms.string('9'),
            volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296')
        ), 
        cms.PSet(
            master = cms.int32(10),
            path = cms.string('S10/grid.[v].bin'),
            sectors = cms.string('10'),
            volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296')
        ), 
        cms.PSet(
            master = cms.int32(11),
            path = cms.string('S11/grid.[v].bin'),
            sectors = cms.string('11'),
            volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296')
        )),
    label = cms.untracked.string(''),
    paramLabel = cms.string('parametrizedField'),
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991),
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
    version = cms.string('grid_1103l_090322_3_8t')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string(''),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False),
    trackerGeometryConstants = cms.PSet(
        BIG_PIX_PER_ROC_X = cms.int32(1),
        BIG_PIX_PER_ROC_Y = cms.int32(2),
        COLS_PER_ROC = cms.int32(52),
        ROCS_X = cms.int32(0),
        ROCS_Y = cms.int32(0),
        ROWS_PER_ROC = cms.int32(80),
        upgradeGeometry = cms.bool(False)
    )
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


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
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
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False),
    trackerGeometryConstants = cms.PSet(
        BIG_PIX_PER_ROC_X = cms.int32(1),
        BIG_PIX_PER_ROC_Y = cms.int32(2),
        COLS_PER_ROC = cms.int32(52),
        ROCS_X = cms.int32(0),
        ROCS_Y = cms.int32(0),
        ROWS_PER_ROC = cms.int32(80),
        upgradeGeometry = cms.bool(False)
    )
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopologyConstants = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string(''),
    pxb_ladderMask = cms.uint32(255),
    pxb_ladderStartBit = cms.uint32(8),
    pxb_layerMask = cms.uint32(15),
    pxb_layerStartBit = cms.uint32(16),
    pxb_moduleMask = cms.uint32(63),
    pxb_moduleStartBit = cms.uint32(2),
    pxf_bladeMask = cms.uint32(63),
    pxf_bladeStartBit = cms.uint32(10),
    pxf_diskMask = cms.uint32(15),
    pxf_diskStartBit = cms.uint32(16),
    pxf_moduleMask = cms.uint32(63),
    pxf_moduleStartBit = cms.uint32(2),
    pxf_panelMask = cms.uint32(3),
    pxf_panelStartBit = cms.uint32(8),
    pxf_sideMask = cms.uint32(3),
    pxf_sideStartBit = cms.uint32(23),
    tec_moduleMask = cms.uint32(7),
    tec_moduleStartBit = cms.uint32(2),
    tec_petalMask = cms.uint32(15),
    tec_petalStartBit = cms.uint32(8),
    tec_petal_fw_bwMask = cms.uint32(3),
    tec_petal_fw_bwStartBit = cms.uint32(12),
    tec_ringMask = cms.uint32(7),
    tec_ringStartBit = cms.uint32(5),
    tec_sideMask = cms.uint32(3),
    tec_sideStartBit = cms.uint32(18),
    tec_sterMask = cms.uint32(3),
    tec_sterStartBit = cms.uint32(0),
    tec_wheelMask = cms.uint32(15),
    tec_wheelStartBit = cms.uint32(14),
    tib_layerMask = cms.uint32(7),
    tib_layerStartBit = cms.uint32(14),
    tib_moduleMask = cms.uint32(3),
    tib_moduleStartBit = cms.uint32(2),
    tib_sterMask = cms.uint32(3),
    tib_sterStartBit = cms.uint32(0),
    tib_strMask = cms.uint32(63),
    tib_strStartBit = cms.uint32(4),
    tib_str_fw_bwMask = cms.uint32(3),
    tib_str_fw_bwStartBit = cms.uint32(12),
    tib_str_int_extMask = cms.uint32(3),
    tib_str_int_extStartBit = cms.uint32(10),
    tid_moduleMask = cms.uint32(31),
    tid_moduleStartBit = cms.uint32(2),
    tid_module_fw_bwMask = cms.uint32(3),
    tid_module_fw_bwStartBit = cms.uint32(7),
    tid_ringMask = cms.uint32(3),
    tid_ringStartBit = cms.uint32(9),
    tid_sideMask = cms.uint32(3),
    tid_sideStartBit = cms.uint32(13),
    tid_sterMask = cms.uint32(3),
    tid_sterStartBit = cms.uint32(0),
    tid_wheelMask = cms.uint32(3),
    tid_wheelStartBit = cms.uint32(11),
    tob_layerMask = cms.uint32(7),
    tob_layerStartBit = cms.uint32(14),
    tob_moduleMask = cms.uint32(7),
    tob_moduleStartBit = cms.uint32(2),
    tob_rodMask = cms.uint32(127),
    tob_rodStartBit = cms.uint32(5),
    tob_rod_fw_bwMask = cms.uint32(3),
    tob_rod_fw_bwStartBit = cms.uint32(12),
    tob_sterMask = cms.uint32(3),
    tob_sterStartBit = cms.uint32(0)
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('PHYS14_25_V3'),
    toGet = cms.VPSet(cms.PSet(
        connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
        record = cms.string('CSCAlignmentErrorExtendedRcd'),
        tag = cms.string('MuonCSCAPEObjectsExtended_v0_mc')
    ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('DTAlignmentErrorExtendedRcd'),
            tag = cms.string('MuonDTAPEObjectsExtended_v0_mc')
        ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('EcalPulseCovariancesRcd'),
            tag = cms.string('EcalPulseCovariances_mc')
        ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('EcalPulseShapesRcd'),
            tag = cms.string('EcalPulseShapes_mc')
        ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('EcalSamplesCorrelationRcd'),
            tag = cms.string('EcalSamplesCorrelation_mc')
        ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('TrackerAlignmentErrorExtendedRcd'),
            tag = cms.string('TrackerAlignmentExtendedError_2011Realistic_v1_mc')
        ))
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    HcalReLabel = cms.PSet(
        RelabelHits = cms.untracked.bool(False),
        RelabelRules = cms.untracked.PSet(
            CorrectPhi = cms.untracked.bool(False),
            Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
                2, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
                3, 3, 4, 4, 4, 
                4, 4, 5, 5, 5, 
                5, 5, 5, 5)
        )
    ),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    ),
    iLumi = cms.double(-1.0),
    toGet = cms.untracked.vstring('GainWidths')
)


process.magfield = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMagneticField.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml', 
        'Geometry/CMSCommonData/data/materials.xml'),
    rootNodeName = cms.string('cmsMagneticField:MAGF')
)


process.prefer("es_hardcode")

process.prefer("magfield")

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    )
)

process.HcalReLabel = cms.PSet(
    RelabelHits = cms.untracked.bool(False),
    RelabelRules = cms.untracked.PSet(
        CorrectPhi = cms.untracked.bool(False),
        Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
            2, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
            3, 3, 4, 4, 4, 
            4, 4, 5, 5, 5, 
            5, 5, 5, 5)
    )
)

process.fieldScaling = cms.PSet(
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991),
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611)
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

childProcess = process
process = parentProcess8759233674377
process.subProcess = cms.SubProcess( process = childProcess, SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('*')
), outputCommands = cms.untracked.vstring('keep *'))
process.hltAK4CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltTowerMakerForAll"),
    srcPVs = cms.InputTag("NotUsed"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(0.9),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4CaloJetsCorrected = cms.EDProducer("CaloJetCorrectionProducer",
    correctors = cms.vstring('hltESPAK4CaloCorrection'),
    src = cms.InputTag("hltAK4CaloJets")
)


process.hltAK4CaloJetsCorrectedIDPassed = cms.EDProducer("CaloJetCorrectionProducer",
    correctors = cms.vstring('hltESPAK4CaloCorrection'),
    src = cms.InputTag("hltAK4CaloJetsIDPassed")
)


process.hltAK4CaloJetsIDPassed = cms.EDProducer("HLTCaloJetIDProducer",
    JetIDParams = cms.PSet(
        ebRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        eeRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        hbheRecHitsColl = cms.InputTag("hltHbhereco"),
        hfRecHitsColl = cms.InputTag("hltHfreco"),
        hoRecHitsColl = cms.InputTag("hltHoreco"),
        useRecHits = cms.bool(True)
    ),
    jetsInput = cms.InputTag("hltAK4CaloJets"),
    max_EMF = cms.double(999.0),
    min_EMF = cms.double(1e-06),
    min_N90 = cms.int32(-2),
    min_N90hits = cms.int32(2)
)


process.hltAK4CaloJetsPF = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltTowerMakerForPF"),
    srcPVs = cms.InputTag("NotUsed"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(-9.0),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4Iter0TrackJets4Iter1 = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.2),
    DzTrVtxMax = cms.double(0.5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(30.0),
    MinVtxNdof = cms.int32(0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(True),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.1),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('TrackJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltTrackIter0RefsForJets4Iter1"),
    srcPVs = cms.InputTag("hltTrimmedPixelVertices"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(0.9),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4Iter1TrackJets4Iter2 = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.2),
    DzTrVtxMax = cms.double(0.5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(30.0),
    MinVtxNdof = cms.int32(0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(True),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.1),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(7.5),
    jetType = cms.string('TrackJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltIter1TrackRefsForJets4Iter2"),
    srcPVs = cms.InputTag("hltTrimmedPixelVertices"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(0.9),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltParticleFlow"),
    srcPVs = cms.InputTag("hltPixelVertices"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(-9.0),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4PFJetsCorrected = cms.EDProducer("PFJetCorrectionProducer",
    correctors = cms.vstring('hltESPAK4PFCorrection'),
    src = cms.InputTag("hltAK4PFJets")
)


process.hltAK8CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.8),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltTowerMakerForAll"),
    srcPVs = cms.InputTag("NotUsed"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(0.9),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK8CaloJetsCorrected = cms.EDProducer("CaloJetCorrectionProducer",
    correctors = cms.vstring('hltESPAK8CaloCorrection'),
    src = cms.InputTag("hltAK8CaloJets")
)


process.hltAK8CaloJetsCorrectedIDPassed = cms.EDProducer("CaloJetCorrectionProducer",
    correctors = cms.vstring('hltESPAK8CaloCorrection'),
    src = cms.InputTag("hltAK8CaloJetsIDPassed")
)


process.hltAK8CaloJetsIDPassed = cms.EDProducer("HLTCaloJetIDProducer",
    JetIDParams = cms.PSet(
        ebRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        eeRecHitsColl = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        hbheRecHitsColl = cms.InputTag("hltHbhereco"),
        hfRecHitsColl = cms.InputTag("hltHfreco"),
        hoRecHitsColl = cms.InputTag("hltHoreco"),
        useRecHits = cms.bool(True)
    ),
    jetsInput = cms.InputTag("hltAK8CaloJets"),
    max_EMF = cms.double(999.0),
    min_EMF = cms.double(1e-06),
    min_N90 = cms.int32(-2),
    min_N90hits = cms.int32(2)
)


process.hltAK8CaloJetsPF = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.8),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltTowerMakerForPF"),
    srcPVs = cms.InputTag("NotUsed"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(-9.0),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK8HtMht = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK8CaloJetsCorrected"),
    maxEtaJetHt = cms.double(2.5),
    maxEtaJetMht = cms.double(5.0),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(150.0),
    minPtJetMht = cms.double(30.0),
    pfCandidatesLabel = cms.InputTag(""),
    usePt = cms.bool(False)
)


process.hltAK8PFHT = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK8PFJetsCorrected"),
    maxEtaJetHt = cms.double(2.5),
    maxEtaJetMht = cms.double(999.0),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(150.0),
    minPtJetMht = cms.double(0.0),
    pfCandidatesLabel = cms.InputTag("hltParticleFlow"),
    usePt = cms.bool(True)
)


process.hltAK8PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.8),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltParticleFlow"),
    srcPVs = cms.InputTag("hltPixelVertices"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(-9.0),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK8PFJetsCorrected = cms.EDProducer("PFJetCorrectionProducer",
    correctors = cms.vstring('hltESPAK8PFCorrection'),
    src = cms.InputTag("hltAK8PFJets")
)


process.hltAK8PFJetsTrimR0p1PT0p03 = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10.0),
    rFilt = cms.double(0.1),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.8),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltParticleFlow"),
    srcPVs = cms.InputTag("hltPixelVertices"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(0.03),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(True),
    voronoiRfact = cms.double(-9.0),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltCaloStage1Digis = cms.EDProducer("L1TRawToDigi",
    FWId = cms.untracked.int32(2),
    FedIds = cms.vint32(1352),
    InputLabel = cms.InputTag("rawDataCollector"),
    Setup = cms.string('stage1::CaloSetup'),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.hltCaloStage1LegacyFormatDigis = cms.EDProducer("L1TCaloUpgradeToGCTConverter",
    InputCollection = cms.InputTag("hltCaloStage1Digis"),
    InputHFCountsCollection = cms.InputTag("hltCaloStage1Digis","HFBitCounts"),
    InputHFSumsCollection = cms.InputTag("hltCaloStage1Digis","HFRingSums"),
    InputIsoTauCollection = cms.InputTag("hltCaloStage1Digis","isoTaus"),
    InputRlxTauCollection = cms.InputTag("hltCaloStage1Digis","rlxTaus")
)


process.hltCsc2DRecHits = cms.EDProducer("CSCRecHitDProducer",
    CSCDebug = cms.untracked.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripClusterSize = cms.untracked.int32(3),
    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripxtalksOffset = cms.double(0.03),
    CSCUseCalibrations = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(False),
    CSCUseStaticPedestals = cms.bool(False),
    CSCUseTimingCorrections = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCstripWireDeltaTime = cms.int32(8),
    ConstSyst_ME12 = cms.double(0.0),
    ConstSyst_ME13 = cms.double(0.0),
    ConstSyst_ME1a = cms.double(0.022),
    ConstSyst_ME1b = cms.double(0.007),
    ConstSyst_ME21 = cms.double(0.0),
    ConstSyst_ME22 = cms.double(0.0),
    ConstSyst_ME31 = cms.double(0.0),
    ConstSyst_ME32 = cms.double(0.0),
    ConstSyst_ME41 = cms.double(0.0),
    NoiseLevel_ME12 = cms.double(9.0),
    NoiseLevel_ME13 = cms.double(8.0),
    NoiseLevel_ME1a = cms.double(7.0),
    NoiseLevel_ME1b = cms.double(8.0),
    NoiseLevel_ME21 = cms.double(9.0),
    NoiseLevel_ME22 = cms.double(9.0),
    NoiseLevel_ME31 = cms.double(9.0),
    NoiseLevel_ME32 = cms.double(9.0),
    NoiseLevel_ME41 = cms.double(9.0),
    UseAverageTime = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    UseParabolaFit = cms.bool(False),
    XTasymmetry_ME12 = cms.double(0.0),
    XTasymmetry_ME13 = cms.double(0.0),
    XTasymmetry_ME1a = cms.double(0.0),
    XTasymmetry_ME1b = cms.double(0.0),
    XTasymmetry_ME21 = cms.double(0.0),
    XTasymmetry_ME22 = cms.double(0.0),
    XTasymmetry_ME31 = cms.double(0.0),
    XTasymmetry_ME32 = cms.double(0.0),
    XTasymmetry_ME41 = cms.double(0.0),
    readBadChambers = cms.bool(True),
    readBadChannels = cms.bool(False),
    stripDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCStripDigi"),
    wireDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCWireDigi")
)


process.hltCscSegments = cms.EDProducer("CSCSegmentProducer",
    algo_psets = cms.VPSet(cms.PSet(
        algo_name = cms.string('CSCSegAlgoST'),
        algo_psets = cms.VPSet(cms.PSet(
            BPMinImprovement = cms.double(10000.0),
            BrutePruning = cms.bool(True),
            CSCDebug = cms.untracked.bool(False),
            CorrectTheErrors = cms.bool(True),
            Covariance = cms.double(0.0),
            ForceCovariance = cms.bool(False),
            ForceCovarianceAll = cms.bool(False),
            NormChi2Cut2D = cms.double(20.0),
            NormChi2Cut3D = cms.double(10.0),
            Pruning = cms.bool(True),
            SeedBig = cms.double(0.0015),
            SeedSmall = cms.double(0.0002),
            curvePenalty = cms.double(2.0),
            curvePenaltyThreshold = cms.double(0.85),
            dPhiFineMax = cms.double(0.025),
            dRPhiFineMax = cms.double(8.0),
            dXclusBoxMax = cms.double(4.0),
            dYclusBoxMax = cms.double(8.0),
            hitDropLimit4Hits = cms.double(0.6),
            hitDropLimit5Hits = cms.double(0.8),
            hitDropLimit6Hits = cms.double(0.3333),
            maxDPhi = cms.double(999.0),
            maxDTheta = cms.double(999.0),
            maxRatioResidualPrune = cms.double(3.0),
            maxRecHitsInCluster = cms.int32(20),
            minHitsPerSegment = cms.int32(3),
            onlyBestSegment = cms.bool(False),
            preClustering = cms.bool(True),
            preClusteringUseChaining = cms.bool(True),
            prePrun = cms.bool(True),
            prePrunLimit = cms.double(3.17),
            tanPhiMax = cms.double(0.5),
            tanThetaMax = cms.double(1.2),
            useShowering = cms.bool(False),
            yweightPenalty = cms.double(1.5),
            yweightPenaltyThreshold = cms.double(1.0)
        ), 
            cms.PSet(
                BPMinImprovement = cms.double(10000.0),
                BrutePruning = cms.bool(True),
                CSCDebug = cms.untracked.bool(False),
                CorrectTheErrors = cms.bool(True),
                Covariance = cms.double(0.0),
                ForceCovariance = cms.bool(False),
                ForceCovarianceAll = cms.bool(False),
                NormChi2Cut2D = cms.double(20.0),
                NormChi2Cut3D = cms.double(10.0),
                Pruning = cms.bool(True),
                SeedBig = cms.double(0.0015),
                SeedSmall = cms.double(0.0002),
                curvePenalty = cms.double(2.0),
                curvePenaltyThreshold = cms.double(0.85),
                dPhiFineMax = cms.double(0.025),
                dRPhiFineMax = cms.double(8.0),
                dXclusBoxMax = cms.double(4.0),
                dYclusBoxMax = cms.double(8.0),
                hitDropLimit4Hits = cms.double(0.6),
                hitDropLimit5Hits = cms.double(0.8),
                hitDropLimit6Hits = cms.double(0.3333),
                maxDPhi = cms.double(999.0),
                maxDTheta = cms.double(999.0),
                maxRatioResidualPrune = cms.double(3.0),
                maxRecHitsInCluster = cms.int32(24),
                minHitsPerSegment = cms.int32(3),
                onlyBestSegment = cms.bool(False),
                preClustering = cms.bool(True),
                preClusteringUseChaining = cms.bool(True),
                prePrun = cms.bool(True),
                prePrunLimit = cms.double(3.17),
                tanPhiMax = cms.double(0.5),
                tanThetaMax = cms.double(1.2),
                useShowering = cms.bool(False),
                yweightPenalty = cms.double(1.5),
                yweightPenaltyThreshold = cms.double(1.0)
            )),
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
        parameters_per_chamber_type = cms.vint32(2, 1, 1, 1, 1, 
            1, 1, 1, 1, 1)
    )),
    algo_type = cms.int32(1),
    inputObjects = cms.InputTag("hltCsc2DRecHits")
)


process.hltDt1DRecHits = cms.EDProducer("DTRecHitProducer",
    debug = cms.untracked.bool(False),
    dtDigiLabel = cms.InputTag("hltMuonDTDigis"),
    recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
    recAlgoConfig = cms.PSet(
        debug = cms.untracked.bool(False),
        doVdriftCorr = cms.bool(True),
        maxTime = cms.double(420.0),
        minTime = cms.double(-3.0),
        stepTwoFromDigi = cms.bool(False),
        tTrigMode = cms.string('DTTTrigSyncFromDB'),
        tTrigModeConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doT0Correction = cms.bool(True),
            doTOFCorrection = cms.bool(True),
            doWirePropCorrection = cms.bool(True),
            tTrigLabel = cms.string(''),
            tofCorrType = cms.int32(0),
            vPropWire = cms.double(24.4),
            wirePropCorrType = cms.int32(0)
        ),
        useUncertDB = cms.bool(True)
    )
)


process.hltDt4DSegments = cms.EDProducer("DTRecSegment4DProducer",
    Reco4DAlgoConfig = cms.PSet(
        AllDTRecHits = cms.bool(True),
        Reco2DAlgoConfig = cms.PSet(
            AlphaMaxPhi = cms.double(1.0),
            AlphaMaxTheta = cms.double(0.9),
            MaxAllowedHits = cms.uint32(50),
            debug = cms.untracked.bool(False),
            hit_afterT0_resolution = cms.double(0.03),
            nSharedHitsMax = cms.int32(2),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False),
            performT0_vdriftSegCorrection = cms.bool(False),
            perform_delta_rejecting = cms.bool(False),
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doVdriftCorr = cms.bool(True),
                maxTime = cms.double(420.0),
                minTime = cms.double(-3.0),
                stepTwoFromDigi = cms.bool(False),
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                tTrigModeConfig = cms.PSet(
                    debug = cms.untracked.bool(False),
                    doT0Correction = cms.bool(True),
                    doTOFCorrection = cms.bool(True),
                    doWirePropCorrection = cms.bool(True),
                    tTrigLabel = cms.string(''),
                    tofCorrType = cms.int32(0),
                    vPropWire = cms.double(24.4),
                    wirePropCorrType = cms.int32(0)
                ),
                useUncertDB = cms.bool(True)
            ),
            segmCleanerMode = cms.int32(2)
        ),
        Reco2DAlgoName = cms.string('DTCombinatorialPatternReco'),
        debug = cms.untracked.bool(False),
        hit_afterT0_resolution = cms.double(0.03),
        nSharedHitsMax = cms.int32(2),
        nUnSharedHitsMin = cms.int32(2),
        performT0SegCorrection = cms.bool(False),
        performT0_vdriftSegCorrection = cms.bool(False),
        perform_delta_rejecting = cms.bool(False),
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        recAlgoConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doVdriftCorr = cms.bool(True),
            maxTime = cms.double(420.0),
            minTime = cms.double(-3.0),
            stepTwoFromDigi = cms.bool(False),
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            tTrigModeConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doT0Correction = cms.bool(True),
                doTOFCorrection = cms.bool(True),
                doWirePropCorrection = cms.bool(True),
                tTrigLabel = cms.string(''),
                tofCorrType = cms.int32(0),
                vPropWire = cms.double(24.4),
                wirePropCorrType = cms.int32(0)
            ),
            useUncertDB = cms.bool(True)
        ),
        segmCleanerMode = cms.int32(2)
    ),
    Reco4DAlgoName = cms.string('DTCombinatorialPatternReco4D'),
    debug = cms.untracked.bool(False),
    recHits1DLabel = cms.InputTag("hltDt1DRecHits"),
    recHits2DLabel = cms.InputTag("dt2DSegments")
)


process.hltEcalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("hltEcalDigis"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = cms.InputTag("hltEcalDigis"),
    integrityBlockSizeErrors = cms.InputTag("hltEcalDigis","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityTTIdErrors")
)


process.hltEcalDigis = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
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
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
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
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.hltEcalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    ESdigiCollection = cms.string(''),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    debugMode = cms.untracked.bool(False),
    sourceTag = cms.InputTag("rawDataCollector")
)


process.hltEcalPreshowerRecHit = cms.EDProducer("ESRecHitProducer",
    ESRecoAlgo = cms.int32(0),
    ESdigiCollection = cms.InputTag("hltEcalPreshowerDigis"),
    ESrechitCollection = cms.string('EcalRecHitsES'),
    algo = cms.string('ESRecHitWorker')
)


process.hltEcalRecHit = cms.EDProducer("EcalRecHitProducer",
    ChannelStatusToBeExcluded = cms.vstring(),
    EBLaserMAX = cms.double(3.0),
    EBLaserMIN = cms.double(0.5),
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    EBuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEB"),
    EELaserMAX = cms.double(8.0),
    EELaserMIN = cms.double(0.5),
    EErechitCollection = cms.string('EcalRecHitsEE'),
    EEuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEE"),
    algo = cms.string('EcalRecHitWorkerSimple'),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    cleaningConfig = cms.PSet(
        cThreshold_barrel = cms.double(4.0),
        cThreshold_double = cms.double(10.0),
        cThreshold_endcap = cms.double(15.0),
        e4e1Threshold_barrel = cms.double(0.08),
        e4e1Threshold_endcap = cms.double(0.3),
        e4e1_a_barrel = cms.double(0.04),
        e4e1_a_endcap = cms.double(0.02),
        e4e1_b_barrel = cms.double(-0.024),
        e4e1_b_endcap = cms.double(-0.0125),
        e6e2thresh = cms.double(0.04),
        ignoreOutOfTimeThresh = cms.double(1000000000.0),
        tightenCrack_e1_double = cms.double(2.0),
        tightenCrack_e1_single = cms.double(2.0),
        tightenCrack_e4e1_single = cms.double(3.0),
        tightenCrack_e6e2_double = cms.double(3.0)
    ),
    dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
    dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
    ebDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebDetId"),
    ebFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebFE"),
    eeDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeDetId"),
    eeFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeFE"),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring('kOk', 
            'kDAC', 
            'kNoLaser', 
            'kNoisy'),
        kNeighboursRecovered = cms.vstring('kFixedG0', 
            'kNonRespondingIsolated', 
            'kDeadVFE'),
        kNoisy = cms.vstring('kNNoisy', 
            'kFixedG6', 
            'kFixedG1'),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    killDeadChannels = cms.bool(True),
    laserCorrection = cms.bool(True),
    logWarningEtThreshold_EB_FE = cms.double(50.0),
    logWarningEtThreshold_EE_FE = cms.double(50.0),
    recoverEBFE = cms.bool(True),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    recoverEEFE = cms.bool(True),
    recoverEEIsolatedChannels = cms.bool(False),
    recoverEEVFE = cms.bool(False),
    singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
    singleChannelRecoveryThreshold = cms.double(8.0),
    triggerPrimitiveDigiCollection = cms.InputTag("hltEcalDigis","EcalTriggerPrimitives")
)


process.hltEcalUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("hltEcalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = cms.InputTag("hltEcalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
    algoPSet = cms.PSet(
        EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
        EBtimeConstantTerm = cms.double(0.6),
        EBtimeFitLimits_Lower = cms.double(0.2),
        EBtimeFitLimits_Upper = cms.double(1.4),
        EBtimeFitParameters = cms.vdouble(-2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 
            91.01147, -50.35761, 11.05621),
        EBtimeNconst = cms.double(28.5),
        EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
        EEtimeConstantTerm = cms.double(1.0),
        EEtimeFitLimits_Lower = cms.double(0.2),
        EEtimeFitLimits_Upper = cms.double(1.4),
        EEtimeFitParameters = cms.vdouble(-2.390548, 3.553628, -17.62341, 67.67538, -133.213, 
            140.7432, -75.41106, 16.20277),
        EEtimeNconst = cms.double(31.8),
        activeBXs = cms.vint32(-5, -4, -3, -2, -1, 
            0, 1, 2, 3, 4),
        ampErrorCalculation = cms.bool(False),
        amplitudeThresholdEB = cms.double(10.0),
        amplitudeThresholdEE = cms.double(10.0),
        chi2ThreshEB_ = cms.double(65.0),
        chi2ThreshEE_ = cms.double(50.0),
        doPrefitEB = cms.bool(True),
        doPrefitEE = cms.bool(True),
        ebSpikeThreshold = cms.double(1.042),
        kPoorRecoFlagEB = cms.bool(True),
        kPoorRecoFlagEE = cms.bool(False),
        outOfTimeThresholdGain12mEB = cms.double(5.0),
        outOfTimeThresholdGain12mEE = cms.double(1000.0),
        outOfTimeThresholdGain12pEB = cms.double(5.0),
        outOfTimeThresholdGain12pEE = cms.double(1000.0),
        outOfTimeThresholdGain61mEB = cms.double(5.0),
        outOfTimeThresholdGain61mEE = cms.double(1000.0),
        outOfTimeThresholdGain61pEB = cms.double(5.0),
        outOfTimeThresholdGain61pEE = cms.double(1000.0),
        prefitMaxChiSqEB = cms.double(100.0),
        prefitMaxChiSqEE = cms.double(10.0),
        timealgo = cms.string('None'),
        useLumiInfoRunHeader = cms.bool(False)
    )
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


process.hltGtDigis = cms.EDProducer("L1GlobalTriggerRawToDigi",
    ActiveBoardsMask = cms.uint32(65535),
    DaqGtFedId = cms.untracked.int32(813),
    DaqGtInputTag = cms.InputTag("rawDataCollector"),
    UnpackBxInEvent = cms.int32(5),
    Verbosity = cms.untracked.int32(0)
)


process.hltHbhereco = cms.EDProducer("HcalHitReconstructor",
    HFInWindowStat = cms.PSet(

    ),
    PETstat = cms.PSet(

    ),
    S8S1stat = cms.PSet(

    ),
    S9S1stat = cms.PSet(

    ),
    Subdetector = cms.string('HBHE'),
    applyPedConstraint = cms.bool(True),
    applyPulseJitter = cms.bool(False),
    applyTimeConstraint = cms.bool(True),
    applyTimeSlew = cms.bool(True),
    applyUnconstrainedFit = cms.bool(False),
    chargeMax = cms.double(6.0),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(False),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hltHcalDigis"),
    digiTimeFromDB = cms.bool(True),
    digistat = cms.PSet(

    ),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    fitTimes = cms.int32(1),
    flagParameters = cms.PSet(
        hitEnergyMinimum = cms.double(1.0),
        hitMultiplicityThreshold = cms.int32(17),
        nominalPedestal = cms.double(3.0),
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
    hfTimingTrustParameters = cms.PSet(

    ),
    hscpParameters = cms.PSet(
        TimingEnergyThreshold = cms.double(30.0),
        fracLeaderMax = cms.double(0.7),
        fracLeaderMin = cms.double(0.4),
        outerMax = cms.double(0.1),
        outerMin = cms.double(0.0),
        r1Max = cms.double(1.0),
        r1Min = cms.double(0.15),
        r2Max = cms.double(0.5),
        r2Min = cms.double(0.1),
        slopeMax = cms.double(-0.6),
        slopeMin = cms.double(-1.5)
    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    meanPed = cms.double(0.0),
    meanTime = cms.double(-2.5),
    negativeParameters = cms.PSet(
        Cut = cms.vdouble(-50.0, -100.0, -100.0, -100.0, -100.0, 
            -100.0),
        First = cms.int32(4),
        Last = cms.int32(6),
        MinimumChargeThreshold = cms.double(20.0),
        TS4TS5ChargeThreshold = cms.double(70.0),
        Threshold = cms.vdouble(100.0, 120.0, 160.0, 200.0, 300.0, 
            500.0)
    ),
    noise = cms.double(1.0),
    pedSigma = cms.double(0.5),
    puCorrMethod = cms.int32(0),
    pulseJitter = cms.double(1.0),
    pulseShapeParameters = cms.PSet(

    ),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(False),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(False),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(False),
    setTimingShapedCutsFlags = cms.bool(False),
    setTimingTrustFlags = cms.bool(False),
    timeMax = cms.double(10.0),
    timeMin = cms.double(-15.0),
    timeSigma = cms.double(5.0),
    timingshapedcutsParameters = cms.PSet(
        ignorehighest = cms.bool(False),
        ignorelowest = cms.bool(True),
        tfilterEnvelope = cms.vdouble(4.0, 12.04, 13.0, 10.56, 23.5, 
            8.82, 37.0, 7.38, 56.0, 6.3, 
            81.0, 5.64, 114.5, 5.44, 175.5, 
            5.38, 350.5, 5.14),
        win_gain = cms.double(1.0),
        win_offset = cms.double(0.0)
    ),
    ts345chi2 = cms.double(100.0),
    ts3chi2 = cms.double(5.0),
    ts4Max = cms.double(500.0),
    ts4Min = cms.double(5.0),
    ts4chi2 = cms.double(15.0),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hltHcalDigis = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(False),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    silent = cms.untracked.bool(True)
)


process.hltHfreco = cms.EDProducer("HcalHitReconstructor",
    HFInWindowStat = cms.PSet(
        hflongEthresh = cms.double(40.0),
        hflongMaxWindowTime = cms.vdouble(10.0),
        hflongMinWindowTime = cms.vdouble(-10.0),
        hfshortEthresh = cms.double(40.0),
        hfshortMaxWindowTime = cms.vdouble(10.0),
        hfshortMinWindowTime = cms.vdouble(-12.0)
    ),
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        flagsToSkip = cms.int32(0),
        longETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        longEnergyParams = cms.vdouble(43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        shortEnergyParams = cms.vdouble(35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        flagsToSkip = cms.int32(16),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        longEnergyParams = cms.vdouble(40.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0),
        long_optimumSlope = cms.vdouble(0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1),
        shortETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        shortEnergyParams = cms.vdouble(40.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0),
        short_optimumSlope = cms.vdouble(0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1)
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        flagsToSkip = cms.int32(24),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        longEnergyParams = cms.vdouble(43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62),
        long_optimumSlope = cms.vdouble(-99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927),
        shortETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        shortEnergyParams = cms.vdouble(35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093),
        short_optimumSlope = cms.vdouble(-99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927)
    ),
    Subdetector = cms.string('HF'),
    applyPedConstraint = cms.bool(True),
    applyPulseJitter = cms.bool(False),
    applyTimeConstraint = cms.bool(True),
    applyTimeSlew = cms.bool(True),
    applyUnconstrainedFit = cms.bool(False),
    chargeMax = cms.double(6.0),
    correctForPhaseContainment = cms.bool(False),
    correctForTimeslew = cms.bool(False),
    correctTiming = cms.bool(False),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hltHcalDigis"),
    digiTimeFromDB = cms.bool(True),
    digistat = cms.PSet(
        HFdigiflagCoef = cms.vdouble(0.93, -0.012667, -0.38275),
        HFdigiflagExpectedPeak = cms.int32(2),
        HFdigiflagFirstSample = cms.int32(1),
        HFdigiflagMinEthreshold = cms.double(40.0),
        HFdigiflagSamplesToAdd = cms.int32(3)
    ),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(1),
    firstSample = cms.int32(2),
    fitTimes = cms.int32(1),
    flagParameters = cms.PSet(

    ),
    hfTimingTrustParameters = cms.PSet(
        hfTimingTrustLevel1 = cms.int32(1),
        hfTimingTrustLevel2 = cms.int32(4)
    ),
    hscpParameters = cms.PSet(

    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    meanPed = cms.double(0.0),
    meanTime = cms.double(-2.5),
    negativeParameters = cms.PSet(
        Cut = cms.vdouble(-50.0, -100.0, -100.0, -100.0, -100.0, 
            -100.0),
        First = cms.int32(4),
        Last = cms.int32(6),
        MinimumChargeThreshold = cms.double(20.0),
        TS4TS5ChargeThreshold = cms.double(70.0),
        Threshold = cms.vdouble(100.0, 120.0, 160.0, 200.0, 300.0, 
            500.0)
    ),
    noise = cms.double(1.0),
    pedSigma = cms.double(0.5),
    puCorrMethod = cms.int32(0),
    pulseJitter = cms.double(1.0),
    pulseShapeParameters = cms.PSet(

    ),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(2),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(False),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(False),
    setTimingShapedCutsFlags = cms.bool(False),
    setTimingTrustFlags = cms.bool(False),
    timeMax = cms.double(10.0),
    timeMin = cms.double(-15.0),
    timeSigma = cms.double(5.0),
    timingshapedcutsParameters = cms.PSet(

    ),
    ts345chi2 = cms.double(100.0),
    ts3chi2 = cms.double(5.0),
    ts4Max = cms.double(500.0),
    ts4Min = cms.double(5.0),
    ts4chi2 = cms.double(15.0),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hltHoreco = cms.EDProducer("HcalHitReconstructor",
    HFInWindowStat = cms.PSet(

    ),
    PETstat = cms.PSet(

    ),
    S8S1stat = cms.PSet(

    ),
    S9S1stat = cms.PSet(

    ),
    Subdetector = cms.string('HO'),
    applyPedConstraint = cms.bool(True),
    applyPulseJitter = cms.bool(False),
    applyTimeConstraint = cms.bool(True),
    applyTimeSlew = cms.bool(True),
    applyUnconstrainedFit = cms.bool(False),
    chargeMax = cms.double(6.0),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(False),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hltHcalDigis"),
    digiTimeFromDB = cms.bool(True),
    digistat = cms.PSet(

    ),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    fitTimes = cms.int32(1),
    flagParameters = cms.PSet(

    ),
    hfTimingTrustParameters = cms.PSet(

    ),
    hscpParameters = cms.PSet(

    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    meanPed = cms.double(0.0),
    meanTime = cms.double(-2.5),
    negativeParameters = cms.PSet(
        Cut = cms.vdouble(-50.0, -100.0, -100.0, -100.0, -100.0, 
            -100.0),
        First = cms.int32(4),
        Last = cms.int32(6),
        MinimumChargeThreshold = cms.double(20.0),
        TS4TS5ChargeThreshold = cms.double(70.0),
        Threshold = cms.vdouble(100.0, 120.0, 160.0, 200.0, 300.0, 
            500.0)
    ),
    noise = cms.double(1.0),
    pedSigma = cms.double(0.5),
    puCorrMethod = cms.int32(0),
    pulseJitter = cms.double(1.0),
    pulseShapeParameters = cms.PSet(

    ),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(False),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(False),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(False),
    setTimingShapedCutsFlags = cms.bool(False),
    setTimingTrustFlags = cms.bool(False),
    timeMax = cms.double(10.0),
    timeMin = cms.double(-15.0),
    timeSigma = cms.double(5.0),
    timingshapedcutsParameters = cms.PSet(

    ),
    ts345chi2 = cms.double(100.0),
    ts3chi2 = cms.double(5.0),
    ts4Max = cms.double(500.0),
    ts4Min = cms.double(5.0),
    ts4chi2 = cms.double(15.0),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hltHtMht = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK4CaloJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    maxEtaJetMht = cms.double(5.0),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(40.0),
    minPtJetMht = cms.double(30.0),
    pfCandidatesLabel = cms.InputTag(""),
    usePt = cms.bool(False)
)


process.hltHtMht4Jet = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK4CaloJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    maxEtaJetMht = cms.double(5.0),
    minNJetHt = cms.int32(4),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(40.0),
    minPtJetMht = cms.double(30.0),
    pfCandidatesLabel = cms.InputTag(""),
    usePt = cms.bool(False)
)


process.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag("hltPixelTracks"),
    InputVertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(False),
    useProtoTrackKinematics = cms.bool(False)
)


process.hltIter0PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    src = cms.InputTag("hltIter0PFLowPixelSeedsFromPixelTracks"),
    useHitsSplitting = cms.bool(False)
)


process.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter0'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter0PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter0PFlowTrackSelectionHighPurity = cms.EDProducer("AnalyticalTrackSelector",
    applyAbsCutsIfNoPV = cms.bool(False),
    applyAdaptedPVCuts = cms.bool(True),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    chi2n_no1Dmod_par = cms.double(9999.0),
    chi2n_par = cms.double(0.7),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(True),
    d0_par1 = cms.vdouble(0.3, 4.0),
    d0_par2 = cms.vdouble(0.4, 4.0),
    dz_par1 = cms.vdouble(0.35, 4.0),
    dz_par2 = cms.vdouble(0.4, 4.0),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(1),
    max_d0 = cms.double(100.0),
    max_d0NoPV = cms.double(100.0),
    max_eta = cms.double(9999.0),
    max_lostHitFraction = cms.double(1.0),
    max_minMissHitOutOrIn = cms.int32(99),
    max_relpterr = cms.double(9999.0),
    max_z0 = cms.double(100.0),
    max_z0NoPV = cms.double(100.0),
    minHitsToBypassChecks = cms.uint32(20),
    minNumber3DLayers = cms.uint32(0),
    minNumberLayers = cms.uint32(3),
    min_eta = cms.double(-9999.0),
    min_nhits = cms.uint32(0),
    nSigmaZ = cms.double(3.0),
    qualityBit = cms.string('highPurity'),
    res_par = cms.vdouble(0.003, 0.001),
    src = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks"),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertexCut = cms.string('tracksSize>=3'),
    vertices = cms.InputTag("hltTrimmedPixelVertices"),
    vtxNumber = cms.int32(-1)
)


process.hltIter0TrackAndTauJets4Iter1 = cms.EDProducer("TauJetSelectorForHLTTrackSeeding",
    etaMaxCaloJet = cms.double(2.7),
    etaMinCaloJet = cms.double(-2.7),
    fractionMaxChargedPUInCaloCone = cms.double(0.3),
    fractionMinCaloInTauCone = cms.double(0.7),
    inputCaloJetTag = cms.InputTag("hltAK4CaloJetsPFEt5"),
    inputTrackJetTag = cms.InputTag("hltAK4Iter0TrackJets4Iter1"),
    inputTrackTag = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity"),
    isolationConeSize = cms.double(0.5),
    nTrkMaxInCaloCone = cms.int32(0),
    ptMinCaloJet = cms.double(5.0),
    ptTrkMaxInCaloCone = cms.double(1.0),
    tauConeSize = cms.double(0.2)
)


process.hltIter1ClustersRefRemoval = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("hltSiPixelClusters"),
    stripClusters = cms.InputTag("hltSiStripRawToClustersFacility"),
    trajectories = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity")
)


process.hltIter1MaskedMeasurementTrackerEvent = cms.EDProducer("MaskedMeasurementTrackerEventProducer",
    OnDemand = cms.bool(False),
    clustersToSkip = cms.InputTag("hltIter1ClustersRefRemoval"),
    src = cms.InputTag("hltSiStripClusters")
)


process.hltIter1Merged = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltIter0PFlowTrackSelectionHighPurity", "hltIter1PFlowTrackSelectionHighPurity"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltIter0PFlowTrackSelectionHighPurity", "hltIter1PFlowTrackSelectionHighPurity"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltIter1PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltIter1MaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    src = cms.InputTag("hltIter1PFlowPixelSeeds"),
    useHitsSplitting = cms.bool(False)
)


process.hltIter1PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter1'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltIter1MaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter1PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter1PFlowPixelSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("hltSiStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(50000),
        MaxNumberOfPixelClusters = cms.uint32(10000),
        PixelClusterCollectionLabel = cms.InputTag("hltSiPixelClusters"),
        doClusterCheck = cms.bool(False)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            ComponentName = cms.string('PixelTripletHLTGenerator'),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            extraHitRZtolerance = cms.double(0.037),
            maxElement = cms.uint32(100000),
            phiPreFiltering = cms.double(0.3),
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            useMultScattering = cms.bool(True)
        ),
        SeedingLayers = cms.InputTag("hltIter1PixelLayerTriplets"),
        maxElement = cms.uint32(0)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('CandidateSeededTrackingRegionsProducer'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            deltaEta = cms.double(1.0),
            deltaPhi = cms.double(1.0),
            input = cms.InputTag("hltIter0TrackAndTauJets4Iter1"),
            maxNRegions = cms.int32(100),
            maxNVertices = cms.int32(10),
            measurementTrackerName = cms.string('hltIter1MaskedMeasurementTrackerEvent'),
            mode = cms.string('VerticesFixed'),
            nSigmaZBeamSpot = cms.double(3.0),
            originRadius = cms.double(0.05),
            precise = cms.bool(True),
            ptMin = cms.double(0.5),
            searchOpt = cms.bool(True),
            vertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
            zErrorBeamSpot = cms.double(15.0),
            zErrorVetex = cms.double(0.1)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromConsecutiveHitsTripletOnlyCreator')
    )
)


process.hltIter1PFlowTrackSelectionHighPurity = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltIter1PFlowTrackSelectionHighPurityLoose", "hltIter1PFlowTrackSelectionHighPurityTight"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltIter1PFlowTrackSelectionHighPurityLoose", "hltIter1PFlowTrackSelectionHighPurityTight"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltIter1PFlowTrackSelectionHighPurityLoose = cms.EDProducer("AnalyticalTrackSelector",
    applyAbsCutsIfNoPV = cms.bool(False),
    applyAdaptedPVCuts = cms.bool(True),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    chi2n_no1Dmod_par = cms.double(9999.0),
    chi2n_par = cms.double(0.7),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(True),
    d0_par1 = cms.vdouble(0.85, 3.0),
    d0_par2 = cms.vdouble(0.9, 3.0),
    dz_par1 = cms.vdouble(0.8, 3.0),
    dz_par2 = cms.vdouble(0.9, 3.0),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(1),
    max_d0 = cms.double(100.0),
    max_d0NoPV = cms.double(100.0),
    max_eta = cms.double(9999.0),
    max_lostHitFraction = cms.double(1.0),
    max_minMissHitOutOrIn = cms.int32(99),
    max_relpterr = cms.double(9999.0),
    max_z0 = cms.double(100.0),
    max_z0NoPV = cms.double(100.0),
    minHitsToBypassChecks = cms.uint32(20),
    minNumber3DLayers = cms.uint32(0),
    minNumberLayers = cms.uint32(3),
    min_eta = cms.double(-9999.0),
    min_nhits = cms.uint32(0),
    nSigmaZ = cms.double(3.0),
    qualityBit = cms.string('highPurity'),
    res_par = cms.vdouble(0.003, 0.001),
    src = cms.InputTag("hltIter1PFlowCtfWithMaterialTracks"),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertexCut = cms.string('tracksSize>=3'),
    vertices = cms.InputTag("hltTrimmedPixelVertices"),
    vtxNumber = cms.int32(-1)
)


process.hltIter1PFlowTrackSelectionHighPurityTight = cms.EDProducer("AnalyticalTrackSelector",
    applyAbsCutsIfNoPV = cms.bool(False),
    applyAdaptedPVCuts = cms.bool(True),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    chi2n_no1Dmod_par = cms.double(9999.0),
    chi2n_par = cms.double(0.4),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(True),
    d0_par1 = cms.vdouble(1.0, 4.0),
    d0_par2 = cms.vdouble(1.0, 4.0),
    dz_par1 = cms.vdouble(1.0, 4.0),
    dz_par2 = cms.vdouble(1.0, 4.0),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(1),
    max_d0 = cms.double(100.0),
    max_d0NoPV = cms.double(100.0),
    max_eta = cms.double(9999.0),
    max_lostHitFraction = cms.double(1.0),
    max_minMissHitOutOrIn = cms.int32(99),
    max_relpterr = cms.double(9999.0),
    max_z0 = cms.double(100.0),
    max_z0NoPV = cms.double(100.0),
    minHitsToBypassChecks = cms.uint32(20),
    minNumber3DLayers = cms.uint32(0),
    minNumberLayers = cms.uint32(5),
    min_eta = cms.double(-9999.0),
    min_nhits = cms.uint32(0),
    nSigmaZ = cms.double(3.0),
    qualityBit = cms.string('highPurity'),
    res_par = cms.vdouble(0.003, 0.001),
    src = cms.InputTag("hltIter1PFlowCtfWithMaterialTracks"),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertexCut = cms.string('tracksSize>=3'),
    vertices = cms.InputTag("hltTrimmedPixelVertices"),
    vtxNumber = cms.int32(-1)
)


process.hltIter1PixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg')
)


process.hltIter1TrackAndTauJets4Iter2 = cms.EDProducer("TauJetSelectorForHLTTrackSeeding",
    etaMaxCaloJet = cms.double(2.7),
    etaMinCaloJet = cms.double(-2.7),
    fractionMaxChargedPUInCaloCone = cms.double(0.3),
    fractionMinCaloInTauCone = cms.double(0.7),
    inputCaloJetTag = cms.InputTag("hltAK4CaloJetsPFEt5"),
    inputTrackJetTag = cms.InputTag("hltAK4Iter1TrackJets4Iter2"),
    inputTrackTag = cms.InputTag("hltIter1Merged"),
    isolationConeSize = cms.double(0.5),
    nTrkMaxInCaloCone = cms.int32(0),
    ptMinCaloJet = cms.double(5.0),
    ptTrkMaxInCaloCone = cms.double(1.4),
    tauConeSize = cms.double(0.2)
)


process.hltIter1TrackRefsForJets4Iter2 = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltIter1Merged")
)


process.hltIter2ClustersRefRemoval = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(16.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("hltIter1ClustersRefRemoval"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("hltSiPixelClusters"),
    stripClusters = cms.InputTag("hltSiStripRawToClustersFacility"),
    trajectories = cms.InputTag("hltIter1PFlowTrackSelectionHighPurity")
)


process.hltIter2MaskedMeasurementTrackerEvent = cms.EDProducer("MaskedMeasurementTrackerEventProducer",
    OnDemand = cms.bool(False),
    clustersToSkip = cms.InputTag("hltIter2ClustersRefRemoval"),
    src = cms.InputTag("hltSiStripClusters")
)


process.hltIter2Merged = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltIter1Merged", "hltIter2PFlowTrackSelectionHighPurity"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltIter1Merged", "hltIter2PFlowTrackSelectionHighPurity"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltIter2PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltIter2MaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    src = cms.InputTag("hltIter2PFlowPixelSeeds"),
    useHitsSplitting = cms.bool(False)
)


process.hltIter2PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter2'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltIter2MaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter2PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter2PFlowPixelSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("hltSiStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(50000),
        MaxNumberOfPixelClusters = cms.uint32(10000),
        PixelClusterCollectionLabel = cms.InputTag("hltSiPixelClusters"),
        doClusterCheck = cms.bool(False)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitPairGenerator'),
        GeneratorPSet = cms.PSet(
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            maxElement = cms.uint32(100000)
        ),
        SeedingLayers = cms.InputTag("hltIter2PixelLayerPairs"),
        maxElement = cms.uint32(0)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('CandidateSeededTrackingRegionsProducer'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            deltaEta = cms.double(0.8),
            deltaPhi = cms.double(0.8),
            input = cms.InputTag("hltIter1TrackAndTauJets4Iter2"),
            maxNRegions = cms.int32(100),
            maxNVertices = cms.int32(10),
            measurementTrackerName = cms.string('hltIter2MaskedMeasurementTrackerEvent'),
            mode = cms.string('VerticesFixed'),
            nSigmaZBeamSpot = cms.double(3.0),
            originRadius = cms.double(0.025),
            originZPos = cms.double(0.0),
            precise = cms.bool(True),
            ptMin = cms.double(1.2),
            searchOpt = cms.bool(True),
            vertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
            zErrorBeamSpot = cms.double(15.0),
            zErrorVetex = cms.double(0.05)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromConsecutiveHitsCreatorIT')
    )
)


process.hltIter2PFlowTrackSelectionHighPurity = cms.EDProducer("AnalyticalTrackSelector",
    applyAbsCutsIfNoPV = cms.bool(False),
    applyAdaptedPVCuts = cms.bool(True),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    chi2n_no1Dmod_par = cms.double(9999.0),
    chi2n_par = cms.double(0.7),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(True),
    d0_par1 = cms.vdouble(0.3, 4.0),
    d0_par2 = cms.vdouble(0.4, 4.0),
    dz_par1 = cms.vdouble(0.35, 4.0),
    dz_par2 = cms.vdouble(0.4, 4.0),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(1),
    max_d0 = cms.double(100.0),
    max_d0NoPV = cms.double(100.0),
    max_eta = cms.double(9999.0),
    max_lostHitFraction = cms.double(1.0),
    max_minMissHitOutOrIn = cms.int32(99),
    max_relpterr = cms.double(9999.0),
    max_z0 = cms.double(100.0),
    max_z0NoPV = cms.double(100.0),
    minHitsToBypassChecks = cms.uint32(20),
    minNumber3DLayers = cms.uint32(0),
    minNumberLayers = cms.uint32(3),
    min_eta = cms.double(-9999.0),
    min_nhits = cms.uint32(0),
    nSigmaZ = cms.double(3.0),
    qualityBit = cms.string('highPurity'),
    res_par = cms.vdouble(0.003, 0.001),
    src = cms.InputTag("hltIter2PFlowCtfWithMaterialTracks"),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertexCut = cms.string('tracksSize>=3'),
    vertices = cms.InputTag("hltTrimmedPixelVertices"),
    vtxNumber = cms.int32(-1)
)


process.hltIter2PixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
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
        'FPix1_neg+FPix2_neg')
)


process.hltL1GtObjectMap = cms.EDProducer("L1GlobalTrigger",
    AlgorithmTriggersUnmasked = cms.bool(False),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    AlternativeNrBxBoardDaq = cms.uint32(0),
    AlternativeNrBxBoardEvm = cms.uint32(0),
    BstLengthBytes = cms.int32(-1),
    CastorInputTag = cms.InputTag("castorL1Digis"),
    EmulateBxInEvent = cms.int32(1),
    GctInputTag = cms.InputTag("hltCaloStage1LegacyFormatDigis"),
    GmtInputTag = cms.InputTag("hltGtDigis"),
    ProduceL1GtDaqRecord = cms.bool(False),
    ProduceL1GtEvmRecord = cms.bool(False),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    ReadTechnicalTriggerRecords = cms.bool(True),
    RecordLength = cms.vint32(3, 0),
    TechnicalTriggersInputTags = cms.VInputTag("simBscDigis"),
    TechnicalTriggersUnmasked = cms.bool(False),
    TechnicalTriggersUnprescaled = cms.bool(True),
    TechnicalTriggersVetoUnmasked = cms.bool(True),
    WritePsbL1GtDaqRecord = cms.bool(False)
)


process.hltL1extraParticles = cms.EDProducer("L1ExtraParticlesProd",
    centralBxOnly = cms.bool(True),
    centralJetSource = cms.InputTag("hltCaloStage1LegacyFormatDigis","cenJets"),
    etHadSource = cms.InputTag("hltCaloStage1LegacyFormatDigis"),
    etMissSource = cms.InputTag("hltCaloStage1LegacyFormatDigis"),
    etTotalSource = cms.InputTag("hltCaloStage1LegacyFormatDigis"),
    forwardJetSource = cms.InputTag("hltCaloStage1LegacyFormatDigis","forJets"),
    hfRingBitCountsSource = cms.InputTag("hltCaloStage1LegacyFormatDigis"),
    hfRingEtSumsSource = cms.InputTag("hltCaloStage1LegacyFormatDigis"),
    htMissSource = cms.InputTag("hltCaloStage1LegacyFormatDigis"),
    ignoreHtMiss = cms.bool(False),
    isoTauJetSource = cms.InputTag("hltCaloStage1LegacyFormatDigis","isoTauJets"),
    isolatedEmSource = cms.InputTag("hltCaloStage1LegacyFormatDigis","isoEm"),
    muonSource = cms.InputTag("hltGtDigis"),
    nonIsolatedEmSource = cms.InputTag("hltCaloStage1LegacyFormatDigis","nonIsoEm"),
    produceCaloParticles = cms.bool(True),
    produceMuonParticles = cms.bool(True),
    tauJetSource = cms.InputTag("hltCaloStage1LegacyFormatDigis","tauJets")
)


process.hltL2MuonCandidates = cms.EDProducer("L2MuonCandidateProducer",
    InputObjects = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL2MuonSeeds = cms.EDProducer("L2MuonSeedGenerator",
    GMTReadoutCollection = cms.InputTag("hltGtDigis"),
    InputObjects = cms.InputTag("hltL1extraParticles"),
    L1MaxEta = cms.double(2.5),
    L1MinPt = cms.double(0.0),
    L1MinQuality = cms.uint32(1),
    OfflineSeedLabel = cms.untracked.InputTag("hltL2OfflineMuonSeeds"),
    Propagator = cms.string('SteppingHelixPropagatorAny'),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    UseOfflineSeed = cms.untracked.bool(True),
    UseUnassociatedL1 = cms.bool(False)
)


process.hltL2Muons = cms.EDProducer("L2MuonProducer",
    DoSeedRefit = cms.bool(False),
    InputObjects = cms.InputTag("hltL2MuonSeeds"),
    L2TrajBuilderParameters = cms.PSet(
        BWFilterParameters = cms.PSet(
            BWSeedType = cms.string('fromGenerator'),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('outsideIn'),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits")
        ),
        DoBackwardFilter = cms.bool(True),
        DoRefit = cms.bool(False),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('insideOut'),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits")
        ),
        NavigationType = cms.string('Standard'),
        SeedPosition = cms.string('in'),
        SeedPropagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            NMinRecHits = cms.uint32(2),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RescaleError = cms.double(100.0),
            UseSubRecHits = cms.bool(False)
        )
    ),
    MuonTrajectoryBuilder = cms.string('Exhaustive'),
    SeedTransformerParameters = cms.PSet(
        Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        NMinRecHits = cms.uint32(2),
        Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        RescaleError = cms.double(100.0),
        UseSubRecHits = cms.bool(False)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny', 
            'hltESPFastSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPosition = cms.vdouble(0.0, 0.0, 0.0),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(True),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL2OfflineMuonSeeds = cms.EDProducer("MuonSeedGenerator",
    CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
    CSC_01 = cms.vdouble(0.166, 0.0, 0.0, 0.031, 0.0, 
        0.0),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    CSC_02 = cms.vdouble(0.612, -0.207, 0.0, 0.067, -0.001, 
        0.0),
    CSC_03 = cms.vdouble(0.787, -0.338, 0.029, 0.101, -0.008, 
        0.0),
    CSC_12 = cms.vdouble(-0.161, 0.254, -0.047, 0.042, -0.007, 
        0.0),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    CSC_13 = cms.vdouble(0.901, -1.302, 0.533, 0.045, 0.005, 
        0.0),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    CSC_14 = cms.vdouble(0.606, -0.181, -0.002, 0.111, -0.003, 
        0.0),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    CSC_23 = cms.vdouble(-0.081, 0.113, -0.029, 0.015, 0.008, 
        0.0),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    CSC_24 = cms.vdouble(0.004, 0.021, -0.002, 0.053, 0.0, 
        0.0),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_34 = cms.vdouble(0.062, -0.067, 0.019, 0.021, 0.003, 
        0.0),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
    DT_12 = cms.vdouble(0.183, 0.054, -0.087, 0.028, 0.002, 
        0.0),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    DT_13 = cms.vdouble(0.315, 0.068, -0.127, 0.051, -0.002, 
        0.0),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    DT_14 = cms.vdouble(0.359, 0.052, -0.107, 0.072, -0.004, 
        0.0),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    DT_23 = cms.vdouble(0.13, 0.023, -0.057, 0.028, 0.004, 
        0.0),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    DT_24 = cms.vdouble(0.176, 0.014, -0.051, 0.051, 0.003, 
        0.0),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    DT_34 = cms.vdouble(0.044, 0.004, -0.013, 0.029, 0.003, 
        0.0),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    EnableCSCMeasurement = cms.bool(True),
    EnableDTMeasurement = cms.bool(True),
    OL_1213 = cms.vdouble(0.96, -0.737, 0.0, 0.052, 0.0, 
        0.0),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    OL_1222 = cms.vdouble(0.848, -0.591, 0.0, 0.062, 0.0, 
        0.0),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    OL_1232 = cms.vdouble(0.184, 0.0, 0.0, 0.066, 0.0, 
        0.0),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    OL_2213 = cms.vdouble(0.117, 0.0, 0.0, 0.044, 0.0, 
        0.0),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    OL_2222 = cms.vdouble(0.107, 0.0, 0.0, 0.04, 0.0, 
        0.0),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    SMB_10 = cms.vdouble(1.387, -0.038, 0.0, 0.19, 0.0, 
        0.0),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    SMB_11 = cms.vdouble(1.247, 0.72, -0.802, 0.229, -0.075, 
        0.0),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    SMB_12 = cms.vdouble(2.128, -0.956, 0.0, 0.199, 0.0, 
        0.0),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SMB_20 = cms.vdouble(1.011, -0.052, 0.0, 0.188, 0.0, 
        0.0),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    SMB_21 = cms.vdouble(1.043, -0.124, 0.0, 0.183, 0.0, 
        0.0),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    SMB_22 = cms.vdouble(1.474, -0.758, 0.0, 0.185, 0.0, 
        0.0),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    SMB_30 = cms.vdouble(0.505, -0.022, 0.0, 0.215, 0.0, 
        0.0),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    SMB_31 = cms.vdouble(0.549, -0.145, 0.0, 0.207, 0.0, 
        0.0),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    SMB_32 = cms.vdouble(0.67, -0.327, 0.0, 0.22, 0.0, 
        0.0),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    SME_11 = cms.vdouble(3.295, -1.527, 0.112, 0.378, 0.02, 
        0.0),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SME_12 = cms.vdouble(0.102, 0.599, 0.0, 0.38, 0.0, 
        0.0),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    SME_13 = cms.vdouble(-1.286, 1.711, 0.0, 0.356, 0.0, 
        0.0),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SME_21 = cms.vdouble(-0.529, 1.194, -0.358, 0.472, 0.086, 
        0.0),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    SME_22 = cms.vdouble(-1.207, 1.491, -0.251, 0.189, 0.243, 
        0.0),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    SME_31 = cms.vdouble(-1.594, 1.482, -0.317, 0.487, 0.097, 
        0.0),
    SME_32 = cms.vdouble(-0.901, 1.333, -0.47, 0.41, 0.073, 
        0.0),
    SME_41 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    SME_42 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    beamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    crackEtas = cms.vdouble(0.2, 1.6, 1.7),
    crackWindow = cms.double(0.04),
    deltaEtaCrackSearchWindow = cms.double(0.25),
    deltaEtaSearchWindow = cms.double(0.2),
    deltaPhiSearchWindow = cms.double(0.25),
    scaleDT = cms.bool(True)
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
    L3TrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutRPC = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            DYTthrs = cms.vint32(30, 15),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(0.001),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            DeltaR = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            EscapePt = cms.double(1.5),
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            Eta_fixed = cms.double(0.2),
            Eta_min = cms.double(0.05),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            OnDemand = cms.double(-1.0),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Phi_fixed = cms.double(0.2),
            Phi_min = cms.double(0.05),
            Rescale_Dz = cms.double(3.0),
            Rescale_eta = cms.double(3.0),
            Rescale_phi = cms.double(3.0),
            UseFixedRegion = cms.bool(False),
            UseVertex = cms.bool(False),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            vertexCollection = cms.InputTag("pixelVertices")
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2IOHit"),
        tkTrajMaxChi2 = cms.double(9999.0),
        tkTrajMaxDXYBeamSpot = cms.double(0.2),
        tkTrajUseVertex = cms.bool(False),
        tkTrajVertex = cms.InputTag("pixelVertices")
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL3MuonsLinksCombination = cms.EDProducer("L3TrackLinksCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit")
)


process.hltL3MuonsOIHit = cms.EDProducer("L3MuonProducer",
    L3TrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutRPC = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            DYTthrs = cms.vint32(30, 15),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(0.001),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            DeltaR = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            EscapePt = cms.double(1.5),
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            Eta_fixed = cms.double(0.2),
            Eta_min = cms.double(0.05),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            OnDemand = cms.double(-1.0),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Phi_fixed = cms.double(0.2),
            Phi_min = cms.double(0.05),
            Rescale_Dz = cms.double(3.0),
            Rescale_eta = cms.double(3.0),
            Rescale_phi = cms.double(3.0),
            UseFixedRegion = cms.bool(False),
            UseVertex = cms.bool(False),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            vertexCollection = cms.InputTag("pixelVertices")
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2OIHit"),
        tkTrajMaxChi2 = cms.double(9999.0),
        tkTrajMaxDXYBeamSpot = cms.double(0.2),
        tkTrajUseVertex = cms.bool(False),
        tkTrajVertex = cms.InputTag("pixelVertices")
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL3MuonsOIState = cms.EDProducer("L3MuonProducer",
    L3TrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutRPC = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            DYTthrs = cms.vint32(30, 15),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(0.001),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            DeltaR = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            EscapePt = cms.double(1.5),
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            Eta_fixed = cms.double(0.2),
            Eta_min = cms.double(0.05),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            OnDemand = cms.double(-1.0),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Phi_fixed = cms.double(0.2),
            Phi_min = cms.double(0.05),
            Rescale_Dz = cms.double(3.0),
            Rescale_eta = cms.double(3.0),
            Rescale_phi = cms.double(3.0),
            UseFixedRegion = cms.bool(False),
            UseVertex = cms.bool(False),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            vertexCollection = cms.InputTag("pixelVertices")
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2OIState"),
        tkTrajMaxChi2 = cms.double(9999.0),
        tkTrajMaxDXYBeamSpot = cms.double(0.2),
        tkTrajUseVertex = cms.bool(False),
        tkTrajVertex = cms.InputTag("pixelVertices")
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL3TkFromL2OICombination = cms.EDProducer("L3TrackCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit")
)


process.hltL3TkTracksFromL2 = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(100.0),
    LostHitPenalty = cms.double(0.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltL3TkTracksMergeStep1", "hltL3TkTracksFromL2IOHit"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltL3TkTracksMergeStep1", "hltL3TkTracksFromL2IOHit"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltL3TkTracksFromL2IOHit = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIterX'),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('PropagatorWithMaterial'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string(''),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltL3TrackCandidateFromL2IOHit"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.hltL3TkTracksFromL2OIHit = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIterX'),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('PropagatorWithMaterial'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string(''),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltL3TrackCandidateFromL2OIHit"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.hltL3TkTracksFromL2OIState = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIterX'),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('PropagatorWithMaterial'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string(''),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltL3TrackCandidateFromL2OIState"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.hltL3TkTracksMergeStep1 = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(100.0),
    LostHitPenalty = cms.double(0.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltL3TkTracksFromL2OIState", "hltL3TkTracksFromL2OIHit"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltL3TkTracksFromL2OIState", "hltL3TkTracksFromL2OIHit"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltL3TrackCandidateFromL2 = cms.EDProducer("L3TrackCandCombiner",
    labels = cms.VInputTag("hltL3TrackCandidateFromL2IOHit", "hltL3TrackCandidateFromL2OIHit", "hltL3TrackCandidateFromL2OIState")
)


process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer("CkfTrajectoryMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltL3TrajSeedIOHit"),
    trackCandidateAlso = cms.bool(True),
    useHitsSplitting = cms.bool(False)
)


process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer("CkfTrajectoryMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    reverseTrajectories = cms.bool(True),
    src = cms.InputTag("hltL3TrajSeedOIHit"),
    trackCandidateAlso = cms.bool(True),
    useHitsSplitting = cms.bool(False)
)


process.hltL3TrackCandidateFromL2OIState = cms.EDProducer("CkfTrajectoryMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    reverseTrajectories = cms.bool(True),
    src = cms.InputTag("hltL3TrajSeedOIState"),
    trackCandidateAlso = cms.bool(True),
    useHitsSplitting = cms.bool(False)
)


process.hltL3TrajSeedIOHit = cms.EDProducer("TSGFromL2Muon",
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(
        DeltaR = cms.double(0.2),
        DeltaZ_Region = cms.double(15.9),
        EscapePt = cms.double(1.5),
        EtaR_UpperLimit_Par1 = cms.double(0.25),
        EtaR_UpperLimit_Par2 = cms.double(0.15),
        Eta_fixed = cms.double(0.2),
        Eta_min = cms.double(0.1),
        MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
        OnDemand = cms.double(-1.0),
        PhiR_UpperLimit_Par1 = cms.double(0.6),
        PhiR_UpperLimit_Par2 = cms.double(0.2),
        Phi_fixed = cms.double(0.2),
        Phi_min = cms.double(0.1),
        Rescale_Dz = cms.double(3.0),
        Rescale_eta = cms.double(3.0),
        Rescale_phi = cms.double(3.0),
        UseFixedRegion = cms.bool(False),
        UseVertex = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        vertexCollection = cms.InputTag("pixelVertices")
    ),
    PCut = cms.double(2.5),
    PtCut = cms.double(1.0),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('PropagatorWithMaterial'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('DualByL2TSG'),
        L3TkCollectionA = cms.InputTag("hltL3TkFromL2OICombination"),
        PSetNames = cms.vstring('skipTSG', 
            'iterativeTSG'),
        iterativeTSG = cms.PSet(
            ComponentName = cms.string('CombinedTSG'),
            PSetNames = cms.vstring('firstTSG', 
                'secondTSG'),
            firstTSG = cms.PSet(
                ComponentName = cms.string('TSGFromOrderedHits'),
                OrderedHitsFactoryPSet = cms.PSet(
                    ComponentName = cms.string('StandardHitTripletGenerator'),
                    GeneratorPSet = cms.PSet(
                        ComponentName = cms.string('PixelTripletHLTGenerator'),
                        SeedComparitorPSet = cms.PSet(
                            ComponentName = cms.string('none')
                        ),
                        extraHitRPhitolerance = cms.double(0.06),
                        extraHitRZtolerance = cms.double(0.06),
                        maxElement = cms.uint32(0),
                        phiPreFiltering = cms.double(0.3),
                        useBending = cms.bool(True),
                        useFixedPreFiltering = cms.bool(False),
                        useMultScattering = cms.bool(True)
                    ),
                    SeedingLayers = cms.InputTag("hltPixelLayerTriplets")
                ),
                SeedCreatorPSet = cms.PSet(
                    refToPSet_ = cms.string('HLTSeedFromConsecutiveHitsCreator')
                ),
                TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
            ),
            secondTSG = cms.PSet(
                ComponentName = cms.string('TSGFromOrderedHits'),
                OrderedHitsFactoryPSet = cms.PSet(
                    ComponentName = cms.string('StandardHitPairGenerator'),
                    SeedingLayers = cms.InputTag("hltPixelLayerPairs"),
                    maxElement = cms.uint32(0),
                    useOnDemandTracker = cms.untracked.int32(0)
                ),
                SeedCreatorPSet = cms.PSet(
                    refToPSet_ = cms.string('HLTSeedFromConsecutiveHitsCreator')
                ),
                TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
            ),
            thirdTSG = cms.PSet(
                ComponentName = cms.string('DualByEtaTSG'),
                PSetNames = cms.vstring('endcapTSG', 
                    'barrelTSG'),
                SeedCreatorPSet = cms.PSet(
                    refToPSet_ = cms.string('HLTSeedFromConsecutiveHitsCreator')
                ),
                barrelTSG = cms.PSet(

                ),
                endcapTSG = cms.PSet(
                    ComponentName = cms.string('TSGFromOrderedHits'),
                    OrderedHitsFactoryPSet = cms.PSet(
                        ComponentName = cms.string('StandardHitPairGenerator'),
                        SeedingLayers = cms.InputTag("hltMixedLayerPairs"),
                        maxElement = cms.uint32(0),
                        useOnDemandTracker = cms.untracked.int32(0)
                    ),
                    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
                ),
                etaSeparation = cms.double(2.0)
            )
        ),
        skipTSG = cms.PSet(

        )
    ),
    TrackerSeedCleaner = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        cleanerFromSharedHits = cms.bool(True),
        directionCleaner = cms.bool(True),
        ptCleaner = cms.bool(True)
    )
)


process.hltL3TrajSeedOIHit = cms.EDProducer("TSGFromL2Muon",
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(

    ),
    PCut = cms.double(2.5),
    PtCut = cms.double(1.0),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('PropagatorWithMaterial', 
            'hltESPSmartPropagatorAnyOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('DualByL2TSG'),
        L3TkCollectionA = cms.InputTag("hltL3MuonsOIState"),
        PSetNames = cms.vstring('skipTSG', 
            'iterativeTSG'),
        iterativeTSG = cms.PSet(
            ComponentName = cms.string('TSGFromPropagation'),
            ErrorRescaling = cms.double(3.0),
            MaxChi2 = cms.double(40.0),
            MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
            ResetMethod = cms.string('matrix'),
            SelectState = cms.bool(False),
            SigmaZ = cms.double(25.0),
            UpdateState = cms.bool(True),
            UseVertexState = cms.bool(True),
            beamSpot = cms.InputTag("unused"),
            errorMatrixPset = cms.PSet(
                action = cms.string('use'),
                atIP = cms.bool(True),
                errorMatrixValuesPSet = cms.PSet(
                    pf3_V11 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
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
                    pf3_V22 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V23 = cms.PSet(
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
                    ),
                    pf3_V25 = cms.PSet(
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
                    pf3_V34 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V35 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V44 = cms.PSet(
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
                    pf3_V55 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    xAxis = cms.vdouble(0.0, 13.0, 30.0, 70.0, 1000.0),
                    yAxis = cms.vdouble(0.0, 1.0, 1.4, 10.0),
                    zAxis = cms.vdouble(-3.14159, 3.14159)
                )
            )
        ),
        skipTSG = cms.PSet(

        )
    ),
    TrackerSeedCleaner = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        cleanerFromSharedHits = cms.bool(True),
        directionCleaner = cms.bool(True),
        ptCleaner = cms.bool(True)
    )
)


process.hltL3TrajSeedOIState = cms.EDProducer("TSGFromL2Muon",
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(

    ),
    PCut = cms.double(2.5),
    PtCut = cms.double(1.0),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSteppingHelixPropagatorOpposite', 
            'hltESPSteppingHelixPropagatorAlong'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('TSGForRoadSearch'),
        MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
        copyMuonRecHit = cms.bool(False),
        errorMatrixPset = cms.PSet(
            action = cms.string('use'),
            atIP = cms.bool(True),
            errorMatrixValuesPSet = cms.PSet(
                pf3_V11 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
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
                pf3_V22 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V23 = cms.PSet(
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
                ),
                pf3_V25 = cms.PSet(
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
                pf3_V34 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V35 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V44 = cms.PSet(
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
                pf3_V55 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                xAxis = cms.vdouble(0.0, 13.0, 30.0, 70.0, 1000.0),
                yAxis = cms.vdouble(0.0, 1.0, 1.4, 10.0),
                zAxis = cms.vdouble(-3.14159, 3.14159)
            )
        ),
        manySeeds = cms.bool(False),
        maxChi2 = cms.double(40.0),
        option = cms.uint32(3),
        propagatorCompatibleName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
        propagatorName = cms.string('hltESPSteppingHelixPropagatorAlong')
    ),
    TrackerSeedCleaner = cms.PSet(

    )
)


process.hltL3TrajectorySeed = cms.EDProducer("L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag("hltL3TrajSeedIOHit", "hltL3TrajSeedOIState", "hltL3TrajSeedOIHit")
)


process.hltLightPFTracks = cms.EDProducer("LightPFTrackProducer",
    TkColList = cms.VInputTag("hltPFMuonMerging"),
    TrackQuality = cms.string('none'),
    UseQuality = cms.bool(False)
)


process.hltMixedLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
        ),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
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
        'TEC2_neg+TEC3_neg')
)


process.hltMuonCSCDigis = cms.EDProducer("CSCDCCUnpacker",
    Debug = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535557110),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    runDQM = cms.untracked.bool(False)
)


process.hltMuonDTDigis = cms.EDProducer("DTUnpackingModule",
    dataType = cms.string('DDU'),
    dqmOnly = cms.bool(False),
    inputLabel = cms.InputTag("rawDataCollector"),
    maxFEDid = cms.untracked.int32(779),
    minFEDid = cms.untracked.int32(770),
    readOutParameters = cms.PSet(
        debug = cms.untracked.bool(False),
        localDAQ = cms.untracked.bool(False),
        performDataIntegrityMonitor = cms.untracked.bool(False),
        rosParameters = cms.PSet(
            debug = cms.untracked.bool(False),
            localDAQ = cms.untracked.bool(False),
            performDataIntegrityMonitor = cms.untracked.bool(False),
            readDDUIDfromDDU = cms.untracked.bool(True),
            readingDDU = cms.untracked.bool(True),
            writeSC = cms.untracked.bool(True)
        )
    ),
    useStandardFEDid = cms.bool(True)
)


process.hltMuonLinks = cms.EDProducer("MuonLinksProducerForHLT",
    InclusiveTrackerTrackCollection = cms.InputTag("hltPFMuonMerging"),
    LinkCollection = cms.InputTag("hltL3MuonsLinksCombination"),
    pMin = cms.double(2.5),
    ptMin = cms.double(2.5),
    shareHitFraction = cms.double(0.8)
)


process.hltMuonRPCDigis = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    doSynchro = cms.bool(False)
)


process.hltMuons = cms.EDProducer("MuonIdProducer",
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(1.0),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForPF"),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
            HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
            HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("hltAK4CaloJetsPFEt5"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForPF"),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
            HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
            HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            CSCsegments = cms.InputTag("hltCscSegments"),
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                DTsegments = cms.InputTag("hltDt4DSegments"),
                TightMatchCSC = cms.bool(True),
                TightMatchDT = cms.bool(False)
            ),
            PruneCut = cms.double(100.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(2.7),
            DTsegments = cms.InputTag("hltDt4DSegments"),
            DoWireCorr = cms.bool(False),
            DropTheta = cms.bool(True),
            HitError = cms.double(6.0),
            HitsMin = cms.int32(5),
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                DTsegments = cms.InputTag("hltDt4DSegments"),
                TightMatchCSC = cms.bool(True),
                TightMatchDT = cms.bool(False)
            ),
            PruneCut = cms.double(10000.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorCSC = cms.double(7.4),
        ErrorDT = cms.double(6.0),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForPF"),
        DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
        HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("hltOnlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("hltPFMuonMerging")
    ),
    TrackerKinkFinderParameters = cms.PSet(
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(False)
    ),
    addExtraSoftMuons = cms.bool(False),
    arbitrationCleanerOptions = cms.PSet(
        ClusterDPhi = cms.double(0.6),
        ClusterDTheta = cms.double(0.02),
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        OverlapDTheta = cms.double(0.02)
    ),
    debugWithTruthMatching = cms.bool(False),
    ecalDepositName = cms.string('ecal'),
    fillCaloCompatibility = cms.bool(True),
    fillEnergy = cms.bool(True),
    fillGlobalTrackQuality = cms.bool(False),
    fillGlobalTrackRefits = cms.bool(False),
    fillIsolation = cms.bool(True),
    fillMatching = cms.bool(True),
    fillTrackerKink = cms.bool(False),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    inputCollectionLabels = cms.VInputTag("hltPFMuonMerging", "hltMuonLinks", "hltL2Muons"),
    inputCollectionTypes = cms.vstring('inner tracks', 
        'links', 
        'outer tracks'),
    jetDepositName = cms.string('jets'),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    maxAbsEta = cms.double(3.0),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minCaloCompatibility = cms.double(0.6),
    minNumberOfMatches = cms.int32(1),
    minP = cms.double(10.0),
    minPCaloMuon = cms.double(1000000000.0),
    minPt = cms.double(10.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    runArbitrationCleaner = cms.bool(False),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    trackDepositName = cms.string('tracker'),
    writeIsoDeposits = cms.bool(False)
)


process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotOnlineProducer",
    changeToCMSCoordinates = cms.bool(False),
    gtEvmLabel = cms.InputTag(""),
    maxRadius = cms.double(2.0),
    maxZ = cms.double(40.0),
    setSigmaZ = cms.double(0.0),
    src = cms.InputTag("hltScalersRawToDigi")
)


process.hltPFHT = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK4PFJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    maxEtaJetMht = cms.double(999.0),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(40.0),
    minPtJetMht = cms.double(0.0),
    pfCandidatesLabel = cms.InputTag("hltParticleFlow"),
    usePt = cms.bool(True)
)


process.hltPFHT4Jet = cms.EDProducer("HLTHtMhtProducer",
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK4PFJetsCorrected"),
    maxEtaJetHt = cms.double(3.0),
    maxEtaJetMht = cms.double(999.0),
    minNJetHt = cms.int32(4),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(40.0),
    minPtJetMht = cms.double(0.0),
    pfCandidatesLabel = cms.InputTag("hltParticleFlow"),
    usePt = cms.bool(True)
)


process.hltPFMuonMerging = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltL3TkTracksFromL2", "hltIter2Merged"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltL3TkTracksFromL2", "hltIter2Merged"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltParticleFlow = cms.EDProducer("PFProducer",
    GedElectronValueMap = cms.InputTag("gedGsfElectronsTmp"),
    GedPhotonValueMap = cms.InputTag("tmpGedPhotons","valMapPFEgammaCandToPhoton"),
    PFEGammaCandidates = cms.InputTag("particleFlowEGamma"),
    X0_Map = cms.string('RecoParticleFlow/PFProducer/data/allX0histos.root'),
    algoType = cms.uint32(0),
    blocks = cms.InputTag("hltParticleFlowBlock"),
    calibHF_a_EMHAD = cms.vdouble(1.42215, 1.00496, 0.68961, 0.81656, 0.98504, 
        0.98504, 1.00802, 1.0593, 1.4576, 1.4576),
    calibHF_a_EMonly = cms.vdouble(0.96945, 0.96701, 0.76309, 0.82268, 0.87583, 
        0.89718, 0.98674, 1.4681, 1.458, 1.458),
    calibHF_b_EMHAD = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    calibHF_b_HADonly = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    calibHF_eta_step = cms.vdouble(0.0, 2.9, 3.0, 3.2, 4.2, 
        4.4, 4.6, 4.8, 5.2, 5.4),
    calibHF_use = cms.bool(False),
    calibPFSCEle_Fbrem_barrel = cms.vdouble(0.6, 6.0, -0.0255975, 0.0576727, 0.975442, 
        -0.000546394, 1.26147, 25.0, -0.02025, 0.04537, 
        0.9728, -0.0008962, 1.172),
    calibPFSCEle_Fbrem_endcap = cms.vdouble(0.9, 6.5, -0.0692932, 0.101776, 0.995338, 
        -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 
        0.923165, 0.000474665, 1.10782),
    calibPFSCEle_barrel = cms.vdouble(1.004, -1.536, 22.88, -1.467, 0.3555, 
        0.6227, 14.65, 2051.0, 25.0, 0.9932, 
        -0.5444, 0.0, 0.5438, 0.7109, 7.645, 
        0.2904, 0.0),
    calibPFSCEle_endcap = cms.vdouble(1.153, -16.5975, 5.668, -0.1772, 16.22, 
        7.326, 0.0483, -4.068, 9.406),
    cleanedHF = cms.VInputTag("hltParticleFlowRecHitHCAL:Cleaned", "hltParticleFlowClusterHFHAD:Cleaned", "hltParticleFlowClusterHFEM:Cleaned"),
    coneEcalIsoForEgammaSC = cms.double(0.3),
    coneTrackIsoForEgammaSC = cms.double(0.3),
    cosmicRejectionDistance = cms.double(1.0),
    debug = cms.untracked.bool(False),
    dptRel_DispVtx = cms.double(10.0),
    dzPV = cms.double(0.2),
    egammaElectrons = cms.InputTag(""),
    electron_iso_combIso_barrel = cms.double(10.0),
    electron_iso_combIso_endcap = cms.double(10.0),
    electron_iso_mva_barrel = cms.double(-0.1875),
    electron_iso_mva_endcap = cms.double(-0.1075),
    electron_iso_pt = cms.double(10.0),
    electron_missinghits = cms.uint32(1),
    electron_noniso_mvaCut = cms.double(-0.1),
    electron_protectionsForJetMET = cms.PSet(
        maxDPhiIN = cms.double(0.1),
        maxE = cms.double(50.0),
        maxEcalEOverPRes = cms.double(0.2),
        maxEcalEOverP_1 = cms.double(0.5),
        maxEcalEOverP_2 = cms.double(0.2),
        maxEeleOverPout = cms.double(0.2),
        maxEeleOverPoutRes = cms.double(0.5),
        maxEleHcalEOverEcalE = cms.double(0.1),
        maxHcalE = cms.double(10.0),
        maxHcalEOverEcalE = cms.double(0.1),
        maxHcalEOverP = cms.double(1.0),
        maxNtracks = cms.double(3.0),
        maxTrackPOverEele = cms.double(1.0)
    ),
    eventFactorForCosmics = cms.double(10.0),
    eventFractionForCleaning = cms.double(0.8),
    eventFractionForRejection = cms.double(0.8),
    factors_45 = cms.vdouble(10.0, 100.0),
    iCfgCandConnector = cms.PSet(
        bCalibPrimary = cms.bool(False),
        bCalibSecondary = cms.bool(False),
        bCorrect = cms.bool(False),
        nuclCalibFactors = cms.vdouble(0.8, 0.15, 0.5, 0.5, 0.05)
    ),
    isolatedElectronID_mvaWeightFile = cms.string('RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml'),
    maxDPtOPt = cms.double(1.0),
    maxDeltaPhiPt = cms.double(7.0),
    maxSignificance = cms.double(2.5),
    metFactorForCleaning = cms.double(4.0),
    metFactorForFakes = cms.double(4.0),
    metFactorForHighEta = cms.double(25.0),
    metFactorForRejection = cms.double(4.0),
    metSignificanceForCleaning = cms.double(3.0),
    metSignificanceForRejection = cms.double(4.0),
    minDeltaMet = cms.double(0.4),
    minEnergyForPunchThrough = cms.double(100.0),
    minHFCleaningPt = cms.double(5.0),
    minMomentumForPunchThrough = cms.double(100.0),
    minPixelHits = cms.int32(1),
    minPtForPostCleaning = cms.double(20.0),
    minSignificance = cms.double(2.5),
    minSignificanceReduction = cms.double(1.4),
    minTrackerHits = cms.int32(8),
    muon_ECAL = cms.vdouble(0.5, 0.5),
    muon_HCAL = cms.vdouble(3.0, 3.0),
    muon_HO = cms.vdouble(0.9, 0.9),
    muons = cms.InputTag("hltMuons"),
    nTrackIsoForEgammaSC = cms.uint32(2),
    nsigma_TRACK = cms.double(1.0),
    pf_GlobC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFGlobalCorr.root'),
    pf_Res_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFRes.root'),
    pf_convID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt'),
    pf_conv_mvaCut = cms.double(0.0),
    pf_electronID_crackCorrection = cms.bool(False),
    pf_electronID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt'),
    pf_electron_mvaCut = cms.double(-0.1),
    pf_electron_output_col = cms.string('electrons'),
    pf_locC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFClusterCorr.root'),
    pf_nsigma_ECAL = cms.double(0.0),
    pf_nsigma_HCAL = cms.double(1.0),
    photon_HoE = cms.double(0.1),
    photon_MinEt = cms.double(10.0),
    photon_SigmaiEtaiEta_barrel = cms.double(0.0125),
    photon_SigmaiEtaiEta_endcap = cms.double(0.034),
    photon_combIso = cms.double(10.0),
    photon_protectionsForJetMET = cms.PSet(
        sumPtTrackIso = cms.double(2.0),
        sumPtTrackIsoSlope = cms.double(0.001)
    ),
    postHFCleaning = cms.bool(False),
    postMuonCleaning = cms.bool(True),
    ptErrorScale = cms.double(8.0),
    ptFactorForHighEta = cms.double(2.0),
    pt_Error = cms.double(1.0),
    punchThroughFactor = cms.double(3.0),
    punchThroughMETFactor = cms.double(4.0),
    rejectTracks_Bad = cms.bool(False),
    rejectTracks_Step45 = cms.bool(False),
    sumEtEcalIsoForEgammaSC_barrel = cms.double(1.0),
    sumEtEcalIsoForEgammaSC_endcap = cms.double(2.0),
    sumPtTrackIsoForEgammaSC_barrel = cms.double(4.0),
    sumPtTrackIsoForEgammaSC_endcap = cms.double(4.0),
    sumPtTrackIsoForPhoton = cms.double(-1.0),
    sumPtTrackIsoSlopeForPhoton = cms.double(-1.0),
    trackQuality = cms.string('highPurity'),
    useCalibrationsFromDB = cms.bool(True),
    useEGammaElectrons = cms.bool(False),
    useEGammaFilters = cms.bool(False),
    useEGammaSupercluster = cms.bool(False),
    useHO = cms.bool(False),
    usePFConversions = cms.bool(False),
    usePFDecays = cms.bool(False),
    usePFElectrons = cms.bool(False),
    usePFNuclearInteractions = cms.bool(False),
    usePFPhotons = cms.bool(False),
    usePFSCEleCalib = cms.bool(True),
    usePhotonReg = cms.bool(False),
    useProtectionsForJetMET = cms.bool(True),
    useRegressionFromDB = cms.bool(False),
    useVerticesForNeutral = cms.bool(True),
    verbose = cms.untracked.bool(False),
    vertexCollection = cms.InputTag("hltPixelVertices")
)


process.hltParticleFlowBlock = cms.EDProducer("PFBlockProducer",
    debug = cms.untracked.bool(False),
    elementImporters = cms.VPSet(cms.PSet(
        DPtOverPtCuts_byTrackAlgo = cms.vdouble(0.5, 0.5, 0.5, 0.5, 0.5),
        NHitCuts_byTrackAlgo = cms.vuint32(3, 3, 3, 3, 3),
        importerName = cms.string('GeneralTracksImporter'),
        muonSrc = cms.InputTag("hltMuons"),
        source = cms.InputTag("hltLightPFTracks"),
        useIterativeTracking = cms.bool(False)
    ), 
        cms.PSet(
            BCtoPFCMap = cms.InputTag(""),
            importerName = cms.string('ECALClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterECALUnseeded")
        ), 
        cms.PSet(
            importerName = cms.string('GenericClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterHCAL")
        ), 
        cms.PSet(
            importerName = cms.string('GenericClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterHFEM")
        ), 
        cms.PSet(
            importerName = cms.string('GenericClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterHFHAD")
        ), 
        cms.PSet(
            importerName = cms.string('GenericClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterPSUnseeded")
        )),
    linkDefinitions = cms.VPSet(cms.PSet(
        linkType = cms.string('PS1:ECAL'),
        linkerName = cms.string('PreshowerAndECALLinker'),
        useKDTree = cms.bool(True)
    ), 
        cms.PSet(
            linkType = cms.string('PS2:ECAL'),
            linkerName = cms.string('PreshowerAndECALLinker'),
            useKDTree = cms.bool(True)
        ), 
        cms.PSet(
            linkType = cms.string('TRACK:ECAL'),
            linkerName = cms.string('TrackAndECALLinker'),
            useKDTree = cms.bool(True)
        ), 
        cms.PSet(
            linkType = cms.string('TRACK:HCAL'),
            linkerName = cms.string('TrackAndHCALLinker'),
            useKDTree = cms.bool(True)
        ), 
        cms.PSet(
            linkType = cms.string('ECAL:HCAL'),
            linkerName = cms.string('ECALAndHCALLinker'),
            useKDTree = cms.bool(False)
        ), 
        cms.PSet(
            linkType = cms.string('HFEM:HFHAD'),
            linkerName = cms.string('HFEMAndHFHADLinker'),
            useKDTree = cms.bool(False)
        )),
    verbose = cms.untracked.bool(False)
)


process.hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            gatheringThreshold = cms.double(0.08),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9)
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            recHitEnergyNorm = cms.double(0.08)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            doubleSpikeS6S2 = cms.double(0.04),
            doubleSpikeThresh = cms.double(10.0),
            energyThresholdModifier = cms.double(2.0),
            fractionThresholdModifier = cms.double(3.0),
            minS4S1_a = cms.double(0.04),
            minS4S1_b = cms.double(-0.024),
            singleSpikeThresh = cms.double(4.0)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                doubleSpikeS6S2 = cms.double(-1.0),
                doubleSpikeThresh = cms.double(1000000000.0),
                energyThresholdModifier = cms.double(2.0),
                fractionThresholdModifier = cms.double(3.0),
                minS4S1_a = cms.double(0.02),
                minS4S1_b = cms.double(-0.0125),
                singleSpikeThresh = cms.double(15.0)
            ))
    )),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECALUnseeded"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_ENDCAP'),
            seedingThreshold = cms.double(0.6),
            seedingThresholdPt = cms.double(0.15)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.hltParticleFlowClusterECALUnseeded = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        algoName = cms.string('PFClusterEMEnergyCorrector'),
        applyCrackCorrections = cms.bool(False)
    ),
    inputECAL = cms.InputTag("hltParticleFlowClusterECALUncorrectedUnseeded"),
    inputPS = cms.InputTag("hltParticleFlowClusterPSUnseeded"),
    minimumPSEnergy = cms.double(0.0)
)


process.hltParticleFlowClusterHCAL = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            gatheringThreshold = cms.double(0.8),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThreshold = cms.double(0.8),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            recHitEnergyNorm = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.8)
            )),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('RBXAndHPDCleaner')
    )),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHCAL"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            seedingThreshold = cms.double(0.8),
            seedingThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                seedingThreshold = cms.double(1.1),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.hltParticleFlowClusterHFEM = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            gatheringThreshold = cms.double(0.8),
            gatheringThresholdPt = cms.double(0.0)
        )),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            recHitEnergyNorm = cms.double(0.8)
        )),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            doubleSpikeS6S2 = cms.double(-1.0),
            doubleSpikeThresh = cms.double(1000000000.0),
            energyThresholdModifier = cms.double(1.0),
            fractionThresholdModifier = cms.double(1.0),
            minS4S1_a = cms.double(0.11),
            minS4S1_b = cms.double(-0.19),
            singleSpikeThresh = cms.double(80.0)
        ))
    )),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHCAL","HFEM"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(0),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            seedingThreshold = cms.double(1.4),
            seedingThresholdPt = cms.double(0.0)
        ))
    )
)


process.hltParticleFlowClusterHFHAD = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_HAD'),
            gatheringThreshold = cms.double(0.8),
            gatheringThresholdPt = cms.double(0.0)
        )),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HF_HAD'),
            recHitEnergyNorm = cms.double(0.8)
        )),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_HAD'),
            doubleSpikeS6S2 = cms.double(-1.0),
            doubleSpikeThresh = cms.double(1000000000.0),
            energyThresholdModifier = cms.double(1.0),
            fractionThresholdModifier = cms.double(1.0),
            minS4S1_a = cms.double(0.045),
            minS4S1_b = cms.double(-0.08),
            singleSpikeThresh = cms.double(120.0)
        ))
    )),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHCAL","HFHAD"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(0),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_HAD'),
            seedingThreshold = cms.double(1.4),
            seedingThresholdPt = cms.double(0.0)
        ))
    )
)


process.hltParticleFlowClusterPSUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            gatheringThreshold = cms.double(6e-05),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            recHitEnergyNorm = cms.double(6e-05)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitPSUnseeded"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            seedingThreshold = cms.double(0.00012),
            seedingThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.hltParticleFlowRecHitECALUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFEBRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(0.08)
        ), 
            cms.PSet(
                cleaningThreshold = cms.double(2.0),
                name = cms.string('PFRecHitQTestECAL'),
                skipTTRecoveredHits = cms.bool(True),
                timingCleaning = cms.bool(True),
                topologicalCleaning = cms.bool(True)
            )),
        src = cms.InputTag("hltEcalRecHit","EcalRecHitsEB")
    ), 
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                name = cms.string('PFRecHitQTestThreshold'),
                threshold = cms.double(0.3)
            ), 
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEE")
        ))
)


process.hltParticleFlowRecHitHCAL = cms.EDProducer("PFCTRecHitProducer",
    ApplyLongShortDPG = cms.bool(True),
    ApplyPulseDPG = cms.bool(False),
    ApplyTimeDPG = cms.bool(False),
    ECAL_Compensate = cms.bool(False),
    ECAL_Compensation = cms.double(0.5),
    ECAL_Dead_Code = cms.uint32(10),
    ECAL_Threshold = cms.double(10.0),
    EM_Depth = cms.double(22.0),
    HAD_Depth = cms.double(47.0),
    HCAL_Calib = cms.bool(True),
    HCAL_Calib_29 = cms.double(1.35),
    HF_Calib = cms.bool(True),
    HF_Calib_29 = cms.double(1.07),
    HcalMaxAllowedChannelStatusSev = cms.int32(9),
    HcalMaxAllowedHFDigiTimeSev = cms.int32(9),
    HcalMaxAllowedHFInTimeWindowSev = cms.int32(9),
    HcalMaxAllowedHFLongShortSev = cms.int32(9),
    LongFibre_Cut = cms.double(120.0),
    LongFibre_Fraction = cms.double(0.1),
    LongShortFibre_Cut = cms.double(1000000000.0),
    MaxLongTiming_Cut = cms.double(5.0),
    MaxShortTiming_Cut = cms.double(5.0),
    MinLongTiming_Cut = cms.double(-5.0),
    MinShortTiming_Cut = cms.double(-5.0),
    ShortFibre_Cut = cms.double(60.0),
    ShortFibre_Fraction = cms.double(0.01),
    caloTowers = cms.InputTag("hltTowerMakerForPF"),
    hcalRecHitsHBHE = cms.InputTag("hltHbhereco"),
    hcalRecHitsHF = cms.InputTag("hltHfreco"),
    navigation_HF = cms.bool(True),
    navigator = cms.PSet(
        name = cms.string('PFRecHitCaloTowerNavigator')
    ),
    thresh_Barrel = cms.double(0.4),
    thresh_Endcap = cms.double(0.4),
    thresh_HF = cms.double(0.4),
    weight_HFem = cms.double(1.0),
    weight_HFhad = cms.double(1.0)
)


process.hltParticleFlowRecHitPSUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(7e-06)
        )),
        src = cms.InputTag("hltEcalPreshowerRecHit","EcalRecHitsES")
    ))
)


process.hltPixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
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
        'FPix1_neg+FPix2_neg')
)


process.hltPixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg')
)


process.hltPixelTracks = cms.EDProducer("PixelTrackProducer",
    CleanerPSet = cms.PSet(
        ComponentName = cms.string('PixelTrackCleanerBySharedHits')
    ),
    FilterPSet = cms.PSet(
        ComponentName = cms.string('PixelTrackFilterByKinematics'),
        chi2 = cms.double(1000.0),
        nSigmaInvPtTolerance = cms.double(0.0),
        nSigmaTipMaxTolerance = cms.double(0.0),
        ptMin = cms.double(0.1),
        tipMax = cms.double(1.0)
    ),
    FitterPSet = cms.PSet(
        ComponentName = cms.string('PixelFitterByHelixProjections'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        fixImpactParameter = cms.double(0.0)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            ComponentName = cms.string('PixelTripletHLTGenerator'),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
                clusterShapeCacheSrc = cms.InputTag("hltSiPixelClustersCache")
            ),
            extraHitRPhitolerance = cms.double(0.06),
            extraHitRZtolerance = cms.double(0.06),
            maxElement = cms.uint32(100000),
            phiPreFiltering = cms.double(0.3),
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            useMultScattering = cms.bool(True)
        ),
        SeedingLayers = cms.InputTag("hltPixelLayerTriplets")
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            originHalfLength = cms.double(24.0),
            originRadius = cms.double(0.2),
            precise = cms.bool(True),
            ptMin = cms.double(0.9)
        )
    ),
    useFilterWithES = cms.bool(False)
)


process.hltPixelVertices = cms.EDProducer("PixelVertexProducer",
    Finder = cms.string('DivisiveVertexFinder'),
    Method2 = cms.bool(True),
    NTrkMin = cms.int32(2),
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    ),
    PtMin = cms.double(1.0),
    TrackCollection = cms.InputTag("hltPixelTracks"),
    UseError = cms.bool(True),
    Verbosity = cms.int32(0),
    WtAverage = cms.bool(True),
    ZOffset = cms.double(5.0),
    ZSeparation = cms.double(0.05),
    beamSpot = cms.InputTag("hltOnlineBeamSpot")
)


process.hltRpcRecHits = cms.EDProducer("RPCRecHitProducer",
    deadSource = cms.string('File'),
    deadvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat'),
    maskSource = cms.string('File'),
    maskvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat'),
    recAlgo = cms.string('RPCRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    ),
    rpcDigiLabel = cms.InputTag("hltMuonRPCDigis")
)


process.hltScalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    scalersInputTag = cms.InputTag("rawDataCollector")
)


process.hltSiPixelClusters = cms.EDProducer("SiPixelClusterProducer",
    ChannelThreshold = cms.int32(1000),
    ClusterThreshold = cms.double(4000.0),
    MissCalibrate = cms.untracked.bool(True),
    SeedThreshold = cms.int32(1000),
    SplitClusters = cms.bool(False),
    VCaltoElectronGain = cms.int32(65),
    VCaltoElectronOffset = cms.int32(-414),
    maxNumberOfClusters = cms.int32(20000),
    payloadType = cms.string('HLT'),
    src = cms.InputTag("hltSiPixelDigis")
)


process.hltSiPixelClustersCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelDigis = cms.EDProducer("SiPixelRawToDigi",
    ErrorList = cms.vint32(),
    IncludeErrors = cms.bool(False),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    Timing = cms.untracked.bool(False),
    UsePhase1 = cms.bool(False),
    UsePilotBlade = cms.bool(False),
    UseQualityInfo = cms.bool(False),
    UserErrorList = cms.vint32()
)


process.hltSiPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('hltESPPixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiStripClusters = cms.EDProducer("MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    measurementTracker = cms.string('hltESPMeasurementTracker'),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string('hltSiStripRawToClustersFacility'),
    switchOffPixelsIfEmpty = cms.bool(True)
)


process.hltSiStripExcludedFEDListProducer = cms.EDProducer("SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag("rawDataCollector")
)


process.hltSiStripRawToClustersFacility = cms.EDProducer("SiStripClusterizerFromRaw",
    Algorithms = cms.PSet(
        CommonModeNoiseSubtractionMode = cms.string('Median'),
        PedestalSubtractionFedMode = cms.bool(True),
        SiStripFedZeroSuppressionMode = cms.uint32(4),
        TruncateInSuppressor = cms.bool(True),
        doAPVRestore = cms.bool(False),
        useCMMeanMap = cms.bool(False)
    ),
    Clusterizer = cms.PSet(
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        ChannelThreshold = cms.double(2.0),
        ClusterThreshold = cms.double(5.0),
        MaxAdjacentBad = cms.uint32(0),
        MaxSequentialBad = cms.uint32(1),
        MaxSequentialHoles = cms.uint32(0),
        QualityLabel = cms.string(''),
        RemoveApvShots = cms.bool(True),
        SeedThreshold = cms.double(3.0),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
        ),
        setDetId = cms.bool(True)
    ),
    DoAPVEmulatorCheck = cms.bool(False),
    ProductLabel = cms.InputTag("rawDataCollector"),
    onDemand = cms.bool(True)
)


process.hltTowerMakerForAll = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(),
    EEGrid = cms.vdouble(),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring('kTime', 
        'kWeird', 
        'kBad'),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(),
    HBThreshold = cms.double(0.7),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(),
    HEDGrid = cms.vdouble(),
    HEDThreshold = cms.double(0.8),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(),
    HESGrid = cms.vdouble(),
    HESThreshold = cms.double(0.8),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(),
    HF1Grid = cms.vdouble(),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(),
    HF2Grid = cms.vdouble(),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(),
    HOGrid = cms.vdouble(),
    HOThreshold0 = cms.double(3.5),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1e-99),
    HOWeights = cms.vdouble(),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(False),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(False),
    UseSymEBTreshold = cms.bool(False),
    UseSymEETreshold = cms.bool(False),
    ecalInputs = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE"),
    hbheInput = cms.InputTag("hltHbhereco"),
    hfInput = cms.InputTag("hltHfreco"),
    hoInput = cms.InputTag("hltHoreco")
)


process.hltTowerMakerForPF = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(),
    EEGrid = cms.vdouble(),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring('kTime', 
        'kWeird', 
        'kBad'),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(),
    HBThreshold = cms.double(0.4),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(),
    HEDGrid = cms.vdouble(),
    HEDThreshold = cms.double(0.4),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(),
    HESGrid = cms.vdouble(),
    HESThreshold = cms.double(0.4),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(),
    HF1Grid = cms.vdouble(),
    HF1Threshold = cms.double(1.2),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(),
    HF2Grid = cms.vdouble(),
    HF2Threshold = cms.double(1.8),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(),
    HOGrid = cms.vdouble(),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(1.1),
    HOThresholdMinus2 = cms.double(1.1),
    HOThresholdPlus1 = cms.double(1.1),
    HOThresholdPlus2 = cms.double(1.1),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(),
    HcalAcceptSeverityLevel = cms.uint32(11),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(False),
    UseSymEBTreshold = cms.bool(False),
    UseSymEETreshold = cms.bool(False),
    ecalInputs = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE"),
    hbheInput = cms.InputTag("hltHbhereco"),
    hfInput = cms.InputTag("hltHfreco"),
    hoInput = cms.InputTag("hltHoreco")
)


process.hltTrackIter0RefsForJets4Iter1 = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity")
)


process.hltTrimmedPixelVertices = cms.EDProducer("PixelVertexCollectionTrimmer",
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    ),
    fractionSumPt2 = cms.double(0.3),
    maxVtx = cms.uint32(100),
    minSumPt2 = cms.double(0.0),
    src = cms.InputTag("hltPixelVertices")
)


process.hlt1AK8PFJetsTrimR0p1PT0p03Mass50 = cms.EDFilter("HLT1PFJet",
    MaxEta = cms.double(5.0),
    MinE = cms.double(-1.0),
    MinMass = cms.double(50.0),
    MinN = cms.int32(1),
    MinPt = cms.double(0.0),
    inputTag = cms.InputTag("hltAK8PFJetsTrimR0p1PT0p03"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(85)
)


process.hlt4JetHt450 = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltHtMht4Jet"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltHtMht4Jet"),
    minHt = cms.vdouble(450.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(False)
)


process.hlt4JetHt550 = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltHtMht4Jet"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltHtMht4Jet"),
    minHt = cms.vdouble(550.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(False)
)


process.hltAK4CaloJetsPFEt5 = cms.EDFilter("EtMinCaloJetSelector",
    etMin = cms.double(5.0),
    filter = cms.bool(False),
    src = cms.InputTag("hltAK4CaloJetsPF")
)


process.hltAK8CaloJetsPFEt5 = cms.EDFilter("EtMinCaloJetSelector",
    etMin = cms.double(5.0),
    filter = cms.bool(False),
    src = cms.InputTag("hltAK8CaloJetsPF")
)


process.hltAK8Ht600 = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltAK8HtMht"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltAK8HtMht"),
    minHt = cms.vdouble(600.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(False)
)


process.hltAK8PFHT700 = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltAK8PFHT"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltAK8PFHT"),
    minHt = cms.vdouble(700.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(True)
)


process.hltBoolEnd = cms.EDFilter("HLTBool",
    result = cms.bool(True)
)


process.hltHt700 = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltHtMht"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltHtMht"),
    minHt = cms.vdouble(700.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(False)
)


process.hltL1sL1HTT150ORHTT175 = cms.EDFilter("HLTLevel1GTSeed",
    L1CollectionsTag = cms.InputTag("hltL1extraParticles"),
    L1GtObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    L1MuonCollectionTag = cms.InputTag("hltL1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1SeedsLogicalExpression = cms.string('L1_HTT150 OR L1_HTT175'),
    L1TechTriggerSeeding = cms.bool(False),
    L1UseAliasesForSeeding = cms.bool(True),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    saveTags = cms.bool(True)
)


process.hltPF4JetHT550 = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltPFHT4Jet"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltPFHT4Jet"),
    minHt = cms.vdouble(550.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(True)
)


process.hltPF4JetHT650 = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltPFHT4Jet"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltPFHT4Jet"),
    minHt = cms.vdouble(650.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(True)
)


process.hltPF4JetHT750 = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltPFHT4Jet"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltPFHT4Jet"),
    minHt = cms.vdouble(750.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(True)
)


process.hltPFHT900 = cms.EDFilter("HLTHtMhtFilter",
    htLabels = cms.VInputTag("hltPFHT"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltPFHT"),
    minHt = cms.vdouble(900.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(True)
)


process.hltPreAK8PFHT700TrimR0p1PT0p03Mass50 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT5504Jet = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT6504Jet = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT7504Jet = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePFHT900 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltTriggerType = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)


#process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
#    fileName = cms.untracked.string('DQMIO.root')
#)


process.output = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('HLTDEBUG')
    ),
    fileName = cms.untracked.string('myHLT2PAT_prod.root'),
    outputCommands = cms.untracked.vstring('keep *_TriggerResults_*_*', 
        'keep *_patJets*_*_*', 
        'keep *_hltOnlinePrimaryVertices*_*_*', 
        'keep *_goodOfflinePrimaryVertices*_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltPFHT_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltAntiKT5CaloJets_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep *_hltPFHT4Jet_*_*', 
        'keep *_hltAK8HtMht_*_*', 
        'keep *_hltAK8PFJetsTrimR0p1PT0p03_*_*', 
        'keep *_hltAntiKT5PFJets_*_*', 
        'keep *_hltGtDigis_*_*', 
        'keep *_hltHtMht4Jet_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltLightPFTracks_*_*', 
        'keep *_hltAK8PFHT_*_*', 
        'keep *_hltAK4CaloJetsPF_*_*', 
        'keep *_hltAntiKT5PFJetsNoPU_*_*', 
        'keep *_hltHtMht_*_*', 
        'keep *_hltAK8CaloJetsPF_*_*'),
    splitLevel = cms.untracked.int32(0)
)


process.HLTDoLocalPixelSequence = cms.Sequence(process.hltSiPixelDigis+process.hltSiPixelClusters+process.hltSiPixelClustersCache+process.hltSiPixelRecHits)


process.HLTPreshowerSequence = cms.Sequence(process.hltEcalPreshowerDigis+process.hltEcalPreshowerRecHit)


process.HLTParticleFlowSequence = cms.Sequence(process.HLTPreshowerSequence+process.hltParticleFlowRecHitECALUnseeded+process.hltParticleFlowRecHitHCAL+process.hltParticleFlowRecHitPSUnseeded+process.hltParticleFlowClusterECALUncorrectedUnseeded+process.hltParticleFlowClusterPSUnseeded+process.hltParticleFlowClusterECALUnseeded+process.hltParticleFlowClusterHCAL+process.hltParticleFlowClusterHFEM+process.hltParticleFlowClusterHFHAD+process.hltLightPFTracks+process.hltParticleFlowBlock+process.hltParticleFlow)


process.HLTL1UnpackerSequence = cms.Sequence(process.hltGtDigis+process.hltCaloStage1Digis+process.hltCaloStage1LegacyFormatDigis+process.hltL1GtObjectMap+process.hltL1extraParticles)


process.HLTMuonLocalRecoSequence = cms.Sequence(process.hltMuonDTDigis+process.hltDt1DRecHits+process.hltDt4DSegments+process.hltMuonCSCDigis+process.hltCsc2DRecHits+process.hltCscSegments+process.hltMuonRPCDigis+process.hltRpcRecHits)


process.HLTAK4CaloJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAllCalo+process.hltAK4CaloJetsCorrected+process.hltAK4CaloJetsCorrectedIDPassed)


process.HLTAK8PFJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAll+process.hltAK8PFJetsCorrected)


process.HLTDoLocalHcalSequence = cms.Sequence(process.hltHcalDigis+process.hltHbhereco+process.hltHfreco+process.hltHoreco)


process.HLTIter0TrackAndTauJet4Iter1Sequence = cms.Sequence(process.hltTrackIter0RefsForJets4Iter1+process.hltAK4Iter0TrackJets4Iter1+process.hltIter0TrackAndTauJets4Iter1)


process.HLTAK4PFJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAll+process.hltAK4PFJetsCorrected)


process.HLTBeamSpot = cms.Sequence(process.hltScalersRawToDigi+process.hltOnlineBeamSpot)


process.HLTL2muonrecoNocandSequence = cms.Sequence(process.HLTMuonLocalRecoSequence+process.hltL2OfflineMuonSeeds+process.hltL2MuonSeeds+process.hltL2Muons)


process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence(process.hltEcalDigis+process.hltEcalUncalibRecHit+process.hltEcalDetIdToBeRecovered+process.hltEcalRecHit)


process.HLTAK8CaloJetsCorrectionSequence = cms.Sequence(process.hltFixedGridRhoFastjetAllCalo+process.hltAK8CaloJetsCorrected+process.hltAK8CaloJetsCorrectedIDPassed)


process.HLTIter1TrackAndTauJets4Iter2Sequence = cms.Sequence(process.hltIter1TrackRefsForJets4Iter2+process.hltAK4Iter1TrackJets4Iter2+process.hltIter1TrackAndTauJets4Iter2)


process.HLTEndSequence = cms.Sequence(process.hltBoolEnd)


process.HLTIterativeTrackingIteration2 = cms.Sequence(process.hltIter2ClustersRefRemoval+process.hltIter2MaskedMeasurementTrackerEvent+process.hltIter2PixelLayerPairs+process.hltIter2PFlowPixelSeeds+process.hltIter2PFlowCkfTrackCandidates+process.hltIter2PFlowCtfWithMaterialTracks+process.hltIter2PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIteration1 = cms.Sequence(process.hltIter1ClustersRefRemoval+process.hltIter1MaskedMeasurementTrackerEvent+process.hltIter1PixelLayerTriplets+process.hltIter1PFlowPixelSeeds+process.hltIter1PFlowCkfTrackCandidates+process.hltIter1PFlowCtfWithMaterialTracks+process.hltIter1PFlowTrackSelectionHighPurityLoose+process.hltIter1PFlowTrackSelectionHighPurityTight+process.hltIter1PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIteration0 = cms.Sequence(process.hltIter0PFLowPixelSeedsFromPixelTracks+process.hltIter0PFlowCkfTrackCandidates+process.hltIter0PFlowCtfWithMaterialTracks+process.hltIter0PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIter02 = cms.Sequence(process.HLTIterativeTrackingIteration0+process.HLTIter0TrackAndTauJet4Iter1Sequence+process.HLTIterativeTrackingIteration1+process.hltIter1Merged+process.HLTIter1TrackAndTauJets4Iter2Sequence+process.HLTIterativeTrackingIteration2+process.hltIter2Merged)


process.HLTRecopixelvertexingSequence = cms.Sequence(process.hltPixelLayerTriplets+process.hltPixelTracks+process.hltPixelVertices+process.hltTrimmedPixelVertices)


process.HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)


process.HLTDoLocalStripSequence = cms.Sequence(process.hltSiStripExcludedFEDListProducer+process.hltSiStripRawToClustersFacility+process.hltSiStripClusters)


process.HLTDoCaloSequencePF = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence+process.HLTDoLocalHcalSequence+process.hltTowerMakerForPF)


process.HLTAK8CaloJetsPrePFRecoSequence = cms.Sequence(process.HLTDoCaloSequencePF+process.hltAK8CaloJetsPF+process.hltAK4CaloJetsPF)


process.HLTTrackReconstructionForPF = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTRecopixelvertexingSequence+process.HLTDoLocalStripSequence+process.HLTIterativeTrackingIter02+process.hltPFMuonMerging+process.hltMuonLinks+process.hltMuons)


process.HLTL3muonTkCandidateSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.hltL3TrajSeedOIState+process.hltL3TrackCandidateFromL2OIState+process.hltL3TkTracksFromL2OIState+process.hltL3MuonsOIState+process.hltL3TrajSeedOIHit+process.hltL3TrackCandidateFromL2OIHit+process.hltL3TkTracksFromL2OIHit+process.hltL3MuonsOIHit+process.hltL3TkFromL2OICombination+process.hltPixelLayerTriplets+process.hltPixelLayerPairs+process.hltMixedLayerPairs+process.hltL3TrajSeedIOHit+process.hltL3TrackCandidateFromL2IOHit+process.hltL3TkTracksFromL2IOHit+process.hltL3MuonsIOHit+process.hltL3TrajectorySeed+process.hltL3TrackCandidateFromL2)


process.HLTL2muonrecoSequence = cms.Sequence(process.HLTL2muonrecoNocandSequence+process.hltL2MuonCandidates)


process.HLTDoCaloSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence+process.HLTDoLocalHcalSequence+process.hltTowerMakerForAll)


process.HLTPreAK8PFJetsRecoSequence = cms.Sequence(process.HLTAK8CaloJetsPrePFRecoSequence+process.hltAK8CaloJetsPFEt5+process.hltAK4CaloJetsPFEt5)


process.HLTL3muonrecoNocandSequence = cms.Sequence(process.HLTL3muonTkCandidateSequence+process.hltL3TkTracksMergeStep1+process.hltL3TkTracksFromL2+process.hltL3MuonsLinksCombination+process.hltL3Muons)


process.HLTAK4CaloJetsPrePFRecoSequence = cms.Sequence(process.HLTDoCaloSequencePF+process.hltAK4CaloJetsPF)


process.HLTPreAK4PFJetsRecoSequence = cms.Sequence(process.HLTAK4CaloJetsPrePFRecoSequence+process.hltAK4CaloJetsPFEt5)


process.HLTAK4CaloJetsReconstructionSequence = cms.Sequence(process.HLTDoCaloSequence+process.hltAK4CaloJets+process.hltAK4CaloJetsIDPassed)


process.HLTAK4CaloJetsSequence = cms.Sequence(process.HLTAK4CaloJetsReconstructionSequence+process.HLTAK4CaloJetsCorrectionSequence)


process.HLTAK8CaloJetsReconstructionSequence = cms.Sequence(process.HLTDoCaloSequence+process.hltAK8CaloJets+process.hltAK8CaloJetsIDPassed)


process.HLTL3muonrecoSequence = cms.Sequence(process.HLTL3muonrecoNocandSequence+process.hltL3MuonCandidates)


process.HLTAK8PFJetsReconstructionSequence = cms.Sequence(process.HLTL2muonrecoSequence+process.HLTL3muonrecoSequence+process.HLTTrackReconstructionForPF+process.HLTParticleFlowSequence+process.hltAK8PFJets)


process.HLTAK8PFJetsSequence = cms.Sequence(process.HLTPreAK8PFJetsRecoSequence+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence)


process.HLTAK8CaloJetsSequence = cms.Sequence(process.HLTAK8CaloJetsReconstructionSequence+process.HLTAK8CaloJetsCorrectionSequence)


process.HLTAK4PFJetsReconstructionSequence = cms.Sequence(process.HLTL2muonrecoSequence+process.HLTL3muonrecoSequence+process.HLTTrackReconstructionForPF+process.HLTParticleFlowSequence+process.hltAK4PFJets)


process.HLTAK4PFJetsSequence = cms.Sequence(process.HLTPreAK4PFJetsRecoSequence+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence)


process.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150ORHTT175)+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+cms.ignore(process.hltAK8Ht600)+process.HLTAK8CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK8CaloJetsPFEt5)+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK8PFJetsReconstructionSequence+process.HLTAK8PFJetsCorrectionSequence+process.hltAK8PFHT+process.hltAK8PFJetsTrimR0p1PT0p03+cms.ignore(process.hlt1AK8PFJetsTrimR0p1PT0p03Mass50)+cms.ignore(process.hltAK8PFHT700)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT550_4Jet_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150ORHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht4Jet+cms.ignore(process.hlt4JetHt450)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT4Jet+cms.ignore(process.hltPF4JetHT550)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT650_4Jet_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150ORHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht4Jet+cms.ignore(process.hlt4JetHt550)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT4Jet+cms.ignore(process.hltPF4JetHT650)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT750_4Jet_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150ORHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht4Jet+cms.ignore(process.hlt4JetHt550)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT4Jet+cms.ignore(process.hltPF4JetHT750)+cms.ignore(process.hltBoolEnd))


process.HLT_PFHT900_v1 = cms.Path(cms.ignore(process.hltTriggerType)+process.HLTL1UnpackerSequence+process.HLTBeamSpot+cms.ignore(process.hltL1sL1HTT150ORHTT175)+process.HLTAK4CaloJetsSequence+process.hltHtMht+cms.ignore(process.hltHt700)+process.HLTAK4CaloJetsPrePFRecoSequence+cms.ignore(process.hltAK4CaloJetsPFEt5)+process.HLTAK4PFJetsReconstructionSequence+process.HLTAK4PFJetsCorrectionSequence+process.hltPFHT+cms.ignore(process.hltPFHT900)+cms.ignore(process.hltBoolEnd))


#process.DQMOutput = cms.EndPath(process.dqmOutput)
#
#
#process.DQMStore = cms.Service("DQMStore",
#    LSbasedMode = cms.untracked.bool(False),
#    collateHistograms = cms.untracked.bool(False),
#    enableMultiThread = cms.untracked.bool(True),
#    forceResetOnBeginLumi = cms.untracked.bool(False),
#    referenceFileName = cms.untracked.string(''),
#    verbose = cms.untracked.int32(0),
#    verboseQT = cms.untracked.int32(0)
#)


process.EvFDaqDirector = cms.Service("EvFDaqDirector",
    baseDir = cms.untracked.string('.'),
    buBaseDir = cms.untracked.string('.'),
    outputAdler32Recheck = cms.untracked.bool(False),
    requireTransfersPSet = cms.untracked.bool(False),
    runNumber = cms.untracked.uint32(0),
    selectedTransferMode = cms.untracked.string('')
)


process.FastMonitoringService = cms.Service("FastMonitoringService",
    fastMonIntervals = cms.untracked.uint32(2),
    fastName = cms.untracked.string('fastmoni'),
    sleepTime = cms.untracked.int32(1),
    slowName = cms.untracked.string('slowmoni')
)


#process.FastTimerService = cms.Service("FastTimerService",
#    dqmLumiSectionsRange = cms.untracked.uint32(2500),
#    dqmModuleTimeRange = cms.untracked.double(40.0),
#    dqmModuleTimeResolution = cms.untracked.double(0.2),
#    dqmPath = cms.untracked.string('HLT/TimerService'),
#    dqmPathTimeRange = cms.untracked.double(100.0),
#    dqmPathTimeResolution = cms.untracked.double(0.5),
#    dqmTimeRange = cms.untracked.double(1000.0),
#    dqmTimeResolution = cms.untracked.double(5.0),
#    enableDQM = cms.untracked.bool(True),
#    enableDQMSummary = cms.untracked.bool(True),
#    enableDQMbyLumiSection = cms.untracked.bool(True),
#    enableDQMbyModule = cms.untracked.bool(False),
#    enableDQMbyModuleType = cms.untracked.bool(False),
#    enableDQMbyPathActive = cms.untracked.bool(True),
#    enableDQMbyPathCounters = cms.untracked.bool(True),
#    enableDQMbyPathDetails = cms.untracked.bool(True),
#    enableDQMbyPathExclusive = cms.untracked.bool(True),
#    enableDQMbyPathOverhead = cms.untracked.bool(False),
#    enableDQMbyPathTotal = cms.untracked.bool(True),
#    enableDQMbyProcesses = cms.untracked.bool(True),
#    enableTimingExclusive = cms.untracked.bool(True),
#    enableTimingModules = cms.untracked.bool(True),
#    enableTimingPaths = cms.untracked.bool(True),
#    enableTimingSummary = cms.untracked.bool(True),
#    skipFirstPath = cms.untracked.bool(False),
#    useRealTimeClock = cms.untracked.bool(True)
#)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary', 
        'TriggerSummaryProducerAOD', 
        'L1GtTrigReport', 
        'HLTrigReport', 
        'FastReport'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(500)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        placeholder = cms.untracked.bool(True),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    ),
    statistics = cms.untracked.vstring('cerr'),
    suppressDebug = cms.untracked.vstring(),
    suppressError = cms.untracked.vstring('hltOnlineBeamSpot', 
        'hltL3MuonCandidates', 
        'hltL3TkTracksFromL2OIState', 
        'hltPFJetCtfWithMaterialTracks', 
        'hltL3TkTracksFromL2IOHit', 
        'hltL3TkTracksFromL2OIHit'),
    suppressInfo = cms.untracked.vstring(),
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
    threshold = cms.untracked.string('INFO'),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    )
)


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection')
)


process.AutoMagneticFieldESProducer = cms.ESProducer("AutoMagneticFieldESProducer",
    label = cms.untracked.string(''),
    mapLabels = cms.untracked.vstring('090322_3_8t', 
        '0t', 
        '071212_2t', 
        '071212_3t', 
        '071212_3_5t', 
        '090322_3_8t', 
        '071212_4t'),
    nominalCurrents = cms.untracked.vint32(-1, 0, 9558, 14416, 16819, 
        18268, 19262),
    valueOverride = cms.int32(-1)
)


process.CSCChannelMapperESProducer = cms.ESProducer("CSCChannelMapperESProducer",
    AlgoName = cms.string('CSCChannelMapperPostls1')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
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
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz'),
    appendToDataLabel = cms.string('')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    )
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
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
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string(''),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    parameters = cms.PSet(
        BValue = cms.string('')
    ),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.SiStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
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
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SlaveField0 = cms.ESProducer("UniformMagneticFieldESProducer",
    ZFieldInTesla = cms.double(0.0),
    label = cms.untracked.string('slave_0')
)


process.SlaveField20 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    label = cms.untracked.string('slave_20'),
    parameters = cms.PSet(
        BValue = cms.string('2_0T')
    ),
    version = cms.string('OAE_1103l_071212')
)


process.SlaveField30 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    label = cms.untracked.string('slave_30'),
    parameters = cms.PSet(
        BValue = cms.string('3_0T')
    ),
    version = cms.string('OAE_1103l_071212')
)


process.SlaveField35 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    label = cms.untracked.string('slave_35'),
    parameters = cms.PSet(
        BValue = cms.string('3_5T')
    ),
    version = cms.string('OAE_1103l_071212')
)


process.SlaveField38 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    label = cms.untracked.string('slave_38'),
    parameters = cms.PSet(
        BValue = cms.string('3_8T')
    ),
    version = cms.string('OAE_1103l_071212')
)


process.SlaveField40 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    label = cms.untracked.string('slave_40'),
    parameters = cms.PSet(
        BValue = cms.string('4_0T')
    ),
    version = cms.string('OAE_1103l_071212')
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False),
    trackerGeometryConstants = cms.PSet(
        BIG_PIX_PER_ROC_X = cms.int32(1),
        BIG_PIX_PER_ROC_Y = cms.int32(2),
        COLS_PER_ROC = cms.int32(52),
        ROCS_X = cms.int32(0),
        ROCS_Y = cms.int32(0),
        ROWS_PER_ROC = cms.int32(80),
        upgradeGeometry = cms.bool(False)
    )
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VBF0 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    cacheLastVolume = cms.untracked.bool(True),
    debugBuilder = cms.untracked.bool(False),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        master = cms.int32(1),
        path = cms.string('grid.[v].bin'),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    label = cms.untracked.string('0t'),
    paramLabel = cms.string('slave_0'),
    scalingFactors = cms.vdouble(),
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    version = cms.string('grid_1103l_071212_2t')
)


process.VBF20 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    cacheLastVolume = cms.untracked.bool(True),
    debugBuilder = cms.untracked.bool(False),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        master = cms.int32(1),
        path = cms.string('grid.[v].bin'),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    label = cms.untracked.string('071212_2t'),
    paramLabel = cms.string('slave_20'),
    scalingFactors = cms.vdouble(),
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    version = cms.string('grid_1103l_071212_2t')
)


process.VBF30 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    cacheLastVolume = cms.untracked.bool(True),
    debugBuilder = cms.untracked.bool(False),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        master = cms.int32(1),
        path = cms.string('grid.[v].bin'),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    label = cms.untracked.string('071212_3t'),
    paramLabel = cms.string('slave_30'),
    scalingFactors = cms.vdouble(),
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    version = cms.string('grid_1103l_071212_3t')
)


process.VBF35 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    cacheLastVolume = cms.untracked.bool(True),
    debugBuilder = cms.untracked.bool(False),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        master = cms.int32(1),
        path = cms.string('grid.[v].bin'),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    label = cms.untracked.string('071212_3_5t'),
    paramLabel = cms.string('slave_35'),
    scalingFactors = cms.vdouble(),
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    version = cms.string('grid_1103l_071212_3_5t')
)


process.VBF38 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    cacheLastVolume = cms.untracked.bool(True),
    debugBuilder = cms.untracked.bool(False),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        master = cms.int32(1),
        path = cms.string('grid.[v].bin'),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    ), 
        cms.PSet(
            master = cms.int32(3),
            path = cms.string('S3/grid.[v].bin'),
            sectors = cms.string('3'),
            volumes = cms.string('176-186,231-241,286-296')
        ), 
        cms.PSet(
            master = cms.int32(4),
            path = cms.string('S4/grid.[v].bin'),
            sectors = cms.string('4'),
            volumes = cms.string('176-186,231-241,286-296')
        ), 
        cms.PSet(
            master = cms.int32(9),
            path = cms.string('S9/grid.[v].bin'),
            sectors = cms.string('9'),
            volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296')
        ), 
        cms.PSet(
            master = cms.int32(10),
            path = cms.string('S10/grid.[v].bin'),
            sectors = cms.string('10'),
            volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296')
        ), 
        cms.PSet(
            master = cms.int32(11),
            path = cms.string('S11/grid.[v].bin'),
            sectors = cms.string('11'),
            volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296')
        )),
    label = cms.untracked.string('090322_3_8t'),
    paramLabel = cms.string('slave_38'),
    scalingFactors = cms.vdouble(1.0, 1.0, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991),
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
    version = cms.string('grid_1103l_090322_3_8t')
)


process.VBF40 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    cacheLastVolume = cms.untracked.bool(True),
    debugBuilder = cms.untracked.bool(False),
    geometryVersion = cms.int32(71212),
    gridFiles = cms.VPSet(cms.PSet(
        master = cms.int32(1),
        path = cms.string('grid.[v].bin'),
        sectors = cms.string('0'),
        volumes = cms.string('1-312')
    )),
    label = cms.untracked.string('071212_4t'),
    paramLabel = cms.string('slave_40'),
    scalingFactors = cms.vdouble(),
    scalingVolumes = cms.vint32(),
    useParametrizedTrackerField = cms.bool(True),
    version = cms.string('grid_1103l_071212_4t')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    includeBadChambers = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    includeBadChambers = cms.bool(False),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring('kNonRespondingIsolated', 
            'kDeadVFE', 
            'kDeadFE', 
            'kNoDataNoTP'),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring('kDAC', 
            'kNoLaser', 
            'kNoisy', 
            'kNNoisy', 
            'kNNNoisy', 
            'kNNNNoisy', 
            'kNNNNNoisy', 
            'kFixedG6', 
            'kFixedG1', 
            'kFixedG0'),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring('kFaultyHardware', 
            'kDead', 
            'kKilled'),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring('kPoorReco', 
            'kPoorCalib', 
            'kNoisy', 
            'kSaturated'),
        kRecovered = cms.vstring('kLeadingEdgeRecovered', 
            'kTowerRecovered'),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring('kWeird', 
            'kDiWeird')
    ),
    timeThresh = cms.double(2.0)
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    includeBadChambers = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring('HcalCellMask', 
        'HcalCellOff', 
        'HcalCellDead'),
    RecoveredRecHitBits = cms.vstring('TimingAddedBit', 
        'TimingSubtractedBit'),
    SeverityLevels = cms.VPSet(cms.PSet(
        ChannelStatus = cms.vstring(),
        Level = cms.int32(0),
        RecHitFlags = cms.vstring()
    ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring()
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring('HSCP_R1R2', 
                'HSCP_FracLeader', 
                'HSCP_OuterEnergy', 
                'HSCP_ExpFit', 
                'ADCSaturationBit', 
                'HBHEIsolatedNoise', 
                'AddedSimHcalNoise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring('HBHEHpdHitMultiplicity', 
                'HBHEPulseShape', 
                'HOBit', 
                'HFInTimeWindow', 
                'ZDCBit', 
                'CalibrationBit', 
                'TimingErrorBit', 
                'HBHETriangleNoise', 
                'HBHETS4TS5Noise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring('HFLongShort', 
                'HFPET', 
                'HFS8S1Ratio', 
                'HFDigiTime')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12),
            RecHitFlags = cms.vstring('HBHEFlatNoise', 
                'HBHESpikeNoise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring()
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellOff', 
                'HcalCellDead'),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring()
        ))
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer")


process.hltCombinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltCombinedSecondaryVertexV2 = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPAK4CaloAbsoluteCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4CaloHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L3Absolute')
)


process.hltESPAK4CaloCorrection = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPAK4CaloFastJetCorrectionESProducer', 
        'hltESPAK4CaloRelativeCorrectionESProducer', 
        'hltESPAK4CaloAbsoluteCorrectionESProducer')
)


process.hltESPAK4CaloFastJetCorrectionESProducer = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4CaloHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAllCalo")
)


process.hltESPAK4CaloRelativeCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4CaloHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L2Relative')
)


process.hltESPAK4PFAbsoluteCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L3Absolute')
)


process.hltESPAK4PFCorrection = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPAK4PFFastJetCorrectionESProducer', 
        'hltESPAK4PFRelativeCorrectionESProducer', 
        'hltESPAK4PFAbsoluteCorrectionESProducer')
)


process.hltESPAK4PFFastJetCorrectionESProducer = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PFHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAll")
)


process.hltESPAK4PFRelativeCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L2Relative')
)


process.hltESPAK8CaloAbsoluteCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8CaloHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L3Absolute')
)


process.hltESPAK8CaloCorrection = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPAK8CaloFastJetCorrectionESProducer', 
        'hltESPAK8CaloRelativeCorrectionESProducer', 
        'hltESPAK8CaloAbsoluteCorrectionESProducer')
)


process.hltESPAK8CaloFastJetCorrectionESProducer = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8CaloHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAllCalo")
)


process.hltESPAK8CaloRelativeCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8CaloHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L2Relative')
)


process.hltESPAK8PFAbsoluteCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L3Absolute')
)


process.hltESPAK8PFCorrection = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPAK8PFFastJetCorrectionESProducer', 
        'hltESPAK8PFRelativeCorrectionESProducer', 
        'hltESPAK8PFAbsoluteCorrectionESProducer')
)


process.hltESPAK8PFFastJetCorrectionESProducer = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PFHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAll")
)


process.hltESPAK8PFRelativeCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFHLT'),
    appendToDataLabel = cms.string(''),
    level = cms.string('L2Relative')
)


process.hltESPAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPBwdAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPBwdAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.hltESPBwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPBwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2MeasurementEstimator16 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator30 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator9 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    nSigma = cms.double(3.0)
)


process.hltESPCloseComponentsMerger5D = cms.ESProducer("CloseComponentsMergerESProducer5D",
    ComponentName = cms.string('hltESPCloseComponentsMerger5D'),
    DistanceMeasure = cms.string('hltESPKullbackLeiblerDistance5D'),
    MaxComponents = cms.int32(12)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.2),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.2),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.hltESPDummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.hltESPElectronMaterialEffects = cms.ESProducer("GsfMaterialEffectsESProducer",
    BetheHeitlerCorrection = cms.int32(2),
    BetheHeitlerParametrization = cms.string('BetheHeitler_cdfmom_nC6_O5.par'),
    ComponentName = cms.string('hltESPElectronMaterialEffects'),
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    Mass = cms.double(0.000511),
    MultipleScatteringUpdator = cms.string('MultipleScatteringUpdator')
)


process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFittingSmootherIT = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPFittingSmootherIT'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK')
)


process.hltESPFittingSmootherRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPFittingSmootherRK'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK')
)


process.hltESPFwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPFwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPGlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.hltESPGsfElectronFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPGsfElectronFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPGsfTrajectoryFitter'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPGsfTrajectorySmoother')
)


process.hltESPGsfTrajectoryFitter = cms.ESProducer("GsfTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPGsfTrajectoryFitter'),
    GeometricalPropagator = cms.string('hltESPAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGsfTrajectorySmoother = cms.ESProducer("GsfTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPGsfTrajectorySmoother'),
    ErrorRescaling = cms.double(100.0),
    GeometricalPropagator = cms.string('hltESPBwdAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPKFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitter'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmoother')
)


process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon')
)


process.hltESPKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFUpdator = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('hltESPKFUpdator')
)


process.hltESPKullbackLeiblerDistance5D = cms.ESProducer("DistanceBetweenComponentsESProducer5D",
    ComponentName = cms.string('hltESPKullbackLeiblerDistance5D'),
    DistanceMeasure = cms.string('KullbackLeibler')
)


process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    minHits = cms.int32(3)
)


process.hltESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(9999),
            maxConsecutiveBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(9999),
            maxConsecutiveBad = cms.uint32(9999)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(9999),
            maxConsecutiveBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(9999),
            maxConsecutiveBad = cms.uint32(9999)
        )
    )
)


process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPMuonTransientTrackingRecHitBuilder')
)


process.hltESPPixelCPEGeneric = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    PixelErrorParametrization = cms.string('NOTcmsim'),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAAlignmentOffsets = cms.bool(False),
    useLAWidthFromDB = cms.bool(False)
)


process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPRungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.hltESPSmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagator'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite')
)


process.hltESPSoftLeptonByDistance = cms.ESProducer("LeptonTaggerByDistanceESProducer",
    distance = cms.double(0.5)
)


process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPStripCPEfromTrackAngle = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('hltESPStripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.hltESPTTRHBWithTrackAngle = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle')
)


process.hltESPTTRHBuilderPixelOnly = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    appendToDataLabel = cms.string(''),
    trackerGeometryLabel = cms.untracked.string('')
)


process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(0.0),
    ValidHitBonus = cms.double(100.0),
    allowSharedFirstHit = cms.bool(False),
    fractionShared = cms.double(0.5)
)


process.hltESPTrajectoryFitterRK = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTrajectoryFitterRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    minHits = cms.int32(3)
)


process.hltESPTrajectorySmootherRK = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTrajectorySmootherRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    includeBadChambers = cms.bool(False),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.l1GtTriggerMenuXml = cms.ESProducer("L1GtTriggerMenuXmlProducer",
    DefXmlFile = cms.string('L1Menu_Collisions2015_25ns_v2_L1T_Scales_20141121_Imp0_0x1030.xml'),
    TriggerMenuLuminosity = cms.string('startup'),
    VmeXmlFile = cms.string('')
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    etaBinSize = cms.double(0.125),
    includeBadChambers = cms.bool(False),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    includeBadChambers = cms.bool(False),
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
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string(''),
    pxb_ladderMask = cms.uint32(255),
    pxb_ladderStartBit = cms.uint32(8),
    pxb_layerMask = cms.uint32(15),
    pxb_layerStartBit = cms.uint32(16),
    pxb_moduleMask = cms.uint32(63),
    pxb_moduleStartBit = cms.uint32(2),
    pxf_bladeMask = cms.uint32(63),
    pxf_bladeStartBit = cms.uint32(10),
    pxf_diskMask = cms.uint32(15),
    pxf_diskStartBit = cms.uint32(16),
    pxf_moduleMask = cms.uint32(63),
    pxf_moduleStartBit = cms.uint32(2),
    pxf_panelMask = cms.uint32(3),
    pxf_panelStartBit = cms.uint32(8),
    pxf_sideMask = cms.uint32(3),
    pxf_sideStartBit = cms.uint32(23),
    tec_moduleMask = cms.uint32(7),
    tec_moduleStartBit = cms.uint32(2),
    tec_petalMask = cms.uint32(15),
    tec_petalStartBit = cms.uint32(8),
    tec_petal_fw_bwMask = cms.uint32(3),
    tec_petal_fw_bwStartBit = cms.uint32(12),
    tec_ringMask = cms.uint32(7),
    tec_ringStartBit = cms.uint32(5),
    tec_sideMask = cms.uint32(3),
    tec_sideStartBit = cms.uint32(18),
    tec_sterMask = cms.uint32(3),
    tec_sterStartBit = cms.uint32(0),
    tec_wheelMask = cms.uint32(15),
    tec_wheelStartBit = cms.uint32(14),
    tib_layerMask = cms.uint32(7),
    tib_layerStartBit = cms.uint32(14),
    tib_moduleMask = cms.uint32(3),
    tib_moduleStartBit = cms.uint32(2),
    tib_sterMask = cms.uint32(3),
    tib_sterStartBit = cms.uint32(0),
    tib_strMask = cms.uint32(63),
    tib_strStartBit = cms.uint32(4),
    tib_str_fw_bwMask = cms.uint32(3),
    tib_str_fw_bwStartBit = cms.uint32(12),
    tib_str_int_extMask = cms.uint32(3),
    tib_str_int_extStartBit = cms.uint32(10),
    tid_moduleMask = cms.uint32(31),
    tid_moduleStartBit = cms.uint32(2),
    tid_module_fw_bwMask = cms.uint32(3),
    tid_module_fw_bwStartBit = cms.uint32(7),
    tid_ringMask = cms.uint32(3),
    tid_ringStartBit = cms.uint32(9),
    tid_sideMask = cms.uint32(3),
    tid_sideStartBit = cms.uint32(13),
    tid_sterMask = cms.uint32(3),
    tid_sterStartBit = cms.uint32(0),
    tid_wheelMask = cms.uint32(3),
    tid_wheelStartBit = cms.uint32(11),
    tob_layerMask = cms.uint32(7),
    tob_layerStartBit = cms.uint32(14),
    tob_moduleMask = cms.uint32(7),
    tob_moduleStartBit = cms.uint32(2),
    tob_rodMask = cms.uint32(127),
    tob_rodStartBit = cms.uint32(5),
    tob_rod_fw_bwMask = cms.uint32(3),
    tob_rod_fw_bwStartBit = cms.uint32(12),
    tob_sterMask = cms.uint32(3),
    tob_sterStartBit = cms.uint32(0)
)


process.CSCChannelMapperESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCChannelMapperRecord')
)


process.CSCINdexerESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCIndexerRecord')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(0),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('PHYS14_25_V3'),
    pfnPrefix = cms.untracked.string('frontier://FrontierProd/'),
    toGet = cms.VPSet(cms.PSet(
        connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
        record = cms.string('CSCAlignmentErrorExtendedRcd'),
        tag = cms.string('MuonCSCAPEObjectsExtended_v0_mc')
    ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('DTAlignmentErrorExtendedRcd'),
            tag = cms.string('MuonDTAPEObjectsExtended_v0_mc')
        ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('EcalPulseCovariancesRcd'),
            tag = cms.string('EcalPulseCovariances_mc')
        ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('EcalPulseShapesRcd'),
            tag = cms.string('EcalPulseShapes_mc')
        ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('EcalSamplesCorrelationRcd'),
            tag = cms.string('EcalSamplesCorrelation_mc')
        ), 
        cms.PSet(
            connect = cms.untracked.string('frontier://FrontierProd/CMS_CONDITIONS'),
            record = cms.string('TrackerAlignmentErrorExtendedRcd'),
            tag = cms.string('TrackerAlignmentExtendedError_2011Realistic_v1_mc')
        ))
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.L1GtTriggerMenuRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtTriggerMenuRcd')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.hltESSBTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.hltESSEcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.hltESSHcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.magfield = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMagneticField.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml', 
        'Geometry/CMSCommonData/data/materials.xml'),
    rootNodeName = cms.string('cmsMagneticField:MAGF')
)


process.prefer("l1GtTriggerMenuXml")

process.ALCARECOEventContent = cms.PSet(
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
        'drop *_MEtoEDMConverter_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.AODEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
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
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_ak4PFJets_*_*', 
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
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
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
        'keep int_*_bunchSpacing_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
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

process.AODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
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
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_ak4PFJets_*_*', 
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
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
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
        'keep int_*_bunchSpacing_*', 
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
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*')
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
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
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
        'keep ESDigiCollection_ecalPreshowerDigis_*_*'),
    splitLevel = cms.untracked.int32(0)
)

#process.DQMEventContent = cms.PSet(
#    outputCommands = cms.untracked.vstring('drop *', 
#        'keep *_MEtoEDMConverter_*_*'),
#    splitLevel = cms.untracked.int32(0)
#)

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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
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
        'keep *_simHcalTriggerPrimitiveDigis_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTDEBUGHLTEventContent = cms.PSet(
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
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
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
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
        'keep *_hltEcalDigis_EcalIntegrityBlockSizeErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityChIdErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainSwitchErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityTTIdErrors_*', 
        'keep *_hltEcalDigis_EcalTriggerPrimitives_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
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
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
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
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
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
        'keep *_hltOnlinePrimaryVertices_*_*', 
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
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
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
        'keep *_hltVerticesL3_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep EBSrFlagsSorted_hltEcalDigis_*_*', 
        'keep EESrFlagsSorted_hltEcalDigis_*_*', 
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
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTEventContent = cms.PSet(
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep *_pfMetEI_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTHLTALLEventContent = cms.PSet(
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep *_*_*_HLT' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTSIMEventContent = cms.PSet(
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
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
        'keep *_pfMetEI_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.GENRAWEventContent = cms.PSet(
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
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep int_*_bunchSpacing_*', 
        'keep recoGenMETs_*_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_logErrorHarvester_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.GeneratorInterfaceAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.GeneratorInterfaceRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.HLTConfigVersion = cms.PSet(
    tableName = cms.string('/dev/CMSSW_7_4_0/GRun/V34')
)

process.HLTDEBUGEventContent = cms.PSet(
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
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
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
        'keep *_hltEcalDigis_EcalIntegrityBlockSizeErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityChIdErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainSwitchErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityTTIdErrors_*', 
        'keep *_hltEcalDigis_EcalTriggerPrimitives_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
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
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
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
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
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
        'keep *_hltOnlinePrimaryVertices_*_*', 
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
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
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
        'keep *_hltVerticesL3_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep EBSrFlagsSorted_hltEcalDigis_*_*', 
        'keep EESrFlagsSorted_hltEcalDigis_*_*', 
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
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
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
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
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
        'keep *_hltEcalDigis_EcalIntegrityBlockSizeErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityChIdErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainSwitchErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityTTIdErrors_*', 
        'keep *_hltEcalDigis_EcalTriggerPrimitives_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
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
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
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
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
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
        'keep *_hltOnlinePrimaryVertices_*_*', 
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
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
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
        'keep *_hltVerticesL3_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep EBSrFlagsSorted_hltEcalDigis_*_*', 
        'keep EESrFlagsSorted_hltEcalDigis_*_*', 
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
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
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
        'keep *_hltEcalDigis_EcalIntegrityBlockSizeErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityChIdErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainSwitchErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityTTIdErrors_*', 
        'keep *_hltEcalDigis_EcalTriggerPrimitives_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
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
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
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
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
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
        'keep *_hltOnlinePrimaryVertices_*_*', 
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
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
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
        'keep *_hltVerticesL3_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep EBSrFlagsSorted_hltEcalDigis_*_*', 
        'keep EESrFlagsSorted_hltEcalDigis_*_*', 
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
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter1ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter2HighPtTkMuESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter2ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTIter3PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter3ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter3PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter3PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxNumberOfHits = cms.int32(100),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter4ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    minNrOfHitsForRebuild = cms.untracked.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter4PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxNumberOfHits = cms.int32(100),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTPSetCkf3HitTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(-1),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTPSetCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(-1),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiEffTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(9),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(8),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(10.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(-1),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTPSetPvClusterComparer = cms.PSet(
    track_chi2_max = cms.double(9999999.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(10.0),
    track_pt_min = cms.double(2.5)
)

process.HLTPSetPvClusterComparerForBTag = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(0.1)
)

process.HLTPSetPvClusterComparerForIT = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(1.0)
)

process.HLTPSetTrajectoryBuilderForElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryFilterForElectrons = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(-1),
    minHitsMinPt = cms.int32(-1),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTPSetTrajectoryFilterL3 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(1000000000),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(0.5),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(8),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0)
)

process.HLTSeedFromConsecutiveHitsCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    propagator = cms.string('PropagatorWithMaterial')
)

process.HLTSeedFromConsecutiveHitsCreatorIT = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSeedFromProtoTracks = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.HLTSiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.HLTSiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
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
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep *_externalLHEProducer_LHEScriptOutput_*'),
    splitLevel = cms.untracked.int32(0)
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
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep *_slimmedPhotons*_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons*_*_*', 
        'keep *_slimmedTaus*_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs*_*_*', 
        'keep *_slimmedSecondaryVertices*_*_*', 
        'keep *_cmsTopTaggerMap_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsCMSTopTagCHSPacked_SubJets_*', 
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
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_PAT', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep *_caTopTagInfosPAT_*_*')
)

process.MINIAODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep *_slimmedPhotons*_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons*_*_*', 
        'keep *_slimmedTaus*_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs*_*_*', 
        'keep *_slimmedSecondaryVertices*_*_*', 
        'keep *_cmsTopTaggerMap_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsCMSTopTagCHSPacked_SubJets_*', 
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
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_PAT', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep *_caTopTagInfosPAT_*_*', 
        'keep *_slimmedGenJets*_*_*', 
        'keep patPackedGenParticles_packedGenParticles_*_*', 
        'keep recoGenParticles_prunedGenParticles_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep GenRunInfoProduct_*_*_*', 
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*')
)

process.MIXINGMODULEEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_cfWriter_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.MicroEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_slimmedPhotons*_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons*_*_*', 
        'keep *_slimmedTaus*_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs*_*_*', 
        'keep *_slimmedSecondaryVertices*_*_*', 
        'keep *_cmsTopTaggerMap_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsCMSTopTagCHSPacked_SubJets_*', 
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
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_PAT', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep *_caTopTagInfosPAT_*_*')
)

process.MicroEventContentMC = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_slimmedPhotons*_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons*_*_*', 
        'keep *_slimmedTaus*_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs*_*_*', 
        'keep *_slimmedSecondaryVertices*_*_*', 
        'keep *_cmsTopTaggerMap_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsCMSTopTagCHSPacked_SubJets_*', 
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
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_PAT', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep *_caTopTagInfosPAT_*_*', 
        'keep *_slimmedGenJets*_*_*', 
        'keep patPackedGenParticles_packedGenParticles_*_*', 
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
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep int_*_bunchSpacing_*', 
        'keep recoGenMETs_*_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep RPCDetIdRPCDigiMuonDigiCollection_simMuonRPCDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.PREMIXRAWEventContent = cms.PSet(
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'drop CrossingFramePlaybackInfoNew_mix_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RAWDEBUGEventContent = cms.PSet(
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RAWDEBUGHLTEventContent = cms.PSet(
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
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
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
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
        'keep *_hltEcalDigis_EcalIntegrityBlockSizeErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityChIdErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainSwitchErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityTTIdErrors_*', 
        'keep *_hltEcalDigis_EcalTriggerPrimitives_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
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
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
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
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
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
        'keep *_hltOnlinePrimaryVertices_*_*', 
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
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
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
        'keep *_hltVerticesL3_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep EBSrFlagsSorted_hltEcalDigis_*_*', 
        'keep EESrFlagsSorted_hltEcalDigis_*_*', 
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
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RAWRECODEBUGHLTEventContent = cms.PSet(
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
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
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
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
        'keep *_hltEcalDigis_EcalIntegrityBlockSizeErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityChIdErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainSwitchErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityTTIdErrors_*', 
        'keep *_hltEcalDigis_EcalTriggerPrimitives_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
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
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
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
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
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
        'keep *_hltOnlinePrimaryVertices_*_*', 
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
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
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
        'keep *_hltVerticesL3_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep EBSrFlagsSorted_hltEcalDigis_*_*', 
        'keep EESrFlagsSorted_hltEcalDigis_*_*', 
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWRECOEventContent = cms.PSet(
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep FEDRawDataCollection_source_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWRECOSIMHLTEventContent = cms.PSet(
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
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
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
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
        'keep *_hltEcalDigis_EcalIntegrityBlockSizeErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityChIdErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainSwitchErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityTTIdErrors_*', 
        'keep *_hltEcalDigis_EcalTriggerPrimitives_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
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
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
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
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
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
        'keep *_hltOnlinePrimaryVertices_*_*', 
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
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
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
        'keep *_hltVerticesL3_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep EBSrFlagsSorted_hltEcalDigis_*_*', 
        'keep EESrFlagsSorted_hltEcalDigis_*_*', 
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
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWSIMEventContent = cms.PSet(
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep *_logErrorHarvester_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RAWSIMHLTEventContent = cms.PSet(
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
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
        'keep *_hltEcalDigis_EcalIntegrityBlockSizeErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityChIdErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityGainSwitchErrors_*', 
        'keep *_hltEcalDigis_EcalIntegrityTTIdErrors_*', 
        'keep *_hltEcalDigis_EcalTriggerPrimitives_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
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
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
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
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
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
        'keep *_hltOnlinePrimaryVertices_*_*', 
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
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
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
        'keep *_hltVerticesL3_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep EBSrFlagsSorted_hltEcalDigis_*_*', 
        'keep EESrFlagsSorted_hltEcalDigis_*_*', 
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
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RECODEBUGEventContent = cms.PSet(
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RECOEventContent = cms.PSet(
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep *_pfMetEI_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RECOSIMEventContent = cms.PSet(
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
        'keep *_hbheprereco_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.REDIGIEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring('drop *', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*')
)

process.REPACKRAWEventContent = cms.PSet(
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
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'drop FEDRawDataCollection_source_*_*', 
        'drop FEDRawDataCollection_rawDataCollector_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.REPACKRAWSIMEventContent = cms.PSet(
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
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'drop FEDRawDataCollection_rawDataCollector_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RESIMEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring('drop *', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
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
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*')
)

process.RecoBTagFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*')
)

process.RecoBTagRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*')
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
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
        'keep *_egmGedGsfElectronPF*Isolation_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
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
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
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
    outputCommands = cms.untracked.vstring('keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*')
)

process.RecoGenJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*')
)

process.RecoGenJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
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
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_ak4PFJets_*_*', 
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
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*')
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
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca*Mass_*_*', 
        'keep *_ak*Mass_*_*')
)

process.RecoJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*')
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
        'keep *_ecalMultiFitUncalibRecHit_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*')
)

process.RecoLocalCaloRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
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
    outputCommands = cms.untracked.vstring('keep *_dt4DSegments_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*')
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
    outputCommands = cms.untracked.vstring('keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'drop recoHcalNoiseRBXs_*_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *GlobalHaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*')
)

process.RecoMETFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*')
)

process.RecoMETRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*')
)

process.RecoMuonFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
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
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
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
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxHitInfo_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
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
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
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
    outputCommands = cms.untracked.vstring('keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*')
)

process.SimGeneralFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*')
)

process.SimGeneralRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*')
)

process.SimGeneralRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*')
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
    AlCaLumiPixels = cms.vstring('AlCa_LumiPixels_Random_v1', 
        'AlCa_LumiPixels_ZeroBias_v1'),
    AlCaPhiSym = cms.vstring('AlCa_EcalPhiSym_v1'),
    EcalLaser = cms.vstring('HLT_EcalCalibration_v1'),
    HCalNZS = cms.vstring('HLT_HcalNZS_v1', 
        'HLT_HcalPhiSym_v1', 
        'HLT_HcalUTCA_v1'),
    HcalHPDNoise = cms.vstring('HLT_GlobalRunHPDNoise_v1', 
        'HLT_L1Tech_HBHEHO_totalOR_v1', 
        'HLT_L1Tech_HCAL_HF_single_channel_v1'),
    InitialPD = cms.vstring( ('HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_v1', 
        'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1', 
        'HLT_AK8PFJet360_TrimMass30_v1', 
        'HLT_Activity_Ecal_SC7_v1', 
        'HLT_BTagMu_DiJet110_Mu5_v1', 
        'HLT_BTagMu_DiJet20_Mu5_v1', 
        'HLT_BTagMu_DiJet40_Mu5_v1', 
        'HLT_BTagMu_DiJet70_Mu5_v1', 
        'HLT_BTagMu_Jet300_Mu5_v1', 
        'HLT_CaloJet500_NoJetID_v1', 
        'HLT_CaloMET200_NoiseCleaned_v1', 
        'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_BTagCSV0p7_v1', 
        'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_v1', 
        'HLT_DiCentralPFJet70_PFMET120_NoiseCleaned_v1', 
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v1', 
        'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v1', 
        'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80_v1', 
        'HLT_DiPFJetAve100_HFJEC_v1', 
        'HLT_DiPFJetAve160_HFJEC_v1', 
        'HLT_DiPFJetAve220_HFJEC_v1', 
        'HLT_DiPFJetAve300_HFJEC_v1', 
        'HLT_DiPFJetAve30_HFJEC_v1', 
        'HLT_DiPFJetAve60_HFJEC_v1', 
        'HLT_DiPFJetAve80_HFJEC_v1', 
        'HLT_Dimuon0_Jpsi_Muon_v1', 
        'HLT_Dimuon0_Phi_Barrel_v1', 
        'HLT_Dimuon0_Upsilon_Muon_v1', 
        'HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v1', 
        'HLT_Dimuon0er16_Jpsi_NoVertexing_v1', 
        'HLT_Dimuon10_Jpsi_Barrel_v1', 
        'HLT_Dimuon13_PsiPrime_v1', 
        'HLT_Dimuon13_Upsilon_v1', 
        'HLT_Dimuon16_Jpsi_v1', 
        'HLT_Dimuon20_Jpsi_v1', 
        'HLT_Dimuon6_Jpsi_NoVertexing_v1', 
        'HLT_Dimuon8_PsiPrime_Barrel_v1', 
        'HLT_Dimuon8_Upsilon_Barrel_v1', 
        'HLT_Diphoton28_14_R9Id85_OR_Iso50T80LCaloId24b40e_AND_HE10P0_R9Id50b80e_Mass50_Eta_1p5_v1', 
        'HLT_Diphoton30_18_R9Id85_AND_Iso50T80LCaloId24b40e_AND_HE10P0_R9Id50b80e_DoublePV_v1', 
        'HLT_Diphoton30_18_R9Id85_AND_Iso50T80LCaloId24b40e_AND_HE10P0_R9Id50b80e_PV_v1', 
        'HLT_Diphoton30_18_R9Id85_AND_Iso50T80LCaloId24b40e_AND_HE10P0_R9Id50b80e_Solid_Mass30_v1', 
        'HLT_Diphoton30_18_R9Id85_OR_Iso50T80LCaloId24b40e_AND_HE10P0_R9Id50b80e_Mass95_v1', 
        'HLT_Diphoton30_18_R9Id85_OR_Iso50T80LCaloId24b40e_AND_HE10P0_R9Id50b80e_PixelSeed_Mass70_v1', 
        'HLT_Diphoton44_28_R9Id85_OR_Iso50T80LCaloId24b40e_AND_HE10P1_R9Id50b80e_v1', 
        'HLT_DoubleEle24_22_eta2p1_WP75_Gsf_v1', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v1', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1', 
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v1', 
        'HLT_DoubleIsoMu17_eta2p1_v1', 
        'HLT_DoubleJet90_Double30_DoubleCSV0p5_v1', 
        'HLT_DoubleJet90_Double30_TripleCSV0p5_v1', 
        'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v1', 
        'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v1', 
        'HLT_DoubleMu33NoFiltersNoVtx_v1', 
        'HLT_DoubleMu38NoFiltersNoVtx_v1', 
        'HLT_DoubleMu4_3_Bs_v1', 
        'HLT_DoubleMu4_3_Jpsi_Displaced_v1', 
        'HLT_DoubleMu4_JpsiTrk_Displaced_v1', 
        'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v1', 
        'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v1', 
        'HLT_DoubleMu8_Mass8_PFHT300_v1', 
        'HLT_DoublePhoton85_v1', 
        'HLT_ECALHT800_v1', 
        'HLT_Ele105_CaloIdVT_GsfTrkIdT_v1', 
        'HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV0p5PF_v1', 
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v1', 
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
        'HLT_Ele12_CaloIdM_TrackIdM_PFJet30_v1', 
        'HLT_Ele15_IsoVVVL_BTagtop8CSV07_PFHT400_v1', 
        'HLT_Ele15_IsoVVVL_PFHT400_PFMET70_v1', 
        'HLT_Ele15_IsoVVVL_PFHT600_v1', 
        'HLT_Ele15_PFHT300_v1', 
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v1', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v1', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
        'HLT_Ele18_CaloIdL_TrackIdL_IsoVL_PFJet30_v1', 
        'HLT_Ele18_CaloIdM_TrackIdM_PFJet30_v1', 
        'HLT_Ele20WP60_Ele8_Mass55_v1', 
        'HLT_Ele22_eta2p1_WP75_Gsf_LooseIsoPFTau20_v1', 
        'HLT_Ele22_eta2p1_WP75_Gsf_v1', 
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v1', 
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v1', 
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v1', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v1', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
        'HLT_Ele25WP60_SC4_Mass55_v1', 
        'HLT_Ele27_WP85_Gsf_v1', 
        'HLT_Ele27_eta2p1_WP75_Gsf_CentralPFJet30_BTagCSV07_v1', 
        'HLT_Ele27_eta2p1_WP75_Gsf_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
        'HLT_Ele27_eta2p1_WP75_Gsf_LooseIsoPFTau20_v1', 
        'HLT_Ele27_eta2p1_WP75_Gsf_TriCentralPFJet30_v1', 
        'HLT_Ele27_eta2p1_WP75_Gsf_TriCentralPFJet50_40_30_v1', 
        'HLT_Ele27_eta2p1_WP75_Gsf_v1', 
        'HLT_Ele27_eta2p1_WP85_Gsf_HT200_v1', 
        'HLT_Ele32_eta2p1_WP75_Gsf_CentralPFJet30_BTagCSV07_v1', 
        'HLT_Ele32_eta2p1_WP75_Gsf_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
        'HLT_Ele32_eta2p1_WP75_Gsf_LooseIsoPFTau20_v1', 
        'HLT_Ele32_eta2p1_WP75_Gsf_TriCentralPFJet30_v1', 
        'HLT_Ele32_eta2p1_WP75_Gsf_TriCentralPFJet50_40_30_v1', 
        'HLT_Ele32_eta2p1_WP75_Gsf_v1', 
        'HLT_Ele33_CaloIdL_TrackIdL_IsoVL_PFJet30_v1', 
        'HLT_Ele33_CaloIdM_TrackIdM_PFJet30_v1', 
        'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1', 
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v1', 
        'HLT_HT200_v1', 
        'HLT_HT250_v1', 
        'HLT_HT300_v1', 
        'HLT_HT350_DisplacedDijet40_DisplacedTrack_v1', 
        'HLT_HT350_DisplacedDijet80_DisplacedTrack_v1', 
        'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v1', 
        'HLT_HT350_v1', 
        'HLT_HT400_v1', 
        'HLT_HT500_DisplacedDijet40_Inclusive_v1', 
        'HLT_HT550_DisplacedDijet40_Inclusive_v1', 
        'HLT_HT650_DisplacedDijet80_Inclusive_v1', 
        'HLT_HT750_DisplacedDijet80_Inclusive_v1', 
        'HLT_IsoMu16_eta2p1_CaloMET30_LooseIsoPFTau50_Trk30_eta2p1_v1', 
        'HLT_IsoMu16_eta2p1_CaloMET30_v1', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v1', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1', 
        'HLT_IsoMu17_eta2p1_MediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu17_eta2p1_v1', 
        'HLT_IsoMu20_eta2p1_CentralPFJet30_BTagCSV07_v1', 
        'HLT_IsoMu20_eta2p1_TriCentralPFJet30_v1', 
        'HLT_IsoMu20_eta2p1_TriCentralPFJet50_40_30_v1', 
        'HLT_IsoMu20_eta2p1_v1', 
        'HLT_IsoMu20_v1', 
        'HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v1', 
        'HLT_IsoMu24_eta2p1_LooseIsoPFTau20_v1', 
        'HLT_IsoMu24_eta2p1_TriCentralPFJet30_v1', 
        'HLT_IsoMu24_eta2p1_TriCentralPFJet50_40_30_v1', 
        'HLT_IsoMu24_eta2p1_v1', 
        'HLT_IsoMu27_v1', 
        'HLT_IsoTkMu20_eta2p1_v1', 
        'HLT_IsoTkMu20_v1', 
        'HLT_IsoTkMu24_eta2p1_v1', 
        'HLT_IsoTkMu27_v1', 
        'HLT_JetE30_NoBPTX3BX_NoHalo_v1', 
        'HLT_JetE30_NoBPTX_v1', 
        'HLT_JetE50_NoBPTX3BX_NoHalo_v1', 
        'HLT_JetE70_NoBPTX3BX_NoHalo_v1', 
        'HLT_L1SingleEG5_OR_EG10_OR_EG20_v1', 
        'HLT_L1SingleMuOpen_DT_v1', 
        'HLT_L1SingleMuOpen_v1', 
        'HLT_L1Tech_DT_GlobalOR_v1', 
        'HLT_L1_TripleJet_VBF_v1', 
        'HLT_L2DoubleMu23_NoVertex_v1', 
        'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v1', 
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v1', 
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1', 
        'HLT_L2Mu10_NoVertex_NoBPTX_v1', 
        'HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1', 
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v1', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80_v1', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_v1', 
        'HLT_MET75_IsoTrk50_v1', 
        'HLT_MET90_IsoTrk50_v1', 
        'HLT_MonoCentralPFJet80_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v1', 
        'HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v1', 
        'HLT_Mu10_CentralPFJet30_BTagCSV0p5PF_v1', 
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v1', 
        'HLT_Mu12_Photon25_CaloIdL_L1ISO_v1', 
        'HLT_Mu12_Photon25_CaloIdL_L1OR_v1', 
        'HLT_Mu12_Photon25_CaloIdL_v1', 
        'HLT_Mu14er_PFMET120_NoiseCleaned_v1', 
        'HLT_Mu15_IsoVVVL_BTagCSV07_PFHT400_v1', 
        'HLT_Mu15_IsoVVVL_PFHT400_PFMET70_v1', 
        'HLT_Mu15_IsoVVVL_PFHT600_v1', 
        'HLT_Mu15_PFHT300_v1', 
        'HLT_Mu16_TkMu0_dEta18_Onia_v1', 
        'HLT_Mu16_TkMu0_dEta18_Phi_v1', 
        'HLT_Mu16_eta2p1_CaloMET30_v1', 
        'HLT_Mu17_Mu8_DZ_v1', 
        'HLT_Mu17_Mu8_SameSign_DPhi_v1', 
        'HLT_Mu17_Mu8_SameSign_v1', 
        'HLT_Mu17_Photon30_CaloIdL_L1ISO_v1', 
        'HLT_Mu17_Photon35_CaloIdL_L1ISO_v1', 
        'HLT_Mu17_TkMu8_DZ_v1', 
        'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v1', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v1', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1', 
        'HLT_Mu17_TrkIsoVVL_v1', 
        'HLT_Mu17_v1', 
        'HLT_Mu20_v1', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
        'HLT_Mu24_TrkIsoVVL_v1', 
        'HLT_Mu24_eta2p1_v1', 
        'HLT_Mu24_v1', 
        'HLT_Mu25_TkMu0_dEta18_Onia_v1', 
        'HLT_Mu27_TkMu8_v1', 
        'HLT_Mu27_v1', 
        'HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v1', 
        'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v1', 
        'HLT_Mu30_TkMu11_v1', 
        'HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL_v1', 
        'HLT_Mu34_TrkIsoVVL_v1', 
        'HLT_Mu34_v1', 
        'HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v1', 
        'HLT_Mu3er_PFHT140_PFMET125_NoiseCleaned_v1', 
        'HLT_Mu40_TkMu11_v1', 
        'HLT_Mu40_eta2p1_PFJet200_PFJet50_v1', 
        'HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL_v1', 
        'HLT_Mu45_eta2p1_v1', 
        'HLT_Mu50_v1', 
        'HLT_Mu6_PFHT200_PFMET100_NoiseCleaned_BTagCSV07_v1', 
        'HLT_Mu6_PFHT200_PFMET125_NoiseCleaned_v1', 
        'HLT_Mu7p5_L2Mu2_Jpsi_v1', 
        'HLT_Mu7p5_L2Mu2_Upsilon_v1', 
        'HLT_Mu7p5_Track2_Jpsi_v1', 
        'HLT_Mu7p5_Track2_Upsilon_v1', 
        'HLT_Mu7p5_Track3p5_Jpsi_v1', 
        'HLT_Mu7p5_Track3p5_Upsilon_v1', 
        'HLT_Mu7p5_Track7_Jpsi_v1', 
        'HLT_Mu7p5_Track7_Upsilon_v1', 
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v1', 
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v1', 
        'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v1', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v1', 
        'HLT_Mu8_TrkIsoVVL_v1', 
        'HLT_Mu8_v1', 
        'HLT_PFHT200_DiPFJet90_PFAlphaT0p57_v1', 
        'HLT_PFHT250_DiPFJet90_PFAlphaT0p55_v1', 
        'HLT_PFHT300_DiPFJet90_PFAlphaT0p53_v1', 
        'HLT_PFHT350_DiPFJet90_PFAlphaT0p52_v1', 
        'HLT_PFHT350_PFMET120_NoiseCleaned_v1', 
        'HLT_PFHT350_v1', 
        'HLT_PFHT400_DiPFJet90_PFAlphaT0p51_v1', 
        'HLT_PFHT400_SixJet30_BTagCSV0p5_2PFBTagCSV_v1', 
        'HLT_PFHT400_SixJet30_v1', 
        'HLT_PFHT450_SixJet40_PFBTagCSV_v1', 
        'HLT_PFHT450_SixJet40_v1', 
        'HLT_PFHT550_4Jet_v1', 
        'HLT_PFHT600_v1', 
        'HLT_PFHT650_4Jet_v1', 
        'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v1', 
        'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v1', 
        'HLT_PFHT650_v1', 
        'HLT_PFHT750_4Jet_v1', 
        'HLT_PFHT900_v1', 
        'HLT_PFJet140_v1', 
        'HLT_PFJet200_v1', 
        'HLT_PFJet260_v1', 
        'HLT_PFJet320_v1', 
        'HLT_PFJet400_v1', 
        'HLT_PFJet40_v1', 
        'HLT_PFJet450_v1', 
        'HLT_PFJet500_v1', 
        'HLT_PFJet60_v1', 
        'HLT_PFJet80_v1', 
        'HLT_PFMET100_PFMHT100_IDLoose_v1', 
        'HLT_PFMET110_PFMHT110_IDLoose_v1', 
        'HLT_PFMET120_NoiseCleaned_BTagCSV07_v1', 
        'HLT_PFMET120_NoiseCleaned_Mu5_v1', 
        'HLT_PFMET120_PFMHT120_IDLoose_v1', 
        'HLT_PFMET170_NoiseCleaned_v1', 
        'HLT_PFMET90_PFMHT90_IDLoose_v1', 
        'HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v1', 
        'HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v1', 
        'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon120_R9Id90_HE10_IsoM_v1', 
        'HLT_Photon120_v1', 
        'HLT_Photon135_PFMET100_NoiseCleaned_v1', 
        'HLT_Photon165_HE10_v1', 
        'HLT_Photon165_R9Id90_HE10_IsoM_v1', 
        'HLT_Photon175_v1', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon22_R9Id90_HE10_IsoM_v1', 
        'HLT_Photon22_v1', 
        'HLT_Photon250_NoHE_v1', 
        'HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60_v1', 
        'HLT_Photon300_NoHE_v1', 
        'HLT_Photon30_R9Id90_HE10_IsoM_v1', 
        'HLT_Photon30_v1', 
        'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15_v1', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon36_R9Id90_HE10_IsoM_v1', 
        'HLT_Photon36_v1', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon50_R9Id90_HE10_IsoM_v1', 
        'HLT_Photon50_v1', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon75_R9Id90_HE10_IsoM_v1', 
        'HLT_Photon75_v1', 
        'HLT_Photon90_CaloIdL_PFHT500_v1', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
        'HLT_Photon90_R9Id90_HE10_IsoM_v1', 
        'HLT_Photon90_v1', 
        'HLT_Physics_v1', 
        'HLT_QuadJet45_DoubleCSV0p5_v1', 
        'HLT_QuadJet45_TripleCSV0p5_v1', 
        'HLT_QuadMuon0_Dimuon0_Jpsi_v1', 
        'HLT_QuadMuon0_Dimuon0_Upsilon_v1', 
        'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq200_v1', 
        'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq240_v1', 
        'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq460_v1', 
        'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq500_v1', 
        'HLT_QuadPFJet_VBF_v1', 
        'HLT_Random_v1', 
        'HLT_Rsq0p36_v1', 
        'HLT_RsqMR260_Rsq0p09_MR200_4jet_v1', 
        'HLT_RsqMR260_Rsq0p09_MR200_v1', 
        'HLT_RsqMR300_Rsq0p09_MR200_4jet_v1', 
        'HLT_RsqMR300_Rsq0p09_MR200_v1', 
        'HLT_TkMu20_v1', 
        'HLT_TkMu24_eta2p1_v1', 
        'HLT_TkMu27_v1', 
        'HLT_TripleMu_12_10_5_v1', 
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v1', 
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v1', 
        'HLT_VBF_DisplacedJet40_DisplacedTrack_v1', 
        'HLT_VBF_DisplacedJet40_Hadronic_v1', 
        'HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v1', 
        'HLT_VBF_DisplacedJet40_TightID_Hadronic_v1', 
        'HLT_ZeroBias_v1' ) ),
    RPCMonitor = cms.vstring('AlCa_RPCMuonNoHits_v1', 
        'AlCa_RPCMuonNoTriggers_v1', 
        'AlCa_RPCMuonNormalisation_v1'),
    Templates = cms.vstring('HLT_AK4CaloJetsForMC_v1', 
        'HLT_AK4PFJetsForMC_v1', 
        'HLT_AK8CaloHTForMC_v1', 
        'HLT_AK8PFHTForMC_v1', 
        'HLT_AK8PFJetsForMC_v1', 
        'HLT_AK8TrimPFJetsForMC_v1', 
        'HLT_CaloHTForMC_v1', 
        'HLT_CaloMETCleanedForMC_v1', 
        'HLT_CaloMETForMC_v1', 
        'HLT_CaloMHTForMC_v1', 
        'HLT_PFHTForMC_v1', 
        'HLT_PFMETForMC_v1', 
        'HLT_PFMHTForMC_v1', 
        'HLT_ReducedIterativeTracking_v1'),
    TestEnablesEcalHcalDT = cms.vstring('HLT_EcalCalibration_v1', 
        'HLT_HcalCalibration_v1')
)

process.ecalLocalRecoAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.ecalLocalRecoFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ecalMultiFitUncalibRecHit_*_*', 
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
    wantSummary = cms.untracked.bool(False)
)

process.streams = cms.PSet(
    A = cms.vstring('HCalNZS', 
        'HcalHPDNoise', 
        'InitialPD', 
        'Templates'),
    ALCALUMIPIXELS = cms.vstring('AlCaLumiPixels'),
    ALCAPHISYM = cms.vstring('AlCaPhiSym'),
    Calibration = cms.vstring('TestEnablesEcalHcalDT'),
    EcalCalibration = cms.vstring('EcalLaser'),
    RPCMON = cms.vstring('RPCMonitor')
)

