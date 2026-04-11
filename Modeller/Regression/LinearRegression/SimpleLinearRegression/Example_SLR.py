# SIMPLE LINEAR REGRESSION ÖRNEĞİ

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# VERİ SETİ
dataset = pd.DataFrame({
    'deneyim': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'maas':    [30000, 35000, 42000, 48000, 55000, 61000, 70000, 78000, 85000, 95000]
})
x = dataset[['deneyim']]  # 2D DataFrame olması gerekiyor, tek köşeli parantez Series (1D) döndürür
y = dataset['maas']

# VERİ SETİNİ AYIRMA
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# TRAIN SET İLE MODEL EĞİTME
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train) # B0 ve B1 bulunuyor. Yani model öğrendi.

# X_TEST İLE TAHMİNLER ÜRETME
y_pred = regressor.predict(x_test)

karsilastirma = pd.DataFrame({'Gercek':y_test , 'Tahmin':y_pred})

# TRAIN VERİLERİNİ GÖRSELLEŞTİRME
plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Deneyim ve Maas (training set)')
plt.xlabel('Deneyim')
plt.ylabel('Maas')
plt.show()

# TEST VERİLERİNİ GÖRSELLEŞTİRME

plt.scatter(x_test, y_test, color='blue')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Deneyim ve Maas (training set)')
plt.xlabel('Deneyim')
plt.ylabel('Maas')
plt.show()

# SONUÇLARIN KONTROLÜ
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print(r2)