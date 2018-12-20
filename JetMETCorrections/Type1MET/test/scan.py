from ROOT import gSystem
from DataFormats.FWLite import Events, Handle

print('open input file...')

events = Events('metv2.root')

# check event content with:  edmDumpEventContent metv2.root  | grep ModifiedMET
h_blob = Handle('std::vector<reco::VertexCompositePtrCandidate>')
h_modmet =  Handle('std::vector<pat::MET>')
h_met =  Handle('std::vector<pat::MET>')
h_qqchmet =  Handle('std::vector<reco::PFMET>')
h_qqchmet2 =  Handle('std::vector<reco::PFMET>')
h_jetsbad = Handle('std::vector<pat::Jet>')


print('start processing')

accepted = 0

for i,event in enumerate(events): 

    print '\n\n'

    nEvent = event._event.id().event()
    print("processing event {0}: {1}...".format(i, nEvent))

    event.getByLabel(('blobUnclusteredModifiedMET'), h_blob)
    blobs = h_blob.product()
    blob = blobs[0]
    blob.px = 0
    blob.py = 0
    for N in range(blob.numberOfDaughters()):
        blob.px += blob.daughter(N).px()
        blob.py += blob.daughter(N).py()
    blob.pt = (blob.px**2 + blob.py**2)**.5
    print 'blob with {} ptcs'.format(blob.numberOfDaughters()), blob.pt


    event.getByLabel(('qqch'), h_qqchmet)
    RAWmet = h_qqchmet.product()[0]
    print 'RAW met', RAWmet.pt(), RAWmet.px(), RAWmet.py(), RAWmet.phi()

    event.getByLabel(('pfMetModifiedMET'), h_qqchmet2)
    import pdb; pdb.set_trace()
    RAWmet = h_qqchmet2.product()[0]
    print 'pfMetModifiedMET', RAWmet.pt(), RAWmet.px(), RAWmet.py(), RAWmet.phi()

    event.getByLabel(('slimmedMETsModifiedMET'), h_modmet)
    modmet = h_modmet.product()[0]
    print 'mod met', modmet.pt(), modmet.px(), modmet.py(), modmet.phi()

    event.getByLabel(('slimmedMETs'), h_met)
    met = h_met.product()[0]
    print 'met px, py', met.px(), met.py()
    print 'met pt, phi', met.pt(), met.phi()

    event.getByLabel(('pfCandidateJetsWithEEnoiseModifiedMET:bad'), h_jetsbad)
    jetsbad = h_jetsbad.product()
    print 'jets'
    for jet in jetsbad:
        print '\t', jet.pt(), jet.eta(), jet.phi()

