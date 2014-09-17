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

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METFwd.h"

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
		std::string trigger3;
		edm::InputTag oneHLTPFJets;
		edm::InputTag twoHLTPFJets;
		edm::InputTag threeHLTPFJets;
		edm::InputTag oneHLTHT;
		edm::InputTag twoHLTHT;
		edm::InputTag threeHLTHT;

		HLTConfigProvider hltConfig;
		int triggerBit1;
		int triggerBit2;
		int triggerBit3;

		int onlyTrigger1 = 0;
		int onlyTrigger2 = 0;
		int onlyTrigger3 = 0;
		int threeTriggers = 0;
		int bothTriggers = 0;
		int noneTriggers = 0;
		int only1 = 0;
		int only2 = 0;
		int only3 = 0;
		int only12 = 0;
		int only13 = 0;
		int only23 = 0;
		double totalNumberEvents = 0;
		double totalNumberEventsPassing = 0;
		double totalNumberEventsPassingThree = 0;

};



OverlapTriggers::OverlapTriggers(const edm::ParameterSet& iConfig){
	trigger1		= iConfig.getParameter<std::string> ( "trigger1" );   			// Obtain inputs
	trigger2		= iConfig.getParameter<std::string> ( "trigger2" );   			// Obtain inputs
	trigger3		= iConfig.getParameter<std::string> ( "trigger3" );   			// Obtain inputs
	oneHLTPFJets		= iConfig.getParameter<edm::InputTag> ( "oneHLTPFJets" );   			// Obtain inputs
	twoHLTPFJets		= iConfig.getParameter<edm::InputTag> ( "twoHLTPFJets" );   			// Obtain inputs
	threeHLTPFJets		= iConfig.getParameter<edm::InputTag> ( "threeHLTPFJets" );   			// Obtain inputs
	oneHLTHT		= iConfig.getParameter<edm::InputTag> ( "oneHLTHT" );   			// Obtain inputs
	twoHLTHT		= iConfig.getParameter<edm::InputTag> ( "twoHLTHT" );   			// Obtain inputs
	threeHLTHT		= iConfig.getParameter<edm::InputTag> ( "threeHLTHT" );   			// Obtain inputs
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
		triggerBit3 = -1;
		for (size_t j = 0; j < hltConfig.triggerNames().size(); j++) {
			//std::cout << TString(hltConfig.triggerNames()[j]) << std::endl;
			if (TString(hltConfig.triggerNames()[j]).Contains(trigger1)) triggerBit1 = j;
			if (TString(hltConfig.triggerNames()[j]).Contains(trigger2)) triggerBit2 = j;
			if (TString(hltConfig.triggerNames()[j]).Contains(trigger3)) triggerBit3 = j;
		}
		if (triggerBit1 == -1) cout << "HLT path not found" << endl;
		if (triggerBit2 == -1) cout << "HLT path not found" << endl;
		if (triggerBit3 == -1) cout << "HLT path not found" << endl;

	}

	//open the trigger summary
	edm::InputTag triggerResultsLabel = edm::InputTag("TriggerResults", "", "HLT3PB");
	edm::Handle<edm::TriggerResults> triggerResults;
	iEvent.getByLabel(triggerResultsLabel, triggerResults);

	edm::Handle<reco::METCollection> oneHLTPFHT;
	iEvent.getByLabel(oneHLTHT, oneHLTPFHT);
	double oneHT = 0;
	if (oneHLTPFHT->size() > 0) oneHT = oneHLTPFHT->front().sumEt();

	edm::Handle<reco::METCollection> twoHLTPFHT;
	iEvent.getByLabel(twoHLTHT, twoHLTPFHT);
	double twoHT = 0;
	if (twoHLTPFHT->size() > 0) twoHT = twoHLTPFHT->front().sumEt();

	/*edm::Handle<reco::METCollection> threeHLTPFHT;
	iEvent.getByLabel(threeHLTHT, threeHLTPFHT);
	double threeHT = 0;
	if (threeHLTPFHT->size() > 0) threeHT = threeHLTPFHT->front().sumEt();*/

  	edm::Handle<edm::View<reco::Jet> > onePFJets;
	iEvent.getByLabel(oneHLTPFJets, onePFJets);
  	std::vector< TLorentzVector > oneJets;

  	edm::Handle<edm::View<reco::Jet> > twoPFJets;
	iEvent.getByLabel(twoHLTPFJets, twoPFJets);
  	std::vector< TLorentzVector > twoJets;

  	/*edm::Handle<edm::View<reco::Jet> > threePFJets;
	iEvent.getByLabel(threeHLTPFJets, threePFJets);
  	std::vector< TLorentzVector > threeJets;*/

    	for(edm::View<reco::Jet>::const_iterator ijet=onePFJets->begin(); ijet!=onePFJets->end();ijet++){
		if ( ijet->pt() < 40.0 || abs( ijet->eta() ) > 3.0 ) continue;
    		oneJets.push_back( TLorentzVector( ijet->px(), ijet->py(), ijet->pz(), ijet->energy() ) );
	} 

    	for(edm::View<reco::Jet>::const_iterator ijet=twoPFJets->begin(); ijet!=twoPFJets->end();ijet++){
		if ( ijet->pt() < 40.0 || abs( ijet->eta() ) > 3.0 ) continue;
    		twoJets.push_back( TLorentzVector( ijet->px(), ijet->py(), ijet->pz(), ijet->energy() ) );
	} 

	sort( oneJets.begin(), oneJets.end(), compare_JetMass);
	sort( twoJets.begin(), twoJets.end(), compare_JetMass);

	if ( oneJets.size() > 0 ){
		histos1D_[ "MassOneAll" ]->Fill( oneJets[0].M() );
		histos1D_[ "PtOneAll" ]->Fill( oneJets[0].Pt() );
		histos1D_[ "HTOneAll" ]->Fill( oneHT );
		histos2D_[ "HTvsMassOneAll" ]->Fill( oneHT, oneJets[0].M() );
		histos2D_[ "HTvsPtOneAll" ]->Fill( oneHT, oneJets[0].Pt() );
		histos2D_[ "PtvsMassOneAll" ]->Fill( oneJets[0].Pt(), oneJets[0].M() );
		histos2D_[ "AK4vsAK8HTOneAll" ]->Fill( oneHT, twoHT );
	}
	
	if ( twoJets.size() > 0 ){
		histos1D_[ "MassTwoAll" ]->Fill( twoJets[0].M() );
		histos1D_[ "PtTwoAll" ]->Fill( twoJets[0].Pt() );
		histos1D_[ "HTTwoAll" ]->Fill( twoHT );
		histos2D_[ "HTvsMassTwoAll" ]->Fill( twoHT, twoJets[0].M() );
		histos2D_[ "HTvsPtTwoAll" ]->Fill( twoHT, twoJets[0].Pt() );
		histos2D_[ "PtvsMassTwoAll" ]->Fill( twoJets[0].Pt(), twoJets[0].M() );
	}
	
	if (triggerResults->accept(triggerBit1) || triggerResults->accept(triggerBit2)){
		totalNumberEventsPassing+=1;

		if (triggerResults->accept(triggerBit1) && triggerResults->accept(triggerBit2)){
	       		bothTriggers+=1;
			histos1D_[ "MassBoth" ]->Fill( oneJets[0].M() );
			histos1D_[ "PtBoth" ]->Fill( oneJets[0].Pt() );
			histos1D_[ "HTBoth" ]->Fill( oneHT );
			histos2D_[ "HTvsMassBoth" ]->Fill( oneHT, oneJets[0].M() );
			histos2D_[ "HTvsPtBoth" ]->Fill( oneHT, oneJets[0].Pt() );
			histos2D_[ "PtvsMassBoth" ]->Fill( oneJets[0].Pt(), oneJets[0].M() );
		} else {
			if (triggerResults->accept(triggerBit1) ){
		       		onlyTrigger1+=1;
				histos1D_[ "MassOne" ]->Fill( oneJets[0].M() );
				histos1D_[ "PtOne" ]->Fill( oneJets[0].Pt() );
				histos1D_[ "HTOne" ]->Fill( oneHT );
				histos2D_[ "HTvsMassOne" ]->Fill( oneHT, oneJets[0].M() );
				histos2D_[ "HTvsPtOne" ]->Fill( oneHT, oneJets[0].Pt() );
				histos2D_[ "PtvsMassOne" ]->Fill( oneJets[0].Pt(), oneJets[0].M() );

			} else {
		       		onlyTrigger2+=1;
				histos1D_[ "MassTwo" ]->Fill( twoJets[0].M() );
				histos1D_[ "PtTwo" ]->Fill( twoJets[0].Pt() );
				histos1D_[ "HTTwo" ]->Fill( twoHT );
				histos2D_[ "HTvsMassTwo" ]->Fill( twoHT, twoJets[0].M() );
				histos2D_[ "HTvsPtTwo" ]->Fill( twoHT, twoJets[0].Pt() );
				histos2D_[ "PtvsMassTwo" ]->Fill( twoJets[0].Pt(), twoJets[0].M() );
			}
		}
	
	} else {
	       	noneTriggers+=1;
	}

	totalNumberEvents+=1;

	if (triggerResults->accept(triggerBit1) || triggerResults->accept(triggerBit2) || triggerResults->accept(triggerBit3)){
		totalNumberEventsPassingThree+=1;

		if (triggerResults->accept(triggerBit1) && triggerResults->accept(triggerBit2) && triggerResults->accept(triggerBit3)) threeTriggers+=1;
		if (triggerResults->accept(triggerBit1) && triggerResults->accept(triggerBit2) && !triggerResults->accept(triggerBit3)) only12+=1;
		if (triggerResults->accept(triggerBit1) && !triggerResults->accept(triggerBit2) && triggerResults->accept(triggerBit3)) only13+=1;
		if (!triggerResults->accept(triggerBit1) && triggerResults->accept(triggerBit2) && triggerResults->accept(triggerBit3)) only23+=1;
		if (triggerResults->accept(triggerBit1) && !triggerResults->accept(triggerBit2) && !triggerResults->accept(triggerBit3)) only1+=1;
		if (!triggerResults->accept(triggerBit1) && triggerResults->accept(triggerBit2) && !triggerResults->accept(triggerBit3)) only2+=1;
		if (!triggerResults->accept(triggerBit1) && !triggerResults->accept(triggerBit2) && triggerResults->accept(triggerBit3)) only3+=1;
		
	}
}


// ------------ method called once each job just before starting event loop  ------------
void OverlapTriggers::beginJob() {

	edm::Service< TFileService > fileService;

	const char *labelTrigger1 = trigger1.c_str();
	const char *labelTrigger2 = trigger2.c_str();
	const char *labelTrigger3 = trigger3.c_str();
	histos1D_[ "overlapOverAll" ] = fileService->make< TH1D >( "overlapOverAllTriggers", "OverlapTriggers", 4, 0., 4);
    	histos1D_[ "overlapOverAll" ]->GetXaxis()->SetBinLabel( 1, labelTrigger1 );
    	histos1D_[ "overlapOverAll" ]->GetXaxis()->SetBinLabel( 2, labelTrigger2 );
    	histos1D_[ "overlapOverAll" ]->GetXaxis()->SetBinLabel( 3, "Overlap" );
    	histos1D_[ "overlapOverAll" ]->GetXaxis()->SetBinLabel( 4, "None" );
    	histos1D_[ "overlapOverAll" ]->GetYaxis()->SetTitle( "Percentage" );

	histos1D_[ "overlapOverAllSimple" ] = fileService->make< TH1D >( "overlapOverAllSimpleTriggers", "OverlapTriggers", 4, 0., 4);
    	histos1D_[ "overlapOverAllSimple" ]->GetXaxis()->SetBinLabel( 1, labelTrigger1 );
    	histos1D_[ "overlapOverAllSimple" ]->GetXaxis()->SetBinLabel( 2, labelTrigger2 );
    	histos1D_[ "overlapOverAllSimple" ]->GetXaxis()->SetBinLabel( 3, "Overlap" );
    	histos1D_[ "overlapOverAllSimple" ]->GetXaxis()->SetBinLabel( 4, "None" );

	histos1D_[ "overlap" ] = fileService->make< TH1D >( "overlapTriggers", "OverlapTriggers", 3, 0., 3);
    	histos1D_[ "overlap" ]->GetXaxis()->SetBinLabel( 1, labelTrigger1 );
    	histos1D_[ "overlap" ]->GetXaxis()->SetBinLabel( 2, labelTrigger2 );
    	histos1D_[ "overlap" ]->GetXaxis()->SetBinLabel( 3, "Overlap" );
    	histos1D_[ "overlap" ]->GetYaxis()->SetTitle( "Percentage" );

	histos1D_[ "overlapSimple" ] = fileService->make< TH1D >( "overlapSimpleTriggers", "OverlapTriggers", 3, 0., 3);
    	histos1D_[ "overlapSimple" ]->GetXaxis()->SetBinLabel( 1, labelTrigger1 );
    	histos1D_[ "overlapSimple" ]->GetXaxis()->SetBinLabel( 2, labelTrigger2 );
    	histos1D_[ "overlapSimple" ]->GetXaxis()->SetBinLabel( 3, "Overlap" );

	histos2D_[ "overlapThree" ] = fileService->make< TH2D >( "overlapThreeTriggers", "OverlapTriggers", 4, 0., 4, 4, 0., 4. );
    	histos2D_[ "overlapThree" ]->GetXaxis()->SetBinLabel( 1, labelTrigger1 );
    	histos2D_[ "overlapThree" ]->GetXaxis()->SetBinLabel( 2, labelTrigger2 );
    	histos2D_[ "overlapThree" ]->GetXaxis()->SetBinLabel( 3, labelTrigger3 );
    	histos2D_[ "overlapThree" ]->GetXaxis()->SetBinLabel( 4, "Overlap" );
    	histos2D_[ "overlapThree" ]->GetYaxis()->SetBinLabel( 1, labelTrigger1 );
    	histos2D_[ "overlapThree" ]->GetYaxis()->SetBinLabel( 2, labelTrigger2 );
    	histos2D_[ "overlapThree" ]->GetYaxis()->SetBinLabel( 3, labelTrigger3 );
    	histos2D_[ "overlapThree" ]->GetYaxis()->SetBinLabel( 4, "Overlap" );

	histos2D_[ "overlapThreeSimple" ] = fileService->make< TH2D >( "overlapThreeSimpleTriggers", "OverlapTriggers", 4, 0., 4, 4, 0., 4. );
    	histos2D_[ "overlapThreeSimple" ]->GetXaxis()->SetBinLabel( 1, labelTrigger1 );
    	histos2D_[ "overlapThreeSimple" ]->GetXaxis()->SetBinLabel( 2, labelTrigger2 );
    	histos2D_[ "overlapThreeSimple" ]->GetXaxis()->SetBinLabel( 3, labelTrigger3 );
    	histos2D_[ "overlapThreeSimple" ]->GetXaxis()->SetBinLabel( 4, "Overlap" );
    	histos2D_[ "overlapThreeSimple" ]->GetYaxis()->SetBinLabel( 1, labelTrigger1 );
    	histos2D_[ "overlapThreeSimple" ]->GetYaxis()->SetBinLabel( 2, labelTrigger2 );
    	histos2D_[ "overlapThreeSimple" ]->GetYaxis()->SetBinLabel( 3, labelTrigger3 );
    	histos2D_[ "overlapThreeSimple" ]->GetYaxis()->SetBinLabel( 4, "Overlap" );

	histos1D_[ "MassOneAll" ] = fileService->make< TH1D >( "MassOneAll", labelTrigger1, 40, 0., 400. );
	histos1D_[ "MassOneAll" ]->SetXTitle( "Leading Jet Mass [GeV]" );

	histos1D_[ "MassTwoAll" ] = fileService->make< TH1D >( "MassTwoAll", labelTrigger2, 40, 0., 400. );
	histos1D_[ "MassTwoAll" ]->SetXTitle( "Leading Jet Mass [GeV]" );

	histos1D_[ "MassOne" ] = fileService->make< TH1D >( "MassOne", labelTrigger1, 40, 0., 400. );
	histos1D_[ "MassOne" ]->SetXTitle( "Leading Jet Mass [GeV]" );

	histos1D_[ "MassTwo" ] = fileService->make< TH1D >( "MassTwo", labelTrigger2, 40, 0., 400. );
	histos1D_[ "MassTwo" ]->SetXTitle( "Leading Jet Mass [GeV]" );

	histos1D_[ "MassBoth" ] = fileService->make< TH1D >( "MassBoth", labelTrigger1, 40, 0., 400. );
	histos1D_[ "MassBoth" ]->SetXTitle( "Leading Jet Mass [GeV]" );

	histos1D_[ "PtOneAll" ] = fileService->make< TH1D >( "PtOneAll", labelTrigger1, 50, 0., 1000. );
	histos1D_[ "PtOneAll" ]->SetXTitle( "Leading Jet Pt [GeV]" );

	histos1D_[ "PtTwoAll" ] = fileService->make< TH1D >( "PtTwoAll", labelTrigger2, 50, 0., 1000. );
	histos1D_[ "PtTwoAll" ]->SetXTitle( "Leading Jet Pt [GeV]" );

	histos1D_[ "PtOne" ] = fileService->make< TH1D >( "PtOne", labelTrigger1, 50, 0., 1000. );
	histos1D_[ "PtOne" ]->SetXTitle( "Leading Jet Pt [GeV]" );

	histos1D_[ "PtTwo" ] = fileService->make< TH1D >( "PtTwo", labelTrigger2, 50, 0., 1000. );
	histos1D_[ "PtTwo" ]->SetXTitle( "Leading Jet Pt [GeV]" );

	histos1D_[ "PtBoth" ] = fileService->make< TH1D >( "PtBoth", labelTrigger1, 50, 0., 1000. );
	histos1D_[ "PtBoth" ]->SetXTitle( "Leading Jet Pt [GeV]" );

	histos1D_[ "HTOneAll" ] = fileService->make< TH1D >( "HTOneAll", labelTrigger1, 100, 0., 2000. );
	histos1D_[ "HTOneAll" ]->SetXTitle( "Leading Jet HT [GeV]" );

	histos1D_[ "HTTwoAll" ] = fileService->make< TH1D >( "HTTwoAll", labelTrigger2, 100, 0., 2000. );
	histos1D_[ "HTTwoAll" ]->SetXTitle( "Leading Jet HT [GeV]" );

	histos1D_[ "HTOne" ] = fileService->make< TH1D >( "HTOne", labelTrigger1, 100, 0., 2000. );
	histos1D_[ "HTOne" ]->SetXTitle( "Leading Jet HT [GeV]" );

	histos1D_[ "HTTwo" ] = fileService->make< TH1D >( "HTTwo", labelTrigger2, 100, 0., 2000. );
	histos1D_[ "HTTwo" ]->SetXTitle( "Leading Jet HT [GeV]" );

	histos1D_[ "HTBoth" ] = fileService->make< TH1D >( "HTBoth", labelTrigger1, 100, 0., 2000. );
	histos1D_[ "HTBoth" ]->SetXTitle( "Leading Jet HT [GeV]" );

	histos2D_[ "HTvsMassOneAll" ] = fileService->make< TH2D >( "HTvsMassOneAll", labelTrigger1, 100, 0., 2000, 20, 0., 400. );
	histos2D_[ "HTvsMassOneAll" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsMassOneAll" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "HTvsMassTwoAll" ] = fileService->make< TH2D >( "HTvsMassTwoAll", labelTrigger2, 100, 0., 2000, 20, 0., 400. );
	histos2D_[ "HTvsMassTwoAll" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsMassTwoAll" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "HTvsMassOne" ] = fileService->make< TH2D >( "HTvsMassOne", labelTrigger1, 100, 0., 2000, 20, 0., 400. );
	histos2D_[ "HTvsMassOne" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsMassOne" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "HTvsMassTwo" ] = fileService->make< TH2D >( "HTvsMassTwo", labelTrigger2, 100, 0., 2000, 20, 0., 400. );
	histos2D_[ "HTvsMassTwo" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsMassTwo" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "HTvsMassBoth" ] = fileService->make< TH2D >( "HTvsMassBoth", "Both Triggers", 100, 0., 2000, 20, 0., 400. );
	histos2D_[ "HTvsMassBoth" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsMassBoth" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "HTvsPtOneAll" ] = fileService->make< TH2D >( "HTvsPtOneAll", labelTrigger1, 100, 0., 2000, 50, 0., 1000. );
	histos2D_[ "HTvsPtOneAll" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsPtOneAll" ]->SetYTitle( "Leading Jet Pt [GeV]" );

	histos2D_[ "HTvsPtTwoAll" ] = fileService->make< TH2D >( "HTvsPtTwoAll", labelTrigger2, 100, 0., 2000, 50, 0., 1000. );
	histos2D_[ "HTvsPtTwoAll" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsPtTwoAll" ]->SetYTitle( "Leading Jet Pt [GeV]" );

	histos2D_[ "HTvsPtOne" ] = fileService->make< TH2D >( "HTvsPtOne", labelTrigger1, 100, 0., 2000, 50, 0., 1000. );
	histos2D_[ "HTvsPtOne" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsPtOne" ]->SetYTitle( "Leading Jet Pt [GeV]" );

	histos2D_[ "HTvsPtTwo" ] = fileService->make< TH2D >( "HTvsPtTwo", labelTrigger2, 100, 0., 2000, 50, 0., 1000. );
	histos2D_[ "HTvsPtTwo" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsPtTwo" ]->SetYTitle( "Leading Jet Pt [GeV]" );

	histos2D_[ "HTvsPtBoth" ] = fileService->make< TH2D >( "HTvsPtBoth", "Both", 100, 0., 2000, 50, 0., 1000. );
	histos2D_[ "HTvsPtBoth" ]->SetXTitle( "HT [GeV]" );
	histos2D_[ "HTvsPtBoth" ]->SetYTitle( "Leading Jet Pt [GeV]" );

	histos2D_[ "PtvsMassOneAll" ] = fileService->make< TH2D >( "PtvsMassOneAll", labelTrigger1, 50, 0., 1000, 20, 0., 400. );
	histos2D_[ "PtvsMassOneAll" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "PtvsMassOneAll" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "PtvsMassTwoAll" ] = fileService->make< TH2D >( "PtvsMassTwoAll", labelTrigger2, 50, 0., 1000, 20, 0., 400. );
	histos2D_[ "PtvsMassTwoAll" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "PtvsMassTwoAll" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "PtvsMassOne" ] = fileService->make< TH2D >( "PtvsMassOne", labelTrigger1, 50, 0., 1000, 20, 0., 400. );
	histos2D_[ "PtvsMassOne" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "PtvsMassOne" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "PtvsMassTwo" ] = fileService->make< TH2D >( "PtvsMassTwo", labelTrigger2, 50, 0., 1000, 20, 0., 400. );
	histos2D_[ "PtvsMassTwo" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "PtvsMassTwo" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "PtvsMassBoth" ] = fileService->make< TH2D >( "PtvsMassBoth", "both", 50, 0., 1000, 20, 0., 400. );
	histos2D_[ "PtvsMassBoth" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "PtvsMassBoth" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "AK4vsAK8HTOneAll" ] = fileService->make< TH2D >( "AK4vsAK8HTOneAll", labelTrigger1, 100, 0., 2000, 100, 0., 2000. );
	histos2D_[ "AK4vsAK8HTOneAll" ]->SetXTitle( "AK4HT [GeV]" );
	histos2D_[ "AK4vsAK8HTOneAll" ]->SetYTitle( "AK8HT [GeV]" );

}

// ------------ method called once each job just after ending the event loop  ------------
void OverlapTriggers::endJob() {

	std::cout<< onlyTrigger1 << " " << onlyTrigger2 << " " << bothTriggers << " " << noneTriggers << std::endl;
    histos1D_[ "overlapOverAll" ]->SetBinContent( 1, onlyTrigger1/totalNumberEvents );
    histos1D_[ "overlapOverAll" ]->SetBinContent( 2, onlyTrigger2/totalNumberEvents );
    histos1D_[ "overlapOverAll" ]->SetBinContent( 3, bothTriggers/totalNumberEvents );
    histos1D_[ "overlapOverAll" ]->SetBinContent( 4, noneTriggers/totalNumberEvents );

    histos1D_[ "overlap" ]->SetBinContent( 1, onlyTrigger1/totalNumberEventsPassing );
    histos1D_[ "overlap" ]->SetBinContent( 2, onlyTrigger2/totalNumberEventsPassing );
    histos1D_[ "overlap" ]->SetBinContent( 3, bothTriggers/totalNumberEventsPassing );

    histos1D_[ "overlapOverAllSimple" ]->SetBinContent( 1, onlyTrigger1 );
    histos1D_[ "overlapOverAllSimple" ]->SetBinContent( 2, onlyTrigger2 );
    histos1D_[ "overlapOverAllSimple" ]->SetBinContent( 3, bothTriggers );
    histos1D_[ "overlapOverAllSimple" ]->SetBinContent( 4, noneTriggers );

    histos1D_[ "overlapSimple" ]->SetBinContent( 1, onlyTrigger1 );
    histos1D_[ "overlapSimple" ]->SetBinContent( 2, onlyTrigger2 );
    histos1D_[ "overlapSimple" ]->SetBinContent( 3, bothTriggers );

    histos2D_[ "overlapThree" ]->SetBinContent( 1, 1, only1/totalNumberEventsPassingThree );
    histos2D_[ "overlapThree" ]->SetBinContent( 2, 2, only2/totalNumberEventsPassingThree );
    histos2D_[ "overlapThree" ]->SetBinContent( 3, 3, only3/totalNumberEventsPassingThree );
    histos2D_[ "overlapThree" ]->SetBinContent( 1, 2, only12/totalNumberEventsPassingThree );
    histos2D_[ "overlapThree" ]->SetBinContent( 1, 3, only13/totalNumberEventsPassingThree );
    histos2D_[ "overlapThree" ]->SetBinContent( 2, 3, only23/totalNumberEventsPassingThree );
    histos2D_[ "overlapThree" ]->SetBinContent( 4, 4, threeTriggers/totalNumberEventsPassingThree );

    histos2D_[ "overlapThreeSimple" ]->SetBinContent( 1, 1, only1);
    histos2D_[ "overlapThreeSimple" ]->SetBinContent( 2, 2, only2);
    histos2D_[ "overlapThreeSimple" ]->SetBinContent( 3, 3, only3);
    histos2D_[ "overlapThreeSimple" ]->SetBinContent( 1, 2, only12);
    histos2D_[ "overlapThreeSimple" ]->SetBinContent( 1, 3, only13);
    histos2D_[ "overlapThreeSimple" ]->SetBinContent( 2, 3, only23);
    histos2D_[ "overlapThreeSimple" ]->SetBinContent( 4, 4, threeTriggers);

}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void OverlapTriggers::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
}

//define this as a plug-in
DEFINE_FWK_MODULE(OverlapTriggers);
