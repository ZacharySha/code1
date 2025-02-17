import pandas as pd
import numpy as np
from tqdm import tqdm


def main_factor_proportion(csv_path):
    name = csv_path.strip().split("/")[-1].split(".")[0] +'_new_column.csv'
    df = pd.read_csv(csv_path)
    df = df[df['r2']!=1]
    for index, row in df.iterrows():
        interested_data = row
        max_value = np.array([row['gaia'],row['e'],row['pr'],row['tem']]).max()
        if max_value == row['gaia']:
            df.at[index, 'main_factor'] = "gaia"
        if max_value == row['e']:
            df.at[index, 'main_factor'] = "e"
        if max_value == row['pr']:
            df.at[index, 'main_factor'] = "pr"
        if max_value == row['tem']:
            df.at[index, 'main_factor'] = "tem"

    gaia_proportion = len(df[df['main_factor'] == 'gaia'])/len(df)
    e_proportion = len(df[df['main_factor'] == 'e'])/len(df)
    pr_proportion = len(df[df['main_factor'] == 'pr'])/len(df)
    tem_proportion = len(df[df['main_factor'] == 'tem'])/len(df)

    gaia_mean = df['gaia'].mean()
    e_mean = df['e'].mean()
    pr_mean = df['pr'].mean()
    tem_mean = df['tem'].mean()


    print(gaia_proportion*len(df), e_proportion*len(df), pr_proportion*len(df), tem_proportion*len(df),"    ", gaia_mean,e_mean,pr_mean,tem_mean)



    df.to_csv(name, index=False)


if __name__ == '__main__':
    csv_path2000 = "./RF2000_s.csv"
    csv_path2010 = "./RF2010_s.csv"
    csv_path2018 = "./RF2018_s.csv"

    main_factor_proportion(csv_path2000)
    main_factor_proportion(csv_path2010)
    main_factor_proportion(csv_path2018)

    print(" ")
    csv_path2000 = "./RF2000_p.csv"
    csv_path2010 = "./RF2010_p.csv"
    csv_path2018 = "./RF2018_p.csv"

    main_factor_proportion(csv_path2000)
    main_factor_proportion(csv_path2010)
    main_factor_proportion(csv_path2018)