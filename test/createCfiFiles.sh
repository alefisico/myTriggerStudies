
input_Dir=/eos/uscms/store/user/algomez/
PU=$1
#version=6ba8c87d406954f9beb960381b3badb8 ### v714
#version=cbd8fa5b6552de8987640bc30645edc3	### 716 for PU20bx25 40k
#version=3238dff6eaedddc50085b315d9485a61 ## 5k 

#version=d134a266b5ff92a5775db3890e364d37   #### new version 10k
#version=9690e4180ab057b61d0c23d324d73de0    #### new version 10k for PU40bx50

#version=fd868969154cb7a3f3a270ccee8b693b    #### HLT2PAT 10k
#version=721c33a7b3ece2a1c649181a68f869e9   #### HLT2PAT 10k

version=77b61ad319fca9ec590eb2f3faa9e592

if [[ $PU == *20* ]]
then
	ptBins=( '30to50' '50to80' '80to120' '120to170' '170to300' '300to470' '470to600' '600to800' '800to1000' '1000to1400' '1400to1800' '1800' )
	#ptBins=( '170to300' '300to470' '470to600')
else
	ptBins=( '30to50' '50to80' '80to120' '120to170' '170to300' '300to470' '470to600' '600to800' '800to1000' '1000to1400' '1400to1800' )
	#ptBins=( '170to300' '300to470' '470to600')
	#ptBins=( '470to600')
fi


##############################################
##### Create the python file 
##############################################
for bin in ${ptBins[@]};
do
	namePythonFileCFI=QCD_Pt-${bin}_Tune4C_13TeV_pythia8_${PU}_AK8JEC_10k_ProdFiles_cfi.py
	if [ -f $namePythonFileCFI ]; then
		rm -rf $namePythonFileCFI
	fi

	echo "import FWCore.ParameterSet.Config as cms

myfilelist = cms.untracked.vstring()
myfilelist.extend(         [ " >> ${namePythonFileCFI}

	for file in `ls -1 ${input_Dir}/QCD_Pt-${bin}_Tune4C_13TeV_pythia8/openHLT_Prod_triggerStudies_allAK8_QCD_Pt-${bin}_Tune4C_13TeV_pythia8_${PU}/${version}/QCD*root`
	#for file in `ls -1 ${input_Dir}/QCD_Pt-${bin}_TuneZ2star_13TeV_pythia8_${PU}/QCD*root`
	do
		echo "'${file}'," >> ${namePythonFileCFI}
	done

	echo ']
)
source = cms.Source ("PoolSource", fileNames=myfilelist) ' >> ${namePythonFileCFI}
	sed -i 's/\/eos\/uscms//' ${namePythonFileCFI}
done
