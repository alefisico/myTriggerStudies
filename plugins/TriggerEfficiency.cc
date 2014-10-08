// -*- C++ -*-
//
// Package:    MyTrigger/myTriggerStudies
// Class:      TriggerEfficiency.cc
// 
/**\class TriggerEfficiency.cc TriggerEfficiency.cc.cc MyTrigger/myTriggerStudies/plugins/TriggerEfficiency.cc.cc

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

#include "TMath.h"
#include "TH2D.h"
#include "TH1D.h"
#include <TLorentzVector.h>

//
// class declaration
//

class TriggerEfficiency : public edm::EDAnalyzer {
	public:
		explicit TriggerEfficiency(const edm::ParameterSet&);
		~TriggerEfficiency();

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

		edm::InputTag jetsForEff;
		edm::InputTag hltJets;
		edm::InputTag hltJetsTrim;
		edm::InputTag hltJetsTrimMod;
		edm::InputTag hltJetsPruned;
		edm::InputTag patJets;
		edm::InputTag patJetsTrim;
		edm::InputTag patJetsTrimMod;
		edm::InputTag patJetsPruned;
		std::string triggerPath;
		double minHT;
		double minMass;

		HLTConfigProvider hltConfig;
		int triggerBit;
};



TriggerEfficiency::TriggerEfficiency(const edm::ParameterSet& iConfig){
	hltJets			= iConfig.getParameter<edm::InputTag> ( "hltJets" );   			// Obtain inputs
	hltJetsTrim		= iConfig.getParameter<edm::InputTag> ( "hltJetsTrim" );   			// Obtain inputs
	hltJetsTrimMod		= iConfig.getParameter<edm::InputTag> ( "hltJetsTrimMod" );   			// Obtain inputs
	hltJetsPruned		= iConfig.getParameter<edm::InputTag> ( "hltJetsPruned" );   			// Obtain inputs
	patJets			= iConfig.getParameter<edm::InputTag> ( "patJets" );   			// Obtain inputs
	patJetsTrim		= iConfig.getParameter<edm::InputTag> ( "patJetsTrim" );   			// Obtain inputs
	patJetsTrimMod		= iConfig.getParameter<edm::InputTag> ( "patJetsTrimMod" );   			// Obtain inputs
	patJetsPruned		= iConfig.getParameter<edm::InputTag> ( "patJetsPruned" );   			// Obtain inputs
	jetsForEff		= iConfig.getParameter<edm::InputTag> ( "jetsForEff" );   			// Obtain inputs
	triggerPath		= iConfig.getParameter<std::string> ( "triggerPath" );   			// Obtain inputs
	minHT			= iConfig.getParameter<double> ( "minHT" );   			// Obtain inputs
	minMass			= iConfig.getParameter<double> ( "minMass" );   			// Obtain inputs
}


TriggerEfficiency::~TriggerEfficiency()
{
}


//
// member functions
//

// ------------ method called for each event  ------------
void TriggerEfficiency::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {

	using namespace edm;
	using namespace std;

	/* Generator info, maybe I will need it later
	 * edm::Handle<GenEventInfoProduct> genEvent;
	iEvent.getByLabel("generator", genEvent);

	edm::Handle<reco::GenParticleCollection> genParticles;
	iEvent.getByLabel( "prunedGenParticles", genParticles );*/

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


	/*edm::InputTag triggerSummaryLabel_ = edm::InputTag("hltTriggerSummaryAOD", "", "HLT");
	edm::Handle<trigger::TriggerEvent> triggerSummary;
	iEvent.getByLabel(triggerSummaryLabel_, triggerSummary);*/

	edm::Handle<edm::View<reco::PFJet> > hltjets;
	iEvent.getByLabel(hltJets,hltjets);
	TLorentzVector hlt1Jet;
	double hltHT = 0;
	int nhltJets =0;
	for(const pat::Jet &ijet : *hltjets ){
		if ( ijet.pt() < 40.0 || abs( ijet.eta() ) > 3.0 ) continue;
		hltHT += ijet.pt();
		if ( (nhltJets++) == 1 ) hlt1Jet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}
	//edm::LogWarning("test")<< hlt1Jet.M() << " " << hlt1Jet.Pt() << " " << hltHT ;

	edm::Handle<edm::View<reco::PFJet> > hltjetsTrim;
	iEvent.getByLabel(hltJetsTrim,hltjetsTrim);
	TLorentzVector hlt1JetTrim;
	double hltHTTrim = 0;
	int nhltJetsTrim =0;
	for(const pat::Jet &ijet : *hltjetsTrim ){
		if ( ijet.pt() < 40.0 || abs( ijet.eta() ) > 3.0 ) continue;
		hltHTTrim += ijet.pt();
		if ( (nhltJetsTrim++) == 1 ) hlt1JetTrim.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<edm::View<reco::PFJet> > hltjetsTrimMod;
	iEvent.getByLabel(hltJetsTrimMod,hltjetsTrimMod);
	TLorentzVector hlt1JetTrimMod;
	double hltHTTrimMod = 0;
	int nhltJetsTrimMod =0;
	for(const pat::Jet &ijet : *hltjetsTrimMod ){
		if ( ijet.pt() < 40.0 || abs( ijet.eta() ) > 3.0 ) continue;
		hltHTTrimMod += ijet.pt();
		if ( (nhltJetsTrimMod++) == 1 ) hlt1JetTrimMod.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<edm::View<reco::PFJet> > hltjetsPruned;
	iEvent.getByLabel(hltJetsPruned,hltjetsPruned);
	TLorentzVector hlt1JetPruned;
	double hltHTPruned = 0;
	int nhltJetsPruned =0;
	for(const pat::Jet &ijet : *hltjetsPruned ){
		if ( ijet.pt() < 40.0 || abs( ijet.eta() ) > 3.0 ) continue;
		hltHTPruned += ijet.pt();
		if ( (nhltJetsPruned++) == 1 ) hlt1JetPruned.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}
	
	edm::Handle<edm::View<pat::Jet> > patjets;
	iEvent.getByLabel(patJets,patjets);
	TLorentzVector pat1Jet;
	double patHT = 0;
	int npatJets =0;
	for(const pat::Jet &ijet : *patjets ){
		if ( ijet.pt() < 40.0 || abs( ijet.eta() ) > 3.0 ) continue;
		patHT += ijet.pt();
		if ( (npatJets++) == 1 ) pat1Jet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<edm::View<pat::Jet> > patjetsTrim;
	iEvent.getByLabel(patJetsTrim,patjetsTrim);
	TLorentzVector pat1JetTrim;
	double patHTTrim = 0;
	int npatJetsTrim =0;
	for(const pat::Jet &ijet : *patjetsTrim ){
		if ( ijet.pt() < 40.0 || abs( ijet.eta() ) > 3.0 ) continue;
		patHTTrim += ijet.pt();
		if ( (npatJetsTrim++) == 1 ) pat1JetTrim.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<edm::View<pat::Jet> > patjetsTrimMod;
	iEvent.getByLabel(patJetsTrimMod,patjetsTrimMod);
	TLorentzVector pat1JetTrimMod;
	double patHTTrimMod = 0;
	int npatJetsTrimMod =0;
	for(const pat::Jet &ijet : *patjetsTrimMod ){
		if ( ijet.pt() < 40.0 || abs( ijet.eta() ) > 3.0 ) continue;
		patHTTrimMod += ijet.pt();
		if ( (npatJetsTrimMod++) == 1 ) pat1JetTrimMod.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}
	
	edm::Handle<edm::View<pat::Jet> > patjetsPruned;
	iEvent.getByLabel(patJetsPruned,patjetsPruned);
	TLorentzVector pat1JetPruned;
	double patHTPruned = 0;
	int npatJetsPruned =0;
	for(const pat::Jet &ijet : *patjetsPruned ){
		if ( ijet.pt() < 40.0 || abs( ijet.eta() ) > 3.0 ) continue;
		patHTPruned += ijet.pt();
		if ( (npatJetsPruned++) == 1 ) pat1JetPruned.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<edm::View<pat::Jet> > jets;
	iEvent.getByLabel(jetsForEff, jets);
	TLorentzVector jet1;
	double HT = 0;
	int nJets =0;
	for(const pat::Jet &ijet : *jets ){
		if ( ijet.pt() < 40.0 || abs( ijet.eta() ) > 3.0 ) continue;
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

	if( patHT > 0 && hltHT > 0 ) histos2D_[ "hltVsPatJetMass" ]->Fill( hlt1Jet.M(), pat1Jet.M() );
	if( patHTTrim > 0 && hltHTTrim > 0 ) histos2D_[ "hltVsPatJetMassTrim" ]->Fill( hlt1JetTrim.M(), pat1JetTrim.M() );
	if( patHTTrimMod > 0 && hltHTTrimMod > 0 ) histos2D_[ "hltVsPatJetMassTrimMod" ]->Fill( hlt1JetTrimMod.M(), pat1JetTrimMod.M() );
	if( patHTPruned > 0 && hltHTPruned > 0 ) histos2D_[ "hltVsPatJetMassPruned" ]->Fill( hlt1JetPruned.M(), pat1JetPruned.M() );

	if( HT > minHT && jet1.M() > minMass  ) {
		histos1D_[ "HTDenom" ]->Fill( HT );
		histos1D_[ "jetMassDenom" ]->Fill( jet1.M() );
		histos2D_[ "jetMassHTDenom" ]->Fill( HT, jet1.M() );
		histos2D_[ "jetMassPtDenom" ]->Fill( jet1.Pt(), jet1.M() );

		if (triggerResults->accept(triggerBit)){
			histos1D_[ "HTPassing" ]->Fill( HT );
			histos1D_[ "jetMassPassing" ]->Fill( jet1.M() );
			histos2D_[ "jetMassHTPassing" ]->Fill( HT, jet1.M() );
			histos2D_[ "jetMassPtPassing" ]->Fill( jet1.Pt(), jet1.M() );
		}
	}

}


// ------------ method called once each job just before starting event loop  ------------
void TriggerEfficiency::beginJob() {

	edm::Service< TFileService > fileService;
	histos2D_[ "jetMassHTDenom" ] = fileService->make< TH2D >( "jetMassHTDenom", "HT vs Leading Jet Mass", 20, 0., 2000, 16, 0., 400. );
	histos2D_[ "jetMassHTDenom" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "jetMassHTDenom" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassHTPassing" ] = fileService->make< TH2D >( "jetMassHTPassing", "HT vs Leading Jet Mass passing path", 20, 0., 2000, 16, 0., 400. );
	histos2D_[ "jetMassHTPassing" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "jetMassHTPassing" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassHT2Defficiency" ] = fileService->make< TH2D >( "jetMassHT2Defficiency", "Comparative efficiency", 20, 0., 2000, 16, 0., 400. );
	histos2D_[ "jetMassHT2Defficiency" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "jetMassHT2Defficiency" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassPtDenom" ] = fileService->make< TH2D >( "jetMassPtDenom", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
	histos2D_[ "jetMassPtDenom" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "jetMassPtDenom" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassPtPassing" ] = fileService->make< TH2D >( "jetMassPtPassing", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
	histos2D_[ "jetMassPtPassing" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "jetMassPtPassing" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassPt2Defficiency" ] = fileService->make< TH2D >( "jetMassPt2Defficiency", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
	histos2D_[ "jetMassPt2Defficiency" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "jetMassPt2Defficiency" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos1D_[ "jetMassDenom" ] = fileService->make< TH1D >( "jetMassDenom", "Jet mass", 40, 0., 400);
	histos1D_[ "jetMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassDenom" ]->Sumw2();

	histos1D_[ "jetMassPassing" ] = fileService->make< TH1D >( "jetMassPassing", "Jet mass passing", 40, 0., 400);
	histos1D_[ "jetMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassPassing" ]->Sumw2();

	histos1D_[ "jetMassEfficiency" ] = fileService->make< TH1D >( "jetMassEfficiency", "Leading jet mass efficiency", 40, 0., 400);
	histos1D_[ "jetMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "jetMassTrimDenom" ] = fileService->make< TH1D >( "jetMassTrimDenom", "Jet mass", 40, 0., 400);
	histos1D_[ "jetMassTrimDenom" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "jetMassTrimDenom" ]->Sumw2();

	histos1D_[ "jetMassTrimPassing" ] = fileService->make< TH1D >( "jetMassTrimPassing", "Jet mass passing", 40, 0., 400);
	histos1D_[ "jetMassTrimPassing" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "jetMassTrimPassing" ]->Sumw2();

	histos1D_[ "jetMassTrimEfficiency" ] = fileService->make< TH1D >( "jetMassTrimEfficiency", "Leading jet mass efficiency", 40, 0., 400);
	histos1D_[ "jetMassTrimEfficiency" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "jetMassTrimEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "jetMassTrimModDenom" ] = fileService->make< TH1D >( "jetMassTrimModDenom", "Jet mass", 40, 0., 400);
	histos1D_[ "jetMassTrimModDenom" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "jetMassTrimModDenom" ]->Sumw2();

	histos1D_[ "jetMassTrimModPassing" ] = fileService->make< TH1D >( "jetMassTrimModPassing", "Jet mass passing", 40, 0., 400);
	histos1D_[ "jetMassTrimModPassing" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "jetMassTrimModPassing" ]->Sumw2();

	histos1D_[ "jetMassTrimModEfficiency" ] = fileService->make< TH1D >( "jetMassTrimModEfficiency", "Leading jet mass efficiency", 40, 0., 400);
	histos1D_[ "jetMassTrimModEfficiency" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "jetMassTrimModEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "HTDenom" ] = fileService->make< TH1D >( "HTDenom", "HT", 200, 0., 2000);
	histos1D_[ "HTDenom" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "HTDenom" ]->Sumw2();

	histos1D_[ "HTPassing" ] = fileService->make< TH1D >( "HTPassing", "HT passing", 200, 0., 2000);
	histos1D_[ "HTPassing" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "HTPassing" ]->Sumw2();

	histos1D_[ "HTEfficiency" ] = fileService->make< TH1D >( "HTEfficiency", "HT efficiency", 200, 0., 2000);
	histos1D_[ "HTEfficiency" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "HTEfficiency" ]->SetYTitle( "Efficiency" );

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
	histos2D_[ "hltVsPatJetMass" ]->SetXTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "hltVsPatJetMass" ]->SetYTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "hltVsPatJetMassTrim" ] = fileService->make< TH2D >( "hltVsPatJetMassTrim", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "hltVsPatJetMassTrim" ]->SetXTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "hltVsPatJetMassTrim" ]->SetYTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "hltVsPatJetMassTrimMod" ] = fileService->make< TH2D >( "hltVsPatJetMassTrimMod", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "hltVsPatJetMassTrimMod" ]->SetXTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "hltVsPatJetMassTrimMod" ]->SetYTitle( "Online Leading Jet Mass [GeV]" );

	histos2D_[ "hltVsPatJetMassPruned" ] = fileService->make< TH2D >( "hltVsPatJetMassPruned", "Online vs Offline Leading Jet Mass", 40, 0., 400, 40, 0., 400. );
	histos2D_[ "hltVsPatJetMassPruned" ]->SetXTitle( "Offline Leading Jet Mass [GeV]" );
	histos2D_[ "hltVsPatJetMassPruned" ]->SetYTitle( "Online Leading Jet Mass [GeV]" );

}

// ------------ method called once each job just after ending the event loop  ------------
void TriggerEfficiency::endJob() {

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

    histos1D_[ "HTEfficiency" ]->Sumw2();
    histos1D_[ "HTEfficiency" ]->Divide(histos1D_[ "HTPassing" ], histos1D_[ "HTDenom" ], 1,1,"B");

}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void TriggerEfficiency::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerEfficiency);
