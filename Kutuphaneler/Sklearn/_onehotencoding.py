# ONEHOTENCODING

from sklearn.preprocessing import OneHotEncoder # sklearn paketinde bulunur.
import pandas as pd

# Makine öğrenmesi algoritmaları sayısal verilerle çalışır.
# Ama veri setlerinde kategorik verilerde bulunabilir.
# OneHotEncoding bu verileri 0 ve 1'lerden oluşan sütunlara dönüştürür.

# ÖRNEK
# Bir veri setinde "sehir" adında sütun olsun.
# "Ankara", "İstanbul", "İzmir", "Ankara"

# OneHotEncoding bu verileri şuna dönüştürür:

# "sehir_Ankara" | "sehir_İstanbul" | "sehir_İzmir"
#       1                0                  0
#       0                1                  0
#       0                0                  1
#       1                0                  0

# Yani veri o kategorideyse 1, değilse 0 yazar.

veri = {
    "isim"  : ["Ahmet", "Merve", "Burak", "Selin", "Tarık"],
    "sehir" : ["Ankara", "Istanbul", "Izmir", "Ankara", "Istanbul"],
    "yas"   : [32, 27, 45, 23, 38],
    "maas"  : [8000, 6500, 11000, 4500, 9500]
}

x = pd.DataFrame(veri)

encoder = OneHotEncoder()
x_transformed = encoder.fit_transform(x)
# Kategorik tüm verileri işleme tabi tutar

# Bu işlemden sonra "sehir" sütunu tablodan düşmez. Normalde düşmesi lazım.
# Çünkü oradaki verileri sayısallaştırdık.
# Burada sütun düşürme işlemini yapacak olan bir sınıfımız var.
# Sütun düşürme işlemini otomatik olarak yapan ColumnTransformer sınıfı vardır.
# İlgili dosyaya geçebilirsiniz.