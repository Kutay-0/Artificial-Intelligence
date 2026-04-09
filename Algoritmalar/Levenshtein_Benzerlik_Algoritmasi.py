# -----Levenshtein Mesafesi Benzerlik Algoritması-----
# Amacımız: Bu algoritmayı kullanarak iki metin arasındaki benzerlik oranını tespit etmektir.

# Bu algoritma şu şekilde çalışmaktadır:
# A ve B birer metin olsun. A metnini kaç işlem sonucunda B metnine çevirebiliriz sorusunun cevabını bulmaktır.
# İşlem sayısı ne kadar az ise bu iki metin birbirine o kadar benzerdir.
# Aynı şekilde işlem sayısı ne kadar fazla ise bu iki metin birbirinden o kadar farklıdır.

# ÖRNEK:
# A: Araba
# B: Arap

# A metnini B metnine çevirebilmemiz için "b" harfini "p" harfine çevirmemiz ve "a" harfini kaldırmamız gerekmektedir.
# Yani bir tane harf değiştirme işlemi ve bir tane harf silme işlemi ile toplamda 2 adet işlem yapmış olduk.

# Buradaki işlem sayısı ne kadar az ise o kadar benzerdir diyeceğiz.

import numpy

# Bu algoritma hesaplanırken bazı fonksiyonlara ihtiyaç duyacağız.

# 1) maximum() fonksiyonu:

def maximum(str1_len, str2_len):    # Uzun olan string'in değerini döndürmek.

    if str1_len > str2_len:
        return str1_len
    
    return str2_len

# 2) minimum() fonksiyonu:

def minimum(a, b, c):   # "Bu aşamaya kadar en kısa yol en az ne kadar maliyet ister" sorusunun cevabı döner.

    if a <= b and a <= c:
        return a

    if b <= a and b <= c:
        return b
    
    if c <= a and c <= b:
        return c


# 3) def LevenshteinMesafesi() fonksiyonu

def LevenshteinMesafesi(A, B):      # Benzerlik hesaplaması yapacağımız fonksiyon.
    K = numpy.zeros((len(A) + 1, len(B) + 1)) # A ve B stringlerinin uzunluğun 1 fazlası uzunluğunda 0 matris oluşturuyoruz.
    A_len = len(A)
    B_len = len(B)

    for i in range (A_len+1):           # 
        K[i][0] = i                     #
                                        # İlk satır ve sütunu artan bir indis olarak değiştiriyoruz.
    for i in range (B_len+1):           # Bu sayede algoritmamızın matrisini hazırlamış oluyoruz.
        K[0][i] = i                     #

    silme = 0
    ekleme = 0                      # Silme, ekleme ve değiştirme işlemlerimizin sayısı tutacak değişkenlerimizi tanımlıyoruz.
    degistirme = 0

    for i in range (1, A_len + 1):          # Satır gezmek için döngü
        for j in range (1, B_len + 1):      # Sütun gezmek için döngü
            if A[i-1] == B[j-1]:            # Stringlerin belirli indeksteki değerleri aynı olup olmadığını kontrol ediyoruz.
                K[i][j] = K[i-1][j-1]       
            else:                           # Eğer farklı ise,
                silme = K[i-1][j] + 1           
                ekleme = K[i][j-1] + 1
                degistirme = K[i-1][j-1] + 1
                K[i][j] = minimum(silme, ekleme, degistirme) # Bu işlemleri deneyerek en az maliyetli olanı döndürüyor.
    
    print(K)
    return K[A_len][B_len]

# Şimdi ise bu kodların çalışmasını sağlayalım.

str1 = input("1.Kelimeyi giriniz: ")
str2 = input("2.Kelimeyi giriniz: ")

mesafe = LevenshteinMesafesi(str1, str2)

print(f"{str1} ve {str2} kelimeleri arasındaki Levenshtein mesafesi: {mesafe} birimdir.")

max_length = maximum(len(str1), len(str2))
benzerlik_oran = (max_length - mesafe)/max_length

print(f"Bu kelimelerin benzerlik oranı: {benzerlik_oran}")

# Bu algoritma "Spell Checker" gibi yazım yanlışlarını düzeltmek için kullanılan yazılımlarda kullanılır.
# Arama motorlarında, makine öğrenmesi için verilerin kümelenmesinde ve optimizasyonunda kullanılır.