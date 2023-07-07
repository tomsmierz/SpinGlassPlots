import pandas as pd
import os
from tqdm import tqdm

cwd = os.getcwd()
folder_path = os.path.join(cwd, "P16_truncate_2_20_i21+")
old_dataframe_path = os.path.join(cwd, "data", "P16_CBFM-P_tr2^20.csv")

dataframes = []

for file_name in tqdm(os.listdir(folder_path)):
    file_path = os.path.join(folder_path, file_name)
    if file_name.endswith('.csv'):
        df = pd.read_csv(file_path, sep=";")
        dataframes.append(df)


old_df = pd.read_csv(old_dataframe_path, sep=";")
combined_df = pd.concat(dataframes, ignore_index=True)
combined_df = pd.concat([combined_df, old_df], ignore_index=True)

combined_df.to_csv("P16_CBFM-P_tr2^20_new.csv", sep=";")
