#Bir kelimenin palindrom olup olmadığını kontrol eden bir Python programı yazın.
'''
#Çözüm1
kelime=input("Kelime giriniz:")
ters_kelime = ""
for i in range(1,len(kelime)+1):
    ters_kelime+=kelime[-i]
if ters_kelime == kelime:
    print("Kelime palindromdur.")
else:
    print("Kelime palindrom değildir.")
#Çözüm2
kelime=input("Kelime giriniz:")
ters_kelime = kelime[::-1]
if ters_kelime==kelime:
    print("Kelime palindromdur.")
else:
    print("Kelime palindrom değildir.")
#Çözüm3
kelime = input("Kelime giriniz:")
ters_kelime = ""
for harf in kelime:
    ters_kelime = harf + ters_kelime
if ters_kelime == kelime:
    print("Kelime palindromdur.")
else:
    print("Kelime palindrom değildir.")
'''
#İki string'in birbirinin anagramı olup olmadığını kontrol eden bir Python fonksiyonu yazın.
'''
kelime1=input("Kelime giriniz:")
kelime2=input("Kelime giriniz:")
if len(kelime1)==len(kelime2):
    kontrol = 0
    for harf in kelime1:
        if harf in kelime2:
            kontrol = 1
        else:
            kontrol = 0
    if kontrol == 1:
        print("Kelimeler birbirinin anagramıdır.")
    else:
        print("Kelimeler birbirinin anagramı değildir.")
else:
    print("Kelimeler aynı uzunlukta değildir.")
'''
#Bir string'i tersine çeviren bir Python fonksiyonu yazın.
'''
#Çözüm1
metin = input("Metin giriniz:")
tersmetin=""

for i in range(1,len(metin)+1):
    tersmetin += metin[-i]

print("Orjinal metin:",metin)
print("Ters çevrilmiş hali:",tersmetin)

#Çözüm2
metin = input("Metin giriniz:")
tersmetin=metin[::-1]

print("Orjinal metin:",metin)
print("Ters çevrilmiş hali:",tersmetin)
'''
#Verilen bir string içindeki tekrarlanan karakterleri bulan bir Python programı yazın.
'''
metin = input("Metin giriniz:")

karakter = {}

for char in metin:
    if char in karakter:
        karakter[char] += 1
    else:
        karakter[char] = 1

for char in karakter:
    if karakter[char] > 1:
        print(f"'{char}' karakteri {karakter[char]} kere tekrarlanıyor.")
'''
#Bir string içindeki büyük harfleri küçük harflere, küçük harfleri büyük harflere çeviren bir Python fonksiyonu yazın.***
'''
metin= input("Metin giriniz:")
kelime = ""
for karakter in metin:
    ascii_deger = ord(karakter)
    if 65 <= ascii_deger <= 90: 
        kelime += chr(ascii_deger + 32)
    elif 97 <= ascii_deger <= 122:  
        kelime += chr(ascii_deger - 32)
    else:
        kelime += karakter
print(kelime)
'''
#Verilen bir string içindeki baştaki ve sondaki boşlukları kaldıran bir Python fonksiyonu yazın.
'''
metin = input("Metin giriniz:")

for i in metin:
    if i != " ":
        print(i,end="")
    else:
        continue
'''
#Verilen bir sayı içeren string'i tam bir sayıya dönüştüren bir Python fonksiyonu yazın.
'''
metin = input("Metin giriniz:")
sayac = 0
for i in metin:
    if i != " ":
        sayac+=1
    else:
        print(sayac,end=" ")
        sayac = 0
else:
    print(sayac)
'''
#Verilen bir cümledeki kelime sayısını hesaplayan bir Python programı yazın.
#Çözüm1 
'''
metin = input("Metin giriniz:")
kelimesayac = 0

for i in metin:
    if i == " ":
        kelimesayac += 1

if metin[-1] == " ":
    kelimesayac -= 1

print("Kelime sayısı:", kelimesayac)


#Çözüm 2

metin= input("Metin giriniz:")
kelime_sayisi = 0
kelime_baslangici = True

for karakter in metin:
    if karakter != ' ' and kelime_baslangici:
        kelime_sayisi += 1
        kelime_baslangici = False
    elif karakter == ' ':
        kelime_baslangici = True

print("Kelime sayısı",kelime_sayisi)
'''
#Bir string içindeki alt çizgileri kaldıran bir Python fonksiyonu yazın.
'''
metin = input("Metin giriniz:")

for i in metin:
    if i != "_":
        print(i,end="")
    else:
        print(" ",end="")
'''
#Verilen bir string içindeki çift ve tek karakterleri ayrı iki string olarak döndüren bir Python fonksiyonu yazın.
'''
metin = input("Metin giriniz:")
liste = []
kelime = ""

for i in metin:
    if i != " ":
        kelime += i
    else:
        liste.append(kelime)
        kelime = ""
if kelime not in liste:
    liste.append(kelime)

tekstring = ""
çiftstring = ""

for kelime in liste:
    if len(kelime) % 2 == 0:
        çiftstring += kelime + " "
    else:
        tekstring += kelime + " "

print("Tek Karakterli Kelimeler:", tekstring)
print("Çift Karakterli Kelimeler:", çiftstring)
'''
#Bir string'in uzunluğunu hesaplayan bir Python programı yazın.
'''
metin=input("Metin giriniz:")
sayac = 0
for i in metin:
    sayac+=1
print("Stringin uzunluğu:",sayac)
'''
#Bir string'i belirli bir karaktere göre parçalayan bir Python fonksiyonu yazın.
'''
metin=input("Metin giriniz:")
bas=int(input("Parçalama başlangış:"))
son=int(input("Parçalama son:"))

print(metin[bas:son])
'''
#Verilen bir string içindeki boşlukları kaldırdıktan sonra kalan string'in uzunluğunu hesaplayan bir Python fonksiyonu yazın.
'''
metin=input("Metin giriniz:")
uzunluk = 0
for i in metin:
    if i != " ":
        uzunluk +=1 

print("Metinin boşluksuz uzunluğu = ",uzunluk)
'''
#İki string'i birleştiren bir Python fonksiyonu yazın.
'''
metin1=input("Metin giriniz:")
metin2=input("Metin giriniz:")

son = metin1 + metin2

print(son)
'''
#Verilen bir cümledeki her kelimenin sırasını tersine çeviren bir Python programı yazın.
'''
metin=input("Metin giriniz:")
kelimeliste = []
kelime=""
for i in metin:
    if i != " ":
        kelime+=i
    else:
        kelimeliste.append(kelime)
        kelime=""
if kelime not in kelimeliste:
    kelimeliste.append(kelime)

for i in range(len(kelimeliste)-1,-1,-1):
    print(kelimeliste[i],end=" ")
'''
#İki string içinde ortak karakterleri bulan bir Python fonksiyonu yazın.
'''
metin1=input("1.metini giriniz:")
metin2=input("2.metini giriniz:")
ortak=[]
for i in metin1:
    if i in metin2 and i not in ortak:
        ortak.append(i)

print("İki Stringdeki ortak karakterler:",end=" ")

for i in ortak:
    print(i,end=" ")
'''
#Belirli bir karakter dizisini belirli bir sayıda tekrarlayarak yeni bir string oluşturan bir Python fonksiyonu yazın.
'''
metin = input("Tekrarlanacak metini girin:")
adet = int(input("Metinin kaç adet tekrarlanacağını girin:"))
yeni = metin*adet
print(yeni)
'''
#Girilen yazıdaki kelime, rakam ve karakter sayısını bulan program?
'''
metin = input("Metin giriniz:")

rakamlist = ['0','1','2','3','4','5','6','7','8','9']
rakamsayac=0
karaktersayac=0
kelimeliste = []
kelime = ""

for i in metin:
    karaktersayac +=1
    if i in rakamlist:
        rakamsayac += 1
    if i != " " and i not in rakamlist:
        kelime += i
    else:
        if kelime != "":
            kelimeliste.append(kelime)
            kelime = ""
if kelime not in kelimeliste and kelime != "":
    kelimeliste.append(kelime)

print(f"Cümledeki kelime sayısı: {len(kelimeliste)},Cümledeki rakam sayısı:{rakamsayac},Cümledeki karakter sayısı:{karaktersayac}")

'''
#En fazla tekrar eden elemanı sil
'''
def enfazlatekrarsil(liste):
    sozluk = {}
    for eleman in liste:
        if eleman in sozluk:
            sozluk[eleman] += 1
        else:
            sozluk[eleman] = 1

    tekrarliste = []
    maxtekrar = 0
    for eleman in sozluk:
        tekrar = sozluk[eleman]
        if tekrar > maxtekrar:
            maxtekrar = tekrar
            tekrarliste = [eleman]
        elif tekrar == maxtekrar:
            tekrarliste.append(eleman)

    yeni_liste = []
    for eleman in liste:
        if eleman not in tekrarliste:
            yeni_liste.append(eleman)

    return yeni_liste

liste = [1, 2, 3, 2, 4, 2, 5, 6, 2, 7, 2, 8, 9, 2]
print(enfazlatekrarsil(liste))
'''
#Bir cümledeki kelimeleri uzunluklarına göre sıralayan bir Python programı yazın.
'''
metin = input("Metin giriniz:")
kelime = ""
kelimeliste = []

for i in metin:
    if i != " ":
        kelime += i
    else:
        kelimeliste.append(kelime)
        kelime = ""

if kelime != "":
    kelimeliste.append(kelime)

for i in range(len(kelimeliste)-1):
    for j in range(len(kelimeliste)-i-1):
        if len(kelimeliste[j]) < len(kelimeliste[j+1]):
            kelimeliste[j], kelimeliste[j+1] = kelimeliste[j+1], kelimeliste[j]

print(f"Girilen cümledeki kelimelerin uzunluklarına göre büyükten küçüğe sıralanmış hali => {kelimeliste}")
'''
#Belirli bir uzunluktaki rastgele bir string oluşturan bir Python fonksiyonu yazın.
'''
import random

uzunluk = int(input("Uzunluk giriniz:"))

kelime=""

for i in range(uzunluk):
    k=random.randint(65,90)
    l=random.randint(97,122)
    for i in range(random.randint(1,2)):
        if i == 1 :
            kelime += chr(k)
        else:
            kelime += chr(l)

print(kelime)
'''
#Verilen bir string içindeki harfleri ve rakamları ayıran bir Python fonksiyonu yazın.
'''
metin = input("Metin giriniz:")
rakam=['1','2','3','4','5','6','7','8','9','0']

harfler=[]
rakamlar=[]

for i in metin:
    if i in rakam and i !=" ":
        rakamlar.append(i)
    else:
        if i !=" ":
            harfler.append(i)

print(f"Girilen metindeki harfler = {harfler} \nGirilen metindeki rakamlar = {rakamlar}")
'''
#ASCII karakterlerini içeren bir string oluşturan bir Python programı yazın.
'''
asciliste =[]
for i in range(33,128,+1):
    asciliste.append(chr(i))

print(asciliste)
'''
#Verilen bir sayıyı Roma rakamlarına çeviren bir Python fonksiyonu yazın.
'''
romarakam=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']

sayi = int(input("Sayı giriniz:"))

for i in range(sayi):
    if i+1==sayi:
        print(f"{sayi} nın roma rakamlarıyla karşılığı = {romarakam[i]}")
'''
#Verilen bir string içindeki çift sıradaki harfleri çıkaran bir Python programı yazın.

metin=input("Metin giriniz:")
yenimetin=""
for i in range(1,len(metin)+1):
    if i % 2 != 0:
        yenimetin += metin[i-1]
    else:
        yenimetin += " "

print(yenimetin)