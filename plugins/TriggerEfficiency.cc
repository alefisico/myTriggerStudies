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

		//edm::InputTag hltJets;
		edm::InputTag patJets;
		std::string triggerPath;
		double scale;

		HLTConfigProvider hltConfig;
		int triggerBit;
};



TriggerEfficiency::TriggerEfficiency(const edm::ParameterSet& iConfig){
	//hltJets			= iConfig.getParameter<edm::InputTag> ( "hltJets" );   			// Obtain inputs
	patJets			= iConfig.getParameter<edm::InputTag> ( "patJets" );   			// Obtain inputs
	triggerPath		= iConfig.getParameter<std::string> ( "triggerPath" );   			// Obtain inputs
	scale			= iConfig.getParameter<double> ( "sf" );   			// Obtain inputs
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

	/*trigger objects we want to match
	edm::Handle<edm::View<reco::PFJet> > hltjets;
	iEvent.getByLabel(hltJets,hltjets);*/

	edm::Handle<edm::View<pat::Jet> > patjets;
	iEvent.getByLabel(patJets,patjets);

	std::vector< TLorentzVector > patJetsCollection;

	//for(edm::View<reco::PFJet>::const_iterator ijet=patjets->begin(); ijet!=patjets->end();ijet++){
	double HT = 0;
	for(edm::View<pat::Jet>::const_iterator ijet=patjets->begin(); ijet!=patjets->end();ijet++){

		if ( ijet->pt() < 40.0 || abs( ijet->eta() ) > 3.0 ) continue;
		HT += ijet->pt();
		patJetsCollection.push_back( TLorentzVector( ijet->px(), ijet->py(), ijet->pz(), ijet->energy() ) );
	}

	if( HT > 0 ) {

		sort( patJetsCollection.begin(), patJetsCollection.end(), compare_JetMass);
		histos1D_[ "HTDenom" ]->Fill( HT, scale );
		histos1D_[ "jetMassDenom" ]->Fill( patJetsCollection[0].M(), scale );
		histos2D_[ "jetMassHTDenom" ]->Fill( HT, patJetsCollection[0].M() );

		if (triggerResults->accept(triggerBit)){

			histos1D_[ "HTPassing" ]->Fill( HT, scale );
			histos1D_[ "jetMassPassing" ]->Fill( patJetsCollection[0].M(), scale );
			histos2D_[ "jetMassHTPassing" ]->Fill( HT, patJetsCollection[0].M() );
		}
	}
}


// ------------ method called once each job just before starting event loop  ------------
void TriggerEfficiency::beginJob() {

	edm::Service< TFileService > fileService;
	histos2D_[ "jetMassHTDenom" ] = fileService->make< TH2D >( "jetMassHTDenom", "HT vs Leading Jet Mass", 100, 0., 2000, 80, 0., 400. );
	histos2D_[ "jetMassHTDenom" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "jetMassHTDenom" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassHTPassing" ] = fileService->make< TH2D >( "jetMassHTPassing", "HT vs Leading Jet Mass passing path", 100, 0., 2000, 80, 0., 400. );
	histos2D_[ "jetMassHTPassing" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "jetMassHTPassing" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassHT2Defficiency" ] = fileService->make< TH2D >( "jetMassHT2Defficiency", "Comparative efficiency", 100, 0., 2000, 80, 0., 400. );
	histos2D_[ "jetMassHT2Defficiency" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "jetMassHT2Defficiency" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos1D_[ "jetMassDenom" ] = fileService->make< TH1D >( "jetMassDenom", "Jet mass", 40, 0., 400);
	histos1D_[ "jetMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassDenom" ]->Sumw2();

	histos1D_[ "jetMassPassing" ] = fileService->make< TH1D >( "jetMassPassing", "Jet mass passing", 40, 0., 400);
	histos1D_[ "jetMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassPassing" ]->Sumw2();

	histos1D_[ "jetMassEfficiency" ] = fileService->make< TH1D >( "jetMassEfficiency", "Leading jet mass efficiency", 40, 0., 400);
	histos1D_[ "jetMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "HTDenom" ] = fileService->make< TH1D >( "HTDenom", "HT", 200, 0., 2000);
	histos1D_[ "HTDenom" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "HTDenom" ]->Sumw2();

	histos1D_[ "HTPassing" ] = fileService->make< TH1D >( "HTPassing", "HT passing", 200, 0., 2000);
	histos1D_[ "HTPassing" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "HTPassing" ]->Sumw2();

	histos1D_[ "HTEfficiency" ] = fileService->make< TH1D >( "HTEfficiency", "HT efficiency", 200, 0., 2000);
	histos1D_[ "HTEfficiency" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "HTEfficiency" ]->SetYTitle( "Efficiency" );


}

// ------------ method called once each job just after ending the event loop  ------------
void TriggerEfficiency::endJob() {

    histos2D_[ "jetMassHT2Defficiency" ]->Sumw2();
    histos2D_[ "jetMassHT2Defficiency" ]->Divide(histos2D_[ "jetMassHTPassing" ],histos2D_[ "jetMassHTDenom" ],1,1,"B");
    
    
    histos1D_[ "jetMassEfficiency" ]->Sumw2();
    histos1D_[ "jetMassEfficiency" ]->Divide(histos1D_[ "jetMassPassing" ], histos1D_[ "jetMassDenom" ], 1,1,"B");

    histos1D_[ "HTEfficiency" ]->Sumw2();
    histos1D_[ "HTEfficiency" ]->Divide(histos1D_[ "HTPassing" ], histos1D_[ "HTDenom" ], 1,1,"B");

}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void TriggerEfficiency::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerEfficiency);
