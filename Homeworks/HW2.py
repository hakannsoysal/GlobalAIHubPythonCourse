# liste ve sözlük tanımlanması
students = []
notlar = []
ogrenciler = {}

# kullanıcıdan isim,not alma ve ekleme işlemleri
for i in range(5):
    student=str(input("Lütfen {}. öğrencinin ismini giriniz: ".format(i+1)))
    vize=int(input("Lütfen vize notunu giriniz: "))
    odev=int(input("Lütfen ödev notunu giriniz: "))
    final=int(input("Lütfen final notunu giriniz: "))
    students.append(student)
    notlar.append(vize)
    notlar.append(odev)
    notlar.append(final)
    ogrenciler["İsim"] = students
    ogrenciler["Vize,Ödev,Final"] = notlar

# ortalama bulma fonksiyonu 
def maxOrtalamaBul(nott):
    ort = []
    ort1 = []
    ort.append((nott[0] + nott[1] + nott[2] ) / 3)
    ort.append((nott[3] + nott[4] + nott[5]) / 3)
    ort.append((nott[6] + nott[7] + nott[8]) / 3)
    ort.append((nott[9] + nott[10] + nott[11]) / 3)
    ort.append((nott[12] + nott[13] + nott[14]) / 3)
    ort1 = ort
    ort.sort()
    max = ort[4]
    if ort1.index(max) == 0:
        print("Tebrikler {} ! Ortalaman :".format(students[0]), ort[4])

    elif ort1.index(max) == 1:
        print("Tebrikler {} ! Ortalaman :".format(students[1]), ort[4])

    elif ort1.index(max) == 2:
        print("Tebrikler {} ! Ortalaman :".format(students[2]), ort[4])
    elif ort1.index(max) == 3:
        print("Tebrikler {} ! Ortalaman :".format(students[3]), ort[4])

    elif ort1.index(max) == 4:
        print("Tebrikler {} ! Ortalaman :".format(students[4]), ort[4])

    elif ort1.index(max) == 5:
        print("Tebrikler {} ! Ortalaman :".format(students[5]), ort[4])    

# öğrencileri ve notları ekrana yazdırma işlemi
for j in range(len(students)):
    print("{}. Öğrenci : {} | Vize Notu: {} | Ödev Notu: {} | Final Notu: {} | \n".format(j+1, students[j],notlar[j],notlar[j+1],notlar[j+2] ) ) 

# sözlüğü ekrana bastırma işlemi 
print(ogrenciler)  

# en yüksek ortalama
maxOrtalamaBul(notlar)




    




