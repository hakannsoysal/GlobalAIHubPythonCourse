class FettuciniAlfredo():
    def __init__(self,makarnaTuru,yagTuru,yagTuru1,sosTuru):
        self.makarnaTuru=makarnaTuru
        self.yagTuru=yagTuru
        self.sosTuru=sosTuru
        self.yagTuru1=yagTuru1
        print("Gerekli Ana Malzemeler :",makarnaTuru,yagTuru,yagTuru1,sosTuru)

    def neKadarKullanmanGerek(self):
        print("2 kişilik makarna yapmak istersen;")
        print("Yarım paket " + self.makarnaTuru)
        print("1 yemek kaşığı tereyağı \n 1 yemek kaşığı zeytinyağı \n 100 gram mantar \n 150 gram tavuk göğsü \n 1,5 diş sarımsak \n 1 su bardağı krema \n 1/4 demet fesleğen \n 1/2 su bardağı rendelenmiş parmesan peyniri \n 1/2 çay kaşığı karabiber \n 1 çay kaşığı tuz")
        print("Püf Noktası : Sosu kısık ateşte kaynatmak !")
       
        print("4 kişilik makarna yapmak istersen;")
        print("Bir paket makarna \n 2 yemek kaşığı tereyağı \n 2 yemek kaşığı zeytinyağı \n 200 gram mantar \n 300 gram tavuk göğsü \n 3 diş sarımsak \n 1 su bardağı krema \n 1/4 demet fesleğen \n 1/2 su bardağı rendelenmiş parmesan peyniri \n 1/2 çay kaşığı karabiber \n 1 çay kaşığı tuz")
        print("Püf Noktası : Sosu kısık ateşte kaynatmak !")

    def pisir(self):
        print("pişiyor....")     

class KakaoluIslakKek(FettuciniAlfredo):
    def __init__(self,yag,seker,yumurta,vanilya,kakao,kabartmaTozu,un):
        self.yag=yag
        self.seker=seker
        self.yumurta=yumurta
        self.vanilya=vanilya
        self.kakao=kakao
        self.kabartmaTozu=kabartmaTozu
        self.un=un
        print("Gerekli Ana Malzemeler :",yag,seker,yumurta,vanilya,kakao,kabartmaTozu,un)

    def malzeme(self):
        print("6 kişilik kakaolu ıslak kek yapmak istersen;")
        print("3 adet yumurta \n 1 su bardağı toz şeker \n 1 su bardağı ayçicek yağı \n 1 su bardağı süt \n 1 paket vanilya \n 2 yemek kaşığı kakao \n 1 paket kabartma tozu \n 1 su bardağı un")

        print("Sosu için :")
        print("1 su bardağı süt \n 4 yemek kaşığı kakao \n 1 su bardağı toz şeker \n 1 çay bardağı sıvı yağ \n 1/2 çay kaşığı tuz")


class Kısır():
    def __init__(self,yag,tuz,pulBiber,bulgur,narEksisi,sogan,nane,salca):
        self.yag=yag
        self.tuz=tuz
        self.pulBiber=pulBiber
        self.bulgur=bulgur
        self.narEksisi=narEksisi
        self.sogan=sogan
        self.nane=nane
        print("Gerekli Ana Malzemeler :",yag,tuz,pulBiber,bulgur,narEksisi,sogan,nane,salca)

    def malzeme(self):
        print("6 kişilik kısır yapmak istersen;")
        print("2 su bardağı ince bulgur \n 1,5 su badağı sıcak su \n 2 yemek kaşığı domates salçası \n 1 çay bardağı zeytin yağı \n 1 tatlı kaşığı tuz \n 1 tatlı kaşığı pulbiber \n 2 adet limon suyu \n 1/2 çay bardağı nar ekşisi \n 6 dal taze soğan \n 1/2 demet maydanoz \n 1/2 demet nane ")

        print("Püf Noktası : Yeşillikleri iyice kuruttuktan sonra doğrayın, bekletmeden kısıra ilave edin.")    
          
f1=FettuciniAlfredo("fettucine","zeytinyağı","tereyağı","krema")     
f1.neKadarKullanmanGerek()
f1.pisir

k1=KakaoluIslakKek("ayçicek yağı","toz şeker","yumurta","vanilya tozu","kakao","kabartma tozu","buğday unu")
k1.malzeme()
k1.pisir()

k2=Kısır("zeytin yağı","tuz","pulbiber","ince bulgur","nar ekşisi","taze soğan","kuru nane","domates salçası")
k2.malzeme()


