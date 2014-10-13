
input_Dir=/eos/uscms/store/user/algomez/

#PUScenario=( 'PU20bx25' 'PU40bx25' )
#NAME=( 'RPVSt100tojj' '500St2toZSt1_150RPVSt1tojj' '500SbtoWSt_RPVSt100tojj' )
#DIR_NAME=( 'RPVSt100tojj_13TeV_pythia8_GENSIM' 'St2toZSt1_150RPVSt1tojj_13TeV_100k_GENSIM' 'Sig_500SbtoWSt_100RPVSttojj_13TeV_100K_GENSIM' )
PUScenario=( 'PU40bx25' )
NAME=( 'RPVSt100tojj_13TeV_pythia8' 'RSGravitonToWW_M_1000_Tune4C_13TeV')
DIR_NAME=( 'RPVSt100tojj_13TeV_pythia8_GENSIM' 'RSGravitonToWW_kMpl01_M_1000_Tune4C_13TeV_pythia8' )
#version=( 'd5c91d12d136f78ab21b93deae731020' '' )

version=d5c91d12d136f78ab21b93deae731020

##############################################
##### Create the python file 
##############################################
for i in 0 1 #2
do
	for PU in ${PUScenario[@]};
	do 
		namePythonFileCFI=${NAME[${i}]}_${PU}_v720pre8_FiltFiles_cfi.py
		if [ -f $namePythonFileCFI ]; then
			rm -rf $namePythonFileCFI
		fi

		echo "import FWCore.ParameterSet.Config as cms

myfilelist = cms.untracked.vstring()
myfilelist.extend(         [ " >> ${namePythonFileCFI}

		for file in `ls -1 ${input_Dir}/${DIR_NAME[${i}]}/openHLT_Filt_v720pre8_v1_${NAME[${i}]}_${PU}_Filt/${version}/*root`
		do
			echo "'${file}'," >> ${namePythonFileCFI}
		done

		echo ']
)
source = cms.Source ("PoolSource", fileNames=myfilelist) ' >> ${namePythonFileCFI}
		sed -i 's/\/eos\/uscms//' ${namePythonFileCFI}
	done
done
