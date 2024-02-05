# ClusterPoison

It is a widely applicable poisoning attack scheme for recommender systems

ClusterPoison is a versatile solution applicable to current poisoning attacks targeting RS. The objective of this scheme is to maximize the impact of a single fake user.

The process involves the following steps:

1. **Clustering**: Utilize clustering methods to cluster the original dataset.

2. **Poisoning Data Generation**: Employ poisoning attacks to generate poison data from the largest cluster obtained after clustering.

3. **Filtering**: Select a single fake user through filtering.

Our scheme can be applied to both SeqPoison and RecommPoison. Theoretically, it can also be applied similarly to other poisoning attacks.


# ClusterPoison Dataset

This repository contains datasets generated using ClusterPoison combined with different poisoning attack methods, as well as model files used for pretraining the target model.

## Dataset Directory Structure

- **ClusterPoison+SeqPoison Dataset**: Contains datasets generated using ClusterPoison combined with SeqPoison. Each original dataset includes one fake user.
  - Directory Path: `/ClusterPoison_datasets/ClusterPoison+SeqPoison`

- **ClusterPoison+RecommPoison Dataset**: Contains datasets generated using ClusterPoison combined with RecommPoison. Each original dataset includes one fake user.
  - Directory Path: `/ClusterPoison_datasets/ClusterPoison+Recomm`

- **Baseline Dataset**: Contains datasets generated using baseline methods. Each original dataset includes one fake user.
  - Directory Path: `/ClusterPoison_datasets/baseline`

## Pretrained Model on Target Model

In the `/Target_model_S3Rec/output` directory, you can find model files pretrained on the target model.

## Reproducing Experimental Results

You can use the `/Target_model_S3Rec/run_finetune_sample.py` script to reproduce our experimental results. This script can be used for fine-tuning on the pretrained model.

