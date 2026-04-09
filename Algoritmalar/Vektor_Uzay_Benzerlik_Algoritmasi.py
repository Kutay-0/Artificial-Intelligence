#-----Vektör Uzay Benzerlik Algoritması-----
# Amaç: Çok parametreli verileri görselleştirmek, anlamlı geometrik yorumlar yapmak ve kümeleyebilmek için kullanılır.
# Verileri birim çemberde sayısal değerlere çevirip aralarındaki benzerlik oranını bulmak.
# Birim çember şart değildir. Benzerlik oranını 0-1 aralığında (0 = Çok farklı, 1 = çok benzer) değerlendirmek için kullanıyoruz.
# İki veri noktasının özelliklerinin birbirine göre dağılımının ne kadar benzer olduğunu ölçer.

# İki boyutlu bir koordinat düzlemi düşünelim.
# Bu koordinat düzleminde A ve B olmak üzere x ve y değerlerine sahip iki parametreli, iki farklı veri gibi düşünelim.
# Örneğin daha anlaşılabilir olması için bu A ve B'yi birer insan olarak kabul edelim.
# X ekseni boyu, Y ekseni kilyou temsil etsin.

# Bu benzerlik teoremi, bu iki insanın benzerlik oranını kıyaslamak için, aralarındaki mesafeyi kullanır.
# Bu mesafeyi tümleşik öklid teoremini kullanarak hesaplayabiliriz.

# N boyutta 2 nokta arası mesafe = ((x2-x1)^2 + (y2-y1)^2 + .... + (n2-n1)^2)^(1/2) olarak hesaplanabilir.

# Bu insan örneğinde belirlediğimiz kilo ve boy değişkenleri doğrusal olarak artış göstermek zorunda değildir.
# Örnek olarak: X'in en düşük değeri 100 cm, en büyük değeri 200 cm olurken
# Y'nin en düşük değeri 50 kilo, en yüksek değeri 100 kilo olabilir.

# Verileri koordinat düzleminde kullanabilmek için normalizasyon yapmamız gerekir. 

# Örnek olarak A ve B birer insan olsun.
# A = (180, 90) = Boyu 180 cm, kilosu 90 kilogram
# B = (150, 75) = Boyu 150 cm, kilosu 75 kilogram

# Birim çemberde A kişisinin somut değerlerini bulalım

# birim çemberde boy = boy / ((maksimum boy - minimum boy)/100)
# birim çemberde kilo = kilo / ((maksimum kilo - minimum kilo)/100)

# Bu işlemlere göre A noktasının X değerinin birim çemberdeki karşılığı:
# X = (X - Xmin) / (Xmax - Xmin) = (180-100) / (200-100) = 0.8
# Y = (Y - Ymin) / (Ymax - Ymin) = (90-50) / (100-50) = 0.8

# Şimdi A noktasının merkeze uzaklığı ile merkeze en uzak nokta arasındaki uzaklığa oranı hesaplanabilir.
# Bu sonuç esasen A noktasının merkeze uzaklığının 0-1 arasındaki oranıdır.

# Şimdi bu algoritmayı kullanarak bir örnek çözelim

#--------------İKİ RENK ARASI BENZERLİK ORANINI TESPİT ETMEK------------------------

# Önceliğimiz bir sıkıştırma algoritması yazmaktır.

def arrange(item, dimension, min, max):
    return [(x - min) / (max - min) for x in item]

# Öklid teoremini uygulayabilmek için kokal ve usal fonksiyonlarını yazalım.

def kokal(x):
    return x**(1/2)

def usal(x):
    return x*x

# Şimdi ise renkleri tanımlayalım

kirmizi = [255,0,0]
koyuKirmizi = [181, 25, 25]
kahverengi = [48, 34, 15]
siyah = [0, 0, 0]
beyaz = [255, 255, 255]
gri = [82, 82, 82]

# Renkleri tanımladıktan sonra arrange() fonksiyonumuzu kullanarak bu renkleri istediğimiz aralığa sıkıştıralım.

normalKirmizi = arrange(kirmizi, 3, 0, 255)
normalKoyuKirmizi = arrange(koyuKirmizi, 3, 0, 255)
normalKahverengi = arrange(kahverengi, 3, 0, 255)
normalSiyah = arrange(siyah, 3, 0, 255)
normalBeyaz = arrange(beyaz, 3, 0 ,255)
normalGri = arrange(gri, 3, 0, 255)

# Sıra oluşan bu vektörler arasında benzerlik oranı hesaplayan fonksiyonu yazalım.

def vectorSimilarity(A, B):
    if len(A) != len(B):
        raise ValueError("Vektör Boyutları Eşit Olmalı.")
    
    distance = kokal(sum((b - a) ** 2 for a, b in zip(A,B)))

    max_dist = kokal(len(A))

    similarity = 1 - (distance / max_dist)
    return similarity
    
# Şimdi ise programı deneyelim.

benzerlik_orani = vectorSimilarity(normalKirmizi, normalKoyuKirmizi)

print(f"Benzerlik oranı: {benzerlik_orani}")