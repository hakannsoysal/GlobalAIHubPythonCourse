import random
hayvanlar =["maymun","fare","kedi","aslan","kaplan"]
teknoloji =["bilgisayar","telefon","powerbank","televizyon","kulaklık"]
markalar =["apple","acer","fanta","razer","vestel","asus","samsung"]

class Game():
    def __init__(self):
        print("Her soruda üç hakkınız vardır.")
        
        print("Lütfen bir kategori seçiniz.(markalar, teknoloji, hayvanlar)")
        a=str(input())
        kategori(a)
        
        
        




class kategori():
    def __init__(self,kelime):
        hak = 2
        if(kelime == "hayvanlar"):
            hayvan=random.choice(hayvanlar)
            print("Kelimeniz {} harflidir.".format(len(hayvan)))
            for i in range(len(hayvan)):
                print("{}. harfi nedir ?".format(i+1))
                a=str(input())
                if a==hayvan[i]:
                    print("Güzel.. Devam edin.")

                else:
                    hak -=1
                    if hak==0:
                        print("Hakkınız kalmadı :((((")
                        break
                    print("{} hakkınız kaldı.".format(hak))
                    for j in range(len(hayvan)):
                        print("{}. harfi nedir?".format(j+1))
                        b=str(input())
                        if b==hayvan[j]:
                            print("Güzel.. Devam edin.")

                        else:
                            hak -= 1
                            if hak==0:
                                print("Hakkınız kalmadı :((((")
                                exit()
                            print("{} hakkınız kaldı.".format(hak))    
                    
                    
                    
            

        elif (kelime == "teknoloji"):
            hak = 2
            tekno=random.choice(teknoloji)
            print("Kelimeniz {} harflidir.".format(len(tekno)))
            for i in range(len(tekno)):
                print("{}. harfi nedir ?".format(i+1))
                a=str(input())
                if a==tekno[i]:
                    print("Güzel.. Devam edin.")

                else:
                    hak -=1
                    if hak==0:
                        print("Hakkınız kalmadı :((((")
                        break
                    print("{} hakkınız kaldı.".format(hak))
                    for j in range(len(tekno)):
                        print("{}. harfi nedir?".format(j+1))
                        b=str(input())
                        if b==tekno[j]:
                            print("Güzel.. Devam edin.")

                        else:
                            hak -= 1
                            if hak==0:
                                print("Hakkınız kalmadı :((((")
                                exit()
                            print("{} hakkınız kaldı.".format(hak))    
                    
            

        elif (kelime == "markalar"):
            hak = 2
            marka=random.choice(markalar)
            print("Kelimeniz {} harflidir.".format(len(marka)))    
            for i in range(len(marka)):
                print("{}. harfi nedir ?".format(i+1))
                a=str(input())
                if a==marka[i]:
                    print("Güzel.. Devam edin.")

                else:
                    hak -=1
                    if hak==0:
                        print("Hakkınız kalmadı :((((")
                        break
                    print("{} hakkınız kaldı.".format(hak))
                    for j in range(len(marka)):
                        print("{}. harfi nedir?".format(j+1))
                        b=str(input())
                        if b==marka[j]:
                            print("Güzel.. Devam edin.")

                        else:
                            hak -= 1
                            if hak==0:
                                print("Hakkınız kalmadı :((((")
                                exit()
                            print("{} hakkınız kaldı.".format(hak))    
                    
        
    
print("Adam asmaca oynamak ister misiniz ?")
a= str(input())

if ( (a=="Evet") or (a=="evet") or (a=="yes") or (a=="Yes") ):
    Game()
else:
    print(":(")    
    


