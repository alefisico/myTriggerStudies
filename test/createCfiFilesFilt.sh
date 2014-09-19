
input_Dir=/eos/uscms/store/user/algomez/
PU=$1
NAME=$2

#version=fc649452ae54dcedc6e66dc723d9581f
version=7799d5eab63196045b8111a8418afcfc


##############################################
##### Create the python file 
##############################################
#namePythonFileCFI=RPVSt100tojj_13TeV_pythia8_${PU}_allAK8_100k_FiltFiles_cfi.py
namePythonFileCFI=${NAME}_13TeV_pythia8_${PU}_allAK8_100k_FiltFiles_cfi.py
#namePythonFileCFI=500SbtoWSt_100RPVSttojj_13TeV_pythia8_${PU}_allAK8_100k_ProdFiles_cfi.py
#namePythonFileCFI=500St2toZSt1_150RPVSt1tojj_13TeV_pythia8_${PU}_allAK8_100k_ProdFiles_cfi.py
if [ -f $namePythonFileCFI ]; then
	rm -rf $namePythonFileCFI
fi

echo "import FWCore.ParameterSet.Config as cms

myfilelist = cms.untracked.vstring()
myfilelist.extend(         [ " >> ${namePythonFileCFI}

for file in `ls -1 ${input_Dir}/${NAME}_13TeV_pythia8/openHLT_Filt_triggerStudies_allAK8_Trk1B_v4_${NAME}_13TeV_pythia8_${PU}_Filt/6a8bc4a2571c6fe42c1fff6128b4f573/*root`
#for file in `ls -1 ${input_Dir}/${NAME}_13TeV_${PU}_Filt/*root`
#for file in `ls -1 ${input_Dir}/${NAME}_13TeV_pythia8_${PU}_Filt/*root`
#for file in `ls -1 ${input_Dir}/RPVSt100tojj_13TeV_pythia8_GENSIM/openHLT_Prod_triggerStudies_allAK8_Trk1B_RPVSt100tojj_13TeV_pythia8_${PU}_HLT2PAT/${version}/*root`
#for file in `ls -1 ${input_Dir}/Sig_500SbtoWSt_100RPVSttojj_13TeV_100K_GENSIM/openHLT_Prod_triggerStudies_allAK8_Trk1B_500SbtoWSt_RPVSt100tojj_13TeV_pythia8_PU20bx25_HLT2PAT/fc649452ae54dcedc6e66dc723d9581f/*root`
#for file in `ls -1 ${input_Dir}/St2toZSt1_150RPVSt1tojj_13TeV_100k_GENSIM/openHLT_Prod_triggerStudies_allAK8_Trk1B_500St2toZSt1_150RPVSt1tojj_13TeV_pythia8_PU20bx25_HLT2PAT/${version}/*root`
do
	echo "'${file}'," >> ${namePythonFileCFI}
done

echo ']
)
source = cms.Source ("PoolSource", fileNames=myfilelist) ' >> ${namePythonFileCFI}
sed -i 's/\/eos\/uscms//' ${namePythonFileCFI}
