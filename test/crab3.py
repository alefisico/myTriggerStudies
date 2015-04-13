##################################################################
########   TO RUN THIS: python crab3_QCD.py
########   DO NOT DO: crab submit crab3_QCD.py
##################################################################

from CRABClient.UserUtilities import config
config = config()

version = 'Prod_v01'

config.General.requestName = ''
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.allowNonProductionCMSSW = True

config.Data.inputDataset = ''
config.Data.outLFN = '/store/user/algomez/'
config.Data.publication = True
config.Data.ignoreLocality = True
config.Data.useParent = True
config.Data.publishDataName = 'TriggerStudies_Fall13TSG_PU20bx25_'+version
#config.Data.publishDataName = 'TriggerStudies_PHYS14_PU20bx25_'+version

config.Site.storageSite = 'T3_US_FNALLPC'

if __name__ == '__main__':

	from CRABAPI.RawCommand import crabCommand

	Samples = [ 
			### Phys14
			#'/RPVSt350tojj_13TeV_pythia8/algomez-AODSIM_PHYS14_v720_PU20bx25-f3f189e1357b6e0f0db026fdc7709264/USER',
			'/QCD_Pt-80to120_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU20bx25_POSTLS162_V2-v1/AODSIM',
			'/QCD_Pt-120to170_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU20bx25_POSTLS162_V2-v1/AODSIM',
			'/QCD_Pt-170to300_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU20bx25_POSTLS162_V2-v1/AODSIM',
			'/QCD_Pt-300to470_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU20bx25_POSTLS162_V2-v1/AODSIM',
			'/QCD_Pt-470to600_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU20bx25_POSTLS162_V2-v1/AODSIM',
			'/QCD_Pt-600to800_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU20bx25_POSTLS162_V2-v1/AODSIM',
			'/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU20bx25_POSTLS162_V2-v1/AODSIM',
			'/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU20bx25_POSTLS162_V2-v1/AODSIM',
			'/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU20bx25_POSTLS162_V2-v1/AODSIM',
			]

	
	for dataset in Samples:
		config.Data.inputDataset = dataset
		if 'QCD' in dataset: 
			procName = dataset.split('/')[1]+'_'+version
			config.Data.splitting = 'LumiBased'
			config.Data.unitsPerJob = 20
			config.Data.totalUnits = 1000
			config.JobType.psetName = 'myQCDPATproducer_openHLT.py'
		else: 
			procName = dataset.split('/')[1]+dataset.split('/')[2].replace('algomez-AODSIM', '').split('-')[0]+'_'+version
			config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader'
			config.Data.splitting = 'FileBased'
			config.Data.unitsPerJob = 1
			config.JobType.psetName = 'myPATproducer_openHLT.py'
		config.General.requestName = procName
		crabCommand('submit', config = config)


