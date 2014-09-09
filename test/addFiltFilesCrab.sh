
input_Dir=$PWD
PU=$1


ptBins=( '50to80' '80to120' '120to170' '170to300' '300to470' '470to600' '600to800' '800to1000' )

for bin in ${ptBins[@]};
do
	sed -n '/TrigReport ---------- Path   Summary ------------/,/TrigReport -------End-Path   Summary ------------/p'  QCD_Pt-${bin}_Tune4C_13TeV_pythia8_${PU}_Filt/res/CMSSW_*.stdout | awk '{a[$8]+=$4;b[$8]+=$5;c[$8]+=$6}END{for (i in a) print i,a[i],b[i],c[i]}' | sort > $PWD/Rates/rates_QCD_Pt-${bin}_Tune4C_13TeV_pythia8_${PU}.txt
done
