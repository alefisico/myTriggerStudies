
input_Dir=/eos/uscms/store/user/algomez/
PU=$1
NAME=$2

version=3bab4fdea7e0e47ca242046da90bc3f6
#version=b1834abb05f8f591d863d03e0f2d8972


##############################################
##### Create the python file 
##############################################
#namePythonFileCFI=RPVSt100tojj_13TeV_pythia8_${PU}_v718_FiltFiles_cfi.py
namePythonFileCFI=${NAME}_13TeV_pythia8_${PU}_v718_HLT2PATFiles_cfi.py
if [ -f $namePythonFileCFI ]; then
	rm -rf $namePythonFileCFI
fi

echo "import FWCore.ParameterSet.Config as cms

myfilelist = cms.untracked.vstring()
myfilelist.extend(         [ " >> ${namePythonFileCFI}

#for file in `ls -1 ${input_Dir}/${NAME}_13TeV_pythia8/openHLT_Filt_triggerStudies_allAK8_Trk1B_v4_${NAME}_13TeV_pythia8_${PU}_Filt/6a8bc4a2571c6fe42c1fff6128b4f573/*root`
#for file in `ls -1 ${input_Dir}/${NAME}_13TeV_${PU}_Filt/*root`
#for file in `ls -1 ${input_Dir}/${NAME}_13TeV_pythia8_${PU}_Filt/*root`
#for file in `ls -1 ${input_Dir}/RPVSt100tojj_13TeV_pythia8_GENSIM/openHLT_Filt_v718_v2_RPVSt100tojj_13TeV_pythia8_${PU}_Filt/${version}/*root`
#for file in `ls -1 ${input_Dir}/RPVSt100tojj_13TeV_pythia8_GENSIM/openHLT_Prod_v718_v3_RPVSt100tojj_13TeV_pythia8_${PU}_HLT2PAT/${version}/*root`
#for file in `ls -1 ${input_Dir}/Sig_500SbtoWSt_100RPVSttojj_13TeV_100K_GENSIM/openHLT_Filt_v718_v2_500SbtoWSt_RPVSt100tojj_13TeV_pythia8_${PU}_Filt/${version}/*root`
#for file in `ls -1 ${input_Dir}/Sig_500SbtoWSt_100RPVSttojj_13TeV_100K_GENSIM/openHLT_Prod_v718_v3_500SbtoWSt_RPVSt100tojj_13TeV_pythia8_${PU}_HLT2PAT/${version}/*root`
#for file in `ls -1 ${input_Dir}/St2toZSt1_150RPVSt1tojj_13TeV_100k_GENSIM/openHLT_Filt_v718_v2_500St2toZSt1_150RPVSt1tojj_13TeV_pythia8_${PU}_Filt/${version}/*root`
for file in `ls -1 ${input_Dir}/St2toZSt1_150RPVSt1tojj_13TeV_100k_GENSIM/openHLT_Prod_v718_v3_500St2toZSt1_150RPVSt1tojj_13TeV_pythia8_${PU}_HLT2PAT/${version}/*root`
do
	echo "'${file}'," >> ${namePythonFileCFI}
done

echo ']
)
source = cms.Source ("PoolSource", fileNames=myfilelist) ' >> ${namePythonFileCFI}
sed -i 's/\/eos\/uscms//' ${namePythonFileCFI}
