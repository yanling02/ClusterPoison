
# Generating Poison Data with RecommPoison after Clustering

After clustering, RecommPoison is used to generate poison data. The clustered dataset is located in the `dataset` folder.

To generate poison data:

1. Run `main.py`.

2. Afterwards, run `filter` to screen fake users.

    Note: RecommPoison generates item sequences of equal length and appends the target item to the end of the sequence. Therefore, the purpose of the filter is to compute the similarity between the embeddings of the generated poison data and the embeddings of all users in the target cluster to identify the user most similar to the target cluster.
