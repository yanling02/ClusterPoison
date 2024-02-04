# ClusterPoison

It is a widely applicable poisoning attack scheme for recommender systems

ClusterPoison is a versatile solution applicable to current poisoning attacks targeting RS. The objective of this scheme is to maximize the impact of a single fake user.

The process involves the following steps:

1. **Clustering**: Utilize clustering methods to cluster the original dataset.

2. **Poison Generation**: Employ poisoning attacks to generate poison data from the largest cluster obtained after clustering.

3. **Filtering**: Select a single fake user through filtering.

Our scheme can be applied to both SeqPoison and RecommPoison. Theoretically, it can also be applied similarly to other poisoning attacks.
