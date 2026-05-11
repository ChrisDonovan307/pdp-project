#!/bin/bash

#SBATCH --partition=short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=2G
#SBATCH --time=1:00
#SBATCH --job-name=pdp_test
#SBATCH --output=output/%x_%j.out
#SBATCH --mail-type=NONE


cd /gpfs1/home/c/d/cdonov12/pdp_testing/pdp_proj/task-1

python src/main.py

echo "======" >> log.txt
echo "node: $(hostname)" >> log.txt
echo "Job ID: $SLURM_JOB_ID" >> log.txt
echo -e "Finished: $(date)\n" >> log.txt
