# read_csv() FONKSİYONUNUN TANIMI

import pandas as pd # read_csv burada bulunur.

dataset = pd.read_csv("veri_seti.csv", usecols=["ad","soyad","yas"], nrows=10)

# read_csv : Diske kaydedilmiş bir .csv uzantılı dosyayı okuyup
# DataFrame'e dönüştüren bir fonksiyondur.

# DataFrame : Satır ve Sütunlardan oluşan 2 boyutlu bir tablodur.
# Her satır ya da sütun "Series" yapısındadır

# DataFrame 2 farklı şekilde oluşturulabilir:

# ÖRNEK 1 - Dictionary

veri_dict = {
    "ad" : ["Ali", "Veli", "Ayşe"],
    "yas" : [25, 35, 45],
    "maas" : [5000, 7000, 9000]
}

dataframe_dict = pd.DataFrame(veri_dict)

# ÖRNEK 2 - Liste

dataframe_list = pd.DataFrame(
    [
        ["Ali", 25, 5000],
        ["Veli", 30, 7000],
        ["Ayşe", 35, 6500]
    ],
        columns=["ad", "yas", "maas"]
)