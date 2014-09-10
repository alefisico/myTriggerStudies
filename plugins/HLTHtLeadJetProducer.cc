/** \class HLTHtLeadJetProducer
 *
 * See header file for documentation
 *
 *  \author Alejandro Gomez Espinosa
 *
 */

//#include "HLTrigger/JetMET/interface/HLTHtLeadJetProducer.h"
#include "MyTrigger/myTriggerStudies/interface/HLTHtLeadJetProducer.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/MakerMacros.h"


// Constructor
HLTHtLeadJetProducer::HLTHtLeadJetProducer(const edm::ParameterSet & iConfig) :
  usePt_                  ( iConfig.getParameter<bool>("usePt") ),
  minNJetHt_              ( iConfig.getParameter<int>("minNJetHt") ),
  minPtJetHt_             ( iConfig.getParameter<double>("minPtJetHt") ),
  maxEtaJetHt_            ( iConfig.getParameter<double>("maxEtaJetHt") ),
  jetsLabel_              ( iConfig.getParameter<edm::InputTag>("jetsLabel") ){

    m_theJetToken = consumes<edm::View<reco::Jet>>(jetsLabel_);
    // Register the products
    produces<reco::METCollection>();
}

// Destructor
HLTHtLeadJetProducer::~HLTHtLeadJetProducer() {}

// Fill descriptions
void HLTHtLeadJetProducer::fillDescriptions(edm::ConfigurationDescriptions & descriptions) {
    // Current default is for hltHt
    edm::ParameterSetDescription desc;
    desc.add<bool>("usePt", false);
    desc.add<int>("minNJetHt", 0);
    desc.add<double>("minPtJetHt", 40.);
    desc.add<double>("maxEtaJetHt", 3.);
    desc.add<edm::InputTag>("jetsLabel", edm::InputTag("hltCaloJetL1FastJetCorrected"));
    descriptions.add("hltHtLeadJetProducer", desc);
}

// Produce the products
void HLTHtLeadJetProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

    // Create a pointer to the products
    std::auto_ptr<reco::METCollection> result(new reco::METCollection());


    edm::Handle<reco::JetView> jets;
    iEvent.getByToken(m_theJetToken, jets);

    int nj_ht = 0;
    double ht = 0.;

    if (jets->size() > 0) {
        for(reco::JetView::const_iterator j = jets->begin(); j != jets->end(); ++j) {
            double pt = usePt_ ? j->pt() : j->et();
            double eta = j->eta();
            //double phi = j->phi();
            //double px = usePt_ ? j->px() : j->et() * cos(phi);
            //double py = usePt_ ? j->py() : j->et() * sin(phi);

            if (pt > minPtJetHt_ && std::abs(eta) < maxEtaJetHt_) {
                ht += pt;
                ++nj_ht;
            }

        }
    }

    reco::MET::LorentzVector p4(0, 0, 0, 0);
    if (nj_ht  < minNJetHt_ ) { ht = 0; } 
    else { p4 = jets->begin()->p4(); }

    //std::cout << ht << " " <<  p4.Pt() << std::endl;

    reco::MET::Point vtx(0, 0, 0);
    reco::MET htJet1(ht, p4, vtx);
    result->push_back(htJet1);

    // Put the products into the Event
    iEvent.put(result);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HLTHtLeadJetProducer);
