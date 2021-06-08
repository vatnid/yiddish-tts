#!/bin/sh

#SBATCH --gres=gpu:1

nvidia-smi

echo $CUDA_VISIBLE_DEVICES
source /home/s2122322/anaconda2/bin/activate
conda activate dctts
echo Conda environment dctts activated

echo TEST DONE