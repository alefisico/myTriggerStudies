#ifndef HLTHtJetMassProducer_h_
#define HLTHtJetMassProducer_h_

/** \class HLTHtJetMassProducer
 *
 *  \brief  This produces a reco::MET object that stores HT and Leading Jet Information
 *  \author Alejandro Gomez
 *
 *  HT are calculated using input CaloJet or PFJet collection.
 *  HT is stored as `sumet_`, Leading Jet Info is stored as `p4_` in the output.
 *
 */

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/View.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METFwd.h"


// Class declaration
class HLTHtJetMassProducer : public edm::EDProducer {
  public:
    explicit HLTHtJetMassProducer(const edm::ParameterSet & iConfig);
    ~HLTHtJetMassProducer();
    static void fillDescriptions(edm::ConfigurationDescriptions & descriptions);
    virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup);

  private:
    /// Use pt; otherwise, use et.
    bool usePt_;

    /// Minimum number of jets passing pt and eta requirements
    int minNJetHt_;

    /// Minimum pt requirement for jets
    double minPtJetHt_;

    /// Maximum (abs) eta requirement for jets
    double maxEtaJetHt_;

    /// Input jet, PFCandidate collections
    edm::InputTag jetsLabel_;

    edm::EDGetTokenT<reco::JetView> m_theJetToken;
};

#endif  // HLTHtJetMassProducer_h_

