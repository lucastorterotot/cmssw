#!/bin/bash
# submit_array.sh
#
#SBATCH --job-name=NANOprod
#
# mail-type=BEGIN, END, FAIL, REQUEUE, ALL, STAGE_OUT, TIME_LIMIT_90
#SBATCH --mail-type=ALL
#SBATCH --mail-user=${USER}@ipnl.in2p3.fr

echo
echo
echo -n "Hostname:              " ; hostname -f
echo -n "Uptime:                " ; uptime
echo
echo -n "Je suis:               "; id -a
echo

oldLANG=$LANG
LANG=fr_FR.iso88591
date
echo
temps=$(grid-proxy-info -timeleft 2>/dev/null)
if [ $? == 0 ]; then
  echo -n "Temps restant : $temps secondes, soit dans "; date -u -d @"$temps" +'%-Hh %-Mm %-Ss'
  echo -n "Le proxy expirera le "; date -d "now + $temps seconds" +"%A %d %B a %T"
else
  echo "Pas de proxy valide"
fi

LANG=$oldLANG

# Check if Globus certificate is expiring soon
CERT="$HOME/.globus/usercert.pem"
which openssl > /dev/null 2>&1
if [ $? == 0 ]; then
  if [ -r "$CERT" ]; then
    openssl x509 -in "$CERT" -noout -checkend 0 > /dev/null 2>&1
    if [ $? == 1 ]; then
      MSG="Your certificate has expired"
    else
      #604800=60*60*24*7
      openssl x509 -in "$CERT" -noout -checkend 604800 > /dev/null 2>&1
      if [ $? == 1 ]; then
	MSG="Your certificate is going to expire before one week"
      fi
    fi
  else
    MSG="Can't find certificate $CERT"
  fi
fi


sh prod_aod.sh $SLURM_ARRAY_TASK_ID 10000
sh prod_mini.sh $SLURM_ARRAY_TASK_ID 10000
sh prod_nano.sh $SLURM_ARRAY_TASK_ID 10000

lscpu

echo
echo "espace dans TMPDIR (TMPDIR=$TMPDIR) :"
df -h $TMPDIR

echo
echo "espace dans HOME (HOME=$HOME)"
df -h $HOME

echo
echo "espace dans le repertoire local (.=$PWD)"
df -h $PWD

echo
echo "versions des variables d'environnement MPI : "
env | grep MPI_ | grep VERSION

echo
echo "versions des librairies MPI : "
rpm -qa|grep mpi

echo
echo "environnement :"
env


echo "SLURM Input environment variables : "
echo SLURM_JOB_NAME=$SLURM_JOB_NAME
echo SLURM_JOB_NUM_NODES=$SLURM_JOB_NUM_NODES
echo SLURM_MEM_PER_CPU=$SLURM_MEM_PER_CPU
echo SLURM_MEM_PER_NODE=$SLURM_MEM_PER_NODE
echo SLURM_NTASKS=$SLURM_NTASKS
echo SLURM_NTASKS_PER_CORE=$SLURM_NTASKS_PER_CORE
echo SLURM_NTASKS_PER_NODE=$SLURM_NTASKS_PER_NODE
echo SLURM_NTASKS_PER_SOCKET=$SLURM_NTASKS_PER_SOCKET
echo SLURM_THREADS=$SLURM_THREADS
echo SLURM_WORKING_DIR=$SLURM_WORKING_DIR
echo SLURM_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
echo SLURM_ARRAY_TASK_COUNT=$SLURM_ARRAY_TASK_COUNT
echo SLURM_ARRAY_TASK_ID=$SLURM_ARRAY_TASK_ID
echo SLURM_ARRAY_TASK_STEP=$SLURM_ARRAY_TASK_STEP
echo SLURM_ARRAY_JOB_ID=$SLURM_ARRAY_JOB_ID
echo
echo "SLURM Output environment variables : "
echo SLURM_CPUS_ON_NODE=$SLURM_CPUS_ON_NODE
echo SLURM_JOB_CPUS_PER_NODE=$SLURM_JOB_CPUS_PER_NODE
echo SLURM_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
echo SLURM_JOB_ID=$SLURM_JOB_ID
echo SLURM_JOB_NODELIST=$SLURM_JOB_NODELIST
echo SLURM_NTASKS=$SLURM_NTASKS

