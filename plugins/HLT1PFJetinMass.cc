// -*- C++ -*-
//
// Package:    MyTrigger/myTriggerStudies
// Class:      HLT1PFJetinMass
// 
/**\class HLT1PFJetinMass HLT1PFJetinMass.cc MyTrigger/myTriggerStudies/plugins/HLT1PFJetinMass.cc

 Description: HLT Filter. Order Jets in Mass and apply selection.
*/
//
// Original Author:  Alejandro Gomez Espinosa
//         Created:  Thu, 21 Aug 2014 22:34:41 GMT
//
//


// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "HLTrigger/HLTcore/interface/HLTFilter.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "FWCore/Utilities/interface/InputTag.h"

//
// class declaration
//

class HLT1PFJetinMass : public HLTFilter {
   public:
      explicit HLT1PFJetinMass(const edm::ParameterSet&);
      ~HLT1PFJetinMass();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
      virtual bool hltFilter(edm::Event&, const edm::EventSetup&, trigger::TriggerFilterObjectWithRefs & filterproduct) const override;
      static bool compare_JetMass(const reco::PFJet& jet1, const reco::PFJet& jet2){
	      return ( jet1.mass() > jet2.mass() );
      }

   private:
      // ----------member data ---------------------------
      const edm::InputTag                    inputTag_;     // input tag identifying product
      const int    min_N_;                                  // number of objects passing cuts required
      const double min_E_;                                  // energy threshold in GeV
      const double min_Pt_;                                 // pt threshold in GeV
      const double min_Mass_;                               // mass threshold in GeV
      const double max_Eta_;                                // eta range (symmetric)
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
HLT1PFJetinMass::HLT1PFJetinMass(const edm::ParameterSet& iConfig) : HLTFilter(iConfig),
	inputTag_    (iConfig.getParameter<edm::InputTag>("inputTag")),
	min_N_    (iConfig.getParameter<int>          ("MinN"    )),
	min_E_    (iConfig.getParameter<double>       ("MinE"    )),
	min_Pt_   (iConfig.getParameter<double>       ("MinPt"   )),
	min_Mass_ (iConfig.getParameter<double>       ("MinMass" )),
	max_Eta_  (iConfig.getParameter<double>       ("MaxEta"  ))
{
}


HLT1PFJetinMass::~HLT1PFJetinMass()
{
}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
HLT1PFJetinMass::hltFilter(edm::Event& iEvent, const edm::EventSetup& iSetup, trigger::TriggerFilterObjectWithRefs & filterproduct) const
{
	using namespace std;
	using namespace edm;
	using namespace reco;
	using namespace trigger;


	// All HLT filters must create and fill an HLT filter object,
	// recording any reconstructed physics objects satisfying (or not)
	// this HLT filter, and place it in the Event.

	// The filter object
	if (saveTags()) filterproduct.addCollectionTag(inputTag_);


	// Get the input list of basic jets corresponding to the hard jets
	Handle<reco::PFJetCollection> pPFJets;
	iEvent.getByLabel(inputTag_, pPFJets);

	std::vector<reco::PFJet> selectedJets;
	for( reco::PFJetCollection::const_iterator i = pPFJets->begin(); i!=pPFJets->end(); i++) {
		reco::PFJet i_jet = *i;
		selectedJets.push_back(i_jet);
	}
	sort( selectedJets.begin(), selectedJets.end(), compare_JetMass);

	// look at all objects, check cuts and add to filter object
	int n(0);
	for(std::vector<reco::PFJet>::const_iterator j = selectedJets.begin(); j!=selectedJets.end(); j++){
	if ( (j->energy() >= min_E_) &&
			(j->pt() >= min_Pt_) &&
			(j->mass() >= min_Mass_) &&
			( (max_Eta_ < 0.0) || (std::abs(j->eta()) <= max_Eta_) ) ) {
		n++;
		reco::PFJetRef ref = reco::PFJetRef(pPFJets,distance(pPFJets->begin(),j));

		//add ref to event
		filterproduct.addObject(trigger::TriggerJet,ref);
		}
	}
	bool accept(n>=min_N_);

	// filter decision
	return accept;
}

 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HLT1PFJetinMass::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	edm::ParameterSetDescription desc;
	makeHLTFilterDescription(desc);
	desc.add<edm::InputTag>("inputTag",edm::InputTag("hltAntiKT4PFJetsTrim"));
	desc.add<int>("triggerType",trigger::TriggerJet);
	desc.add<double>("MinE",-1.0);
	desc.add<double>("MinPt",-1.0);
	desc.add<double>("MinMass",-1.0);
	desc.add<double>("MaxEta",-1.0);
	desc.add<int>("MinN",1);
	descriptions.add("hlt1PFJetinMass",desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(HLT1PFJetinMass);

