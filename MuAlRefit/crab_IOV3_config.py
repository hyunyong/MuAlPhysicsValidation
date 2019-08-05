from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.requestName = 'MuAlRefit_data_2018_UL_IOV3'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'refit_ideal_MuAl_IOV3_cfg.py'
config.JobType.outputFiles = ['out.root']
#6DOF
config.JobType.inputFiles = ['Geometries/data_DT-1100-111111_2018UL_IOV3_CMSSW106_JSON-322603-325172_dataRun2_MuAl_v1_01.db',
'Geometries/data_CSC-1100-110001_2018UL_IOV3_CMSSW106_JSON-322603-325172_dataRun2_MuAl_v1_01.db',
'Geometries/GPR_Aug03_2019_SW1060_GT106X_dataRun2_newTkAl_v18_IOV3_dL_iter1.db']


config.section_("Data")
config.Data.inputDataset = '/SingleMuon/Run2018D-ZMu-PromptReco-v2/RAW-RECO'

config.Data.inputDBS = 'global' # global`
config.Data.splitting = 'LumiBased'
config.Data.splitting = 'Automatic'	
config.Data.lumiMask = 'Geometries/2018_UL_IOV3.txt'
config.Data.outLFNDirBase =  '/store/group/alca_muonalign/hyunyong/MuAlRefit_data_2018_UL_IOV3'
config.Data.publication = False
config.JobType.allowUndistributedCMSSW = True


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
