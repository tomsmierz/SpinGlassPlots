import pandas as pd
import os
from tqdm import tqdm

cwd = os.getcwd()
folder_path = os.path.join(cwd, "P8_CBFM-P")

dataframes = []
instance = []

for file_name in tqdm(os.listdir(folder_path)):
    file_path = os.path.join(folder_path, file_name)
    if file_name.endswith('.txt'):
        name = str(file_name).replace(".txt", "")
        instance.append(name)
        df = pd.read_csv(file_path)
        dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)
combined_df["instance"] = instance
combined_df.to_csv("P8_CFBM-P_pt.csv", sep=";")
