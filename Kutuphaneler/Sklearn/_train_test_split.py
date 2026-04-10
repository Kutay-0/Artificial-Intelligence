# TRAIN TEST SPLIT

from sklearn.model_selection import train_test_split # sklearn paketinde bulunur.
import pandas as pd

# Bu fonksiyon veri ön işleme aşamasının önemli parçalarından biridir.
# Elimizdeki veri setini 2 parçaya böler. Train ve Test.
# Bir model eğitildiğinde o modelin daha önce hiç görmediği veriler üzerinde ne kadar iyi çalıştığını ölçmemiz gerekir.
# Eğer modeli bütün veri ile eğitip ardından bu verilerle test edersek model ezbercilik yapmış olur.
# Yani Overfitting durumuyla karşı karşıya kalırız.
# Bu problemi çözmek içinse verinin bir kısmıyla modeli eğitip diğer kısmıyla modeli test ediyoruz.

veri = {
    "yas"     : [32, 27, 45, 23, 38, 41, 29, 35],
    "maas"    : [8000, 6500, 11000, 4500, 9500, 10000, 7000, 8500],
    "ise_alindi" : [1, 0, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(veri)

x = df[["yas", "maas"]] # Özellikler
y = df["ise_alindi"] 


x_train, x_test, y_train_, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# Bu fonksiyon 4 tane veri kümesi döndürür.
# test_size = 0.2 : Verilerin %20'sini test verisi olarak böl
# random_state = 42 : 42 sayısı tamamen gelenek. Kod paylaşıldığında aynı sayı girilirse veriler aynı şekilde bölünür.
# stratify = y : Eğer orantısız bir veri seti varsa (örn: %90 sağlıklı | %10 hasta)
# Bu verilerin aynı oranda hem train hem de test veri kümesinde bulunmasını sağlar. Kısaca aynı oranda dağıtır.