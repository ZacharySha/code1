import geopandas as gpd
import pandas as pd


csv_data_shate = pd.read_csv('/Users/shate/Desktop/paper/code/build_data/aaall_water.csv')
shapefile_shate = gpd.read_file('/Users/shate/Desktop/paper/code/data/grid_data/grids_over10urban.shp')
result_shate = shapefile_shate.merge(csv_data_shate, on='Id', how='inner')
result_shate.to_file('all_grids_2018.shp')


# csv_data_yuejie = pd.read_csv('/Users/shate/Desktop/paper/code/data/fwater_withcoast_withouturban/all_yuejie.csv')
# shapefile_yuejie = gpd.read_file('/Users/shate/Desktop/paper/code/data/shp/zyj_grid.shp')
# result_yuejie = shapefile_yuejie.merge(csv_data_yuejie, on='Id', how='inner')
# result_yuejie.to_file('yuejie.shp')
