from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'RPVSt350tojj_13TeV_pythia8_Prod_Trigger_PHYS14_v720_PU20bx25'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'dumpMC.py'

config.Data.inputDataset = '/RPVSt350tojj_13TeV_pythia8/algomez-AODSIM_PHYS14_v720_PU20bx25-f3f189e1357b6e0f0db026fdc7709264/USER'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFN = '/store/user/algomez/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.useParent = True
config.Data.ignoreLocality = True
config.Data.publishDataName = 'Prod_Trigger_PHYS14_v720_PU20bx25'

config.Site.storageSite = 'T3_US_FNALLPC'
