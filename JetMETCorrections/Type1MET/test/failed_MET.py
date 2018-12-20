import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("TEST")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

run_events_to_select = [
    [1, [969280]]
]

def vevent_range(run_events):
    verange = cms.untracked.VEventRange()
    for run, events in run_events:
        for event in events: 
            verange.append('{run}:{event}-{run}:{event}'.format(run=run,event=event))
    return verange

process.RAWpfMET = cms.EDProducer("PFMETProducer",
    alias = cms.string('RAWpfMet'),
    calculateSignificance = cms.bool(False),
    globalThreshold = cms.double(0.0),
    src = cms.InputTag("packedPFCandidates")
)

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/VBFHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2EE992B1-F942-E811-8F11-0CC47A4C8E8A.root'
        ),
    # selecting events between event 1 of run 1 and event 10 of run 1. 
    # for a single event, write: '1:5-1:5'
    eventsToProcess = vevent_range(run_events_to_select),
    )

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('failed_MET_output.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
        )
    )
##____________________________________________________________________________||
process.p = cms.Path(
    process.RAWpfMET
    )

process.e1 = cms.EndPath(
    process.out
    )

##____________________________________________________________________________||
