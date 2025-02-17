import pandas as pd
import glob
import os
from tqdm import tqdm

def extend_data(df_path1, all_path):
    df_list1 = glob.glob(os.path.join(df_path1,"*.csv"))
    for i in tqdm(range(len(df_list1)-1)):
        # df1 = pd.read_csv(df_list[i]).drop(columns=['COUNT', 'AREA'])
        # df2 = pd.read_csv(df_list[i+1]).drop(columns=['COUNT', 'AREA'])
        df1 = pd.read_csv(df_list1[i])
        df2 = pd.read_csv(df_list1[i+1])[["Id","hm","pop","time2city"]]
        # 使用merge方法将两个DataFrame合并，通过"id"列匹配
        if i == 0:
            merged_df = df1.merge(df2, on="ORIG_FID", how="inner")
        else:
            merged_df = merged_df.merge(df2, on="ORIG_FID", how="inner")

    merged_df.to_csv(all_path, index=False)
    # 打印合并后的DataFrame
    print(merged_df)


if __name__ == '__main__':

    path1 = "/Users/shate/Desktop/paper/code/build_data/季节_partial_cor_2018.csv"
    path2 = "/Users/shate/Desktop/paper/result/GCCM_results/季节2018/季节gccm_results2018.csv"
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)
    # df2 = pd.read_csv(path2)[pd.read_csv(path2)['year'] == 2000]
    merged_df = df2.merge(df1, on="ORIG_FID", how="inner")
    merged_df.to_csv("/Users/shate/Desktop/output.csv", index=False)