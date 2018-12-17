import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("TEST")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

run_events_to_select = [
    [1, [969113, 969111, 969119, 969123, 969147, 969151, 969159, 969168, 969258, 969280]]
]

def vevent_range(run_events):
    verange = cms.untracked.VEventRange()
    for run, events in run_events:
        for event in events: 
            verange.append('{run}:{event}-{run}:{event}'.format(run=run,event=event))
    return verange

print vevent_range(run_events_to_select)

##____________________________________________________________________________||

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

##____________________________________________________________________________||
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

##____________________________________________________________________________||
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetType1Type2_cff")
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetType0PFCandidate_cff")
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetType0RecoTrack_cff")
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetMult_cff")

##____________________________________________________________________________||
process.load("JetMETCorrections.Type1MET.correctedMet_cff")


from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
runMetCorAndUncFromMiniAOD (
        process,
        isData = True, # false for MC
        fixEE2017 = True,
        fixEE2017Params = {'userawPt': True, 'ptThreshold':50.0, 'minEtaThreshold':2.65, 'maxEtaThreshold': 3.139} ,
        postfix = "ModifiedMET"
)

##____________________________________________________________________________||
# from JetMETCorrections.Type1MET.testInputFiles_cff import corrMETtestInputFiles
# process.source = cms.Source(
#     "PoolSource",
#     fileNames = cms.untracked.vstring(corrMETtestInputFiles)
#     )
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/home/cms/torterotot/public/picked_events_MET_V2.root'
        ),
    # selecting events between event 1 of run 1 and event 10 of run 1. 
    # for a single event, write: '1:5-1:5'
    eventsToProcess = vevent_range(run_events_to_select),
    )

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('metv2.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
#        'drop *',
#        'keep *_*_*_TEST'
        )
    )

##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

##____________________________________________________________________________||
process.p = cms.Path(
    process.fullPatMetSequenceModifiedMET 
#     process.correctionTermsPfMetType1Type2 +
#     process.correctionTermsPfMetType0RecoTrack +
#     process.correctionTermsPfMetType0PFCandidate +
#     process.correctionTermsPfMetMult +
#     process.pfMetT0rt +
#     process.pfMetT0rtT1 +
#     process.pfMetT0rtT1T2 +
#     process.pfMetT0pc +
#     process.pfMetT0pcT1 +
#     process.pfMetT1 +
#     process.pfMetT1T2 +
#     process.pfMetT0rtTxy + 
#     process.pfMetT0rtT1Txy + 
#     process.pfMetT0rtT1T2Txy + 
#     process.pfMetT0pcTxy +
#     process.pfMetT0pcT1Txy +
#     process.pfMetT1Txy+ 
#     process.pfMetT1T2Txy
    )

process.e1 = cms.EndPath(
    process.out
    )

##____________________________________________________________________________||
