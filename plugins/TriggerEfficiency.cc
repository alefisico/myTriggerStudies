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

	private:
		virtual void beginJob() override;
		virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
		virtual void endJob() override;


		// ----------member data ---------------------------
		std::map< std::string, TH2D* > histos2D_;
		std::map< std::string, TH1D* > histos1D_;

		edm::EDGetTokenT<pat::JetCollection> patJets;
		edm::EDGetTokenT<pat::JetCollection> patJetsGrom;
		std::string triggerPath;
		double minPt;
		double minHT;
		double minMass;

		HLTConfigProvider hltConfig;
		int triggerBit;
};



TriggerEfficiency::TriggerEfficiency(const edm::ParameterSet& iConfig):
	patJets(consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag> ( "patJets" ))),
	patJetsGrom(consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag> ( "patJetsGrom" )))
{
	triggerPath		= iConfig.getParameter<std::string> ( "triggerPath" );   			// Obtain inputs
	minHT			= iConfig.getParameter<double> ( "minHT" );   			// Obtain inputs
	minPt			= iConfig.getParameter<double> ( "minPt" );   			// Obtain inputs
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

	bool changedConfig = false;
	if (!hltConfig.init(iEvent.getRun(), iSetup, "HLT3PB", changedConfig)) {
		cout << "Initialization of HLTConfigProvider failed!!" << endl;
		return;
	}
	if (changedConfig){
		std::cout << "the curent menu is " << hltConfig.tableName() << std::endl;
		triggerBit = -1;
		for (size_t j = 0; j < hltConfig.triggerNames().size(); j++) {
			if (TString(hltConfig.triggerNames()[j]).Contains(triggerPath)) triggerBit = j;
		}
		if (triggerBit == -1) cout << "HLT path not found" << endl;

	}

	//open the trigger summary
	edm::InputTag triggerResultsLabel = edm::InputTag("TriggerResults", "", "HLT3PB");
	edm::Handle<edm::TriggerResults> triggerResults;
	iEvent.getByLabel(triggerResultsLabel, triggerResults);


	edm::Handle<pat::JetCollection> patjets;
	iEvent.getByToken(patJets,patjets);
	edm::Handle<pat::JetCollection> patjetsgrom;
	iEvent.getByToken(patJetsGrom,patjetsgrom);

	TLorentzVector pat1Jet, pat1JetGrom, pat2Jet, pat1JetinMassGrom;
	std::vector<TLorentzVector> vecPatJetsGrom;
	double patHT = 0;
	double patSumMass = 0;
	int npatJets =0;
	int npatJetsGrom =0;
	//int npatJets2 =0;
	//bool deltaEta = 0;
	//bool dijetMass;
	for(const pat::Jet &ijet : *patjets ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		patHT += ijet.pt();
		if ( (npatJets++) == 1 ) pat1Jet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
	}

	for(const pat::Jet &ijet : *patjetsgrom ){
		if ( ijet.pt() < minPt || abs( ijet.eta() ) > 2.4 ) continue;
		patSumMass += ijet.mass();
		TLorentzVector tmpJet;
		tmpJet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
		vecPatJetsGrom.push_back( tmpJet );
		if ( (npatJetsGrom++) == 1 ) pat1JetGrom.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
		/*if ( (npatJets2++) == 2 ) {
			pat2Jet.SetPtEtaPhiE( ijet.pt(), ijet.eta(), ijet.phi(), ijet.energy() );
			//deltaEta = abs( pat1JetGrom.Eta() - pat2Jet.Eta()  ) < 1.3;
			//TLorentzVector tmpVector = pat1JetGrom + pat2Jet;
			//dijetMass = tmpVector.M() > 890;
		}*/
	}
	if ( vecPatJetsGrom.size() > 0 ){
		sort(vecPatJetsGrom.begin(), vecPatJetsGrom.end(), [](const TLorentzVector &p1, const TLorentzVector &p2) { return p1.M() > p2.M(); }); // the joys of C++11
		pat1JetinMassGrom = vecPatJetsGrom[0];
	}
	//edm::LogWarning("test")<< patHT << " " << pat1Jet.Eta() << " " << pat2Jet.Eta() << " " << deltaEta << " " << dijetMass ;

	if( ( patHT > minHT ) && ( pat1JetGrom.M() > minMass ) ) {

		histos1D_[ "HTDenom" ]->Fill( patHT );
		histos1D_[ "jetMassDenom" ]->Fill( pat1JetGrom.M() );
		histos1D_[ "ptDenom" ]->Fill( pat1Jet.Pt() );
		histos2D_[ "jetMassHTDenom" ]->Fill(  pat1JetGrom.M(), patHT );
		histos2D_[ "jetMassPtDenom" ]->Fill( pat1JetGrom.M(), pat1Jet.Pt() );
		histos1D_[ "jetMassInMassDenom" ]->Fill( pat1JetinMassGrom.M() );
		histos1D_[ "jetPtInMassDenom" ]->Fill( pat1JetinMassGrom.Pt() );
		histos2D_[ "jetMassInMassHTDenom" ]->Fill(  pat1JetinMassGrom.M(), patHT );
		histos2D_[ "jetMassPtInMassDenom" ]->Fill( pat1JetinMassGrom.M(), pat1JetinMassGrom.Pt() );


		if (triggerResults->accept(triggerBit)){
			histos1D_[ "HTPassing" ]->Fill( patHT );
			histos1D_[ "jetMassPassing" ]->Fill( pat1JetGrom.M() );
			histos1D_[ "ptPassing" ]->Fill( pat1Jet.Pt() );
			histos2D_[ "jetMassHTPassing" ]->Fill(  pat1JetGrom.M(), patHT );
			histos2D_[ "jetMassPtPassing" ]->Fill( pat1JetGrom.M(), pat1Jet.Pt() );
			histos1D_[ "jetMassInMassPassing" ]->Fill( pat1JetinMassGrom.M() );
			histos1D_[ "jetPtInMassPassing" ]->Fill( pat1JetinMassGrom.Pt() );
			histos2D_[ "jetMassInMassHTPassing" ]->Fill(  pat1JetinMassGrom.M(), patHT );
			histos2D_[ "jetMassPtInMassPassing" ]->Fill( pat1JetinMassGrom.M(), pat1JetinMassGrom.Pt() );
		}
	}
}


// ------------ method called once each job just before starting event loop  ------------
void TriggerEfficiency::beginJob() {

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

	histos2D_[ "jetMassInMassHTDenom" ] = fileService->make< TH2D >( "jetMassInMassHTDenom", "HT vs Leading Jet Mass", 16, 0., 400. , 20, 0., 2000);
	histos2D_[ "jetMassInMassHTDenom" ]->SetYTitle( "HT [GeV]" );
	histos2D_[ "jetMassInMassHTDenom" ]->SetXTitle( "Leading Jet Trimmed Mass [GeV]" );

	histos2D_[ "jetMassInMassHTPassing" ] = fileService->make< TH2D >( "jetMassInMassHTPassing", "HT vs Leading Jet Mass passing path", 16, 0., 400. , 20, 0., 2000);
	histos2D_[ "jetMassInMassHTPassing" ]->SetYTitle( "HT [GeV]" );
	histos2D_[ "jetMassInMassHTPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassInMassHT2Defficiency" ] = fileService->make< TH2D >( "jetMassInMassHT2Defficiency", "Comparative efficiency", 16, 0., 400. , 20, 0., 2000);
	histos2D_[ "jetMassInMassHT2Defficiency" ]->SetYTitle( "HT [GeV]" );
	histos2D_[ "jetMassInMassHT2Defficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassPtInMassDenom" ] = fileService->make< TH2D >( "jetMassPtInMassDenom", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
	histos2D_[ "jetMassPtInMassDenom" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "jetMassPtInMassDenom" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassPtInMassPassing" ] = fileService->make< TH2D >( "jetMassPtInMassPassing", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
	histos2D_[ "jetMassPtInMassPassing" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "jetMassPtInMassPassing" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos2D_[ "jetMassPtInMass2Defficiency" ] = fileService->make< TH2D >( "jetMassPtInMass2Defficiency", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
	histos2D_[ "jetMassPtInMass2Defficiency" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos2D_[ "jetMassPtInMass2Defficiency" ]->SetYTitle( "Leading Jet Mass [GeV]" );

	histos1D_[ "jetMassDenom" ] = fileService->make< TH1D >( "jetMassDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "jetMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassDenom" ]->Sumw2();

	histos1D_[ "jetMassPassing" ] = fileService->make< TH1D >( "jetMassPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "jetMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassPassing" ]->Sumw2();

	histos1D_[ "jetMassEfficiency" ] = fileService->make< TH1D >( "jetMassEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "jetMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassEfficiency" ]->SetYTitle( "Efficiency" );

	histos1D_[ "jetMassInMassDenom" ] = fileService->make< TH1D >( "jetMassInMassDenom", "Jet mass", 20, 0., 400);
	histos1D_[ "jetMassInMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassInMassDenom" ]->Sumw2();

	histos1D_[ "jetMassInMassPassing" ] = fileService->make< TH1D >( "jetMassInMassPassing", "Jet mass passing", 20, 0., 400);
	histos1D_[ "jetMassInMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassInMassPassing" ]->Sumw2();

	histos1D_[ "jetMassInMassEfficiency" ] = fileService->make< TH1D >( "jetMassInMassEfficiency", "Leading jet mass efficiency", 20, 0., 400);
	histos1D_[ "jetMassInMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
	histos1D_[ "jetMassInMassEfficiency" ]->SetYTitle( "Efficiency" );

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

	histos1D_[ "jetPtInMassDenom" ] = fileService->make< TH1D >( "jetPtInMassDenom", "jetPtInMass", 100, 0., 1000);
	histos1D_[ "jetPtInMassDenom" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos1D_[ "jetPtInMassDenom" ]->Sumw2();

	histos1D_[ "jetPtInMassPassing" ] = fileService->make< TH1D >( "jetPtInMassPassing", "Leading Jet Pt passing", 100, 0., 1000);
	histos1D_[ "jetPtInMassPassing" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos1D_[ "jetPtInMassPassing" ]->Sumw2();

	histos1D_[ "jetPtInMassEfficiency" ] = fileService->make< TH1D >( "jetPtInMassEfficiency", "Leading Jet Pt efficiency", 100, 0., 1000);
	histos1D_[ "jetPtInMassEfficiency" ]->SetXTitle( "Leading Jet Pt [GeV]" );
	histos1D_[ "jetPtInMassEfficiency" ]->SetYTitle( "Efficiency" );
}

// ------------ method called once each job just after ending the event loop  ------------
void TriggerEfficiency::endJob() {

    histos2D_[ "jetMassHT2Defficiency" ]->Sumw2();
    histos2D_[ "jetMassHT2Defficiency" ]->Divide(histos2D_[ "jetMassHTPassing" ],histos2D_[ "jetMassHTDenom" ],1,1,"B");
    
    histos2D_[ "jetMassInMassHT2Defficiency" ]->Sumw2();
    histos2D_[ "jetMassInMassHT2Defficiency" ]->Divide(histos2D_[ "jetMassInMassHTPassing" ],histos2D_[ "jetMassInMassHTDenom" ],1,1,"B");
    
    histos2D_[ "jetMassPt2Defficiency" ]->Sumw2();
    histos2D_[ "jetMassPt2Defficiency" ]->Divide(histos2D_[ "jetMassPtPassing" ],histos2D_[ "jetMassPtDenom" ],1,1,"B");
    
    histos1D_[ "jetMassInMassEfficiency" ]->Sumw2();
    histos1D_[ "jetMassInMassEfficiency" ]->Divide(histos1D_[ "jetMassInMassPassing" ], histos1D_[ "jetMassInMassDenom" ], 1,1,"B");

    histos1D_[ "jetMassEfficiency" ]->Sumw2();
    histos1D_[ "jetMassEfficiency" ]->Divide(histos1D_[ "jetMassPassing" ], histos1D_[ "jetMassDenom" ], 1,1,"B");

    histos1D_[ "HTEfficiency" ]->Sumw2();
    histos1D_[ "HTEfficiency" ]->Divide(histos1D_[ "HTPassing" ], histos1D_[ "HTDenom" ], 1,1,"B");

    histos1D_[ "ptEfficiency" ]->Sumw2();
    histos1D_[ "ptEfficiency" ]->Divide(histos1D_[ "ptPassing" ], histos1D_[ "ptDenom" ], 1,1,"B");

    histos1D_[ "jetPtInMassEfficiency" ]->Sumw2();
    histos1D_[ "jetPtInMassEfficiency" ]->Divide(histos1D_[ "jetPtInMassPassing" ], histos1D_[ "jetPtInMassDenom" ], 1,1,"B");


}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void TriggerEfficiency::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	desc.add<double>("MinHT", 0.0);
	desc.add<double>("MinPt", 40.0);
	desc.add<double>("MinMass", 0.0);
	descriptions.add("TriggerEfficiency",desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerEfficiency);
