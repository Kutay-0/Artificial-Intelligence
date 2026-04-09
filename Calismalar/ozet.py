import pandas as pd # Veri okuma, manipülasyon ve analiz kütüphanesi
import matplotlib.pyplot as plt # Grafik ve görselleştirme kütüphanesi
import numpy as np # Dizi ve matris işlemleri kütüphanesi

dataset = pd.read_csv('data.csv') # data.csv dosyasını okuyup DataFrame olarak kaydeder

x = dataset.iloc[:,:-1] # Son sütun hariç tüm sütunları bağımsız değişken olarak alır
y = dataset.iloc[:,-1]  # Yalnızca son sütunu bağımlı değişken olarak alır

from sklearn.impute import SimpleImputer # Kayıp verileri istatistiksel yöntemle dolduran sınıf
imputer = SimpleImputer() # Varsayılan olarak ortalama (mean) stratejisiyle çalışır
imputer.fit(x[:,1:3]) # 1. ve 2. sütunların ortalamasını öğrenir
x[:,1:3] = imputer.transform(x[:,1:3]) # Kayıp hücreleri öğrenilen ortalama ile doldurur

from sklearn.preprocessing import OneHotEncoder # Kategorik verileri binary sütunlara dönüştüren sınıf
from sklearn.compose import ColumnTransformer # Farklı sütunlara farklı dönüşümler uygulamayı sağlayan sınıf

ct = ColumnTransformer(transformers=[('encode', OneHotEncoder(), [0])], remainder='passthrough') # 0. sütuna OneHotEncoding uygular, diğer sütunları değiştirmeden aktarır
x = np.array(ct.fit_transform(x)) # Dönüşümü uygular ve sonucu numpy dizisine çevirir

from sklearn.preprocessing import LabelEncoder # Kategorik etiketleri sayısal değerlere dönüştüren sınıf
le = LabelEncoder() # LabelEncoder nesnesi oluşturur
y = le.fit_transform(y) # Bağımlı değişkendeki etiketleri öğrenip sayısal değerlere dönüştürür (örn: No=0, Yes=1)

from sklearn.model_selection import train_test_split # Veri setini eğitim ve test olarak bölmek için kullanılan fonksiyon
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1) # Veriyi %80 eğitim %20 test olarak böler, random_state tekrar üretilebilirliği sağlar

from sklearn.preprocessing import StandardScaler # Verileri ortalama=0, standart sapma=1 olacak şekilde ölçekleyen sınıf
sc = StandardScaler() # StandardScaler nesnesi oluşturur

x_train[:,3:] = sc.fit_transform(x_train[:,3:]) # Eğitim verisinin sayısal sütunlarından istatistikleri öğrenip standardizasyon uygular
x_test[:,3:] = sc.transform(x_test[:,3:]) # Eğitimden öğrenilen istatistiklerle test verisine standardizasyon uygular (veri sızıntısını önlemek için fit kullanılmaz)
