#ifndef HLTHtLeadJetFilter_h_
#define HLTHtLeadJetFilter_h_

/** \class HLTHtLeadJetFilter
 *
 *  \brief  This filters events based on HT and MHT produced by HLTHtLeadJetProducer2
 *  \author Steven Lowette
 *
 *  This filter can accept more than one pair of HT and MHT. An event is kept
 *  if at least one pair satisfies:
 *    - HT > `minHt_[i]` ; and
 *    - MHT > `minMht_[i]` ; and
 *    - sqrt(MHT + `meffSlope_[i]` * HT) > `minMeff_[i]`
 *
 */

#include "HLTrigger/HLTcore/interface/HLTFilter.h"

#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METFwd.h"


namespace edm {
    class ConfigurationDescriptions;
}

// Class declaration
class HLTHtLeadJetFilter : public HLTFilter {
  public:
    explicit HLTHtLeadJetFilter(const edm::ParameterSet & iConfig);
    ~HLTHtLeadJetFilter();
    static void fillDescriptions(edm::ConfigurationDescriptions & descriptions);
    virtual bool hltFilter(edm::Event & iEvent, const edm::EventSetup & iSetup, trigger::TriggerFilterObjectWithRefs & filterproduct) const override;

  private:
    /// Minimum HT requirements
    std::vector<double> minHt_;

    /// Minimum MHT requirements
    std::vector<double> minMht_;

    /// Minimum Meff requirements
    std::vector<double> minMeff_;

    /// Meff slope requirements
    std::vector<double> meffSlope_;

    /// Input reco::MET collections to retrieve HT and MHT
    std::vector<edm::InputTag> htLabels_;
    std::vector<edm::InputTag> mhtLabels_;

    unsigned int nOrs_;  /// number of pairs of HT and MHT

    std::vector<edm::EDGetTokenT<reco::METCollection> > m_theHtToken;
    std::vector<edm::EDGetTokenT<reco::METCollection> > m_theMhtToken;
};

#endif  // HLTHtLeadJetFilter_h_

