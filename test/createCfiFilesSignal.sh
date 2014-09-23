
input_Dir=/eos/uscms/store/user/algomez/

PUScenario=( 'PU20bx25' 'PU40bx25' )
NAME=( 'RPVSt100tojj' '500St2toZSt1_150RPVSt1tojj' '500SbtoWSt_RPVSt100tojj' )
DIR_NAME=( 'RPVSt100tojj_13TeV_pythia8_GENSIM' 'St2toZSt1_150RPVSt1tojj_13TeV_100k_GENSIM' 'Sig_500SbtoWSt_100RPVSttojj_13TeV_100K_GENSIM' )

#version=3bab4fdea7e0e47ca242046da90bc3f6
version=b1834abb05f8f591d863d03e0f2d8972

##############################################
##### Create the python file 
##############################################
for i in 0 1 2
do
	for PU in ${PUScenario[@]};
	do 
		namePythonFileCFI=${NAME[${i}]}_13TeV_pythia8_${PU}_v718_FiltFiles_cfi.py
		if [ -f $namePythonFileCFI ]; then
			rm -rf $namePythonFileCFI
		fi

		echo "import FWCore.ParameterSet.Config as cms

myfilelist = cms.untracked.vstring()
myfilelist.extend(         [ " >> ${namePythonFileCFI}

		for file in `ls -1 ${input_Dir}/${DIR_NAME[${i}]}/openHLT_Filt_v718_v2_${NAME[${i}]}_13TeV_pythia8_${PU}_Filt/${version}/*root`
		do
			echo "'${file}'," >> ${namePythonFileCFI}
		done

		echo ']
)
source = cms.Source ("PoolSource", fileNames=myfilelist) ' >> ${namePythonFileCFI}
		sed -i 's/\/eos\/uscms//' ${namePythonFileCFI}
	done
done
