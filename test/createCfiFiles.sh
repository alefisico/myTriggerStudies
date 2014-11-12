
input_Dir=/eos/uscms/store/user/algomez/
PU=$1

version=fd2179ffc0ee5fe4cc46fc40ae1e5de7

#if [[ $PU == *20* ]]
#then
#ptBins=( '30to50' '50to80' '80to120' '120to170' '170to300' '300to470' '470to600' '600to800' '800to1000' '1000to1400' '1400to1800' '1800' )
ptBins=( '80to120' '120to170' '170to300' '300to470' '470to600' '600to800' '800to1000' )
#ptBins=( '170to300' '300to470' '470to600')
#ptBins=( '470to600')
#fi


##############################################
##### Create the python file 
##############################################
for bin in ${ptBins[@]};
do
	namePythonFileCFI=QCD_Pt-${bin}_Tune4C_13TeV_pythia8_${PU}_v721patch2_Filt_cfi.py
	if [ -f $namePythonFileCFI ]; then
		rm -rf $namePythonFileCFI
	fi

	echo "import FWCore.ParameterSet.Config as cms

myfilelist = cms.untracked.vstring()
myfilelist.extend(         [ " >> ${namePythonFileCFI}

	for file in `ls -1 ${input_Dir}/QCD_Pt-${bin}_Tune4C_13TeV_pythia8/openHLT_Filt_v721patch2_QCD_Pt-${bin}_Tune4C_13TeV_pythia8_${PU}_Filt/${version}/*root`
	#for file in `ls -1 ${input_Dir}/QCD_Pt-${bin}_TuneZ2star_13TeV_pythia8_${PU}/QCD*root`
	do
		echo "'${file}'," >> ${namePythonFileCFI}
	done

	echo ']
)
source = cms.Source ("PoolSource", fileNames=myfilelist) ' >> ${namePythonFileCFI}
	sed -i 's/\/eos\/uscms//' ${namePythonFileCFI}
done
