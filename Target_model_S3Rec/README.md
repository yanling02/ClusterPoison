
# Poisoning Target Recommender System with Single Fake User Data

After generating poison data with only one fake user, it can be used to poison the target Recommender System (RS). Follow the steps below:

1. Run `run_pretrain.py` to generate poison data.

2. Next, execute `run_finetune_sample.py` to generate metrics for target items.

    Note: You can modify the item for which metrics are generated in `dataset.py`.
