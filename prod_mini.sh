#!/bin/bash

export nEvents=$2
export Higgs_mass=$1

echo "Higgs mass: $Higgs_mass"
echo "nEvents: $nEvents"

export SCRAM_ARCH=slc7_amd64_gcc820;
echo $VO_CMS_SW_DIR;
source $VO_CMS_SW_DIR/cmsset_default.sh;
cd /home/cms/${USER}/prod_nano/CMSSW_10_2_22/src;
pwd
cmsenv

cmsDriver.py step3 --python_filename Step_MiniAOD_cfg_"$Higgs_mass"_.py --conditions auto:phase1_2017_realistic --fast  -n "$nEvents" --era Run2_2017_FastSim --eventcontent MINIAODSIM --runUnscheduled  --filein file:/gridgroup/cms/htt/shared_files/Data/AODSIM/Htt_"$Higgs_mass"_AODSIM.root --fileout file:/gridgroup/cms/htt/shared_files/Data/MiniAODSIM/Htt_"$Higgs_mass"_MiniAODSIM.root -s PAT --datatier MINIAODSIM --mc


