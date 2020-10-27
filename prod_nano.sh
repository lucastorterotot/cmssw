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
cd /home/cms/${USER}/prod_nano/CMSSW_10_2_22/src;
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

mkdir -p /gridgroup/cms/htt/shared_files/Data/NanoAODSIM/nevents_${nEvents}_PU${PU_YEAR}/

cmsDriver.py step1 --python_filename Step_NanoAOD_cfg_"$Higgs_mass"_PU"$PU_YEAR"_.py --filein file:/gridgroup/cms/htt/shared_files/Data/MiniAODSIM/Htt_"$Higgs_mass"_PU"$PU_YEAR"_MiniAODSIM.root --fileout file:/gridgroup/cms/htt/shared_files/Data/NanoAODSIM/nevents_"$nEvents"_PU"$PU_YEAR"/Htt_"$Higgs_mass"_PU"$PU_YEAR"_NanoAODSIM.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions auto:phase1_2017_realistic --step NANO --fast --era "$era" -n "$nEvents"

