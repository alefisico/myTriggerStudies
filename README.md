# My Trigger Studies

* Most of the things here are based on the new openHLT (https://github.com/jiafulow/HLTrigger-HLTanalyzers-test-openHLT) 
* Trigger Rates with: test/GetRates.py (you need log files from openHLT Filter)


To reproduce these results:
```
export SCRAM_ARCH=slc6_amd64_gcc481
cmsrel CMSSW_7_4_0
cd CMSSW_7_4_0/src
cmsenv
git cms-addpkg HLTrigger/Configuration
git clone https://github.com/alefisico/myTriggerStudies.git MyTrigger/myTriggerStudies -b v740
git clone git@github.com:jiafulow/HLTrigger-HLTanalyzers-test-openHLT.git MyTrigger/myTriggerStudies/test/openHLT
scramv1 b -j 18
cmsenv 
```
