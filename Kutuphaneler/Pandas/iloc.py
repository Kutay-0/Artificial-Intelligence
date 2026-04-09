# ILOC[] METODU

import pandas as pd # Pandas kütüphanesinde kullanılır.

dataFrame = pd.read_csv('veri.csv', usecols=["ad","maas","yil","a","b","c","d","e"], nrows=10)

# Bir DataFrame'de sayısal index numaralarıyla satır ve sütunlara erişmeni sağlar.

print(dataFrame.iloc[1:2 , 1:5])
# Burada dataFrame'in 1 indexli satırına ve 1,2,3,4 indexli sütunlarına erişiyoruz.

print(dataFrame.iloc[1]) # Sadece 1. satırı getir
print(dataFrame.iloc[:,1]) # Sadece 1. sütunu getir.
print(dataFrame.iloc[[1,5,6] , [2,4]]) # 2 ve 4. sütunlardan sadece 1, 5 ve 6. satırları getir.