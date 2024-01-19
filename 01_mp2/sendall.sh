#!/bin/bash
for i in {0..16}
do
    sbatch -J hf_geom_${i} hf.sh $i
done
