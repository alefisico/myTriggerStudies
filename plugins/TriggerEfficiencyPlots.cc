// -*- C++ -*-
//
// Package:    MyTrigger/myTriggerStudies
// Class:      TriggerEfficiencyPlots.cc
// 
/**\class TriggerEfficiencyPlots.cc TriggerEfficiencyPlots.cc.cc MyTrigger/myTriggerStudies/plugins/TriggerEfficiencyPlots.cc.cc

 Description: Computesi HT and Leading Jet Mass turn-on curves for trigger paths.

*/
//
// Original Author:  Alejandro Gomez Espinosa
//         Created:  Wed, 27 Aug 2014 19:40:39 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"


#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "TMath.h"
#include "TH2D.h"
#include "TH1D.h"
#include <TLorentzVector.h>

//
// class declaration
//

class TriggerEfficiencyPlots : public edm::EDAnalyzer {
	public:
		explicit TriggerEfficiencyPlots(const edm::ParameterSet&);
		~TriggerEfficiencyPlots();

		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
		static bool compare_JetMass(const TLorentzVector jet1, const TLorentzVector jet2){
			return ( jet1.M() > jet2.M() );
		}


	private:
		virtual void beginJob() override;
		virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
		virtual void endJob() override;


		// ----------member data ---------------------------
		std::map< std::string, TH2D* > histos2D_;
		std::map< std::string, TH1D* > histos1D_;

		edm::EDGetTokenT<reco::PFJetCollection> jetsForEff;
		edm::EDGetTokenT<reco::PFJetCollection> hltJets;
		edm::EDGetTokenT<reco::PFJetCollection> hltJetsTrim;
		edm::EDGetTokenT<reco::PFJetCollection> hltJetsTrimMod;
		edm::EDGetTokenT<reco::PFJetCollection> hltJetsPruned;
		edm::EDGetTokenT<pat::JetCollection> patJets;
		edm::EDGetTokenT<pat::JetCollection> patJetsTrim;
		edm::EDGetTokenT<pat::JetCollection> patJetsTrimMod;
		edm::EDGetTokenT<pat::JetCollection> patJetsPruned;
		edm::EDGetTokenT<reco::VertexCollection> hltPV;
		std::string triggerPath;
		double minPt;
		double minHT;
		double minMass;

		HLTConfigProvider hltConfig;
		int triggerBit;
};



TriggerEfficiencyPlots::TriggerEfficiencyPlots(const edm::ParameterSet& iConfig):
	jetsForEff(consumes<reco::PFJetCollection>(iConfig.getParameter<edm::InputTag> ( "jetsForEff" ))),   			// Obtain inputs
	hltJets(consumes<reco::PFJetCollection>(iConfig.getParameter<edm::InputTag> ( "hltJets" ))),  	// Obtain inputs
	hltJetsTrim(consumes<reco::PFJetCollection>(iConfig.getParameter<edm::InputTag> ( "hltJetsTrim" ))),   			// Obtain inputs
	hltJetsTrimMod(consumes<reco::PFJetCollection>(iConfig.getParameter<edm::InputTag> ( "hltJetsTrimMod" ))),   			// Obtain inputs
	hltJetsPruned(consumes<reco::PFJetCollection>(iConfig.getParameter<edm::InputTag> ( "hltJetsPruned" ))),   			// Obtain inputs
	patJets(consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag> ( "patJets" ))),   			// Obtain inputs
	patJetsTrim(consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag> ( "patJetsTrim" ))),   			// Obtain inputs
	patJetsTrimMod(consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag> ( "patJetsTrimMod" ))),   			// Obtain inputs
	patJetsPruned(consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag> ( "patJetsPruned" ))),   			// Obtain inputs
	hltPV(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag> ( "primaryVertex" )))   			// Obtain inputs
{
	triggerPath		= iConfig.getParameter<std::string> ( "triggerPath" );   			// Obtain inputs
	minHT			= iConfig.getParameter<double> ( "minHT" );   			// Obtain inputs
	minPt			= iConfig.getParameter<double> ( "minPt" );   			// Obtain inputs
	minMass			= iConfig.getParameter<double> ( "minMass" );   			// Obtain inputs
}


TriggerEfficiencyPlots::~TriggerEfficiencyPlots()
{
}


//
// member functions
//

// ------------ method called for each event  ------------
void TriggerEfficiencyPlots::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {

	using namespace edm;
	using namespace std;

	bool changedConfig = false;
	if (!hltConfig.init(iEvent.getRun(), iSetup, "HLT3PB", changedConfig)) {
		cout << "Initialization of HLTConfigProvider failed!!" << endl;
		return;
	}
	if (changedConfig){
		std::cout << "the curent menu is " << hltConfig.tableName() << std::endl;
		triggerBit = -1;
		for (size_t j = 0; j < hltConfig.triggerNames().size(); j++) {
			//std::cout << TString(hltConfig.triggerNames()[j]) << std::endl;
			if (TString(hltConfig.triggerNames()[j]).Contains(triggerPath)) triggerBit = j;
		}
		//std::cout << triggerBit << std::endl;
		if (triggerBit == -1) cout << "HLT path not found" << endl;

	}

	//open the trigger summary
	edm::InputTag triggerResultsLabel = edm::InputTag("TriggerResults", "", "HLT3PB");
	edm::Handle<edm::TriggerResults> triggerResults;
	iEvent.getByLabel(triggerResultsLabel, triggerResults);

	edm::Handle<reco::VertexCollection> vertices;
	iEvent.getByToken(hltPV, vertices);
	//edm::LogWarning("test")<< vertices->size();
	//int NPV = vertices->size();
	histos1D_[ "numPV" ]->Fill( vertices->size() );
	

	/*edm::InputTag triggerSummaryLabel_ = edm::InputTag("hltTriggerSummaryAOD", "", "HLT");
	edm::Handle<trigger::TriggerEvent> triggerSummary;
	iEvent.getByToken(triggerSummaryLabel_, triggerSummary);*/

	edm::Handle<reco::PFJetCollection> hltjets;
	iEvent.getByToken(hltJets,hltjets);
	TLorentzVector hlt1Jet;
	double hltHT = 0;
	int nhltJets =0;
	for(const pat::Jet &ijet : *hltjets ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		hltHT += ijet.pt();
		if ( (nhltJets++) == 1 ) hlt1Jet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}
	//edm::LogWarning("test")<< hlt1Jet.M() << " " << hlt1Jet.Pt() << " " << hltHT ;

	edm::Handle<reco::PFJetCollection> hltjetsTrim;
	iEvent.getByToken(hltJetsTrim,hltjetsTrim);
	TLorentzVector hlt1JetTrim;
	double hltHTTrim = 0;
	int nhltJetsTrim =0;
	for(const pat::Jet &ijet : *hltjetsTrim ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		hltHTTrim += ijet.pt();
		if ( (nhltJetsTrim++) == 1 ) hlt1JetTrim.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<reco::PFJetCollection> hltjetsTrimMod;
	iEvent.getByToken(hltJetsTrimMod,hltjetsTrimMod);
	TLorentzVector hlt1JetTrimMod;
	std::vector<TLorentzVector> vecHltJetsTrim;
	double hltHTTrimMod = 0;
	for(const pat::Jet &ijet : *hltjetsTrimMod ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		hltHTTrimMod += ijet.pt();
		TLorentzVector tmpJet;
		tmpJet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
		vecHltJetsTrim.push_back( tmpJet );
	}
	if ( vecHltJetsTrim.size() > 0 ){
		sort(vecHltJetsTrim.begin(), vecHltJetsTrim.end(), [](const TLorentzVector &p1, const TLorentzVector &p2) { return p1.M() > p2.M(); }); // the joys of C++11
		hlt1JetTrimMod = vecHltJetsTrim[0];
	}

	edm::Handle<reco::PFJetCollection> hltjetsPruned;
	iEvent.getByToken(hltJetsPruned,hltjetsPruned);
	TLorentzVector hlt1JetPruned;
	double hltHTPruned = 0;
	int nhltJetsPruned =0;
	for(const pat::Jet &ijet : *hltjetsPruned ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		hltHTPruned += ijet.pt();
		if ( (nhltJetsPruned++) == 1 ) hlt1JetPruned.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}
	
	edm::Handle<pat::JetCollection> patjets;
	iEvent.getByToken(patJets,patjets);
	TLorentzVector pat1Jet;
	TLorentzVector pat2Jet;
	double patHT = 0;
	int npatJets =0;
	int npatJets2 =0;
	//bool deltaEta = 0;
	//bool dijetMass;
	for(const pat::Jet &ijet : *patjets ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		patHT += ijet.pt();
		if ( (npatJets++) == 1 ) pat1Jet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
		if ( (npatJets2++) == 2 ) {
			pat2Jet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
			//deltaEta = abs( pat1Jet.Eta() - pat2Jet.Eta()  ) < 1.3;
			//TLorentzVector tmpVector = pat1Jet + pat2Jet;
			//dijetMass = tmpVector.M() > 890;
		}
	}
	//edm::LogWarning("test")<< patHT << " " << pat1Jet.Eta() << " " << pat2Jet.Eta() << " " << deltaEta << " " << dijetMass ;

	edm::Handle<pat::JetCollection> patjetsTrim;
	iEvent.getByToken(patJetsTrim,patjetsTrim);
	TLorentzVector pat1JetTrim;
	double patHTTrim = 0;
	int npatJetsTrim =0;
	for(const pat::Jet &ijet : *patjetsTrim ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		patHTTrim += ijet.pt();
		if ( (npatJetsTrim++) == 1 ) pat1JetTrim.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<pat::JetCollection> patjetsTrimMod;
	iEvent.getByToken(patJetsTrimMod,patjetsTrimMod);
	TLorentzVector pat1JetTrimMod;
	double patHTTrimMod = 0;
	int npatJetsTrimMod =0;
	for(const pat::Jet &ijet : *patjetsTrimMod ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		patHTTrimMod += ijet.pt();
		if ( (npatJetsTrimMod++) == 1 ) pat1JetTrimMod.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}
	
	edm::Handle<pat::JetCollection> patjetsPruned;
	iEvent.getByToken(patJetsPruned,patjetsPruned);
	TLorentzVector pat1JetPruned;
	double patHTPruned = 0;
	int npatJetsPruned =0;
	for(const pat::Jet &ijet : *patjetsPruned ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		patHTPruned += ijet.pt();
		if ( (npatJetsPruned++) == 1 ) pat1JetPruned.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<pat::JetCollection> jets;
	iEvent.getByToken(jetsForEff, jets);
	TLorentzVector jet1;
	double HT = 0;
	int nJets =0;
	for(const pat::Jet &ijet : *jets ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		HT += ijet.pt();
		if ( (nJets++) == 1 ) jet1.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	if( hltHT > 0 ) histos1D_[ "hltJetMass" ]->Fill( hlt1Jet.M() );
	if( hltHTTrim > 0 ) histos1D_[ "hltJetMassTrim" ]->Fill( hlt1JetTrim.M() );
	if( hltHTTrimMod > 0 ) histos1D_[ "hltJetMassTrimMod" ]->Fill( hlt1JetTrimMod.M() );
	if( hltHTPruned > 0 ) histos1D_[ "hltJetMassPruned" ]->Fill( hlt1JetPruned.M() );
	if( patHT > 0 ) histos1D_[ "patJetMass" ]->Fill( pat1Jet.M() );
	if( patHTTrim > 0 ) histos1D_[ "patJetMassTrim" ]->Fill( pat1JetTrim.M() );
	if( patHTTrimMod > 0 ) histos1D_[ "patJetMassTrimMod" ]->Fill( pat1JetTrimMod.M() );
	if( patHTPruned > 0 ) histos1D_[ "patJetMassPruned" ]->Fill( pat1JetPruned.M() );

	if (hltHTTrim > 0 ) {
		if( patHT > 0 ) histos2D_[ "hltVsPatJetMass" ]->Fill( hlt1JetTrimMod.M(), pat1Jet.M() );
		if( patHTTrim > 0 ) histos2D_[ "hltVsPatJetMassTrim" ]->Fill( hlt1JetTrimMod.M(), pat1JetTrim.M() );
		if( patHTTrimMod > 0 ) histos2D_[ "hltVsPatJetMassTrimMod" ]->Fill( hlt1JetTrimMod.M(), pat1JetTrimMod.M() );
		if( patHTPruned > 0 ) histos2D_[ "hltVsPatJetMassPruned" ]->Fill( hlt1JetTrimMod.M(), pat1JetPruned.M() );
	}

	if (triggerResults->accept(triggerBit)) {
		histos2D_[ "passedHltVsPatJetMass" ]->Fill( hlt1JetTrimMod.M(), pat1Jet.M() );
		histos2D_[ "passedHltVsPatJetMassTrim" ]->Fill( hlt1JetTrimMod.M(), pat1JetTrim.M() );
		histos2D_[ "passedHltVsPatJetMassTrimMod" ]->Fill( hlt1JetTrimMod.M(), pat1JetTrimMod.M() );
		histos2D_[ "passedHltVsPatJetMassPruned" ]->Fill( hlt1JetTrimMod.M(), pat1JetPruned.M() );
	}

	//if( deltaEta && ( patHT > minHT ) && ( pat1Jet.M() > minMass ) ) {
	if( ( patHT > minHT ) && ( pat1Jet.M() > minMass ) ) {

		if (triggerResults->accept(triggerBit)) {
			histos2D_[ "passedHltVsPatJetMass" ]->Fill( hlt1JetTrimMod.M(), pat1Jet.M() );
			histos2D_[ "passedHltVsPatJetMassTrim" ]->Fill( hlt1JetTrimMod.M(), pat1JetTrim.M() );
			histos2D_[ "passedHltVsPatJetMassTrimMod" ]->Fill( hlt1JetTrimMod.M(), pat1JetTrimMod.M() );
			histos2D_[ "passedHltVsPatJetMassPruned" ]->Fill( hlt1JetTrimMod.M(), pat1JetPruned.M() );
		}

		histos1D_[ "HTDenom" ]->Fill( patHT );
		histos1D_[ "jetMassDenom" ]->Fill( pat1Jet.M() );
		histos1D_[ "jetMassTrimDenom" ]->Fill( pat1JetTrim.M() );
		histos1D_[ "jetMassTrimModDenom" ]->Fill( pat1JetTrimMod.M() );
		histos1D_[ "jetMassPrunedDenom" ]->Fill( pat1JetPruned.M() );
		histos1D_[ "ptDenom" ]->Fill( pat1Jet.Pt() );
		histos2D_[ "jetMassHTDenom" ]->Fill(  pat1JetTrimMod.M(), patHT );
		histos2D_[ "jetMassPtDenom" ]->Fill( pat1JetTrimMod.M(), pat1Jet.Pt() );


		if (triggerResults->accept(triggerBit)){
			histos1D_[ "HTPassing" ]->Fill( patHT );
			histos1D_[ "jetMassPassing" ]->Fill( pat1Jet.M() );
			histos1D_[ "jetMassTrimPassing" ]->Fill( pat1JetTrim.M() );
			histos1D_[ "jetMassTrimModPassing" ]->Fill( pat1JetTrimMod.M() );
			histos1D_[ "jetMassPrunedPassing" ]->Fill( pat1JetPruned.M() );
			histos1D_[ "ptPassing" ]->Fill( pat1Jet.Pt() );
			histos2D_[ "jetMassHTPassing" ]->Fill( pat1JetTrimMod.M(), patHT );
			histos2D_[ "jetMassPtPassing" ]->Fill( pat1JetTrimMod.M(), pat1Jet.Pt() );

		}
	}

}


// ------------ method called once each job just before starting event loop  ------------
void TriggerEfficiencyPlots::beginJob() {

	edm::Service< TFileService > fileService;
	histos2D_[ "jetMassHTDenom" ] = fileService->make< TH2D >( "jetMassHTDenom", "HT vs Leading Jet Mass", 16, 0., 400. , 20, 0., 2000);
	histos2D_[ "jetMassHTDenom" ]->SetYTitle( "HT [GeV]" );
	histos2D_[ "jetMassHTDenom" ]->SetXTitle( "Leading Jet Trimmed Mass [GeV]" );

	histos2D_[ "jetMassHTPassing" ] = fileService->make< TH2D >( "jetMassHTPassing", "HT vs Leading Jet Mass passing path", 16, 0., 400. , 20, 0., 2000);
	histos2D_[ "jetMassHTPassing" ]->SetYTitle( "HT [GeV]" );
	histos2D_[ "jetMassHTPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassHT2Defficiency" ] = fileService->make< TH2D >( "jetMassHT2Defficiency", "Comparative efficiency", 16, 0., 400. , 20, 0., 2000);
	histos2D_[ "jetMassHT2Defficiency" ]->SetYTitle( "HT [GeV]" );
	histos2D_[ "jetMassHT2Defficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassPtDenom" ] = fileService->make< TH2D >( "jetMassPtDenom", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
	histos2D_[ "jetMassPtDenom" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "jetMassPtDenom" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassPtPassing" ] = fileService->make< TH2D >( "jetMassPtPassing", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
	histos2D_[ "jetMassPtPassing" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "jetMassPtPassing" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassPt2Defficiency" ] = fileService->make< TH2D >( "jetMassPt2Defficiency", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
	histos2D_[ "jetMassPt2Defficiency" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "jetMassPt2Defficiency" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos1D_[ "jetMassDenom" ] = fileService->make< TH1D >( "jetMassDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "jetMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassDenom" ]->Sumw2();

	histos1D_[ "jetMassPassing" ] = fileService->make< TH1D >( "jetMassPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "jetMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassPassing" ]->Sumw2();

	histos1D_[ "jetMassEfficiency" ] = fileService->make< TH1D >( "jetMassEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "jetMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "jetMassTrimDenom" ] = fileService->make< TH1D >( "jetMassTrimDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "jetMassTrimDenom" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "jetMassTrimDenom" ]->Sumw2();

	histos1D_[ "jetMassTrimPassing" ] = fileService->make< TH1D >( "jetMassTrimPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "jetMassTrimPassing" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "jetMassTrimPassing" ]->Sumw2();

	histos1D_[ "jetMassTrimEfficiency" ] = fileService->make< TH1D >( "jetMassTrimEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "jetMassTrimEfficiency" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "jetMassTrimEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "jetMassTrimModDenom" ] = fileService->make< TH1D >( "jetMassTrimModDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "jetMassTrimModDenom" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "jetMassTrimModDenom" ]->Sumw2();

	histos1D_[ "jetMassTrimModPassing" ] = fileService->make< TH1D >( "jetMassTrimModPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "jetMassTrimModPassing" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "jetMassTrimModPassing" ]->Sumw2();

	histos1D_[ "jetMassTrimModEfficiency" ] = fileService->make< TH1D >( "jetMassTrimModEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "jetMassTrimModEfficiency" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "jetMassTrimModEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "jetMassPrunedDenom" ] = fileService->make< TH1D >( "jetMassPrunedDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "jetMassPrunedDenom" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "jetMassPrunedDenom" ]->Sumw2();

	histos1D_[ "jetMassPrunedPassing" ] = fileService->make< TH1D >( "jetMassPrunedPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "jetMassPrunedPassing" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "jetMassPrunedPassing" ]->Sumw2();

	histos1D_[ "jetMassPrunedEfficiency" ] = fileService->make< TH1D >( "jetMassPrunedEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "jetMassPrunedEfficiency" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "jetMassPrunedEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "HTDenom" ] = fileService->make< TH1D >( "HTDenom", "HT", 100, 0., 2000);
	histos1D_[ "HTDenom" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "HTDenom" ]->Sumw2();

	histos1D_[ "HTPassing" ] = fileService->make< TH1D >( "HTPassing", "HT passing", 100, 0., 2000);
	histos1D_[ "HTPassing" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "HTPassing" ]->Sumw2();

	histos1D_[ "HTEfficiency" ] = fileService->make< TH1D >( "HTEfficiency", "HT efficiency", 100, 0., 2000);
	histos1D_[ "HTEfficiency" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "HTEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "ptDenom" ] = fileService->make< TH1D >( "ptDenom", "pt", 100, 0., 1000);
	histos1D_[ "ptDenom" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "ptDenom" ]->Sumw2();

	histos1D_[ "ptPassing" ] = fileService->make< TH1D >( "ptPassing", "pt passing", 100, 0., 1000);
	histos1D_[ "ptPassing" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "ptPassing" ]->Sumw2();

	histos1D_[ "ptEfficiency" ] = fileService->make< TH1D >( "ptEfficiency", "pt efficiency", 100, 0., 1000);
	histos1D_[ "ptEfficiency" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "ptEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "numPV" ] = fileService->make< TH1D >( "numPV", "Number of Primary Vertex", 100, 0., 100);
	histos1D_[ "numPV" ]->Sumw2();

	histos1D_[ "hltJetMass" ] = fileService->make< TH1D >( "hltJetMass", "Jet mass ", 40, 0., 400);
	histos1D_[ "hltJetMass" ]->Sumw2();
	histos1D_[ "hltJetMassTrim" ] = fileService->make< TH1D >( "hltJetMassTrim", "Jet mass ", 40, 0., 400);
	histos1D_[ "hltJetMassTrim" ]->Sumw2();
	histos1D_[ "hltJetMassTrimMod" ] = fileService->make< TH1D >( "hltJetMassTrimMod", "Jet mass ", 40, 0., 400);
	histos1D_[ "hltJetMassTrimMod" ]->Sumw2();
	histos1D_[ "hltJetMassPruned" ] = fileService->make< TH1D >( "hltJetMassPruned", "Jet mass ", 40, 0., 400);
	histos1D_[ "hltJetMassPruned" ]->Sumw2();

	histos1D_[ "patJetMass" ] = fileService->make< TH1D >( "patJetMass", "Jet mass ", 40, 0., 400);
	histos1D_[ "patJetMass" ]->Sumw2();
	histos1D_[ "patJetMassTrim" ] = fileService->make< TH1D >( "patJetMassTrim", "Jet mass ", 40, 0., 400);
	histos1D_[ "patJetMassTrim" ]->Sumw2();
	histos1D_[ "patJetMassTrimMod" ] = fileService->make< TH1D >( "patJetMassTrimMod", "Jet mass ", 40, 0., 400);
	histos1D_[ "patJetMassTrimMod" ]->Sumw2();
	histos1D_[ "patJetMassPruned" ] = fileService->make< TH1D >( "patJetMassPruned", "Jet mass ", 40, 0., 400);
	histos1D_[ "patJetMassPruned" ]->Sumw2();

	histos2D_[ "hltVsPatJetMass" ] = fileService->make< TH2D >( "hltVsPatJetMass", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "hltVsPatJetMass" ]->SetYTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "hltVsPatJetMass" ]->SetXTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "hltVsPatJetMassTrim" ] = fileService->make< TH2D >( "hltVsPatJetMassTrim", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "hltVsPatJetMassTrim" ]->SetYTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "hltVsPatJetMassTrim" ]->SetXTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "hltVsPatJetMassTrimMod" ] = fileService->make< TH2D >( "hltVsPatJetMassTrimMod", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "hltVsPatJetMassTrimMod" ]->SetYTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "hltVsPatJetMassTrimMod" ]->SetXTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "hltVsPatJetMassPruned" ] = fileService->make< TH2D >( "hltVsPatJetMassPruned", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "hltVsPatJetMassPruned" ]->SetYTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "hltVsPatJetMassPruned" ]->SetXTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "passedHltVsPatJetMass" ] = fileService->make< TH2D >( "passedHltVsPatJetMass", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "passedHltVsPatJetMass" ]->SetYTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "passedHltVsPatJetMass" ]->SetXTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "passedHltVsPatJetMassTrim" ] = fileService->make< TH2D >( "passedHltVsPatJetMassTrim", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "passedHltVsPatJetMassTrim" ]->SetYTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "passedHltVsPatJetMassTrim" ]->SetXTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "passedHltVsPatJetMassTrimMod" ] = fileService->make< TH2D >( "passedHltVsPatJetMassTrimMod", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "passedHltVsPatJetMassTrimMod" ]->SetYTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "passedHltVsPatJetMassTrimMod" ]->SetXTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "passedHltVsPatJetMassPruned" ] = fileService->make< TH2D >( "passedHltVsPatJetMassPruned", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "passedHltVsPatJetMassPruned" ]->SetYTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "passedHltVsPatJetMassPruned" ]->SetXTitle( "Online Leading Jet Mass [GeV]" );
}

// ------------ method called once each job just after ending the event loop  ------------
void TriggerEfficiencyPlots::endJob() {

    histos2D_[ "jetMassHT2Defficiency" ]->Sumw2();
    histos2D_[ "jetMassHT2Defficiency" ]->Divide(histos2D_[ "jetMassHTPassing" ],histos2D_[ "jetMassHTDenom" ],1,1,"B");
    
    histos2D_[ "jetMassPt2Defficiency" ]->Sumw2();
    histos2D_[ "jetMassPt2Defficiency" ]->Divide(histos2D_[ "jetMassPtPassing" ],histos2D_[ "jetMassPtDenom" ],1,1,"B");
    
    
    histos1D_[ "jetMassEfficiency" ]->Sumw2();
    histos1D_[ "jetMassEfficiency" ]->Divide(histos1D_[ "jetMassPassing" ], histos1D_[ "jetMassDenom" ], 1,1,"B");

    histos1D_[ "jetMassTrimEfficiency" ]->Sumw2();
    histos1D_[ "jetMassTrimEfficiency" ]->Divide(histos1D_[ "jetMassTrimPassing" ], histos1D_[ "jetMassTrimDenom" ], 1,1,"B");

    histos1D_[ "jetMassTrimModEfficiency" ]->Sumw2();
    histos1D_[ "jetMassTrimModEfficiency" ]->Divide(histos1D_[ "jetMassTrimModPassing" ], histos1D_[ "jetMassTrimModDenom" ], 1,1,"B");

    histos1D_[ "jetMassPrunedEfficiency" ]->Sumw2();
    histos1D_[ "jetMassPrunedEfficiency" ]->Divide(histos1D_[ "jetMassPrunedPassing" ], histos1D_[ "jetMassPrunedDenom" ], 1,1,"B");

    histos1D_[ "HTEfficiency" ]->Sumw2();
    histos1D_[ "HTEfficiency" ]->Divide(histos1D_[ "HTPassing" ], histos1D_[ "HTDenom" ], 1,1,"B");

    histos1D_[ "ptEfficiency" ]->Sumw2();
    histos1D_[ "ptEfficiency" ]->Divide(histos1D_[ "ptPassing" ], histos1D_[ "ptDenom" ], 1,1,"B");


}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void TriggerEfficiencyPlots::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	desc.add<edm::InputTag>("hltJets",edm::InputTag("hltAK8PFJetsCorrected"));
	desc.add<edm::InputTag>("hltJetsTrim",edm::InputTag("hltAK8PFJetsTrim"));
	desc.add<edm::InputTag>("hltJetsTrimMod",edm::InputTag("hltAK8PFJetsTrimR0p1PT0p03"));
	desc.add<double>("MinHT", 0.0);
	desc.add<double>("MinPt", 40.0);
	desc.add<double>("MinMass", 0.0);
	descriptions.add("TriggerEfficiencyPlots",desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerEfficiencyPlots);
