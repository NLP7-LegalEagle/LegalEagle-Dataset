import pandas as pd


def dataset_shuffle(dataset_name):
    df = pd.read_csv(f"./datasets/{dataset_name}.csv")
    df = df.sample(frac=1)
    df = df.sample(frac=1).reset_index(drop=True)
    df.to_csv(f"./datasets/{dataset_name}_shuffle.csv")

dataset_shuffle("dataset_validation")
dataset_shuffle("dataset_test")