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

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

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
		edm::InputTag hltPV;
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
	hltPV			= iConfig.getParameter<edm::InputTag> ( "primaryVertex" );   			// Obtain inputs
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

	edm::Handle<reco::VertexCollection> vertices;
	iEvent.getByLabel(hltPV, vertices);
	//edm::LogWarning("test")<< vertices->size();
	int NPV = vertices->size();
	bool lowNPV = 0;
	bool midNPV = 0;
	bool highNPV = 0;
	histos1D_[ "numPV" ]->Fill( vertices->size() );
	if( NPV < 25 ) lowNPV = 1;
	if( NPV > 25 && NPV < 35 ) midNPV = 1;
	if( NPV > 35 ) highNPV = 1;

	/*edm::InputTag triggerSummaryLabel_ = edm::InputTag("hltTriggerSummaryAOD", "", "HLT");
	edm::Handle<trigger::TriggerEvent> triggerSummary;
	iEvent.getByLabel(triggerSummaryLabel_, triggerSummary);*/

	edm::Handle<edm::View<reco::PFJet> > hltjets;
	iEvent.getByLabel(hltJets,hltjets);
	TLorentzVector hlt1Jet;
	double hltHT = 0;
	int nhltJets =0;
	for(const pat::Jet &ijet : *hltjets ){
		if ( ijet.pt() < 30.0 || abs( ijet.eta() ) > 2.4 ) continue;
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
		if ( ijet.pt() < 30.0 || abs( ijet.eta() ) > 2.4 ) continue;
		hltHTTrim += ijet.pt();
		if ( (nhltJetsTrim++) == 1 ) hlt1JetTrim.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<edm::View<reco::PFJet> > hltjetsTrimMod;
	iEvent.getByLabel(hltJetsTrimMod,hltjetsTrimMod);
	TLorentzVector hlt1JetTrimMod;
	double hltHTTrimMod = 0;
	int nhltJetsTrimMod =0;
	for(const pat::Jet &ijet : *hltjetsTrimMod ){
		if ( ijet.pt() < 30.0 || abs( ijet.eta() ) > 2.4 ) continue;
		hltHTTrimMod += ijet.pt();
		if ( (nhltJetsTrimMod++) == 1 ) hlt1JetTrimMod.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<edm::View<reco::PFJet> > hltjetsPruned;
	iEvent.getByLabel(hltJetsPruned,hltjetsPruned);
	TLorentzVector hlt1JetPruned;
	double hltHTPruned = 0;
	int nhltJetsPruned =0;
	for(const pat::Jet &ijet : *hltjetsPruned ){
		if ( ijet.pt() < 30.0 || abs( ijet.eta() ) > 2.4 ) continue;
		hltHTPruned += ijet.pt();
		if ( (nhltJetsPruned++) == 1 ) hlt1JetPruned.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}
	
	edm::Handle<edm::View<pat::Jet> > patjets;
	iEvent.getByLabel(patJets,patjets);
	TLorentzVector pat1Jet;
	TLorentzVector pat2Jet;
	double patHT = 0;
	int npatJets =0;
	int npatJets2 =0;
	bool deltaEta = 0;
	//bool dijetMass;
	for(const pat::Jet &ijet : *patjets ){
		if ( ijet.pt() < 30.0 || abs( ijet.eta() ) > 2.4 ) continue;
		patHT += ijet.pt();
		if ( (npatJets++) == 1 ) pat1Jet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
		if ( (npatJets2++) == 2 ) {
			pat2Jet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
			deltaEta = abs( pat1Jet.Eta() - pat2Jet.Eta()  ) < 1.3;
			//TLorentzVector tmpVector = pat1Jet + pat2Jet;
			//dijetMass = tmpVector.M() > 890;
		}
	}
	//edm::LogWarning("test")<< patHT << " " << pat1Jet.Eta() << " " << pat2Jet.Eta() << " " << deltaEta << " " << dijetMass ;

	edm::Handle<edm::View<pat::Jet> > patjetsTrim;
	iEvent.getByLabel(patJetsTrim,patjetsTrim);
	TLorentzVector pat1JetTrim;
	double patHTTrim = 0;
	int npatJetsTrim =0;
	for(const pat::Jet &ijet : *patjetsTrim ){
		if ( ijet.pt() < 30.0 || abs( ijet.eta() ) > 2.4 ) continue;
		patHTTrim += ijet.pt();
		if ( (npatJetsTrim++) == 1 ) pat1JetTrim.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<edm::View<pat::Jet> > patjetsTrimMod;
	iEvent.getByLabel(patJetsTrimMod,patjetsTrimMod);
	TLorentzVector pat1JetTrimMod;
	double patHTTrimMod = 0;
	int npatJetsTrimMod =0;
	for(const pat::Jet &ijet : *patjetsTrimMod ){
		if ( ijet.pt() < 30.0 || abs( ijet.eta() ) > 2.4 ) continue;
		patHTTrimMod += ijet.pt();
		if ( (npatJetsTrimMod++) == 1 ) pat1JetTrimMod.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}
	
	edm::Handle<edm::View<pat::Jet> > patjetsPruned;
	iEvent.getByLabel(patJetsPruned,patjetsPruned);
	TLorentzVector pat1JetPruned;
	double patHTPruned = 0;
	int npatJetsPruned =0;
	for(const pat::Jet &ijet : *patjetsPruned ){
		if ( ijet.pt() < 30.0 || abs( ijet.eta() ) > 2.4 ) continue;
		patHTPruned += ijet.pt();
		if ( (npatJetsPruned++) == 1 ) pat1JetPruned.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	edm::Handle<edm::View<pat::Jet> > jets;
	iEvent.getByLabel(jetsForEff, jets);
	TLorentzVector jet1;
	double HT = 0;
	int nJets =0;
	for(const pat::Jet &ijet : *jets ){
		if ( ijet.pt() < 30.0 || abs( ijet.eta() ) > 2.4 ) continue;
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

	if( deltaEta && ( patHT > minHT ) && ( pat1Jet.M() > minMass ) ) {
		histos1D_[ "HTDenom" ]->Fill( patHT );
		histos1D_[ "jetMassDenom" ]->Fill( pat1Jet.M() );
		histos1D_[ "jetMassTrimDenom" ]->Fill( pat1JetTrim.M() );
		histos1D_[ "jetMassTrimModDenom" ]->Fill( pat1JetTrimMod.M() );
		histos1D_[ "jetMassPrunedDenom" ]->Fill( pat1JetPruned.M() );
		histos1D_[ "ptDenom" ]->Fill( pat1Jet.Pt() );
		histos2D_[ "jetMassHTDenom" ]->Fill( patHT, pat1Jet.M() );
		histos2D_[ "jetMassPtDenom" ]->Fill( pat1Jet.Pt(), pat1Jet.M() );

		if ( lowNPV ){
			histos1D_[ "lowPUHTDenom" ]->Fill( patHT );
			histos1D_[ "lowPUjetMassDenom" ]->Fill( pat1Jet.M() );
			histos1D_[ "lowPUjetMassTrimDenom" ]->Fill( pat1JetTrim.M() );
			histos1D_[ "lowPUjetMassTrimModDenom" ]->Fill( pat1JetTrimMod.M() );
			histos1D_[ "lowPUjetMassPrunedDenom" ]->Fill( pat1JetPruned.M() );
			histos1D_[ "lowPUptDenom" ]->Fill( pat1Jet.Pt() );
		}
		if ( midNPV ){
			histos1D_[ "midPUHTDenom" ]->Fill( patHT );
			histos1D_[ "midPUjetMassDenom" ]->Fill( pat1Jet.M() );
			histos1D_[ "midPUjetMassTrimDenom" ]->Fill( pat1JetTrim.M() );
			histos1D_[ "midPUjetMassTrimModDenom" ]->Fill( pat1JetTrimMod.M() );
			histos1D_[ "midPUjetMassPrunedDenom" ]->Fill( pat1JetPruned.M() );
			histos1D_[ "midPUptDenom" ]->Fill( pat1Jet.Pt() );
		}
		if ( highNPV ){
			histos1D_[ "highPUHTDenom" ]->Fill( patHT );
			histos1D_[ "highPUjetMassDenom" ]->Fill( pat1Jet.M() );
			histos1D_[ "highPUjetMassTrimDenom" ]->Fill( pat1JetTrim.M() );
			histos1D_[ "highPUjetMassTrimModDenom" ]->Fill( pat1JetTrimMod.M() );
			histos1D_[ "highPUjetMassPrunedDenom" ]->Fill( pat1JetPruned.M() );
			histos1D_[ "highPUptDenom" ]->Fill( pat1Jet.Pt() );
		}

		if (triggerResults->accept(triggerBit)){
			histos1D_[ "HTPassing" ]->Fill( patHT );
			histos1D_[ "jetMassPassing" ]->Fill( pat1Jet.M() );
			histos1D_[ "jetMassTrimPassing" ]->Fill( pat1JetTrim.M() );
			histos1D_[ "jetMassTrimModPassing" ]->Fill( pat1JetTrimMod.M() );
			histos1D_[ "jetMassPrunedPassing" ]->Fill( pat1JetPruned.M() );
			histos1D_[ "ptPassing" ]->Fill( pat1Jet.Pt() );
			histos2D_[ "jetMassHTPassing" ]->Fill( patHT, pat1Jet.M() );
			histos2D_[ "jetMassPtPassing" ]->Fill( pat1Jet.Pt(), pat1Jet.M() );

			if ( lowNPV ){
				histos1D_[ "lowPUHTPassing" ]->Fill( patHT );
				histos1D_[ "lowPUjetMassPassing" ]->Fill( pat1Jet.M() );
				histos1D_[ "lowPUjetMassTrimPassing" ]->Fill( pat1JetTrim.M() );
				histos1D_[ "lowPUjetMassTrimModPassing" ]->Fill( pat1JetTrimMod.M() );
				histos1D_[ "lowPUjetMassPrunedPassing" ]->Fill( pat1JetPruned.M() );
				histos1D_[ "lowPUptPassing" ]->Fill( pat1Jet.Pt() );
			}
			if ( midNPV ){
				histos1D_[ "midPUHTPassing" ]->Fill( patHT );
				histos1D_[ "midPUjetMassPassing" ]->Fill( pat1Jet.M() );
				histos1D_[ "midPUjetMassTrimPassing" ]->Fill( pat1JetTrim.M() );
				histos1D_[ "midPUjetMassTrimModPassing" ]->Fill( pat1JetTrimMod.M() );
				histos1D_[ "midPUjetMassPrunedPassing" ]->Fill( pat1JetPruned.M() );
				histos1D_[ "midPUptPassing" ]->Fill( pat1Jet.Pt() );
			}
			if ( highNPV ){
				histos1D_[ "highPUHTPassing" ]->Fill( patHT );
				histos1D_[ "highPUjetMassPassing" ]->Fill( pat1Jet.M() );
				histos1D_[ "highPUjetMassTrimPassing" ]->Fill( pat1JetTrim.M() );
				histos1D_[ "highPUjetMassTrimModPassing" ]->Fill( pat1JetTrimMod.M() );
				histos1D_[ "highPUjetMassPrunedPassing" ]->Fill( pat1JetPruned.M() );
				histos1D_[ "highPUptPassing" ]->Fill( pat1Jet.Pt() );
			}
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

	histos1D_[ "lowPUjetMassDenom" ] = fileService->make< TH1D >( "lowPUjetMassDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "lowPUjetMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "lowPUjetMassDenom" ]->Sumw2();

	histos1D_[ "lowPUjetMassPassing" ] = fileService->make< TH1D >( "lowPUjetMassPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "lowPUjetMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "lowPUjetMassPassing" ]->Sumw2();

	histos1D_[ "lowPUjetMassEfficiency" ] = fileService->make< TH1D >( "lowPUjetMassEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "lowPUjetMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "lowPUjetMassEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "lowPUjetMassTrimDenom" ] = fileService->make< TH1D >( "lowPUjetMassTrimDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "lowPUjetMassTrimDenom" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "lowPUjetMassTrimDenom" ]->Sumw2();

	histos1D_[ "lowPUjetMassTrimPassing" ] = fileService->make< TH1D >( "lowPUjetMassTrimPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "lowPUjetMassTrimPassing" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "lowPUjetMassTrimPassing" ]->Sumw2();

	histos1D_[ "lowPUjetMassTrimEfficiency" ] = fileService->make< TH1D >( "lowPUjetMassTrimEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "lowPUjetMassTrimEfficiency" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "lowPUjetMassTrimEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "lowPUjetMassTrimModDenom" ] = fileService->make< TH1D >( "lowPUjetMassTrimModDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "lowPUjetMassTrimModDenom" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "lowPUjetMassTrimModDenom" ]->Sumw2();

	histos1D_[ "lowPUjetMassTrimModPassing" ] = fileService->make< TH1D >( "lowPUjetMassTrimModPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "lowPUjetMassTrimModPassing" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "lowPUjetMassTrimModPassing" ]->Sumw2();

	histos1D_[ "lowPUjetMassTrimModEfficiency" ] = fileService->make< TH1D >( "lowPUjetMassTrimModEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "lowPUjetMassTrimModEfficiency" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "lowPUjetMassTrimModEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "lowPUjetMassPrunedDenom" ] = fileService->make< TH1D >( "lowPUjetMassPrunedDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "lowPUjetMassPrunedDenom" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "lowPUjetMassPrunedDenom" ]->Sumw2();

	histos1D_[ "lowPUjetMassPrunedPassing" ] = fileService->make< TH1D >( "lowPUjetMassPrunedPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "lowPUjetMassPrunedPassing" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "lowPUjetMassPrunedPassing" ]->Sumw2();

	histos1D_[ "lowPUjetMassPrunedEfficiency" ] = fileService->make< TH1D >( "lowPUjetMassPrunedEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "lowPUjetMassPrunedEfficiency" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "lowPUjetMassPrunedEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "lowPUHTDenom" ] = fileService->make< TH1D >( "lowPUHTDenom", "HT", 100, 0., 2000);
	histos1D_[ "lowPUHTDenom" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "lowPUHTDenom" ]->Sumw2();

	histos1D_[ "lowPUHTPassing" ] = fileService->make< TH1D >( "lowPUHTPassing", "HT passing", 100, 0., 2000);
	histos1D_[ "lowPUHTPassing" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "lowPUHTPassing" ]->Sumw2();

	histos1D_[ "lowPUHTEfficiency" ] = fileService->make< TH1D >( "lowPUHTEfficiency", "HT efficiency", 100, 0., 2000);
	histos1D_[ "lowPUHTEfficiency" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "lowPUHTEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "lowPUptDenom" ] = fileService->make< TH1D >( "lowPUptDenom", "pt", 100, 0., 1000);
	histos1D_[ "lowPUptDenom" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "lowPUptDenom" ]->Sumw2();

	histos1D_[ "lowPUptPassing" ] = fileService->make< TH1D >( "lowPUptPassing", "pt passing", 100, 0., 1000);
	histos1D_[ "lowPUptPassing" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "lowPUptPassing" ]->Sumw2();

	histos1D_[ "lowPUptEfficiency" ] = fileService->make< TH1D >( "lowPUptEfficiency", "pt efficiency", 100, 0., 1000);
	histos1D_[ "lowPUptEfficiency" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "lowPUptEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "midPUjetMassDenom" ] = fileService->make< TH1D >( "midPUjetMassDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "midPUjetMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "midPUjetMassDenom" ]->Sumw2();

	histos1D_[ "midPUjetMassPassing" ] = fileService->make< TH1D >( "midPUjetMassPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "midPUjetMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "midPUjetMassPassing" ]->Sumw2();

	histos1D_[ "midPUjetMassEfficiency" ] = fileService->make< TH1D >( "midPUjetMassEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "midPUjetMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "midPUjetMassEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "midPUjetMassTrimDenom" ] = fileService->make< TH1D >( "midPUjetMassTrimDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "midPUjetMassTrimDenom" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "midPUjetMassTrimDenom" ]->Sumw2();

	histos1D_[ "midPUjetMassTrimPassing" ] = fileService->make< TH1D >( "midPUjetMassTrimPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "midPUjetMassTrimPassing" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "midPUjetMassTrimPassing" ]->Sumw2();

	histos1D_[ "midPUjetMassTrimEfficiency" ] = fileService->make< TH1D >( "midPUjetMassTrimEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "midPUjetMassTrimEfficiency" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "midPUjetMassTrimEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "midPUjetMassTrimModDenom" ] = fileService->make< TH1D >( "midPUjetMassTrimModDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "midPUjetMassTrimModDenom" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "midPUjetMassTrimModDenom" ]->Sumw2();

	histos1D_[ "midPUjetMassTrimModPassing" ] = fileService->make< TH1D >( "midPUjetMassTrimModPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "midPUjetMassTrimModPassing" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "midPUjetMassTrimModPassing" ]->Sumw2();

	histos1D_[ "midPUjetMassTrimModEfficiency" ] = fileService->make< TH1D >( "midPUjetMassTrimModEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "midPUjetMassTrimModEfficiency" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "midPUjetMassTrimModEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "midPUjetMassPrunedDenom" ] = fileService->make< TH1D >( "midPUjetMassPrunedDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "midPUjetMassPrunedDenom" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "midPUjetMassPrunedDenom" ]->Sumw2();

	histos1D_[ "midPUjetMassPrunedPassing" ] = fileService->make< TH1D >( "midPUjetMassPrunedPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "midPUjetMassPrunedPassing" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "midPUjetMassPrunedPassing" ]->Sumw2();

	histos1D_[ "midPUjetMassPrunedEfficiency" ] = fileService->make< TH1D >( "midPUjetMassPrunedEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "midPUjetMassPrunedEfficiency" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "midPUjetMassPrunedEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "midPUHTDenom" ] = fileService->make< TH1D >( "midPUHTDenom", "HT", 100, 0., 2000);
	histos1D_[ "midPUHTDenom" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "midPUHTDenom" ]->Sumw2();

	histos1D_[ "midPUHTPassing" ] = fileService->make< TH1D >( "midPUHTPassing", "HT passing", 100, 0., 2000);
	histos1D_[ "midPUHTPassing" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "midPUHTPassing" ]->Sumw2();

	histos1D_[ "midPUHTEfficiency" ] = fileService->make< TH1D >( "midPUHTEfficiency", "HT efficiency", 100, 0., 2000);
	histos1D_[ "midPUHTEfficiency" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "midPUHTEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "midPUptDenom" ] = fileService->make< TH1D >( "midPUptDenom", "pt", 100, 0., 1000);
	histos1D_[ "midPUptDenom" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "midPUptDenom" ]->Sumw2();

	histos1D_[ "midPUptPassing" ] = fileService->make< TH1D >( "midPUptPassing", "pt passing", 100, 0., 1000);
	histos1D_[ "midPUptPassing" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "midPUptPassing" ]->Sumw2();

	histos1D_[ "midPUptEfficiency" ] = fileService->make< TH1D >( "midPUptEfficiency", "pt efficiency", 100, 0., 1000);
	histos1D_[ "midPUptEfficiency" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "midPUptEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "highPUjetMassDenom" ] = fileService->make< TH1D >( "highPUjetMassDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "highPUjetMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "highPUjetMassDenom" ]->Sumw2();

	histos1D_[ "highPUjetMassPassing" ] = fileService->make< TH1D >( "highPUjetMassPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "highPUjetMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "highPUjetMassPassing" ]->Sumw2();

	histos1D_[ "highPUjetMassEfficiency" ] = fileService->make< TH1D >( "highPUjetMassEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "highPUjetMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "highPUjetMassEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "highPUjetMassTrimDenom" ] = fileService->make< TH1D >( "highPUjetMassTrimDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "highPUjetMassTrimDenom" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "highPUjetMassTrimDenom" ]->Sumw2();

	histos1D_[ "highPUjetMassTrimPassing" ] = fileService->make< TH1D >( "highPUjetMassTrimPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "highPUjetMassTrimPassing" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "highPUjetMassTrimPassing" ]->Sumw2();

	histos1D_[ "highPUjetMassTrimEfficiency" ] = fileService->make< TH1D >( "highPUjetMassTrimEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "highPUjetMassTrimEfficiency" ]->SetXTitle( "Leading Jet MassTrim [GeV]" );
	histos1D_[ "highPUjetMassTrimEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "highPUjetMassTrimModDenom" ] = fileService->make< TH1D >( "highPUjetMassTrimModDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "highPUjetMassTrimModDenom" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "highPUjetMassTrimModDenom" ]->Sumw2();

	histos1D_[ "highPUjetMassTrimModPassing" ] = fileService->make< TH1D >( "highPUjetMassTrimModPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "highPUjetMassTrimModPassing" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "highPUjetMassTrimModPassing" ]->Sumw2();

	histos1D_[ "highPUjetMassTrimModEfficiency" ] = fileService->make< TH1D >( "highPUjetMassTrimModEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "highPUjetMassTrimModEfficiency" ]->SetXTitle( "Leading Jet MassTrimMod [GeV]" );
	histos1D_[ "highPUjetMassTrimModEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "highPUjetMassPrunedDenom" ] = fileService->make< TH1D >( "highPUjetMassPrunedDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "highPUjetMassPrunedDenom" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "highPUjetMassPrunedDenom" ]->Sumw2();

	histos1D_[ "highPUjetMassPrunedPassing" ] = fileService->make< TH1D >( "highPUjetMassPrunedPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "highPUjetMassPrunedPassing" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "highPUjetMassPrunedPassing" ]->Sumw2();

	histos1D_[ "highPUjetMassPrunedEfficiency" ] = fileService->make< TH1D >( "highPUjetMassPrunedEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "highPUjetMassPrunedEfficiency" ]->SetXTitle( "Leading Jet MassPruned [GeV]" );
	histos1D_[ "highPUjetMassPrunedEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "highPUHTDenom" ] = fileService->make< TH1D >( "highPUHTDenom", "HT", 100, 0., 2000);
	histos1D_[ "highPUHTDenom" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "highPUHTDenom" ]->Sumw2();

	histos1D_[ "highPUHTPassing" ] = fileService->make< TH1D >( "highPUHTPassing", "HT passing", 100, 0., 2000);
	histos1D_[ "highPUHTPassing" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "highPUHTPassing" ]->Sumw2();

	histos1D_[ "highPUHTEfficiency" ] = fileService->make< TH1D >( "highPUHTEfficiency", "HT efficiency", 100, 0., 2000);
	histos1D_[ "highPUHTEfficiency" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "highPUHTEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "highPUptDenom" ] = fileService->make< TH1D >( "highPUptDenom", "pt", 100, 0., 1000);
	histos1D_[ "highPUptDenom" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "highPUptDenom" ]->Sumw2();

	histos1D_[ "highPUptPassing" ] = fileService->make< TH1D >( "highPUptPassing", "pt passing", 100, 0., 1000);
	histos1D_[ "highPUptPassing" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "highPUptPassing" ]->Sumw2();

	histos1D_[ "highPUptEfficiency" ] = fileService->make< TH1D >( "highPUptEfficiency", "pt efficiency", 100, 0., 1000);
	histos1D_[ "highPUptEfficiency" ]->SetXTitle( "pt [GeV]" );
	histos1D_[ "highPUptEfficiency" ]->SetYTitle( "Efficiency" );

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

    histos1D_[ "jetMassPrunedEfficiency" ]->Sumw2();
    histos1D_[ "jetMassPrunedEfficiency" ]->Divide(histos1D_[ "jetMassPrunedPassing" ], histos1D_[ "jetMassPrunedDenom" ], 1,1,"B");

    histos1D_[ "HTEfficiency" ]->Sumw2();
    histos1D_[ "HTEfficiency" ]->Divide(histos1D_[ "HTPassing" ], histos1D_[ "HTDenom" ], 1,1,"B");

    histos1D_[ "ptEfficiency" ]->Sumw2();
    histos1D_[ "ptEfficiency" ]->Divide(histos1D_[ "ptPassing" ], histos1D_[ "ptDenom" ], 1,1,"B");

    histos1D_[ "lowPUjetMassEfficiency" ]->Sumw2();
    histos1D_[ "lowPUjetMassEfficiency" ]->Divide(histos1D_[ "lowPUjetMassPassing" ], histos1D_[ "lowPUjetMassDenom" ], 1,1,"B");

    histos1D_[ "lowPUjetMassTrimEfficiency" ]->Sumw2();
    histos1D_[ "lowPUjetMassTrimEfficiency" ]->Divide(histos1D_[ "lowPUjetMassTrimPassing" ], histos1D_[ "lowPUjetMassTrimDenom" ], 1,1,"B");

    histos1D_[ "lowPUjetMassTrimModEfficiency" ]->Sumw2();
    histos1D_[ "lowPUjetMassTrimModEfficiency" ]->Divide(histos1D_[ "lowPUjetMassTrimModPassing" ], histos1D_[ "lowPUjetMassTrimModDenom" ], 1,1,"B");

    histos1D_[ "lowPUjetMassPrunedEfficiency" ]->Sumw2();
    histos1D_[ "lowPUjetMassPrunedEfficiency" ]->Divide(histos1D_[ "lowPUjetMassPrunedPassing" ], histos1D_[ "lowPUjetMassPrunedDenom" ], 1,1,"B");

    histos1D_[ "lowPUHTEfficiency" ]->Sumw2();
    histos1D_[ "lowPUHTEfficiency" ]->Divide(histos1D_[ "lowPUHTPassing" ], histos1D_[ "lowPUHTDenom" ], 1,1,"B");

    histos1D_[ "lowPUptEfficiency" ]->Sumw2();
    histos1D_[ "lowPUptEfficiency" ]->Divide(histos1D_[ "lowPUptPassing" ], histos1D_[ "lowPUptDenom" ], 1,1,"B");


    histos1D_[ "midPUjetMassEfficiency" ]->Sumw2();
    histos1D_[ "midPUjetMassEfficiency" ]->Divide(histos1D_[ "midPUjetMassPassing" ], histos1D_[ "midPUjetMassDenom" ], 1,1,"B");

    histos1D_[ "midPUjetMassTrimEfficiency" ]->Sumw2();
    histos1D_[ "midPUjetMassTrimEfficiency" ]->Divide(histos1D_[ "midPUjetMassTrimPassing" ], histos1D_[ "midPUjetMassTrimDenom" ], 1,1,"B");

    histos1D_[ "midPUjetMassTrimModEfficiency" ]->Sumw2();
    histos1D_[ "midPUjetMassTrimModEfficiency" ]->Divide(histos1D_[ "midPUjetMassTrimModPassing" ], histos1D_[ "midPUjetMassTrimModDenom" ], 1,1,"B");

    histos1D_[ "midPUjetMassPrunedEfficiency" ]->Sumw2();
    histos1D_[ "midPUjetMassPrunedEfficiency" ]->Divide(histos1D_[ "midPUjetMassPrunedPassing" ], histos1D_[ "midPUjetMassPrunedDenom" ], 1,1,"B");

    histos1D_[ "midPUHTEfficiency" ]->Sumw2();
    histos1D_[ "midPUHTEfficiency" ]->Divide(histos1D_[ "midPUHTPassing" ], histos1D_[ "midPUHTDenom" ], 1,1,"B");

    histos1D_[ "midPUptEfficiency" ]->Sumw2();
    histos1D_[ "midPUptEfficiency" ]->Divide(histos1D_[ "midPUptPassing" ], histos1D_[ "midPUptDenom" ], 1,1,"B");

    histos1D_[ "highPUjetMassEfficiency" ]->Sumw2();
    histos1D_[ "highPUjetMassEfficiency" ]->Divide(histos1D_[ "highPUjetMassPassing" ], histos1D_[ "highPUjetMassDenom" ], 1,1,"B");

    histos1D_[ "highPUjetMassTrimEfficiency" ]->Sumw2();
    histos1D_[ "highPUjetMassTrimEfficiency" ]->Divide(histos1D_[ "highPUjetMassTrimPassing" ], histos1D_[ "highPUjetMassTrimDenom" ], 1,1,"B");

    histos1D_[ "highPUjetMassTrimModEfficiency" ]->Sumw2();
    histos1D_[ "highPUjetMassTrimModEfficiency" ]->Divide(histos1D_[ "highPUjetMassTrimModPassing" ], histos1D_[ "highPUjetMassTrimModDenom" ], 1,1,"B");

    histos1D_[ "highPUjetMassPrunedEfficiency" ]->Sumw2();
    histos1D_[ "highPUjetMassPrunedEfficiency" ]->Divide(histos1D_[ "highPUjetMassPrunedPassing" ], histos1D_[ "highPUjetMassPrunedDenom" ], 1,1,"B");

    histos1D_[ "highPUHTEfficiency" ]->Sumw2();
    histos1D_[ "highPUHTEfficiency" ]->Divide(histos1D_[ "highPUHTPassing" ], histos1D_[ "highPUHTDenom" ], 1,1,"B");

    histos1D_[ "highPUptEfficiency" ]->Sumw2();
    histos1D_[ "highPUptEfficiency" ]->Divide(histos1D_[ "highPUptPassing" ], histos1D_[ "highPUptDenom" ], 1,1,"B");


}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void TriggerEfficiency::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerEfficiency);
