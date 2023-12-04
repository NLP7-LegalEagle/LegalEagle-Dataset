import pandas as pd


class DatasetController:
    casehold_file_paths = ["./casehold/casehold_test.csv",
                           "./casehold/casehold_train.csv",
                           "./casehold/casehold_val.csv"]
    judgement_file_paths = ["./judgement/judgement_train.csv"]

    def __init__(self):
        headers = ["input", "output"]
        datasets = [self.load_dataset(self.casehold_file_paths, headers),
                    self.load_dataset(self.judgement_file_paths, headers)]
        ratio = (0.8, 0.1, 0.1)
        dataset_dict = {"train":[],
                        "validation": [],
                        "test": []}
        for dataset in datasets:
            dataset = self.split_dataset(dataset, ratio)
            dataset_dict["train"].append(dataset[0])
            dataset_dict["validation"].append(dataset[1])
            dataset_dict["test"].append(dataset[2])
        print( pd.concat(dataset_dict["train"]))
        self.train_dataset = pd.concat(dataset_dict["train"])
        self.validation_dataset = pd.concat(dataset_dict["validation"])
        self.test_dataset = pd.concat(dataset_dict["test"])

    def load_dataset(self, file_paths, headers):
        datasets = pd.DataFrame(columns=headers)
        for file_path in file_paths:
            dataset = pd.read_csv(file_path)
            dataset.columns = headers
            datasets = pd.concat([datasets, dataset])
        return datasets

    def split_dataset(self, dataset, ratio):
        if sum(ratio) > 1.0:
            return
        start_ratio = 0
        end_ratio = 0

        datasets = []
        for i, r in enumerate(ratio):
            end_ratio += r
            start_index = int(len(dataset) * start_ratio)
            end_index = int(len(dataset) * end_ratio)
            print(start_index, end_index)
            datasets.append(dataset[start_index:end_index])
            start_ratio = end_ratio
        return datasets

    def save(self, directory_path):
        self.train_dataset.to_csv(f"{directory_path}/dataset_train.csv", index=False)
        self.validation_dataset.to_csv(f"{directory_path}/dataset_validation.csv", index=False)
        self.test_dataset.to_csv(f"{directory_path}/dataset_test.csv", index=False)

controller = DatasetController()
# controller.save("./datasets")


# f"<s>[INST] {input} [/INST] output </s>"
