'''
üç tane tek tırnak
 arasına yorum satırı çoklu 
 
 satır olarak yazılır
 '''

# hashtag ifadesi ile yorum satırı tek satır olarak yazılır


#print(4+5+52+213/8)
'''
Sayi= 11
sayi = 10   #Bu bir tamsayı (integer) değişken tanımlamasıdır.
SAyi=12
onladikliSayi= 5.0 # bu bir ondalıklı sayı (float) değişken tanımlamasıdır.

print(sayi)
print(onladikliSayi)
print(Sayi)
print(SAyi)

print(type(sayi))          # type() fonksiyonu değişkenin türünü gösterir.
print(type(onladikliSayi))




Değişken isimlendirme kuralları:
Değişken isimleri harf (A-Z, a-z) veya alt çizgi (_) ile başlamalıdır.
12metin="metin" şeklinde bir değişken tanımlaması yapılamaz çünkü değişken isimleri rakam ile başlayamaz.
Değişkenler büyük küçük harf duyarlıdır. Sayi, sayi ve SAyi birbirinden farklı değişkenlerdir.
Promlama dilinde özel karakterler ve boşluklar değişken isimlerinde kullanılamaz.
Değişkenlerin başına ortasına boşluk karakteri konulamaz.

ogrenci adı= "Ali" # Bu şekilde bir kullanım yoktur.
'''
'''
metin = "Merhaba Dünya!" # metin (String) türünde bir değişken tanımlaması
Metin="Bu farklı bir metin ifadesidir." # Değişken isimleri büyük küçük harf duyarlıdır.

print(metin)
print(Metin)
print(type(metin))

_degisken= 123
degisken=23
degisken123= 21312    # Geçerli değişken isimlendirmeleri
degisken_turu="deneme"


#for=12312
#if=!'312  #Geçersiz değişken isimlendirmeleri özel karakterler barındırır.
#None=21312

yas=25 #int
sicaklık= 35.5 #float
metin="Bugün hava çok güzel." #string
PI=3.123 # sabit

print(type(yas))
print(type(sicaklık))
print(type(metin))
print(type(PI))

'''

'''
yasDegeri= 30

isim= input("Lütfen isminizi giriniz: ")
print("Merhaba " + isim + "!") 
'''
#aritematikse operatörler (+ - * / % // **)
# sayi1 = 10
# sayi2 = 3
# toplam=0

# toplam= sayi1 + sayi2
# fark= sayi1 - sayi2
# carpim= sayi1 * sayi2
# bolum= sayi1 / sayi2

# print("Toplam: " , toplam)
# print("İşlemin farkının sonucu:",fark)
# print(carpim)
# print(bolum)


# #atama operatorleri
# sayi5=10
# print("Başlangıç değeri:",sayi5)

# sayi5 +=5 #sayi= sayi +5 anlamına gelir

# print("5 eklendi:",sayi5)

# sayi5 -=3 # sayi= sayi -3 anlamına gelir

# print("3 çıkarıldı:",sayi5)


# #üs alma
# taban=2
# us=3
# sonuc= taban ** us # üs alma işlemini ** operatörü ile yaparız
# print("Sonuç:",sonuc)


# sayi= 513

# negatifSayi= -sayi
# pozitifSayi = +sayi

# print("Negatif sayı:",negatifSayi)
# print("Pozitif sayı:",pozitifSayi)



# #karışık işlemler

# a=10

# b=5

# c=3

# sonuc= (a+b)*c-b  #matematikteki işlem önceliğine göre yapılır

# print("Sonuç:",sonuc)

#karşılatştırma operatörleri

# ==: İki değer eşit mi?
# !=: İki değer eşit değil mi?
# >: Soldaki değer büyük mü?
# <: Soldaki değer küçük mü?
# >=: Soldaki değer büyük veya eşit mi?
# <=: Soldaki değer küçük veya eşit mi?


#not karşılatırma örneği

not_ornek= 70

print("Notunuz 70' e eşitmi ?",(not_ornek==70))
print("Notunuz 70' den farklı mı ?",(not_ornek!=70))
print("Notumuz 80 den küçük mü", not_ornek<80)
print("Notumuz 80 den büyük mü ", not_ornek>80)
print("Notumzu 80 den küçük veya 80 eşit mi?",not_ornek<=80)
print("Notumzu 80 den büyük veya 80 eşit mi?",not_ornek>=80)


#ürün fiyat karşılatırma örneği

fiyat=200
indirim=150

print(fiyat>indirim) # True (indirim fiyatından pahalı)
print(fiyat<=150) #False (150 tlden pahalı oldugunu anlatır)
print(fiyat!= indirim)#True (Fiyat ile indirim eşit değil)


yas=15

print(yas>18) #False (yani yetişkibn birey değildir)
print(yas<18) #True ( yani yetişkin birey değil yası 18 den küçüktür)
print(yas==15 ) #True (öğrencin yaşı 15 tir)