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
    run=2016
    era=$run
    PU_suffix=""
else
    run=${PU_YEAR}
    era=$run
    PU_suffix="_PU"
    if [[ ${PU_YEAR} == 2016 ]]
    then
        pileup_cfg=2016_25ns_Moriond17MC_PoissonOOTPU
    elif [[ ${PU_YEAR} == 2017 ]]
    then
        era=${era}_FastSim
        pileup_cfg=2017_25ns_WinterMC_PUScenarioV1_PoissonOOTPU
    elif [[ ${PU_YEAR} == 2018 ]]
    then
        era=${era}_FastSim
        pileup_cfg=2018_25ns_JuneProjectionFull18_PoissonOOTPU
    fi
fi

if [[ ${PU_YEAR} == 0 ]]
then
    cmsDriver.py H"$Higgs_mass"GGgluonfusion_13TeV_TuneCUETP8M1_cfi --python_filename Step_AOD_cfg_"$Higgs_mass"_PU"$PU_YEAR"_.py --conditions auto:run2_mc --fast -n "$nEvents" --era Run2_2016 --eventcontent AODSIM --relval 100000,500 --step GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO --beamspot Realistic50ns13TeVCollision --datatier AODSIM --fileout /gridgroup/cms/htt/shared_files/Data/AODSIM/Htt_"$Higgs_mass"_PU"$PU_YEAR"_AODSIM.root
else
    cmsDriver.py H"$Higgs_mass"GGgluonfusion_13TeV_TuneCUETP8M1_cfi --python_filename Step_AOD_cfg_"$Higgs_mass"_PU"$PU_YEAR"_.py --conditions auto:run2_mc --fast -n "$nEvents" --era Run2_2016 --eventcontent AODSIM --relval 100000,500 --step GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO --beamspot Realistic50ns13TeVCollision --datatier AODSIM --pileup_input file:/gridgroup/cms/htt/shared_files/Data/PU_mixing/MinBias_13TeV_pythia8_TuneCUETP8M1_cfi_GEN_SIM_RECOBEFMIX.root --pileup "$pileup_cfg" --fileout /gridgroup/cms/htt/shared_files/Data/AODSIM/Htt_"$Higgs_mass"_PU"$PU_YEAR"_AODSIM.root
fi



