#### AK8PFTrimHT450 Triggers
./path_maker.py -i hlt_DiffHT_717_Trk1B_MC.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT550 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_v1 -c "hltPreAK8PFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT650 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_v1 -c "hltPreAK8PFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT750 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_v1 -c "hltPreAK8PFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT850 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT450_TrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_TrimMod_v1 -c "hltPreAK8PFTrimHT450TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT550_TrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_TrimMod_v1 -c "hltPreAK8PFTrimHT550TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT650_TrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_TrimMod_v1 -c "hltPreAK8PFTrimHT650TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT750_TrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_TrimMod_v1 -c "hltPreAK8PFTrimHT750TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT850_TrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_TrimMod_v1 -c "hltPreAK8PFTrimHT850TrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py



#### AK8PFTrimHT450_JetTrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_JetTrimMod_v1 -c "hltPreAK8PFTrimHT450JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT550_JetTrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT550_JetTrimMod_v1 -c "hltPreAK8PFTrimHT550JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT650_JetTrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT650_JetTrimMod_v1 -c "hltPreAK8PFTrimHT650JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT750_JetTrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT750_JetTrimMod_v1 -c "hltPreAK8PFTrimHT750JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFTrimHT850_JetTrimMod Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_JetTrimMod_v1 -c "hltPreAK8PFTrimHT850JetTrimMod.offset=cms.uint32( 0 )" "hlt1AK8PFJetsJetTrimModMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFNOJECTrimHT450 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT450_v1 -c "hltPreAK8PFNOJECTrimHT450.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFNOJECTrimHT550 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT550_v1 -c "hltPreAK8PFNOJECTrimHT550.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFNOJECTrimHT650 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT650_v1 -c "hltPreAK8PFNOJECTrimHT650.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFNOJECTrimHT750 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT750_v1 -c "hltPreAK8PFNOJECTrimHT750.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


#### AK8PFNOJECTrimHT850 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFNOJECTrimHT850_v1 -c "hltPreAK8PFNOJECTrimHT850.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimMass00.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py

#### PFTrimHT450 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT450_v1 -c "hltPrePFTrimHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py


#### PFTrimHT550 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT550_v1 -c "hltPrePFTrimHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py


#### PFTrimHT650 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT650_v1 -c "hltPrePFTrimHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py


#### PFTrimHT750 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT750_v1 -c "hltPrePFTrimHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py

#### PFTrimHT850 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFTrimHT850_v1 -c "hltPrePFTrimHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsTrimMass00.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py


#### PFHT450 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 0.0 )" -r "Mass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 5.0 )" -r "Mass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 10.0 )" -r "Mass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 15.0 )" -r "Mass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 20.0 )" -r "Mass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 25.0 )" -r "Mass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 30.0 )" -r "Mass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 35.0 )" -r "Mass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 40.0 )" -r "Mass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 45.0 )" -r "Mass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 50.0 )" -r "Mass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT450_v1 -c "hltPrePFHT450.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 55.0 )" -r "Mass55" -o hlt_tmp2.py

#### PFHT550 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 0.0 )" -r "Mass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 5.0 )" -r "Mass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 10.0 )" -r "Mass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 15.0 )" -r "Mass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 20.0 )" -r "Mass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 25.0 )" -r "Mass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 30.0 )" -r "Mass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 35.0 )" -r "Mass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 40.0 )" -r "Mass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 45.0 )" -r "Mass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 50.0 )" -r "Mass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT550_v1 -c "hltPrePFHT550.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 55.0 )" -r "Mass55" -o hlt_tmp2.py

#### PFHT650 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 0.0 )" -r "Mass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 5.0 )" -r "Mass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 10.0 )" -r "Mass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 15.0 )" -r "Mass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 20.0 )" -r "Mass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 25.0 )" -r "Mass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 30.0 )" -r "Mass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 35.0 )" -r "Mass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 40.0 )" -r "Mass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 45.0 )" -r "Mass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 50.0 )" -r "Mass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT650_v1 -c "hltPrePFHT650.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 55.0 )" -r "Mass55" -o hlt_tmp2.py

#### PFHT750 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 0.0 )" -r "Mass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 5.0 )" -r "Mass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 10.0 )" -r "Mass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 15.0 )" -r "Mass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 20.0 )" -r "Mass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 25.0 )" -r "Mass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 30.0 )" -r "Mass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 35.0 )" -r "Mass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 40.0 )" -r "Mass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 45.0 )" -r "Mass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 50.0 )" -r "Mass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT750_v1 -c "hltPrePFHT750.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 55.0 )" -r "Mass55" -o hlt_tmp2.py

#### PFHT850 Triggers
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 0.0 )" -r "Mass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 5.0 )" -r "Mass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 10.0 )" -r "Mass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 15.0 )" -r "Mass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 20.0 )" -r "Mass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 25.0 )" -r "Mass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 30.0 )" -r "Mass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 35.0 )" -r "Mass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 40.0 )" -r "Mass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 45.0 )" -r "Mass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 50.0 )" -r "Mass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT850_v1 -c "hltPrePFHT850.offset=cms.uint32( 0 )" "hlt1AK4PFJetsMass00.MinMass=cms.double( 55.0 )" -r "Mass55" -o hlt_tmp2.py


./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hltAK8Ht350.minHt=cms.vdouble( 250.0 )" -r "CaloHT250" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hltAK8Ht350.minHt=cms.vdouble( 300.0 )" -r "CaloHT300" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hltAK8Ht350.minHt=cms.vdouble( 350.0 )" -r "CaloHT350" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hltAK8Ht350.minHt=cms.vdouble( 400.0 )" -r "CaloHT400" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT450_v1 -c "hltPreAK8PFTrimHT450.offset=cms.uint32( 0 )" "hltAK8Ht350.minHt=cms.vdouble( 450.0 )" -r "CaloHT450" -o hlt_tmp1.py

./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hltAK8Ht750.minHt=cms.vdouble( 550.0 )" -r "CaloHT550" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hltAK8Ht750.minHt=cms.vdouble( 600.0 )" -r "CaloHT600" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hltAK8Ht750.minHt=cms.vdouble( 650.0 )" -r "CaloHT650" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hltAK8Ht750.minHt=cms.vdouble( 700.0 )" -r "CaloHT700" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFTrimHT850_v1 -c "hltPreAK8PFTrimHT850.offset=cms.uint32( 0 )" "hltAK8Ht750.minHt=cms.vdouble( 750.0 )" -r "CaloHT750" -o hlt_modified.py

rm -rf hlt_tmp*
