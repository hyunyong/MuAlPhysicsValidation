import FWCore.ParameterSet.Config as cms
import os

ijob = int(os.environ["IJOB"])
input_files = os.environ["INPUTFILES"].split(" ")

process = cms.Process("MUAL")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(*input_files))

process.muAlAnalyzer = cms.EDAnalyzer('MuAlAnalyzer',
  debugLevel      = cms.int32(1),
  recoMuons       = cms.InputTag("muAlMuons"),
  recoBeamSpot    = cms.InputTag("offlineBeamSpot"),
  genParticle     = cms.InputTag("genParticles"),
  fillRecoMuons   = cms.bool(True),
  fillRecoDimuons = cms.bool(True),
  fillGenMuons    = cms.bool(True),
)

process.p = cms.Path(process.muAlAnalyzer)

process.TFileService = cms.Service("TFileService",
  fileName = cms.string("out_%03d.root" % ijob)
)
