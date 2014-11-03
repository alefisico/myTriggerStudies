// -*- C++ -*-
//
// Package:    MyTrigger/myTriggerStudies
// Class:      SimpleAnalyzer
// 
/**\class SimpleAnalyzer SimpleAnalyzer.cc MyTrigger/myTriggerStudies/plugins/SimpleAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  alejandro gomez
//         Created:  Fri, 31 Oct 2014 14:40:20 GMT
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
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/PatCandidates/interface/Jet.h"

#include "TMath.h"
#include "TH2D.h"
#include "TH1D.h"
#include <TLorentzVector.h>
//
// class declaration
//

class SimpleAnalyzer : public edm::EDAnalyzer {
	public:
		explicit SimpleAnalyzer(const edm::ParameterSet&);
		~SimpleAnalyzer();

		//static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


	private:
		virtual void beginJob() override;
		virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
		virtual void endJob() override;

		//virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
		//virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
		//virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
		//virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

		// ----------member data ---------------------------
		std::map< std::string, TH2D* > histos2D_;
		std::map< std::string, TH1D* > histos1D_;

		edm::EDGetTokenT<reco::PFJetCollection> jets_;
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
SimpleAnalyzer::SimpleAnalyzer(const edm::ParameterSet& iConfig):
	jets_(consumes<reco::PFJetCollection>(iConfig.getParameter<edm::InputTag>("jets")))
{
   //now do what ever initialization is needed

}


SimpleAnalyzer::~SimpleAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
SimpleAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	using namespace reco;

	Handle<reco::PFJetCollection> jets;
	iEvent.getByToken(jets_, jets);

	double HT40 = 0;
	int numJets40 = 0;
	double HT100 = 0;
	int numJets100 = 0;
	for( const reco::Jet &ijet : *jets ){
		histos1D_[ "jetPt" ]->Fill( ijet.pt() );
		histos1D_[ "jetEta" ]->Fill( ijet.eta() );

		if( ijet.pt() < 40 || abs( ijet.eta() ) > 3.0 ) continue;
		numJets40 += 1;
		HT40 += ijet.pt();
		histos1D_[ "jetPt40" ]->Fill( ijet.pt() );
		histos1D_[ "jetEta40" ]->Fill( ijet.eta() );

		if( ijet.pt() < 100 || abs( ijet.eta() ) > 3.0 ) continue;
		HT100 += ijet.pt();
		numJets100 += 1;
		histos1D_[ "jetPt100" ]->Fill( ijet.pt() );
		histos1D_[ "jetEta100" ]->Fill( ijet.eta() );

	}
	if ( HT40 > 0 ) histos1D_[ "HT40" ]->Fill( HT40 );
	histos1D_[ "numJets40" ]->Fill( numJets40 );
	if ( HT100 > 0 ) histos1D_[ "HT100" ]->Fill( HT100 );
	histos1D_[ "numJets100" ]->Fill( numJets100 );
}


// ------------ method called once each job just before starting event loop  ------------
void 
SimpleAnalyzer::beginJob()
{
	edm::Service< TFileService > fileService;
	histos1D_[ "jetPt" ] = fileService->make< TH1D >( "jetPt", "jetPt", 40, 0., 400. );
	histos1D_[ "jetPt" ]->SetXTitle( "Jet p_{T} [GeV]" );
	histos1D_[ "jetEta" ] = fileService->make< TH1D >( "jetEta", "jetEta", 10, -5.0, 5.0 );
	histos1D_[ "jetEta" ]->SetXTitle( "Jet #eta [GeV]" );

	histos1D_[ "jetPt40" ] = fileService->make< TH1D >( "jetPt40", "jetPt40", 40, 0., 400. );
	histos1D_[ "jetPt40" ]->SetXTitle( "Jet p_{T} [GeV]" );
	histos1D_[ "jetEta40" ] = fileService->make< TH1D >( "jetEta40", "jetEta40", 10, -5.0, 5.0 );
	histos1D_[ "jetEta40" ]->SetXTitle( "Jet #eta [GeV]" );
	histos1D_[ "HT40" ] = fileService->make< TH1D >( "HT40", "HT40", 150, 0., 1500. );
	histos1D_[ "HT40" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "numJets40" ] = fileService->make< TH1D >( "numJets40", "numJets40", 15, 0., 15. );
	histos1D_[ "numJets40" ]->SetXTitle( "Jet Multiplicity [GeV]" );

	histos1D_[ "jetPt100" ] = fileService->make< TH1D >( "jetPt100", "jetPt100", 40, 0., 400. );
	histos1D_[ "jetPt100" ]->SetXTitle( "Jet p_{T} [GeV]" );
	histos1D_[ "jetEta100" ] = fileService->make< TH1D >( "jetEta100", "jetEta100", 10, -5.0, 5.0 );
	histos1D_[ "jetEta100" ]->SetXTitle( "Jet #eta [GeV]" );
	histos1D_[ "HT100" ] = fileService->make< TH1D >( "HT100", "HT100", 150, 0., 1500. );
	histos1D_[ "HT100" ]->SetXTitle( "HT [GeV]" );
	histos1D_[ "numJets100" ] = fileService->make< TH1D >( "numJets100", "numJets100", 15, 0., 15. );
	histos1D_[ "numJets100" ]->SetXTitle( "Jet Multiplicity [GeV]" );
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SimpleAnalyzer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
SimpleAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
SimpleAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
SimpleAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
SimpleAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
/*void
SimpleAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}*/

//define this as a plug-in
DEFINE_FWK_MODULE(SimpleAnalyzer);
