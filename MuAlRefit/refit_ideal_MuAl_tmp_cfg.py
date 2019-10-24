import FWCore.ParameterSet.Config as cms 
import os

process = cms.Process("MUALREFIT")
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/9E6AD29E-BEA5-E811-BD40-FA163E73968C.root')
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring("cout"),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR"),
                                                              ERROR = cms.untracked.PSet( limit = cms.untracked.int32(10) )
                                                             )
                                   )

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GTINPUT" #! GT Here

process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load("Geometry.CMSCommonData.cmsExtendedGeometry2018XML_cfi")
process.load('Configuration.StandardSequences.MagneticField_cff')

process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("RecoTracker.TrackProducer.TrackRefitter_cfi")
process.load("RecoTracker.MeasurementDet.MeasurementTrackerEventProducer_cfi")

process.MeasurementTrackerEvent = process.MeasurementTrackerEvent.clone()

process.muAlGeneralTracks = process.TrackRefitter.clone()

process.muAlAncientMuonSeed = process.ancientMuonSeed.clone()

process.muAlStandAloneMuons = process.standAloneMuons.clone()
# this line switch on "old" hit based muon reconstruction
#process.muAlStandAloneMuons.STATrajBuilderParameters.BWFilterParameters.MuonTrajectoryUpdatorParameters.Granularity = 2
process.muAlStandAloneMuons.InputObjects = cms.InputTag("muAlAncientMuonSeed")

process.muAlGlobalMuons = process.globalMuons.clone()
process.muAlGlobalMuons.TrackerCollectionLabel = cms.InputTag("muAlGeneralTracks")
process.muAlGlobalMuons.MuonCollectionLabel = cms.InputTag("muAlStandAloneMuons","UpdatedAtVtx")

process.muAlTevMuons = process.tevMuons.clone()
process.muAlTevMuons.MuonCollectionLabel = cms.InputTag("muAlGlobalMuons")

process.muAlGlbTrackQual = process.glbTrackQual.clone()
process.muAlGlbTrackQual.InputCollection = cms.InputTag("muAlGlobalMuons")
process.muAlGlbTrackQual.InputLinksCollection = cms.InputTag("muAlGlobalMuons")

process.muAlMuons = process.muons1stStep.clone()
process.muAlMuons.fillShowerDigis = cms.bool(False)
process.muAlMuons.inputCollectionTypes = cms.vstring('inner tracks','links','outer tracks','tev firstHit','tev picky','tev dyt')
process.muAlMuons.inputCollectionLabels = cms.VInputTag( cms.InputTag("muAlGeneralTracks"),
                                                         cms.InputTag("muAlGlobalMuons"),
                                                         cms.InputTag("muAlStandAloneMuons","UpdatedAtVtx"),
                                                         cms.InputTag("muAlTevMuons","firstHit"),
                                                         cms.InputTag("muAlTevMuons","picky"),
                                                         cms.InputTag("muAlTevMuons","dyt")
                                                       )

process.muAlMuons.fillGlobalTrackQuality = cms.bool(True)
process.muAlMuons.globalTrackQualityInputTag = cms.InputTag('muAlGlbTrackQual')
#process.muAlMuons.fillGlobalTrackRefits = cms.bool(False)

# This is to load new CondDB
from CondCore.DBCommon.CondDBSetup_cfi import *
#from CondCore.CondDB.CondDB_cfi import *
#process.GlobalTag.toGet = cms.VPSet(
#         cms.PSet(record = cms.string("TrackerAlignmentRcd"),
#                  tag =  cms.string("Alignments"),
#                  connect = cms.string('sqlite_file:alignments_MP.db')
#                  ),
#         cms.PSet(record = cms.string("TrackerAlignmentErrorExtendedRcd"),
#                  tag =  cms.string("AlignmentErrorsExtended"),
#                  connect = cms.string('sqlite_file:alignments_MP.db')
#                  ),
#         cms.PSet(record = cms.string("TrackerSurfaceDeformationRcd"),
#                  tag =  cms.string("Deformations"),
#                  connect = cms.string('sqlite_file:alignments_MP.db')
#                  ),
#)
# New Tracker geometry from GT in this case
#process.GlobalTag.toGet = cms.VPSet(
#        ###### starts customization of tracker part
#         cms.PSet(record = cms.string("TrackerAlignmentRcd"),
#                  tag =  cms.string("TrackerAlignment_MP_Run2016B_v2"),
#                  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
#                  ),
#         cms.PSet(record = cms.string("TrackerAlignmentErrorExtendedRcd"),
#                  tag =  cms.string("TrackerAlignmentExtendedErrors_MP_Run2016B"),
#                  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
#                  ),
#         cms.PSet(record = cms.string("SiPixelTemplateDBObjectRcd"),
#                  tag =  cms.string("SiPixelTemplateDBObject_38T_2016_v1_hltvalidation"),
#                  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
#                  )
#)

# Muon geometry (CRAB copies take the files location in the crab.py file and copy it where the cmsRun command is executed)
process.muonDtAlignment = cms.ESSource("PoolDBESSource", CondDBSetup,
                                     connect = cms.string('sqlite_file:DTDBINPUT'),
                                     toGet   = cms.VPSet(cms.PSet(record = cms.string("DTAlignmentRcd"),  tag = cms.string("DTAlignmentRcd")))
                                     )
process.es_prefer_muonDtAlignment = cms.ESPrefer("PoolDBESSource","muonDtAlignment")

process.muonCscAlignment = cms.ESSource("PoolDBESSource", CondDBSetup,
                                     connect = cms.string('sqlite_file:CSCDBINPUT'),
                                     toGet   = cms.VPSet(cms.PSet(record = cms.string("CSCAlignmentRcd"), tag = cms.string("CSCAlignmentRcd")))
                                     )
process.es_prefer_muonCscAlignment = cms.ESPrefer("PoolDBESSource","muonCscAlignment")

process.globalPosition = cms.ESSource("PoolDBESSource", CondDBSetup,
                                     connect = cms.string('sqlite_file:GPRDBINPUT'),
                                     toGet   = cms.VPSet(cms.PSet(record = cms.string("GlobalPositionRcd"), tag = cms.string("IdealGeometry")))
                                     )
process.es_prefer_globalPosition = cms.ESPrefer("PoolDBESSource","globalPosition")


process.muAlAnalyzer = cms.EDAnalyzer('MuAlAnalyzer',
  debugLevel      = cms.int32(1),
  recoMuons       = cms.InputTag("muAlMuons"),
  recoBeamSpot    = cms.InputTag("offlineBeamSpot"),
  fillRecoMuons   = cms.bool(True),
  fillRecoDimuons = cms.bool(True),
  fillGenMuons    = cms.bool(False),
)
# Asymptotic Muon APEs
#process.GlobalTag.toGet = cms.VPSet(
#         cms.PSet(record = cms.string("CSCAlignmentErrorExtendedRcd"),
#                  tag =  cms.string("MuonCSCAPEObjectsExtended_v0_mc"),
#                  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
#                  ),
#         cms.PSet(record = cms.string("DTAlignmentErrorExtendedRcd"),
#                  tag =  cms.string("DTAlignmentErrorExtendedRcd"),
#                  connect = cms.string('sqlite_file:APEs_DT_Data_AllContributions_AllTypesOfApes_3DOF.db')
#                  )
#)

process.Path = cms.Path(process.MeasurementTrackerEvent * process.muAlGeneralTracks * process.muAlAncientMuonSeed * process.muAlStandAloneMuons * process.muAlGlobalMuons * process.muAlTevMuons * process.muAlGlbTrackQual * process.muAlMuons * process.muAlAnalyzer)
"""
process.out = cms.OutputModule("PoolOutputModule",
                                fileName = cms.untracked.string("output.root"),
                                SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("Path")),
                                )
"""
process.TFileService = cms.Service("TFileService",
  fileName = cms.string("out.root")
)