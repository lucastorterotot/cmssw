#!/bin/bash

Higgs_mass=125
N_events=default
PU_YEAR=2017

while getopts ":m:N:P:" opt
do
    case $opt in
        m) Higgs_mass="$OPTARG"
            ;;
        N) N_events="$OPTARG"
           ;;
        P) PU_YEAR="$OPTARG"
           ;;
        \?) echo "Invalid option -$OPTARG" >&2
            ;;
    esac
done


if [[ ${N_events} == default ]]
then
    if [[ ${Higgs_mass} < 300 ]]
    then
        N_events=60000
    elif [[ ${Higgs_mass} < 500 ]]
    then
        N_events=20000
    else
        N_events=10000
    fi
fi

mkdir -p /home/cms/${USER}/slurmJobs/

sbatch --job-name=HTT_gen_${Higgs_mass}GeV_PU${PU_YEAR} --output=/home/cms/${USER}/slurmJobs/submitted_${Higgs_mass}_PU${PU_YEAR} --mail-type=ALL --mail-user=${USER}@ipnl.in2p3.fr submit_single.sh ${Higgs_mass} ${N_events} ${PU_YEAR}
