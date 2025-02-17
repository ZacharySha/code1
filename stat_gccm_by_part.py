import os
import pandas as pd
import numpy as np

csv_path = "/Users/shate/Desktop/dbf/GCCMp2018.csv"
df = pd.read_csv(csv_path)

developed = df['GUB_9227_2']==1
developing = df['GUB_9227_2']==0

# pos = df['CE_yxmapx']>0
# pos = df['CE_yxmapx']<0

Asia = df['GUB_9227_5'] == "Asia"
Africa = df['GUB_9227_5'] == "Africa"
Europe = df['GUB_9227_5'] == "Europe"
SouthAmerica = df['GUB_9227_5'] == "SouthAmerica"
NorthAmerica = df['GUB_9227_5'] == "NorthAmerica"
Oceania = df['GUB_9227_5'] == "Oceania"

# developed_pos = df[developed][pos]
# developed_pos_std = np.std(developed_pos['CE_yxmapx'])
# developed_pos_mean = np.mean(developed_pos['CE_yxmapx'])
# developing_pos = df[developing][pos]
# developing_pos_std = np.std(developing_pos['CE_yxmapx'])
# developing_pos_mean = np.mean(developing_pos['CE_yxmapx'])
# print(len(developed_pos),developed_pos_mean, developed_pos_std)

# def CE_sign():
#     Asia_pos = df[Asia][pos]
#     Asia_pos_std = np.std(Asia_pos['CE_yxmapx'])
#     Asia_pos_mean = np.mean(Asia_pos['CE_yxmapx'])
#
#     Africa_pos = df[Africa][pos]
#     Africa_pos_std = np.std(Africa_pos['CE_yxmapx'])
#     Africa_pos_mean = np.mean(Africa_pos['CE_yxmapx'])
#
#     Europe_pos = df[Europe][pos]
#     Europe_pos_std = np.std(Europe_pos['CE_yxmapx'])
#     Europe_pos_mean = np.mean(Europe_pos['CE_yxmapx'])
#
#     SouthAmerica_pos = df[SouthAmerica][pos]
#     SouthAmerica_pos_std = np.std(SouthAmerica_pos['CE_yxmapx'])
#     SouthAmerica_pos_mean = np.mean(SouthAmerica_pos['CE_yxmapx'])
#
#     NorthAmerica_pos = df[NorthAmerica][pos]
#     NorthAmerica_pos_std = np.std(NorthAmerica_pos['CE_yxmapx'])
#     NorthAmerica_pos_mean = np.mean(NorthAmerica_pos['CE_yxmapx'])
#
#     Oceania_pos = df[Oceania][pos]
#     Oceania_pos_std = np.std(Oceania_pos['CE_yxmapx'])
#     Oceania_pos_mean = np.mean(Oceania_pos['CE_yxmapx'])
#
#     # print(len(Asia_pos),Asia_pos_mean, Asia_pos_std)
#     # print(len(Africa_pos),Africa_pos_mean, Africa_pos_std)
#     # print(len(Europe_pos),Europe_pos_mean, Europe_pos_std)
#     # print(len(SouthAmerica_pos),SouthAmerica_pos_mean, SouthAmerica_pos_std)
#     # print(len(NorthAmerica_pos),NorthAmerica_pos_mean, NorthAmerica_pos_std)
#     print(len(Oceania_pos),Oceania_pos_mean, Oceania_pos_std)



field = 'P2018GCC_3'
pos = df['P2018GCC_3']>df['P2018GCC_1']
P = df['P2018GCC_4']<=0.05

Global_pos = df[pos][P]
Global_pos_std = np.std(Global_pos[field])
Global_pos_mean = np.mean(Global_pos[field])

Developed_pos = df[developed][pos][P]
Developed_pos_std = np.std(Developed_pos[field])
Developed_pos_mean = np.mean(Developed_pos[field])

developing_pos = df[developing][pos][P]
developing_pos_std = np.std(developing_pos[field])
developing_pos_mean = np.mean(developing_pos[field])

Asia_pos = df[Asia][pos][P]
Asia_pos_std = np.std(Asia_pos[field])
Asia_pos_mean = np.mean(Asia_pos[field])

Africa_pos = df[Africa][pos][P]
Africa_pos_std = np.std(Africa_pos[field])
Africa_pos_mean = np.mean(Africa_pos[field])

Europe_pos = df[Europe][pos][P]
Europe_pos_std = np.std(Europe_pos[field])
Europe_pos_mean = np.mean(Europe_pos[field])

SouthAmerica_pos = df[SouthAmerica][pos][P]
SouthAmerica_pos_std = np.std(SouthAmerica_pos[field])
SouthAmerica_pos_mean = np.mean(SouthAmerica_pos[field])

NorthAmerica_pos = df[NorthAmerica][pos][P]
NorthAmerica_pos_std = np.std(NorthAmerica_pos[field])
NorthAmerica_pos_mean = np.mean(NorthAmerica_pos[field])

Oceania_pos = df[Oceania][pos][P]
Oceania_pos_std = np.std(Oceania_pos[field])
Oceania_pos_mean = np.mean(Oceania_pos[field])


print(len(Global_pos),Global_pos_mean, Global_pos_std)

print(len(Developed_pos),Developed_pos_mean, Developed_pos_std)
print(len(developing_pos),developing_pos_mean, developing_pos_std)

print(len(Asia_pos),Asia_pos_mean, Asia_pos_std)
print(len(Europe_pos),Europe_pos_mean, Europe_pos_std)
print(len(Africa_pos),Africa_pos_mean, Africa_pos_std)
print(len(NorthAmerica_pos),NorthAmerica_pos_mean, NorthAmerica_pos_std)
print(len(SouthAmerica_pos),SouthAmerica_pos_mean, SouthAmerica_pos_std)
print(len(Oceania_pos), Oceania_pos_mean, Oceania_pos_std)