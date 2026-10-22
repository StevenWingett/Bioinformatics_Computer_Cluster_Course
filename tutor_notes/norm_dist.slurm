#!/bin/bash
#SBATCH --job-name=Rscript_job
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=[add_username_here]@mrclmb.ac.uk
#SBATCH --mem=30G

# Bash command
module load R/4.5.1
Rscript norm_dist_1_billion.R
