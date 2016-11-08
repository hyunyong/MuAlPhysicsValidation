from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.requestName = 'MuAlRefit_Run2016E_RAWreco_DT6DOF_CSC3DOF_APE02'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'refit_PromptGT_TrackerMay2016_MuAl_DT2016D6DOF_CSC2016D3DOF_cfg.py'
config.JobType.outputFiles = ['output.root']
#3DOF
#config.JobType.inputFiles = ['Geometries/data_DT-1100-110001_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrack_v1_03.db','Geometries/data_CSC-1100-110001_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrack_v1_03.db','Geometries/GPR_May24_2016_SW808_gprGT_Tk_MP_Run2016B_v2_dL4_iter1.db','APE/APEs_DT_Data_AllContributions_AllTypesOfApes_3DOF.db']
#6DOF
config.JobType.inputFiles = ['Geometries/data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrack_v1_03.db','Geometries/data_CSC-1100-110001_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrack_v1_03.db','Geometries/GPR_May24_2016_SW808_gprGT_Tk_MP_Run2016B_v2_dL4_iter1.db','APE/APEs_DT_Data_AllContributions_AllTypesOfApes_6DOF.db']

config.section_("Data")
config.Data.inputDataset = '/SingleMuon/Run2016E-ZMu-PromptReco-v2/RAW-RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 7
config.Data.lumiMask = 'Cert_271036-279931_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
config.Data.outLFNDirBase =  '/store/group/alca_muonalign/lpernie/MuAlRefit_Run2016E_RAWreco_DT6DOF_CSC3DOF_APE02'
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
