from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.requestName = 'MuAlRefit_Run2017B_RAWRECO_2016Geom'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'refit_PromptGT_MuAl_2016Geometry_2017B_cfg.py'
config.JobType.outputFiles = ['output.root']

config.JobType.inputFiles = ['Geometries/data_DT-1100-111111_SingleMuon_Run2016G_MuAlCalIsolatedMu_278820_280385_8_0_24_Rerecov1_03.db','Geometries/data_CSC-1100-110001_SingleMuon_Run2016G_MuAlCalIsolatedMu_278820_280385_8_0_24_Rerecov1_03.db','Geometries/GPR_July11_2017_SW924_Run2017B_dL4_iter1.db']

config.section_("Data")
config.Data.inputDataset = '/SingleMuon/Run2017B-ZMu-PromptReco-v1/RAW-RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 7
config.Data.lumiMask = 'Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt'
config.Data.outLFNDirBase =  '/store/group/alca_muonalign/lpernie/MuAlRefit_Run2017B_RAWRECO_2016Geom'
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
