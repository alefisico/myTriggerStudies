./path_maker.py -i hlt_DiffHT_741patch1_MC.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 0.0 )" -r "" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 0.0 )" -r "AK8PFHT650_TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double(  5.0 )" -r "AK8PFHT650_TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 10.0 )" -r "AK8PFHT650_TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 15.0 )" -r "AK8PFHT650_TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 20.0 )" -r "AK8PFHT650_TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 25.0 )" -r "AK8PFHT650_TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 30.0 )" -r "AK8PFHT650_TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 35.0 )" -r "AK8PFHT650_TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 40.0 )" -r "AK8PFHT650_TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 45.0 )" -r "AK8PFHT650_TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 50.0 )" -r "AK8PFHT650_TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 55.0 )" -r "AK8PFHT650_TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 60.0 )" -r "AK8PFHT650_TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 65.0 )" -r "AK8PFHT650_TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 70.0 )" -r "AK8PFHT650_TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 75.0 )" -r "AK8PFHT650_TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 80.0 )" -r "AK8PFHT650_TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 550.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 85.0 )" -r "AK8PFHT650_TrimMass85" -o hlt_tmp2.py


./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 0.0 )" -r "AK8PFHT600_TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double(  5.0 )" -r "AK8PFHT600_TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 10.0 )" -r "AK8PFHT600_TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 15.0 )" -r "AK8PFHT600_TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 20.0 )" -r "AK8PFHT600_TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 25.0 )" -r "AK8PFHT600_TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 30.0 )" -r "AK8PFHT600_TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 35.0 )" -r "AK8PFHT600_TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 40.0 )" -r "AK8PFHT600_TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 45.0 )" -r "AK8PFHT600_TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 50.0 )" -r "AK8PFHT600_TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 55.0 )" -r "AK8PFHT600_TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 60.0 )" -r "AK8PFHT600_TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 65.0 )" -r "AK8PFHT600_TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 70.0 )" -r "AK8PFHT600_TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 75.0 )" -r "AK8PFHT600_TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 80.0 )" -r "AK8PFHT600_TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1 -c "hltPreAK8PFHT700TrimR0p1PT0p03Mass50.offset=cms.uint32( 0 )" "hltAK8Ht600.minHt=cms.vdouble( 500.0 )" "hltAK8PFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 85.0 )" -r "AK8PFHT600_TrimMass85" -o hlt_tmp2.py


./path_maker.py -i hlt_tmp2.py -p HLT_PFHT750_4JetPt50_v1 -c "hltPrePFHT7504JetPt50.offset=cms.uint32( 0 )" "hltHtMht4JetPt50.minPtJetHt=cms.double( 60.0 )" "hltPFHT4JetPt50.minPtJetHt=cms.double( 60.0 )" -r "4JetPt60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT750_4JetPt50_v1 -c "hltPrePFHT7504JetPt50.offset=cms.uint32( 0 )" "hltHtMht4JetPt50.minPtJetHt=cms.double( 40.0 )" "hltPFHT4JetPt50.minPtJetHt=cms.double( 40.0 )" -r "4JetPt40" -o hlt_tmp2.py



./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 0.0 )" -r "TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )"  "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 0.0 )" -r "" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double(  5.0 )" -r "TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 10.0 )" -r "TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 15.0 )" -r "TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 20.0 )" -r "TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 25.0 )" -r "TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 30.0 )" -r "TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 35.0 )" -r "TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 40.0 )" -r "TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 45.0 )" -r "TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 50.0 )" -r "TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 55.0 )" -r "TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 60.0 )" -r "TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 65.0 )" -r "TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 70.0 )" -r "TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 75.0 )" -r "TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 80.0 )" -r "TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 85.0 )" -r "TrimMass85" -o hlt_tmp2.py


./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 0.0 )" -r "PFHT650_TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double(  5.0 )" -r "PFHT650_TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 10.0 )" -r "PFHT650_TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 15.0 )" -r "PFHT650_TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 20.0 )" -r "PFHT650_TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 25.0 )" -r "PFHT650_TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 30.0 )" -r "PFHT650_TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 35.0 )" -r "PFHT650_TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 40.0 )" -r "PFHT650_TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 45.0 )" -r "PFHT650_TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 50.0 )" -r "PFHT650_TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 55.0 )" -r "PFHT650_TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 60.0 )" -r "PFHT650_TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 65.0 )" -r "PFHT650_TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 70.0 )" -r "PFHT650_TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 75.0 )" -r "PFHT650_TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 80.0 )" -r "PFHT650_TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 550.0 )" "hltPFHT700.minHt=cms.vdouble( 650.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 85.0 )" -r "PFHT650_TrimMass85" -o hlt_tmp2.py


./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 0.0 )" -r "PFHT600_TrimMass00" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double(  5.0 )" -r "PFHT600_TrimMass05" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 10.0 )" -r "PFHT600_TrimMass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 15.0 )" -r "PFHT600_TrimMass15" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 20.0 )" -r "PFHT600_TrimMass20" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 25.0 )" -r "PFHT600_TrimMass25" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 30.0 )" -r "PFHT600_TrimMass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 35.0 )" -r "PFHT600_TrimMass35" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 40.0 )" -r "PFHT600_TrimMass40" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 45.0 )" -r "PFHT600_TrimMass45" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 50.0 )" -r "PFHT600_TrimMass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 55.0 )" -r "PFHT600_TrimMass55" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 60.0 )" -r "PFHT600_TrimMass60" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 65.0 )" -r "PFHT600_TrimMass65" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 70.0 )" -r "PFHT600_TrimMass70" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 75.0 )" -r "PFHT600_TrimMass75" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 80.0 )" -r "PFHT600_TrimMass80" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_PFHT700_AK8TrimMass50_v1 -c "hltPrePFHT700AK8TrimMass50.offset=cms.uint32( 0 )" "hltHT600.minHt=cms.vdouble( 500.0 )" "hltPFHT700.minHt=cms.vdouble( 600.0 )" "hlt1AK8PFJetsTrimR0p1PT0p03Mass50.MinMass=cms.double( 85.0 )" -r "PFHT600_TrimMass85" -o hlt_modified.py


