from ROOT import gSystem
from DataFormats.FWLite import Events, Handle

print('open input file...')

events = Events('metv2.root')

# check event content with:  edmDumpEventContent metv2.root  | grep ModifiedMET
h_blob = Handle('std::vector<reco::VertexCompositePtrCandidate>')
h_modmet =  Handle('std::vector<pat::MET>')
h_met =  Handle('std::vector<pat::MET>')
h_jetsbad = Handle('std::vector<pat::Jet>')


print('start processing')

accepted = 0

for i,event in enumerate(events): 

    nEvent = event._event.id().event()
    print("processing event {0}: {1}...".format(i, nEvent))

    event.getByLabel(('blobUnclusteredModifiedMET'), h_blob)
    blobs = h_blob.product()
    print 'blob', len(blobs), blobs[0].pt()

    event.getByLabel(('slimmedMETsModifiedMET'), h_modmet)
    modmet = h_modmet.product()[0]
    print 'mod met', modmet.pt(), modmet.phi()

    event.getByLabel(('slimmedMETs'), h_met)
    met = h_met.product()[0]
    print 'met', met.pt(), met.phi()

    event.getByLabel(('pfCandidateJetsWithEEnoiseModifiedMET:bad'), h_jetsbad)
    jetsbad = h_jetsbad.product()
    print 'jets'
    for jet in jetsbad:
        print '\t', jet.pt(), jet.eta(), jet.phi()

