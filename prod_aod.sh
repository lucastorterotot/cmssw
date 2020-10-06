#!/bin/bash

export nEvents=$2
export Higgs_mass=$1

echo "Higgs mass: $Higgs_mass"
echo "nEvents: $nEvents"

export SCRAM_ARCH=slc7_amd64_gcc820;
echo $VO_CMS_SW_DIR;
source $VO_CMS_SW_DIR/cmsset_default.sh;
cd /home/cms/asilar/prod_nano/CMSSW_10_2_22/src;
pwd
cmsenv

cmsDriver.py H"$Higgs_mass"GGgluonfusion_13TeV_TuneCUETP8M1_cfi --python_filename Step_AOD_cfg_"$Higgs_mass"_.py --conditions auto:run2_mc --fast -n "$nEvents" --era Run2_2016 --eventcontent AODSIM --relval 100000,500 --step GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO --beamspot Realistic50ns13TeVCollision --datatier AODSIM --fileout /gridgroup/cms/htt/shared_files/Data/AODSIM/Htt_"$Higgs_mass"_AODSIM.root


