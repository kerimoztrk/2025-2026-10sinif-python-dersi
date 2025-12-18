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

# not_ornek= 70

# print("Notunuz 70' e eşitmi ?",(not_ornek==70))
# print("Notunuz 70' den farklı mı ?",(not_ornek!=70))
# print("Notumuz 80 den küçük mü", not_ornek<80)
# print("Notumuz 80 den büyük mü ", not_ornek>80)
# print("Notumzu 80 den küçük veya 80 eşit mi?",not_ornek<=80)
# print("Notumzu 80 den büyük veya 80 eşit mi?",not_ornek>=80)


# #ürün fiyat karşılatırma örneği

# fiyat=200
# indirim=150

# print(fiyat>indirim) # True (indirim fiyatından pahalı)
# print(fiyat<=150) #False (150 tlden pahalı oldugunu anlatır)
# print(fiyat!= indirim)#True (Fiyat ile indirim eşit değil)


# yas=15

# print(yas>18) #False (yani yetişkibn birey değildir)
# print(yas<18) #True ( yani yetişkin birey değil yası 18 den küçüktür)
# print(yas==15 ) #True (öğrencin yaşı 15 tir)



# HATA türleri

# 1. Söz dizimi hatası (Syntax Error) dilin kuralları gereği uyulamsı gereken kurallar ihlal edilirse ortaya çıkar

#print("merhaba dünya)


# 2. Çalışma zamanı hatası (Runtime Error) program çalışırken ortaya çıkan hatalardır. Örneğin sıfıra bölme hatası

#sayi= int("merhaba")


#3. Mantık hatası (Logical Error) program çalışır ancak beklenen sonucu vermez. Örneğin yanlış işlem 

# vize=40
# final=60

# ortalama= (vize*0.40) + (final*0.60)  # Doğru formül vize ınavı çarpı 40 bölü 100 işlemi yapılıyor final için ise çarpu 60 bölü 100
# print("Ortalama:",ortalama)


# istisna (Exception)  0'a bölünme hataları bunu kapsar

# sayi1=10
# sayi2=0

# print(sayi1/sayi2)


# Koşullu İfadeler (if, elif, else)

#örnek 1 : şifre kontrol

# sifre= input("Lütfenm şifrenizi giriniz:")

# if sifre == "parola123":
#     print("Şifre doğru, giriş başarılı.")
# else:
#     print("Şifre yanlış, giriş başarısız.")       


#örnek 2 : Başkent ülke kontrolü

# baskent= input("Lütfen bir şehir ismi giriniz:")

# ulke= input("Lütfen bir ülke ismi giriniz:")

# if(baskent=="Ankara" and ulke=="Türkiye"):
#     print("Doğru! Ankara Türkiye'nin başkentidir.")
# else: print("başarısız")

#örnek 3 : sayi tahmini uygulaması

# sayi=input("Lütfe tahmin ettiğiniz sayıyı giriniz")

# if(sayi=="3"):
#     print("Tahmin ettiğiniz sayı doğrudur")
# else:
#     print("Tahmininiz yanlış tekrar deneyin")


#örnek 4 not ortalpması hesabı

# sinav1=float(input("1.sınav notunu girin:"))
# sinav2=float(input("2.sınav notunu girin:"))
# sinav3=float(input("3.sınav notunu girin:"))

# ortalama=(sinav1+sinav2+sinav3)/3
# print("Sınavların ortalamsı =",ortalama)


# if( 0<ortalama<50):
#     sonuc="Sonuc Rezalet"
# elif (50<ortalama<70):
#     sonuc="Sonuc Ortalana"
# elif (70<ortalama<85):
#     sonuc="İyi"
# else: sonuc="Mükkemmel"

# print(sonuc)

#İÇ içe if yapısı kullanarak şifre kontorlü uygulaması


# sifre=input("Şifreyi giriniz:")

# if sifre == "12a34":
#     print("şifre doğru")

#     yetki=input("Yetkiniz var mı ? (evet/hayır):")

#     if yetki=="evet":
#         print("Giriş başarılı")
#     else:
#         print("Yetkiniz yok giriş başarısız")
# else:
#     print("Şifre yanlış girildi.")


# ortalama= float(input("lütfen ortalamanızı girin:"))
# devamsizlik= int(input("Lütfen devamsızlık sayınızı girin:"))

# if ortalama>=50:
#     if devamsizlik<=10:
#         print("Tebrikler dersten geçtiniz!")
#     else:
#         print("Devamsızlıktan kaldın!")
# else:
#     print("Nottan kaldın!")


yas= int(input("Lütfen yaşınızı giriniz:"))

if yas>=18:
    print("giriş yapabilirsin")
else:
    izin=input("Veli izni varmo (evet/hayır)")

    if izin=="evet":
        print("Veli izniyle giriş yapıldı")
    else:
        print("giirş yapılamaz")

