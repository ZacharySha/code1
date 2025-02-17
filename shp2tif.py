from osgeo import ogr, gdal
import glob
import os
from tqdm import tqdm


def vector_to_tiff(input_vector, output_tiff, field_name):
    # Open the vector file
    vector_ds = ogr.Open(input_vector)
    if vector_ds is None:
        print(f"Failed to open {input_vector}")
        return

    # Get the layer
    layer = vector_ds.GetLayer()

    # Get the extent of the layer
    extent = layer.GetExtent()

    # Create a raster dataset
    pixel_size = 1000  # Set the pixel size (modify according to your needs)
    x_res = int((extent[1] - extent[0]) / pixel_size)
    y_res = int((extent[3] - extent[2]) / pixel_size)

    target_ds = gdal.GetDriverByName('GTiff').Create(output_tiff, x_res, y_res, 1, gdal.GDT_Float32)

    # Set the spatial reference system
    target_ds.SetProjection(layer.GetSpatialRef().ExportToWkt())
    target_ds.SetGeoTransform((extent[0], pixel_size, 0, extent[3], 0, -pixel_size))

    # Get the raster band
    band = target_ds.GetRasterBand(1)
    band.SetNoDataValue(-9999)  # Set NoData value (modify according to your needs)

    # Rasterize the layer based on the specified field
    gdal.RasterizeLayer(target_ds, [1], layer, options=["ATTRIBUTE=" + field_name])

    # Close datasets
    target_ds = None
    vector_ds = None

    # print(f"Rasterization completed. Output TIFF: {output_tiff}")



if __name__ == '__main__':
    field_name = "gaia"
    out_tif_path = "/Users/shate/Desktop/tif/gaia_tif"
    shp_list = glob.glob("/Users/shate/Desktop/each_city_2000_1029/*.shp")
    for input_vector in tqdm(shp_list):
        output_tiff_name = input_vector.split("/")[-1].replace("shp","tif")
        output_tiff = os.path.join(out_tif_path,output_tiff_name)
        vector_to_tiff(input_vector, output_tiff, field_name)