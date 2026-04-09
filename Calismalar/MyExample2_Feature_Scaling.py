import pandas as pd # Veri okuma kütüphanesi
import numpy as np # Dizi işlemleri kütüphanesi

# VERİ OKUMA

dataset = pd.read_csv('veri_kumesi_2.csv') # Veri kümesinin okunması

x = dataset.iloc[:,:7] # Bağımsız değişkenler matrisi
y = dataset.iloc[:,-1] # Bağımlı değişkenler matrisi

# KAYIP VERİ DOLDURMA

from sklearn.impute import SimpleImputer

# Sayısal verileri doldurma
imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
imputer.fit(x.iloc[:,:3])
x.iloc[:,:3] = imputer.transform(x.iloc[:,:3])

# Kategorik verileri doldurma
imputer2 = SimpleImputer(missing_values=np.NaN, strategy='most_frequent')
imputer2.fit(x.iloc[:,3:6])
x.iloc[:,3:6] = imputer2.transform(x.iloc[:,3:6])

# ENCODİNG

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3,4,5,6])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

# TRAIN-SPLIT-TEST

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# FEATURE SCALING

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

x_train[:,:23] = sc.fit_transform(x_train[:,:23])
x_test[:,:23] = sc.transform(x_test[:,:23])