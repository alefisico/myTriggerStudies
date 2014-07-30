// -*- C++ -*-
//
// Package:    MyTrigger/TriggerPlotter
// Class:      TriggerPlotter
// 
/**\class TriggerPlotter TriggerPlotter.cc MyTrigger/TriggerPlotter/plugins/TriggerPlotter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Alejandro Gomez Espinosa
//         Created:  Tue, 22 Jul 2014 23:08:39 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <vector>
#include <sstream>
#include <string>

#include "DataFormats/JetReco/interface/Jet.h"
//#include "AnalysisDataFormats/TopObjects/interface/CATopJetTagInfo.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "PhysicsTools/CandUtils/interface/AddFourMomenta.h"
#include "DataFormats/Candidate/interface/CandMatchMap.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include <Math/VectorUtil.h>
#include "TH1F.h"
#include <TH2.h>
#include <TTree.h>
#include <TLorentzVector.h>

//
// class declaration
//

class TriggerPlotter : public edm::EDProducer {
   public:
      explicit TriggerPlotter(const edm::ParameterSet&);
      ~TriggerPlotter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      void initialize();
	
      edm::Service<TFileService> fs;						// Output File 
      //std::string label_;
      edm::InputTag srcJets_;
      edm::InputTag srcJetsNOJEC_;
      TH1D * jet1pt;
      TH1D * jet1mass;
      TH1D * ht;
      TH1D * eventJetMass;
      TH1D * jet1pt_NOJEC;
      TH1D * jet1mass_NOJEC;
      TH1D * ht_NOJEC;
      TH1D * eventJetMass_NOJEC;
      
      TTree* tree;
      TTree* tree_NOJEC;
      float jetPt;
      std::vector<float> *jetPtVec;
      std::vector<float> *jetEtaVec;
      std::vector<float> *jetPhiVec;
      std::vector<float> *jetEnergyVec;
      std::vector<float> *jetPtVec_NOJEC;
      std::vector<float> *jetEtaVec_NOJEC;
      std::vector<float> *jetPhiVec_NOJEC;
      std::vector<float> *jetEnergyVec_NOJEC;
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
TriggerPlotter::TriggerPlotter(const edm::ParameterSet& iConfig)
{
	srcJets_  		= iConfig.getParameter<edm::InputTag> ( "hltJets" );   			// Obtain inputs
	srcJetsNOJEC_  		= iConfig.getParameter<edm::InputTag> ( "hltJetsNOJEC" );   			// Obtain inputs
  
}


TriggerPlotter::~TriggerPlotter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TriggerPlotter::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

	initialize();
	using namespace std;
	using namespace edm;
	using namespace reco;

  	//edm::Handle<edm::View<reco::MET> > jets;
  	edm::Handle<edm::View<reco::Jet> > jets;
	iEvent.getByLabel(srcJets_,jets);

  	std::vector< TLorentzVector > p4jet;

	double HT = 0;
	double EventJetMass = 0;
    	for(edm::View<reco::Jet>::const_iterator ijet=jets->begin(); ijet!=jets->end();ijet++){
    	//for(edm::View<reco::MET>::const_iterator ijet=jets->begin(); ijet!=jets->end();ijet++){
    		p4jet.push_back( TLorentzVector( ijet->px(), ijet->py(), ijet->pz(), ijet->energy() ) );
		HT += ijet->pt();
		EventJetMass += ijet->mass();

		jetPtVec->push_back( ijet->pt() ); 
		jetEtaVec->push_back( ijet->eta() ); 
		jetPhiVec->push_back( ijet->phi() ); 
		jetEnergyVec->push_back( ijet->energy() ); 
	} 

	if( p4jet.size() > 0 ){
		jet1pt->Fill( p4jet[0].Pt() );
		jet1mass->Fill( p4jet[0].M() );
		ht->Fill( HT );
		eventJetMass->Fill( EventJetMass );
	}

  	edm::Handle<edm::View<reco::Jet> > jets_NOJEC;
	iEvent.getByLabel(srcJetsNOJEC_,jets_NOJEC);

	std::vector< TLorentzVector > p4jet_NOJEC;

	double HT_NOJEC = 0;
	double EventJetMass_NOJEC = 0;
    	for(edm::View<reco::Jet>::const_iterator ijet_NOJEC=jets_NOJEC->begin(); ijet_NOJEC!=jets_NOJEC->end();ijet_NOJEC++){
    		p4jet_NOJEC.push_back( TLorentzVector( ijet_NOJEC->px(), ijet_NOJEC->py(), ijet_NOJEC->pz(), ijet_NOJEC->energy() ) );
		HT_NOJEC += ijet_NOJEC->pt();
		EventJetMass_NOJEC += ijet_NOJEC->mass();

		jetPtVec_NOJEC->push_back( ijet_NOJEC->pt() ); 
		jetEtaVec_NOJEC->push_back( ijet_NOJEC->eta() ); 
		jetPhiVec_NOJEC->push_back( ijet_NOJEC->phi() ); 
		jetEnergyVec_NOJEC->push_back( ijet_NOJEC->energy() ); 
	} 

	if( p4jet_NOJEC.size() > 0 ){
		jet1pt_NOJEC->Fill( p4jet_NOJEC[0].Pt() );
		jet1mass_NOJEC->Fill( p4jet_NOJEC[0].M() );
		ht_NOJEC->Fill( HT_NOJEC );
		eventJetMass_NOJEC->Fill( EventJetMass_NOJEC );
	}

	tree->Fill();
	tree_NOJEC->Fill();
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
TriggerPlotter::beginJob()
{
	jet1pt = fs->make<TH1D>("jet1pt" , "Leading Jet p_{T}", 200 ,0., 2000. );	
	jet1mass = fs->make<TH1D>("jet1mass" , "Leading Mass p_{T}", 50 ,0., 500. );	
	ht = fs->make<TH1D>("ht" , "HT", 500 ,0., 5000. );	
	eventJetMass = fs->make<TH1D>("eventJetMass" , "Event Jet Mass", 500 ,0., 5000. );	

	tree = fs->make<TTree>("JetVariables", "JetVariables");
	jetPtVec = new std::vector<float>;
	jetEtaVec = new std::vector<float>;
	jetPhiVec = new std::vector<float>;
	jetEnergyVec = new std::vector<float>;
	tree->Branch("jetPt", "vector<float>", &jetPtVec);
	tree->Branch("jetEta", "vector<float>", &jetEtaVec);
	tree->Branch("jetPhi", "vector<float>", &jetPhiVec);
	tree->Branch("jetEnergy", "vector<float>", &jetEnergyVec);

	jet1pt_NOJEC = fs->make<TH1D>("jet1pt_NOJEC" , "Leading Jet p_{T}", 200 ,0., 2000. );	
	jet1mass_NOJEC = fs->make<TH1D>("jet1mass_NOJEC" , "Leading Mass p_{T}", 50 ,0., 500. );	
	ht_NOJEC = fs->make<TH1D>("ht_NOJEC" , "HT", 500 ,0., 5000. );	
	eventJetMass_NOJEC = fs->make<TH1D>("eventJetMass_NOJEC" , "Event Jet Mass", 500 ,0., 5000. );	

	tree_NOJEC = fs->make<TTree>("JetVariables_NOJEC", "JetVariables_NOJEC");
	jetPtVec_NOJEC = new std::vector<float>;
	jetEtaVec_NOJEC = new std::vector<float>;
	jetPhiVec_NOJEC = new std::vector<float>;
	jetEnergyVec_NOJEC = new std::vector<float>;
	tree_NOJEC->Branch("jetPt_NOJEC", "vector<float>", &jetPtVec_NOJEC);
	tree_NOJEC->Branch("jetEta_NOJEC", "vector<float>", &jetEtaVec_NOJEC);
	tree_NOJEC->Branch("jetPhi_NOJEC", "vector<float>", &jetPhiVec_NOJEC);
	tree_NOJEC->Branch("jetEnergy_NOJEC", "vector<float>", &jetEnergyVec_NOJEC);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerPlotter::endJob() {

	delete jetPtVec;
	delete jetEtaVec;
	delete jetPhiVec;
	delete jetEnergyVec;
	delete jetPtVec_NOJEC;
	delete jetEtaVec_NOJEC;
	delete jetPhiVec_NOJEC;
	delete jetEnergyVec_NOJEC;
}

void TriggerPlotter::initialize() {

	jetPtVec -> clear();
	jetEtaVec -> clear();
	jetPhiVec -> clear();
	jetEnergyVec -> clear();
	jetPtVec_NOJEC -> clear();
	jetEtaVec_NOJEC -> clear();
	jetPhiVec_NOJEC -> clear();
	jetEnergyVec_NOJEC -> clear();
}

// ------------ method called when starting to processes a run  ------------
/*
void
TriggerPlotter::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
TriggerPlotter::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
TriggerPlotter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
TriggerPlotter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerPlotter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerPlotter);
