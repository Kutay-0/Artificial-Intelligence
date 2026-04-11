# Simple Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Veri setini ekleme
dataset = pd.DataFrame({
    'deneyim': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'maas':    [30000, 35000, 42000, 48000, 55000,
                61000, 70000, 78000, 85000, 95000]
})

# Veri setini ayırma
x = dataset[['deneyim']]
y = dataset['maas']

# Train/Test setlerini ayırma
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Model eğitme
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Tahmin üretme
y_pred = regressor.predict(x_test)

# Train Verilerini Görselleştirme
plt.scatter(x_train, y_train, color='blue') # Train noktalarını nokta nokta çizer
plt.plot(x_train, regressor.predict(x_train), color='blue') # Modelin öğrendiği doğruyu çizer
plt.title('Deneyim ve Maas (training set)') # Grafiğin başlığını ayarlar
plt.xlabel('Deneyim') # X eksenine etiket yazar
plt.ylabel('Maas') # Y eksenine etiket yazar
plt.show() # Grafiği ekranda gösterir

# Test Verilerini Görselleştirme
plt.scatter(x_test, y_test, color='green')  # Test verilerini nokta nokta gösterir.
plt.plot(x_train, regressor.predict(x_train), color='blue') # Modelin öğrendiği doğruyu çizer.
plt.title('Deneyim ve Maas (test set)') # Grafiğin başlığı.
plt.xlabel('Deneyim') # X eksenine etiket yazar.
plt.ylabel('Maas') # Y eksenine etiket yazar.
plt.show() # Grafiği gösterir.

# Model Verimini Hesaplama
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)

print(f"R2 Skoru : {r2}")