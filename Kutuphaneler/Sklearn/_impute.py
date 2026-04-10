# SIMPLE IMPUTER

from sklearn.impute import SimpleImputer # sklearn paketinde bulunur.
import numpy as np
import pandas as pd

# Veri setlerimizde eksik verilerin (NaN) olması çok muhtemeldir.
# Makine öğrenmesi algoritmaları NaN değerle çalışamaz hata verir.
# SimpleImputer ise bu eksik değerleri belli kurallara göre dolduran sınıftır.

veri = {
    "yas"  : [25, np.nan, 35, 28, np.nan],
    "maas" : [5000, 7000, np.nan, 6000, 8000],
    "deneyim" : [2, 5, np.nan, 3, 7]
}

dataFrame = pd.DataFrame(veri)

imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
# strategy, bizim tablodaki boşlukları doldurma şeklimizdir. Bunlar:
# mean : Sütunun ortalamasıyla doldur
# median : Sütunun medyanıyla doldur
# most_frequent : En sık tekrar eden kategoriyle doldur
# constant : Sabit bir değerle doldur

# missing_values ise neyi eksik sayacağımızı girdiğimiz yerdir.

imputer.fit(veri)
# fit() -> veriyi öğrenmek için kullanılır. (Ortalama, medyan)

imputer = imputer.transform(veri)
# transform() -> bulduğu hesaplamayı uygulamak için kullanılır.

# ÖRNEK SENARYO

# Eksik bilgilerin bulunduğu veri seti
veri_deneme = {
    "yas"  : [25, np.nan, 35, 28, np.nan],
    "maas" : [5000, 7000, np.nan, 6000, 8000],
    "deneyim" : [2, 5, np.nan, 3, 7]
}

df = pd.DataFrame(veri_deneme)

imp = SimpleImputer(strategy='mean') # varsayılan missing_values np.nan'dır

df_imp = imp.fit_transform(df) # Hem fit hemde transform uygulandı

# TRAIN TEST KISMINDA DİKKAT EDİLMESİ GEREKEN ŞEY !!!

x_test, x_train = df    # train ve test verileri böyle ayrılmaz !
                        # Sadece hata olarak gözükmesin diye yazılmıştır !

x_train = imp.fit_transform(x_train)    # Şeklinde ayrılması gerekir.
x_test = imp.transform(x_test)      # Çünkü test verisi gerçek dünyada "görmediğimiz" veridir.
                                        # Ondan bir şeyler öğrenmek veri sızıntısına yol açar.