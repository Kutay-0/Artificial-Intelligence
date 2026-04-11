# MULTIPLE LINEAR REGRESSION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Veri Okuma

dataset = pd.read_csv(r'C:\Artificial Intelligence\Modeller\Regression\MultipleLinearRegression\50_Startups.csv')
x = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]

# Encoding İşlemi
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer(transformers=[('encode', OneHotEncoder(), ['State'])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

# Train/Test Ayırma
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Regression Modeli Ekleme
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Model Tahmini
y_pred = regressor.predict(x_test)

# Model Sonucu Ölçme
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)

print(f"R2 Skoru : {r2}")