#!/bin/bash
#SBATCH --job-name=arrayjob_calc_gc
#SBATCH --cpus-per-task=1
#SBATCH --array=1-10
#SBATCH --mail-type=ALL
#SBATCH --mail-user=[add_username_here]@mrclmb.ac.uk

SAMPLE_ID=$((SLURM_ARRAY_TASK_ID))
echo $SAMPLE_ID
python3 calc_gc.py sample.$SAMPLE_ID.fa.gz
