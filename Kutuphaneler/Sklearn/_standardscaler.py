# STANDARDSCALER

from sklearn.preprocessing import StandardScaler # sklearn paketinde bulunur.
from sklearn.model_selection import train_test_split
import pandas as pd

# Veri setlerimizde verilerin değerleri arasındaki farklar çok fazla olabilir.
# Örnek

# 1.özellikler -> [1,2,0,1,2]
# 2.özellikler -> [8000,9000,100,2000,40000]

# 2.özellikler kümesini direkt olarak kullanırsak model eğitiminde çok fazla ağırlık verir.
# Bu da modelin yanlış öğrenmesine yol açar.
# Bu problemi çözmek için ise Standardizasyon yöntemi uygulanır.
# Bu yöntem bir sütundaki bütün verileri yaklaşık olarak [-3 , 3] aralığına indirgemektir.
# Aykırı değerler bu aralıktan çıkabilir.
# Bu işlem şu formülle gerçekleşir.

# z = (x - ortalama) / standart sapma

# Bu yöntem uygulandıktan sonra her sütunun:
# Ortalaması -> 0
# Standart Sapması -> 1 olur.

# Bu işlemi yapan sınıf StandardScaler sınıfıdır.

veri = {
    "yas"     : [32, 27, 45, 23, 38, 41, 29, 35],
    "maas"    : [8000, 6500, 11000, 4500, 9500, 10000, 7000, 8500],
    "ise_alindi" : [1, 0, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(veri)

x = df[["yas", "maas"]] # Özellikler
y = df["ise_alindi"] 


x_train, x_test, y_train_, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# BURADA DİKKAT EDİLMESİ GEREKEN BİR YER VAR.

# Öncelikle bu standardizasyon işlemi mutlaka train_test_split aşamasından sonra yapılmalıdır.
# Çünkü biz modeli test ederken daha önce "hiç karşılaşmadığı" veriler ile test edeceğiz.
# Eğer fit() kısmında x_test kümesini kullanırsak ortalama ve standart sapmanın hesaplanmasında x_test kümesindeki
# verilerinde payı olacak. Bu istemediğimiz bir şey.

# Bu sebeplerden standardizasyon işlemi mutlaka:
# train_test_split işleminden sonra
# Sadece x_train kullanılarak yapılması gereken bir işlemdir.