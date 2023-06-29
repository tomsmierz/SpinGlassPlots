import pandas as pd
import os
from tqdm import tqdm

cwd = os.getcwd()
folder_path = os.path.join(cwd, "results")

dataframes = []
max_sweep = []
replicas = []
beta_min = []
beta_max = []

for file_name in tqdm(os.listdir(folder_path)):
    file_path = os.path.join(folder_path, file_name)
    if file_name.endswith('.txt'):
        parameters = file_name.split("_")

        df = pd.read_csv(file_path)
        df["max_sweeps"] = parameters[1]
        df["replicas"] = parameters[2]
        df["beta_min"] = parameters[3]
        df["beta_max"] = os.path.splitext(parameters[4])[0] # remove extension
        dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)
combined_df_sorted = combined_df.sort_values("energy", ascending=False)
combined_df_sorted.to_csv("P8_optim_res.csv")
