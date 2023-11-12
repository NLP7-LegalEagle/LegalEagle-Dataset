import pandas as pd

class DatasetM:
    def __init__(self, file):
        self.file_paths = file

    def merge(self):
        for file in self.file_paths:
            df = self.read_csv(file)
            df['result'] = df.apply(lambda df: f"<s>[INST] {df['input']} [/INST] {df['output']} </s>", axis=1)
            df = self.drop_columns(df, ['input', 'output'])
            self.save_csv(df, file)

    def read_csv(self, file):
        return pd.read_csv(file)

    def drop_columns(self, df, columns):
        return df.drop(columns=columns)
    
    def save_csv(self, df, file_path):
        file_name = "./datasetsMerge/" + file_path.split('/')[2] 
        #print(file_name)
        df.to_csv(file_name, index=False)
    

file_path = ["./datasets/dataset_test.csv",
            "./datasets/dataset_train.csv",
            "./datasets/dataset_validation.csv"]


data_processor = DatasetM(file_path)
data_processor.merge()
