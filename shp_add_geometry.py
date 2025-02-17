import geopandas as gpd
import glob
import os
from tqdm import tqdm

def add_xy(shp_path,save_path):
    gdf = gpd.read_file(shp_path)

    gdf['x_1'] = gdf.geometry.centroid.x
    gdf['y_1'] = gdf.geometry.centroid.y

    # print(gdf.head())
    gdf.to_file(save_path)

if __name__ == '__main__':
    output_shp_file = "/Users/shate/Desktop/data_2000_10_18/data2018/each_city_2018_xy"
    shp_file = "/Users/shate/Desktop/data_2000_10_18/data2018/each_city_2018/*.shp"
    shp_list = glob.glob(shp_file)
    for shp_path in tqdm(shp_list):
        name = shp_path.split("/")[-1]
        save_path = os.path.join(output_shp_file,name)
        add_xy(shp_path,save_path)
