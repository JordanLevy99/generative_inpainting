#!/bin/bash
INPUT_IMAGE="notebooks/imgs/$1/input_$2.png"
MASK_IMAGE="notebooks/imgs/$1/mask_$2.png"
OUTPUT_IMAGE="/home/jdlevy/DSC_180B/generative_inpainting/notebooks/out/$1/output_$2.png"
CHECKPOINT="logs/$3"
cd ..

python test.py --image $INPUT_IMAGE --mask $MASK_IMAGE --output $OUTPUT_IMAGE --checkpoint_dir $CHECKPOINT