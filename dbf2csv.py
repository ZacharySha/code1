#-*- coding : utf-8-*-
import csv
from dbfread import DBF
import glob
import os
from tqdm import tqdm


def dbf2csv(dbf_path,outcsv_path):
    dbf_list = glob.glob(os.path.join(dbf_path,"*.dbf"))
    for table in tqdm(dbf_list):
        csv_name = table.split("/")[-1].split(".")[0] + ".csv"
        outcsvpath = os.path.join(outcsv_path,csv_name)
        # 创建CSV文件并写入数据
        with open(outcsvpath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # 写入表头
            table = DBF(table, encoding='utf-8')
            writer.writerow(table.field_names)
            # # 写入每行数据
            for record in table:
                writer.writerow(list(record.values()))



        # print('处理结束')

if __name__ == '__main__':
    dbf_path = "/Users/shate/Desktop/dbf"
    outcsv_path = "/Users/shate/Desktop/dbf"
    dbf2csv(dbf_path,outcsv_path)