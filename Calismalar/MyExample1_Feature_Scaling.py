import pandas as pd # Veri okuma işlemleri
import numpy as np  # Dizi işlemleri

# VERİ KÜMESİNİ ÇEKME

dataset = pd.read_csv('veri_kumesi.csv') # .csv uzantılı dosyadan verileri alma

x = dataset.iloc[:,:6] # Bağımsız değişkenlerin alınması
y = dataset.iloc[:,-1] # Bağımlı değişkenlerin alınması
# İlk satır değişken isimlerini gösterdiği için almıyoruz.

# KAYIP VERİLERİ DOLDURMA

from sklearn.impute import SimpleImputer # Kayıp verileri doldurmada kullanılacak sınıf
imputer = SimpleImputer() # İmputer nesnesinin üretilmesi
imputer.fit(x[:,:3]) # Bağımsız değişkenlerin ortalamasının hesaplanması
x[:,:3] = imputer.transform(x[:,:3]) # Ortalamaların boş hücrelere doldurulması

# METİNSEL VERİLERİ SAYISALLAŞTIRMA

from sklearn.preprocessing import OneHotEncoder # Verileri bitleyecek sınıf
from sklearn.compose import ColumnTransformer # Sütun değiştirici

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3,4,5])], remainder='passthrough')
# Dönüştürücü adı: encoderx, OneHotEncoder() işlemi yap, x. sütuna yap, geri kalanlara dokunma
x = np.array(ct.fit_transform(x))

# TRAİN_SET_SPLİT FONKSİYONUNU EKLEMEK

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

# FEATURE SCALİNG

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

x_train[:,0:3] = sc.fit_transform(x_train[:,0:3])
x_test[:,0:3] = sc.transform(x_test[:,0:3])