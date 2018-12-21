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
h_jetsgood = Handle('std::vector<pat::Jet>')
h_patJetCorrFactorsReapplyJECModifiedMET = Handle('edm::ValueMap<pat::JetCorrFactors>')
h_patJetReapplyJECModifiedMET = Handle('std::vector<pat::Jet>')
h_basicJetsForMetModifiedMET = Handle('std::vector<pat::Jet>')
h_jetSelectorForMetModifiedMET = Handle('std::vector<pat::Jet>')
h_cleanedPatJetsModifiedMET = Handle('std::vector<pat::Jet>')
h_patPFMetT1T2CorrModifiedMET = Handle('CorrMETData')
h_patPFMetT1ModifiedMET =  Handle('std::vector<pat::MET>')
h_rho =  Handle('std::double')


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
    RAWmet = h_qqchmet2.product()[0]
    print 'pfMetModifiedMET', RAWmet.pt(), RAWmet.px(), RAWmet.py(), RAWmet.phi()

    event.getByLabel(('slimmedMETsModifiedMET'), h_modmet)
    modmet = h_modmet.product()[0]
    print 'mod met', modmet.pt(), modmet.px(), modmet.py(), modmet.phi()

    event.getByLabel(('slimmedMETs'), h_met)
    met = h_met.product()[0]
    print 'met px, py', met.px(), met.py()
    print 'met pt, phi', met.pt(), met.phi()

    event.getByLabel(('pfCandidateJetsWithEEnoiseModifiedMET:good'), h_jetsgood)
    jetsgood = h_jetsgood.product()
    print 'good jets'
    for jet in jetsgood:
        print '\t', jet.pt(), jet.eta(), jet.phi()

    event.getByLabel(('pfCandidateJetsWithEEnoiseModifiedMET:bad'), h_jetsbad)
    jetsbad = h_jetsbad.product()
    print 'bad jets'
    for jet in jetsbad:
        print '\t', jet.pt(), jet.eta(), jet.phi()

    event.getByLabel(('patJetCorrFactorsReapplyJECModifiedMET'), h_patJetCorrFactorsReapplyJECModifiedMET)
    JetCorrFactorsReapplyJEC = h_patJetCorrFactorsReapplyJECModifiedMET.product()

    event.getByLabel(('patJetsReapplyJECModifiedMET'), h_patJetReapplyJECModifiedMET)
    JetReapplyJEC = h_patJetReapplyJECModifiedMET.product()

    event.getByLabel(('basicJetsForMetModifiedMET'), h_basicJetsForMetModifiedMET)
    basicJetsForMetModifiedMET = h_basicJetsForMetModifiedMET.product()

    event.getByLabel(('jetSelectorForMetModifiedMET'), h_jetSelectorForMetModifiedMET)
    jetSelectorForMetModifiedMET = h_jetSelectorForMetModifiedMET.product()

    event.getByLabel(('cleanedPatJetsModifiedMET'), h_cleanedPatJetsModifiedMET)
    cleanedPatJetsModifiedMET = h_cleanedPatJetsModifiedMET.product()

    event.getByLabel(('patPFMetT1T2CorrModifiedMET:type1'), h_patPFMetT1T2CorrModifiedMET)
    patPFMetT1T2CorrModifiedMET = h_patPFMetT1T2CorrModifiedMET.product()

    event.getByLabel(('patPFMetT1ModifiedMET'), h_patPFMetT1ModifiedMET)
    patPFMetT1ModifiedMET = h_patPFMetT1ModifiedMET.product()

    event.getByLabel(('fixedGridRhoFastjetAll'), h_rho)
    rho = h_rho.product()

    import pdb; pdb.set_trace()
