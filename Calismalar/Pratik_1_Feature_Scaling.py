# Herşeyden önce gerekli kütüphanelerimizi eklemekle başlayalım.

import numpy as np  # Dizilerle çalışmamızı sağlayan kütüphanedir.
import matplotlib.pyplot as plt # Verileri ve sonuçları grafikleştirmemizi sağlayacak kütüphanedir.
import pandas as pd # Veri okuma, veri manipülasyonu ve veri analizi için kullanacağımız kütüphanedir.

# Şimdi veri setimizi ekleyelim.
# İlk amacımız bir değişken oluşturmaktır.
# Bu değişken bizim veri kümemizi tutacak.

dataset = pd.read_csv('Data.csv')   # read_csv() fonksiyonu, .csv uzantılı dosyalardan veri okumak için kullanılan bir fonksiyondur.

# Ancak bu işlem verileri işlemek için yeterli değildir. İki değişkene daha ihtiyacımız var.

# 1 - Özellik Matrisi
# Bu matris bağımsız değişkenlerin matrisidir.

x = dataset.iloc[:,:-1].values # .iloc[satırlar,sütunlar] özelliği, satır ve sütunları index numaralarına göre seçen özelliktir.

# 2 - Bağımlı Değişken Vektörü
# Bu vektör ise bulmak istediğimiz bağımlı değişkenin vektörüdür.

y = dataset.iloc[:,-1].values # Şu an burada "bütün satırları ve sadece son sütunu al." demek istiyoruz.

# Burada bu şekilde ayrım yapmamızın sebebi, veri setimizde bağımsız değişkenlerin ilk sütunlarda
# bağımlı değişkenimizinde son sütunda bulunmasından kaynaklıdır.

# Başka veri setlerinde bağımlı ve bağımsız değişkenler neredeyse ona göre bu iki değişken atanır.

# Şimdi veri setimizi ekledik. Ama bir problemle karşılaşabiliriz.
# Bu problem ise "kayıp veriler"'dir.
# Bu kayıp veriler, veri setlerimizdeki boş yerlerdir.
# Bu boş yerleri, bulunduğu sütundaki değerlerin ortalaması ile dolduracağız.

# Bu işlemi kolay bir şekilde yapabilmek için veri biliminin en kaliteli kütüphanesini ekleyeceğiz.

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy='mean')    # Burada missing_values = np.nan kısmı, veri setinde hangi verileri değiştireceğimizi söylemektir.
imputer.fit(x[:, 1:3])  # 1. ve 2. sütunlardaki (sayısal) verilerin ortalamasını öğrenir. (fit() dönüşüm yapmaz, sadece istatistik hesaplar.)
x[:, 1:3] = imputer.transform(x[:, 1:3])    # transform() metodunu kullanarak boş hücrelerin yerine o sütundaki değerlerin ortalamalarını yazdık.

# Veri kısmını hallettik ama bir sorunumuz var. 
# Veri setimizde sayısal olmayan bazı değerler var (Ülkeler, sonuç gibi)
# Bu verileri eşleştirme işlemini kendimiz yaparsak bu kural tabanlı programlama olur.
# O yüzden bu verileri sayısal değerlere dönüştürmemiz gerekir.
# Bu yönteme de OneHotEncoding yöntemi denir.
# Kaç farklı veri var ise onları 0'lara ve 1'lere dönüştürür.
# Örnek olarak 3 farklı veri olsun. O zaman:
# Birinci veri: 1 0 0
# İkinci veri : 0 1 0
# Üçüncü veri : 0 0 1
# Şeklinde olacaktır.

from sklearn.compose import ColumnTransformer   # ColumnTransformer = Sütun dönüştürücüdür.
from sklearn.preprocessing import OneHotEncoder # Binary dönüşümü işlemini yapacak sınıf

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
# transformers parametresi (isim, dönüştürücü, sütun_indexleri) formatında tuple alır.
# [0] → yalnızca 0. sütuna (kategorik ülke verisi) OneHotEncoding uygulanır.
# remainder='passthrough' → belirtilmeyen diğer sütunlar değiştirilmeden aktarılır.
x = np.array(ct.fit_transform(x))  # fit: kategorileri öğrenir | transform: binary sütunlara dönüştürür | np.array: sonucu numpy dizisine çevirir.

from sklearn.preprocessing import LabelEncoder  # Kategorik etiketleri (örn: "Yes"/"No") sayısal değerlere (0/1) dönüştürür.
le = LabelEncoder()
y = le.fit_transform(y)  # Bağımlı değişkendeki kategorik verileri (örn: Yes=1, No=0) sayıya çevirir. OneHotEncoding'e gerek yok çünkü sadece 2 sınıf var.

# Bu aşamaları geçtikten sonra train set ve test set oluşturmalıyız.
# Bu aşamada bir soru var. 
# Feature Scaling ayırmadan önce mi yapılmalı yoksa sonra mı ?
# Bu sorunun cevabı basit. Ayırmadan sonra. Neden ?
# Train set bizim modeli eğiteceğimiz verilerdir. Test set model eğitimine katılmaz.
# Eğer Feature Scaling'i ayırmadan önce yaparsak eğitim verilerinin dönüşmesi sırasında test verilerininde etkisi olacaktır.
# Ama biz test verilerinin hiçbir şekilde etki etmesini istemiyoruz.
# Eğer test verileri karışırsa buna "Bilgi Sızıntısı" denir.
# Bu sebeple önce veri ayrılır. Ardından Feature Scaling uygulanır.

from sklearn.model_selection import train_test_split  # Veri setini eğitim ve test olarak bölmek için kullanılan fonksiyon.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=1)
# test_size=0.2   → verinin %20'si test, %80'i eğitim olarak ayrılır.
# random_state=1  → rastgele bölme işleminin her çalıştırmada aynı sonucu vermesini sağlar (tekrar üretilebilirlik).

# Verilerimizi ayırdık. Şimdi sırada Feature Scaling.
# 2 tür Feature Scaling yöntemi vardır: 1-Normalization , 2-Standardization
# Peki hangi yöntemi ne zaman kullanmalı ? 
# Normalizasyon -> Eğer verilerin değerleri düzgün bir şekilde dağılmış duruyorsa kullanılır.
# Standardizasyon -> Aslında her zaman kullanılabilir.

from sklearn.preprocessing import StandardScaler  # Standardizasyon: verileri ortalama=0, standart sapma=1 olacak şekilde ölçekler.
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])  # fit: eğitim verisindeki ortalama ve std'yi öğrenir | transform: ölçekleme uygular. Yalnızca sayısal sütunlara (3. sütundan itibaren) uygulanır.
x_test[:, 3:] = sc.transform(x_test[:, 3:])         # Test verisinde sadece transform() kullanılır! fit() DEĞİL. Eğitim verisinden öğrenilen istatistikler uygulanır, böylece veri sızıntısı önlenir.

# Bu aşamalarıda gerçekleştirdiğimizde artık verilerimizi ayırmış, 80'e 20 olacak şekilde bölmüş ve
# standardizasyon uygulamış bulunmaktayız. Şu an verileri modelle işlemek için hazır hale getirdik.