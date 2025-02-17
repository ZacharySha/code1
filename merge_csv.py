import glob
import pandas as pd
from tqdm import tqdm

def merge_csv_files(dir_list, year, target_name):

    df_list = []
    for dir in dir_list:
        df = pd.read_csv(dir)
        if "batch_0" in dir:
            df_list.append(df[:])
        else:
            df_list.append(df[1:])

    merged_df = pd.concat(df_list, ignore_index=True)

    # output_file = f"/Users/shate/Desktop/paper/code/data/climate/{target_name}/result/{target_name}_{year}.csv"  # here
    output_file = f"/Users/shate/Desktop/prepared/poptable/{target_name}_{year}.csv"
    merged_df.to_csv(output_file, index=False)

def merge_csv(dir_list):
    df_list = []
    for i, dir in tqdm(enumerate(dir_list)):
        # df = pd.read_csv(dir)[['Id','gaia_count_2000','p_count_2000','pop_2000','s_count_2000']]
        df = pd.read_csv(dir)
        if i == 0:
            df_list.append(df[:])
        else:
            df_list.append(df[:])
    merged_df = pd.concat(df_list, ignore_index=True)
    # output_file = f"/Users/shate/Desktop/paper/code/data/climate/{target_name}/result/{target_name}_{year}.csv"  # here
    output_file = "aaall_water.csv"
    merged_df.to_csv(output_file, index=False)


if __name__ == '__main__':
    # inlist = glob.glob("/Users/shate/Desktop/gisa_gsw/*.csv")  #here
    # target_name = "all_water"
    # merge_csv(inlist)
    inlist = glob.glob("/Users/shate/Desktop/data_2018/*.csv")  #here
    target_name = "all_water"
    merge_csv(inlist)
    # f = pd.read_csv('./all_water2000.csv')
    # print("a")
    # for y in range(2000,2019):
    #     new_list = []
    #     for i in inlist:
    #         if str(y) in i:
    #             new_list.append(i)
    #     merge_csv_files(new_list,y,target_name)