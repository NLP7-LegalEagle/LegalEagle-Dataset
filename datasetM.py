import pandas as pd

class DatasetM:
    def __init__(self, file):
        self.file_paths = file

    def merge(self, max_length=None):
        for file in self.file_paths:
            df = self.read_csv(file)
            df['result'] = df.apply(lambda df: DatasetM.format_instruction(df), axis=1)
            df = self.drop_columns(df, ['input', 'output'])
            if max_length is not None:
                mask = df.apply(lambda x: len(x[0]) < max_length, axis=1)
                df = df[mask]
            self.save_csv(df, file, max_length)

    @staticmethod
    def format_input_output(sample):
        return f"<s>[INST] {sample['input']} [/INST] {sample['output']} </s>"

    @staticmethod
    def format_instruction(sample):
        return f"""### Instruction:
    Use the Input below to create an instruction, which could have been used to generate the input using an LLM.

    ### Input:
    {sample['input']}

    ### Response:
    {sample['output']}
    """

    def read_csv(self, file):
        return pd.read_csv(file)

    def drop_columns(self, df, columns):
        return df.drop(columns=columns)
    
    def save_csv(self, df, file_path, tag):
        file_name = file_path.split('/')[2].split('.')[0]
        if tag is not None:
            file_name += f"_{tag}"
        file_path = "./instruction_datasets/" + file_name +".csv"
        #print(file_name)
        df.to_csv(file_path, index=False)
    

file_path = ["./datasets/dataset_test.csv",
            "./datasets/dataset_train.csv",
            "./datasets/dataset_validation.csv"]


data_processor = DatasetM(file_path)
data_processor.merge(1024)
