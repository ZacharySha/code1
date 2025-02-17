import pandas as pd
import geopandas as gpd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import glob
import csv
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, r2_score
from tqdm import tqdm

# shp_list = glob.glob('/Users/shate/Desktop/paper/data_2000_10_18/data2018/each_city_2018_xy/*.shp')
shp_list = glob.glob('/Users/shate/Desktop/paper/data_2000_10_18/data2000/each_city_2000_xy/*.shp')

with open('RF2000_s.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ORIG_FID', 'gaia', 'e', 'pr', 'tem', 'r2'])

    for shp in tqdm(shp_list):
        data = gpd.read_file(shp)

        ID = shp.split("/")[-1].split(".")[0]

        X = data[['gaia', 'e', 'pr', 'tem']]
        y = data['s']


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # 初始化随机森林回归器
        rf = RandomForestRegressor(n_estimators=100, random_state=42)

        scorer = make_scorer(r2_score)
        cv_scores = cross_val_score(rf, X, y, cv=10, scoring=scorer)
        # rf.fit(X, y)

        # 训练模型
        rf.fit(X_train, y_train)


        # 获取特征重要性
        importances = rf.feature_importances_

        # 输出特征重要性
        feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
        # print(ID, importances, cv_scores.max())
        cv_scores_mean = cv_scores[cv_scores>0].mean() if cv_scores.max()>0 else 0
        writer.writerow([ID, importances[0], importances[1], importances[2],importances[3], cv_scores_mean])


        # # 绘制特征重要性图
        # plt.figure(figsize=(10, 6))
        # plt.title('Feature Importance')
        # plt.barh(X.columns, importances, color='b', align='center')
        # plt.xlabel('Relative Importance')
        # plt.ylabel('Feature')
        # plt.show()
