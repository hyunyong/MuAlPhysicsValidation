from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.requestName = 'REQUESTNAME'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'CFGNAME'
config.JobType.outputFiles = ['out.root']
#6DOF
config.JobType.inputFiles = ['Geometries/DTDBINPUT',
'Geometries/CSCDBINPUT',
'Geometries/GPRDBINPUT']


config.section_("Data")
config.Data.inputDataset = 'DATASET'

config.Data.inputDBS = 'global' # global`
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.lumiMask = 'Geometries/JSONINPUT'
config.Data.outLFNDirBase =  '/store/group/alca_muonalign/USER/STORAGEDIR'
config.Data.publication = False
config.JobType.allowUndistributedCMSSW = True


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
