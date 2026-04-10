# LABELENCODER

from sklearn.preprocessing import LabelEncoder
import pandas as pd

# LabelEncoder kategorik verileri sayılara dönüştürür. OneHotEncoding'ten farkı ne?

# OneHotEncoding -> Her kategori için ayrı sütun açar.
# LabelEncoding -> Tek sütunda kategorilere sıra numarası verir.

# ÖRNEK - OneHotEncoding
# Ankara ->     | 1 0 0 |
# İstanbul ->   | 0 1 0 |
# İzmir ->      | 0 0 1 |

# ÖRNEK - LabelEncoding
# Ankara ->     | 0 |
# İstanbul ->   | 1 |
# İzmir ->      | 2 |
# İstanbul ->   | 1 |

veri = {
    "isim"  : ["Ahmet", "Merve", "Burak", "Selin", "Tarik"]
}

df = pd.DataFrame(veri)

le = LabelEncoder()
df = le.fit_transform(df)
# Hem kategorileri öğrendi hem de uyguladı.

# LabelEncoding sadece hedef değişken kümesine uygulanmalıdır.
# OneHotEncoding ise özellik değişkenlerine uygulanmalıdır. 

# Eğer LabelEncoding özellik verilerine uygulanırsa model bu verileri büyüklük olarak algılar !
# Örnek
# Ankara -> |1|
# İzmir ->  |2|

# Model : İzmir(2) > Ankara(1)

# Şehirler arasında böyle bir sıralama yoktur.
# Bu sebeple LabelEncoding sadece kategorik hedef değişkenlere uygulanır.