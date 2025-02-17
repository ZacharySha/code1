import pandas as pd
import glob
import os

def change_header(in_df,out_csv_header,year,target_name):
    df = pd.read_csv(in_df)
    # 获取第一行表头
    headers = df.columns
    # 使用列表推导式将"_p"添加到每个表头
    # new_headers = ['precipitation_' + year + header for header in headers]
    new_headers = []
    for header in headers:
        if header == "MEAN":
            new_headers.append(target_name + '_' + year)
        else:
            new_headers.append(header)

    # new_headers = ['precipitation_' + year]
    # 将新表头替换回DataFrame
    df.columns = new_headers
    # 可选：将修改后的DataFrame保存回CSV文件
    df.to_csv(out_csv_header, index=False)

if __name__ == '__main__':
    target_name = "precipitation"  #here
    # in_path = f"/Users/shate/Desktop/paper/cnu/code/data/climate/{target_name}/result"   #here
    # outpath = f"/Users/shate/Desktop/paper/cnu/code/data/climate/{target_name}/result_with_header"    #here
    in_path = "/Users/shate/Desktop/prepared_data/wind"
    outpath = "/Users/shate/Desktop/prepared_data/after_wind"
    csv_list = glob.glob(os.path.join(in_path,"*.csv"))

    for csv in csv_list:
        year = csv.split("_")[-1].split(".")[0]
        # out_csv_header = os.path.join(outpath,target_name + '_' + year + ".csv")
        out_csv_header = os.path.join(outpath, "grid_batch_12_" + year + ".csv")

        change_header(csv,out_csv_header,year,target_name)