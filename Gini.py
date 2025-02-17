import pandas as pd
import numpy as np


def gini_coefficient(x):
    sorted_x = np.sort(x)
    n = len(x)

    cumulative_x = np.cumsum(sorted_x)
    G = (2 * np.sum((np.arange(1, n + 1) * sorted_x)) - (n + 1) * cumulative_x[-1]) / (n * cumulative_x[-1])
    return G

if __name__ == '__main__':
    csv_path = "/Users/shate/Desktop/paper/code/build_data/shp_data/GUB_9227_s_point2000.csv"
    df = pd.read_csv(csv_path)

    developed = df['GUB_9227_2']==1
    developing = df['GUB_9227_2']==0
    Asia = df['GUB_9227_5'] == "Asia"
    Africa = df['GUB_9227_5'] == "Africa"
    Europe = df['GUB_9227_5'] == "Europe"
    SouthAmerica = df['GUB_9227_5'] == "SouthAmerica"
    NorthAmerica = df['GUB_9227_5'] == "NorthAmerica"
    Oceania = df['GUB_9227_5'] == "Oceania"


    # field = 'y_xmap_x'
    # pos = df['y_xmap_x']>df['x_xmap_y']
    # pos = df['y_xmap_x'] > 0
    # P = df['p_y_xmap_x']<=0.5

    # field = 'P2018GCC_3'
    # pos = df['P2018GCC_3'] > df['P2018GCC_1']
    # pos = df['P2018GCC_3'] > 0
    # P = df['P2018GCC_4'] <= 0.5

    field = 'S2000GCC_3'
    pos = df['S2000GCC_3'] > df['S2000GCC_1']
    pos = df['S2000GCC_3'] > 0
    P = df['S2000GCC_4'] <= 0.5


    Global_pos = df[pos][P]
    Developed_pos = df[developed][pos][P]
    developing_pos = df[developing][pos][P]
    Asia_pos = df[Asia][pos][P]
    Africa_pos = df[Africa][pos][P]
    Europe_pos = df[Europe][pos][P]
    SouthAmerica_pos = df[SouthAmerica][pos][P]
    NorthAmerica_pos = df[NorthAmerica][pos][P]
    Oceania_pos = df[Oceania][pos][P]



    gini_global = gini_coefficient(Global_pos[field])
    gini_developed = gini_coefficient(Developed_pos[field])
    gini_developing = gini_coefficient(developing_pos[field])
    gini_Asia_pos = gini_coefficient(Asia_pos[field])
    gini_Africa_pos = gini_coefficient(Africa_pos[field])
    gini_Europe_pos = gini_coefficient(Europe_pos[field])
    gini_SouthAmerica_pos = gini_coefficient(SouthAmerica_pos[field])
    gini_NorthAmerica_pos = gini_coefficient(NorthAmerica_pos[field])
    gini_Oceania_pos = gini_coefficient(Oceania_pos[field])

    print(gini_global)
    print(gini_developed)
    print(gini_developing)
    print(gini_Asia_pos)
    print(gini_Europe_pos)
    print(gini_Africa_pos)
    print(gini_NorthAmerica_pos)
    print(gini_SouthAmerica_pos)
    print(gini_Oceania_pos)

