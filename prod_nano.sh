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

cmsDriver.py step1 --python_filename Step_NanoAOD_cfg_"$Higgs_mass"_.py --filein file:/gridgroup/cms/htt/shared_files/Data/MiniAODSIM/Htt_"$Higgs_mass"_MiniAODSIM.root --fileout file:/gridgroup/cms/htt/shared_files/Data/NanoAODSIM/Htt_"$Higgs_mass"_NanoAODSIM.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions auto:phase1_2017_realistic --step NANO --fast --era Run2_2017_FastSim -n "$nEvents"

