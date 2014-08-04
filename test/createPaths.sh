#### HT Triggers
./path_maker.py -i hlt_DiffHT_714_v134_MC.py -p HLT_HT650_v1 -c "hltPreHT650.offset=cms.uint32( 0 )" "hltHt650.minHt=cms.vdouble( 450.0 )" -r "HT450" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_HT650_v1 -c "hltPreHT650.offset=cms.uint32( 0 )" "hltHt650.minHt=cms.vdouble( 550.0 )" -r "HT550" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_HT650_v1 -c "hltPreHT650.offset=cms.uint32( 0 )" "hltHt650.minHt=cms.vdouble( 750.0 )" -r "HT750" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_HT650_v1 -c "hltPreHT650.offset=cms.uint32( 0 )" "hltHt650.minHt=cms.vdouble( 850.0 )" -r "HT850" -o hlt_tmp2.py

#### PFHT Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltHt650.minHt=cms.vdouble( 350.0 )" "hltPFHT650.minHt=cms.vdouble( 450.0 )" -r "HT450" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltHt650.minHt=cms.vdouble( 450.0 )" "hltPFHT650.minHt=cms.vdouble( 550.0 )" -r "HT550" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltHt650.minHt=cms.vdouble( 650.0 )" "hltPFHT650.minHt=cms.vdouble( 750.0 )" -r "HT750" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltHt650.minHt=cms.vdouble( 750.0 )" "hltPFHT650.minHt=cms.vdouble( 850.0 )" -r "HT850" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltPFHT650.minHt=cms.vdouble( 450.0 )"  -r "AK8HT450" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltPFHT650.minHt=cms.vdouble( 550.0 )"  -r "AK8HT550" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltPFHT650.minHt=cms.vdouble( 650.0 )"  -r "AK8HT650" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltPFHT650.minHt=cms.vdouble( 750.0 )"  -r "AK8HT750" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltPFHT650.minHt=cms.vdouble( 850.0 )"  -r "AK8HT850" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltAntiKT4PFJets.useTrimming=cms.bool( True )" "hltAntiKT4PFJets.rFilt=cms.double( 0.2 )" "hltAntiKT4PFJets.trimPtFracMin=cms.double( 0.03 )" "hltPFHT650.minHt=cms.vdouble( 450.0 )"  -r "AK8TrimHT450" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltAntiKT4PFJets.useTrimming=cms.bool( True )" "hltAntiKT4PFJets.rFilt=cms.double( 0.2 )" "hltAntiKT4PFJets.trimPtFracMin=cms.double( 0.03 )" "hltPFHT650.minHt=cms.vdouble( 550.0 )"  -r "AK8TrimHT550" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltAntiKT4PFJets.useTrimming=cms.bool( True )" "hltAntiKT4PFJets.rFilt=cms.double( 0.2 )" "hltAntiKT4PFJets.trimPtFracMin=cms.double( 0.03 )" "hltPFHT650.minHt=cms.vdouble( 650.0 )"  -r "AK8TrimHT650" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltAntiKT4PFJets.useTrimming=cms.bool( True )" "hltAntiKT4PFJets.rFilt=cms.double( 0.2 )" "hltAntiKT4PFJets.trimPtFracMin=cms.double( 0.03 )" "hltPFHT650.minHt=cms.vdouble( 750.0 )"  -r "AK8TrimHT750" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hltAntiKT4PFJets.rParam=cms.double( 0.8 )" "hltAntiKT4PFJets.useTrimming=cms.bool( True )" "hltAntiKT4PFJets.rFilt=cms.double( 0.2 )" "hltAntiKT4PFJets.trimPtFracMin=cms.double( 0.03 )" "hltPFHT650.minHt=cms.vdouble( 850.0 )"  -r "AK8TrimHT850" -o hlt_tmp2.py


#### PFNoPUHT Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFNoPUHT650_v1 -c "hltPrePFNoPUHT650.offset=cms.uint32( 0 )" "hltPFHT650NoPU.minHt=cms.vdouble( 450.0 )" -r "HT450" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFNoPUHT650_v1 -c "hltPrePFNoPUHT650.offset=cms.uint32( 0 )" "hltPFHT650NoPU.minHt=cms.vdouble( 550.0 )" -r "HT550" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFNoPUHT650_v1 -c "hltPrePFNoPUHT650.offset=cms.uint32( 0 )" "hltPFHT650NoPU.minHt=cms.vdouble( 750.0 )" -r "HT750" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFNoPUHT650_v1 -c "hltPrePFNoPUHT650.offset=cms.uint32( 0 )" "hltPFHT650NoPU.minHt=cms.vdouble( 850.0 )" -r "HT850" -o hlt_modified.py
