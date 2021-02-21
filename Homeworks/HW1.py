import random
asalSayilar = []
i=0

def asalBul(sayi):
    asalmi = True

    if sayi == 1:
        asalmi = False

    for i in range(2, sayi):
        if (sayi % i == 0):
            asalmi = False
            break

    if asalmi:
        return True
    else:
        return False

for j in range(99):
    sayi1 = random.randint(1,100)
    if asalBul(sayi1) == True:
        if len(asalSayilar) <= 8:
            asalSayilar.insert(i,sayi1)
            i += 1
          
print(asalSayilar[0],asalSayilar[1],asalSayilar[2], end="\n")
print(asalSayilar[3],asalSayilar[4],asalSayilar[5], end="\n")
print(asalSayilar[6],asalSayilar[7],asalSayilar[8], end="\n")


