import os
from glob import glob
import pandas as pd
import csv
from tqdm import tqdm

csv_dir = "/Users/shate/Desktop/paper/result/GCCM_results/季节2018/季节地表水2018/*.csv"

csv_list = glob(csv_dir)

with open('/Users/shate/Desktop/paper/result/GCCM_results/季节2018/季节gccm_results2018.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ORIG_FID', 'lib', 'x_xmap_y_means', 'x_xmap_y_Sig', 'y_xmap_x_means', 'y_xmap_x_Sig'])

    for csv_path in tqdm(csv_list):
        df = pd.read_csv(csv_path)
        # col = df.columns
        # print(col)

        lib_id = df["Unnamed: 0"]
        # print(lib_id.values)

        for i, id in enumerate(lib_id):
            if id > 500:
                row_id = lib_id[i-1]
            else:
                row_id = lib_id[len(lib_id)-1]

        df = df[df['Unnamed: 0'] == row_id]



        x_xmap_y_means = df['x_xmap_y_means'].values[0]
        x_xmap_y_Sig = df['x_xmap_y_Sig'].values[0]

        y_xmap_x_means = df['y_xmap_x_means'].values[0]
        y_xmap_x_Sig = df['y_xmap_x_Sig'].values[0]

        uid = csv_path.split("/")[-1].split("_")[1]

        writer.writerow([uid, row_id, x_xmap_y_means, x_xmap_y_Sig, y_xmap_x_means, y_xmap_x_Sig])