# COLUMNTRANSFORMER

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer # sklearn paketinde bulunur.
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np

# Gerçek veri setlerinde hem sayısal hem de kategorik sütunlar bulunur.
# Her sütun tipine farklı işlem uygulamak gerekir.

# Sayısal verilere -> SimpleImputer
# Kategorik verilere -> OneHotEncoding

# ColumnTransformer bütün bu işlemleri tek seferde düzenli yapan sınıftır.

ct = ColumnTransformer(transformers=[('encode', OneHotEncoder(), [0])], remainder='passthrough')
# 'encode' = transformer adı
# OneHotEncoding = Yapılacak işlem
# [0] = uygulanacak sütun indexi
# remainder = kalanlara yapılacak işlem (passthrough : değiştirme, drop : düşür)

# onehotencoding.py sayfasındaki işlemi otomatik olarak yapan sınıf bu

# ÖRNEK

veri = {
    "sehir"   : ["Ankara", "Istanbul", np.nan, "Ankara", "Istanbul"],
    "yas"     : [32, 27, 45, np.nan, 38],
    "maas"    : [8000, np.nan, 11000, 4500, 9500]
}

dataFrame = pd.DataFrame(veri)

kategorik_sutunlar = ["sehir"]
sayisal_sutunlar = ["yas", "maas"]

ct = ColumnTransformer(transformers=[
    ("sayisal", SimpleImputer(strategy='mean'), sayisal_sutunlar),
    ("kategorik", OneHotEncoder(sparse_output=False), kategorik_sutunlar)                                 
    ], remainder= 'passthrough')

# 2 tane farklı amaca hizmet eden transformer oluşturuldu.

dataFrame_transformed = ct.fit_transform(dataFrame)

# Transform edilen verilen atandı.

# Burada işlemden sonra kalacak "sehir" sütunu otomatik olarak düşmüş oldu.
# Yani sadece "sehir_Ankara" ve "sehir_Istanbul" sütunları kaldı.
# "sehir" sütununda bulunan np.NaN değerleri 0 0 olarak kaldı. Çünkü impute uygulanmadı.

# "yas" ve "maas" sütunları mean(ortalama) ile dolduruldu.