#### AK8PFTrimHT450 Triggers
./path_maker.py -i hlt_DiffHT_716_v81_MC.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py

#### AK8PFTrimHT550 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py

#### AK8PFTrimHT650 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py

#### AK8PFTrimHT750 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py

#### AK8PFTrimHT850 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py


#
##### AK8PFTrimNOJECHT450 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py

#### AK8PFNOJECTrimHT550 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py

#### AK8PFNOJECTrimHT650 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py

#### AK8PFNOJECTrimHT750 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py

#### AK8PFNOJECTrimHT850 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass0" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass10_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass10_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass20_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass20_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass30_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass30_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass40_TrimPt100" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass40_TrimPt200" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 5.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 200.0 )" -r "TrimMass50_TrimPt200" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )"  "hlt1AK8PFJetsTrimMass00.MinPt=cms.double( 100.0 )" -r "TrimMass50_TrimPt100" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_modified.py


rm -rf hlt_tmp*
