#!/bin/bash

export PU_YEAR=$3
export nEvents=$2
export Higgs_mass=$1

echo "Higgs mass: $Higgs_mass"
echo "nEvents: $nEvents"
echo "PU: $PU_YEAR"

export SCRAM_ARCH=slc7_amd64_gcc820;
echo $VO_CMS_SW_DIR;
source $VO_CMS_SW_DIR/cmsset_default.sh;
cd /home/cms/torterotot/prod_nano/CMSSW_10_2_22/src;
pwd
cmsenv

if [[ ${PU_YEAR} == 0 ]]
then
    era=Run2_2017_FastSim
elif [[ ${PU_YEAR} == 2016 ]]
then
    era=Run2_2016
elif [[ ${PU_YEAR} == 2017 ]]
then
    era=Run2_2017_FastSim
elif [[ ${PU_YEAR} == 2018 ]]
then
    era=Run2_2018_FastSim
fi

cmsDriver.py step3 --python_filename Step_MiniAOD_cfg_"$Higgs_mass"_PU"$PU_YEAR"_.py --conditions auto:phase1_2017_realistic --fast  -n "$nEvents" --era "$era" --eventcontent MINIAODSIM --runUnscheduled  --filein file:/gridgroup/cms/htt/shared_files/Data/AODSIM/Htt_"$Higgs_mass"_PU"$PU_YEAR"_AODSIM.root --fileout file:/gridgroup/cms/htt/shared_files/Data/MiniAODSIM/Htt_"$Higgs_mass"_PU"$PU_YEAR"_MiniAODSIM.root -s PAT --datatier MINIAODSIM --mc


