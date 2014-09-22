#### AK8PFTrimHT650 Triggers
./path_maker.py -i hlt_DiffHT_718_MC.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimMass00_v1 -c "hltPreAK8PFHT650TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py

#### AK8PFTrimHT700 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimMass00_v1 -c "hltPreAK8PFHT700TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py

#### AK8PFTrimHT750 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimMass00_v1 -c "hltPreAK8PFHT750TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT800 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass00_v1 -c "hltPreAK8PFHT800TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py

#### AK8PFTrimHT850 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimMass00_v1 -c "hltPreAK8PFHT850TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py

#### AK8PFTrimHT900 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimMass00_v1 -c "hltPreAK8PFHT900TrimMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py





#### AK8PFTrimHT650_TrimModMass Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimModMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimModMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimModMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimModMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimModMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimModMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimModMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimModMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimModMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimModMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimModMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimModMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimModMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimModMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimModMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimModMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimModMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModMass00_v1 -c "hltPreAK8PFHT650TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimModMass85" -o hlt_tmp2.py

#### AK8PFTrimHT700 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimModMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimModMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimModMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimModMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimModMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimModMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimModMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimModMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimModMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimModMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimModMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimModMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimModMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimModMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimModMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimModMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimModMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimModMass00_v1 -c "hltPreAK8PFHT700TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimModMass85" -o hlt_tmp2.py

#### AK8PFTrimHT750 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimModMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimModMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimModMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimModMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimModMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimModMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimModMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimModMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimModMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimModMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimModMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimModMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimModMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimModMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimModMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimModMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimModMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT750_TrimModMass00_v1 -c "hltPreAK8PFHT750TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimModMass85" -o hlt_tmp2.py


#### AK8PFTrimHT800 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimModMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimModMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimModMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimModMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimModMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimModMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimModMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimModMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimModMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimModMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimModMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimModMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimModMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimModMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimModMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimModMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimModMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimModMass00_v1 -c "hltPreAK8PFHT800TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimModMass85" -o hlt_tmp2.py

#### AK8PFTrimHT850 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimModMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimModMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimModMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimModMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimModMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimModMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimModMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimModMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimModMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimModMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimModMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimModMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimModMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimModMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimModMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimModMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimModMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT850_TrimModMass00_v1 -c "hltPreAK8PFHT850TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimModMass85" -o hlt_tmp2.py

#### AK8PFTrimHT900 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimModMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimModMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimModMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimModMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimModMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimModMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimModMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimModMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimModMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimModMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimModMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimModMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimModMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimModMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimModMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimModMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimModMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT900_TrimModMass00_v1 -c "hltPreAK8PFHT900TrimModMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimModMass85" -o hlt_tmp2.py


#### AK8PFTrimHT650 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 0.0 )" -r "TrimModTestMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double(  5.0 )" -r "TrimModTestMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 10.0 )" -r "TrimModTestMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 15.0 )" -r "TrimModTestMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 20.0 )" -r "TrimModTestMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 25.0 )" -r "TrimModTestMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 30.0 )" -r "TrimModTestMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 35.0 )" -r "TrimModTestMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 40.0 )" -r "TrimModTestMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 45.0 )" -r "TrimModTestMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 50.0 )" -r "TrimModTestMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 55.0 )" -r "TrimModTestMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 60.0 )" -r "TrimModTestMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 65.0 )" -r "TrimModTestMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 70.0 )" -r "TrimModTestMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 75.0 )" -r "TrimModTestMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 80.0 )" -r "TrimModTestMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT650_TrimModTestMass00_v1 -c "hltPreAK8PFHT650TrimModTestMass00.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModTestMass00.MinMass=cms.double( 85.0 )" -r "TrimModTestMass85" -o hlt_modified.py


rm -rf hlt_tmp*
