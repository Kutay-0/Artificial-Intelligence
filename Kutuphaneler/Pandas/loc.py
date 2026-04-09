# loc[] METODU

import pandas as pd # metot burada bulunur.

dataFrame = pd.read_csv('veri_kumesi.csv', usecols=["a","b","c","d","e","f"], nrows=10)
# DataFrame'de etiket bazlı erişim sağlar.
# Sütun numarası değilde sütun adı girilir.
# iloc[]'tan ayıran farkların diğeride belirtilen aralığın son indexini de döndürür.

print(dataFrame.loc[0:1 , "a":"c"])
# 0 ve 1. satırlar, a'dan c'ye kadar sütunları döndürür.

print(dataFrame.loc[:, "b"])
# Sadece b sütununu döndürür.

print(dataFrame.loc[dataFrame["a"] > 25])
# Sadece koşula uyan satırlar döner.

# INDEX DEĞİŞİMİNDEN ETKİLENİR.

dataFrame = dataFrame.set_index("a")
# Artık satırlarda index numarasıyla değil, sütun adıyla işlem yapılır.
# Örnek:
print(dataFrame.loc["Ali", "Yas"])
# 1 numaralı satır değil , "Ali" etiketli satırdan "Yas" sütununu getir.