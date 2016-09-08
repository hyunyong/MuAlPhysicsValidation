import FWCore.ParameterSet.Config as cms
import os

ijob = int(os.environ["IJOB"])
input_files = os.environ["INPUTFILES"].split(" ")

process = cms.Process("MUAL")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(*input_files))

import FWCore.PythonUtilities.LumiList as LumiList
process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON_MuonPhys.txt').getVLuminosityBlockRange()
'''
import PhysicsTools.PythonAnalysis.LumiList as LumiList
myLumis = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_MuonPhys.txt').getCMSSWString().split(',')
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
process.source.lumisToProcess.extend(myLumis)
'''

process.muAlAnalyzer = cms.EDAnalyzer('MuAlAnalyzer',
  debugLevel      = cms.int32(1),
#  recoMuons       = cms.InputTag("muons"),
  recoMuons       = cms.InputTag("muAlMuons"),
  recoBeamSpot    = cms.InputTag("offlineBeamSpot"),
  fillRecoMuons   = cms.bool(True),
  fillRecoDimuons = cms.bool(True),
  fillGenMuons    = cms.bool(False),
)

process.p = cms.Path(process.muAlAnalyzer)

process.TFileService = cms.Service("TFileService",
  fileName = cms.string("out_%03d.root" % ijob)
)
