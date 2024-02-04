# Generating Poison Data with SeqPoison after Clustering

After clustering, SeqPoison is used to generate poison data. The clustered dataset is located in the `dataset` folder. Follow the steps below to generate poison data:

1. First, run `train_classify.py` on the clustered dataset.

2. Next, run `main.py`.

3. Finally, we obtain a generator for generating fake users. Run `generate_data.py` to generate a batch of poison data.

    Note: When selecting a poison data from this batch, we need to run `filter.py` for data filtering. Then choose a fake user close to the average length of the target cluster.

Make sure you have all the necessary dependencies installed before running the scripts.

