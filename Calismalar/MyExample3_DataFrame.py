# DATAFRAME ÇALIŞMALASI

import pandas as pd

veri = {
    "isim" : ["Ahmet", "Merve", "Burak", "Selin", "Tarik"],
    "sehir" : ["Ankara", "Istanbul", "Izmir", "Bursa", "Ankara"],
    "yas" : [32, 27, 45, 23, 38],
    "maas" : [8000, 6500, 11000, 4500, 9500]
}

dataFrame = pd.DataFrame(veri)

# 1) .iloc[] kullanarak ilk satırı getirme
print(dataFrame.iloc[0])

# 2) .iloc[] kullanarak son satırı getirme
print(dataFrame.iloc[-1])

# 3) .loc kullanarak "yas" sütununu tamamen getirme
print(dataFrame.loc[:, "yas"])

# 4) .loc kullanarak Selin'in satırını getirme
print(dataFrame.loc[3])

# 5) .iloc kullanarak ilk 3 satırı getirme
print(dataFrame.iloc[:3])

# 6) .iloc[] kullanarak sadece "isim" ve "maas" sütunlarını getirme(indexle)
print(dataFrame.iloc[:,[0,3]])

# 7) .loc[] kullanarak "sehir" ve "yas" sütunlarını tamamen getirme
print(dataFrame.loc[:, ["sehir", "yas"]])

# 8) .loc[] kullanarak maaşı 7000'den fazla olanları getirme
print(dataFrame.loc[dataFrame["maas"] > 7000])

# 9) .loc kullanarak yaşı 30'dan büyük olanların sadece
# "isim" ve "maas" sütunlarını getirme
print(dataFrame.loc[dataFrame["yas"] > 30 , ["isim", "maas"]])

# 10) .iloc[] kullanarak 2. ve 4. satırların 0. ve 3. sütunlarını getir.
print(dataFrame.iloc[[2,4], [0,3]])