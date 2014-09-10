// -*- C++ -*-
//
// Package:    MyTrigger/myTriggerStudies
// Class:      OverlapTriggers.cc
// 
/**\class OverlapTriggers.cc OverlapTriggers.cc.cc MyTrigger/myTriggerStudies/plugins/OverlapTriggers.cc.cc

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

class OverlapTriggers : public edm::EDAnalyzer {
	public:
		explicit OverlapTriggers(const edm::ParameterSet&);
		~OverlapTriggers();

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
		std::string trigger1;
		std::string trigger2;

		HLTConfigProvider hltConfig;
		int triggerBit1;
		int triggerBit2;

		int onlyTrigger1 = 0;
		int onlyTrigger2 = 0;
		int bothTriggers = 0;
		int noneTriggers = 0;
		double totalNumberEvents = 0;

};



OverlapTriggers::OverlapTriggers(const edm::ParameterSet& iConfig){
	trigger1		= iConfig.getParameter<std::string> ( "trigger1" );   			// Obtain inputs
	trigger2		= iConfig.getParameter<std::string> ( "trigger2" );   			// Obtain inputs
}


OverlapTriggers::~OverlapTriggers()
{
}


//
// member functions
//

// ------------ method called for each event  ------------
void OverlapTriggers::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {

	using namespace edm;
	using namespace std;

	bool changedConfig = false;
	if (!hltConfig.init(iEvent.getRun(), iSetup, "HLT3PB", changedConfig)) {
		cout << "Initialization of HLTConfigProvider failed!!" << endl;
		return;
	}
	if (changedConfig){
		std::cout << "the curent menu is " << hltConfig.tableName() << std::endl;
		triggerBit1 = -1;
		triggerBit2 = -1;
		for (size_t j = 0; j < hltConfig.triggerNames().size(); j++) {
			//std::cout << TString(hltConfig.triggerNames()[j]) << std::endl;
			if (TString(hltConfig.triggerNames()[j]).Contains(trigger1)) triggerBit1 = j;
			if (TString(hltConfig.triggerNames()[j]).Contains(trigger2)) triggerBit2 = j;
		}
		if (triggerBit1 == -1) cout << "HLT path not found" << endl;
		if (triggerBit2 == -1) cout << "HLT path not found" << endl;

	}

	//open the trigger summary
	edm::InputTag triggerResultsLabel = edm::InputTag("TriggerResults", "", "HLT3PB");
	edm::Handle<edm::TriggerResults> triggerResults;
	iEvent.getByLabel(triggerResultsLabel, triggerResults);


	if (triggerResults->accept(triggerBit1) && triggerResults->accept(triggerBit2)) bothTriggers+=1;
	else{
		if (triggerResults->accept(triggerBit1) ) onlyTrigger1+=1;
		if (triggerResults->accept(triggerBit2) ) onlyTrigger2+=1;
		if (!triggerResults->accept(triggerBit1) && !triggerResults->accept(triggerBit2)) noneTriggers+=1;
	}

	totalNumberEvents+=1;
}


// ------------ method called once each job just before starting event loop  ------------
void OverlapTriggers::beginJob() {

	edm::Service< TFileService > fileService;

	const char *labelTrigger1 = trigger1.c_str();
	const char *labelTrigger2 = trigger2.c_str();
	histos1D_[ "overlap" ] = fileService->make< TH1D >( "overlapTriggers", "OverlapTriggers", 4, 0., 4);
    	histos1D_[ "overlap" ]->GetXaxis()->SetBinLabel( 1, labelTrigger1 );
    	histos1D_[ "overlap" ]->GetXaxis()->SetBinLabel( 2, labelTrigger2 );
    	histos1D_[ "overlap" ]->GetXaxis()->SetBinLabel( 3, "Overlap" );
    	histos1D_[ "overlap" ]->GetXaxis()->SetBinLabel( 4, "None" );
    	histos1D_[ "overlap" ]->GetYaxis()->SetTitle( "Percentage" );

}

// ------------ method called once each job just after ending the event loop  ------------
void OverlapTriggers::endJob() {

	std::cout<< onlyTrigger1 << " " << onlyTrigger2 << " " << bothTriggers << " " << noneTriggers << std::endl;
    histos1D_[ "overlap" ]->SetBinContent( 0, onlyTrigger1*100/totalNumberEvents );
    histos1D_[ "overlap" ]->SetBinContent( 1, onlyTrigger2*100/totalNumberEvents );
    histos1D_[ "overlap" ]->SetBinContent( 2, bothTriggers*100/totalNumberEvents );
    histos1D_[ "overlap" ]->SetBinContent( 3, noneTriggers*100/totalNumberEvents );

}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void OverlapTriggers::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
}

//define this as a plug-in
DEFINE_FWK_MODULE(OverlapTriggers);
