
input_Dir=/eos/uscms/store/user/algomez/
PU=$1
#version=6ba8c87d406954f9beb960381b3badb8 ### v714
version=441ecbd981019bde2a486ce4b85e8ab3
ptBins=( '30to50' '50to80' '80to120' '120to170' '170to300' '300to470' '470to600' '600to800' '800to1000' '1000to1400' '1400to1800' '1800' )


##############################################
##### Create the python file 
##############################################
for bin in ${ptBins[@]};
do
	namePythonFileCFI=QCD_Pt-${bin}_Tune4C_13TeV_pythia8_${PU}_ProdFiles_cfi.py
	if [ -f $namePythonFileCFI ]; then
		rm -rf $namePythonFileCFI
	fi

	echo "import FWCore.ParameterSet.Config as cms

myfilelist = cms.untracked.vstring()
myfilelist.extend(         [ " >> ${namePythonFileCFI}

	for file in `ls -1 ${input_Dir}/QCD_Pt-${bin}_Tune4C_13TeV_pythia8/openHLT_Prod_triggerStudies_QCD_Pt-${bin}_TuneZ2star_13TeV_pythia8_${PU}/${version}/QCD*root`
	do
		echo "'${file}'," >> ${namePythonFileCFI}
	done

	echo ']
)
source = cms.Source ("PoolSource", fileNames=myfilelist) ' >> ${namePythonFileCFI}
	sed -i 's/\/eos\/uscms//' ${namePythonFileCFI}
done
