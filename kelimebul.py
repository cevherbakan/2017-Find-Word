import os


global adres
adres="\Desktop\listeleme deneme"



def uzanti_kaydet(uzanti):
    global liste

 
    ths = open("uzantidosyasi.uzanti", "w")
    ths.write(uzanti)
    ths.close()

    try:
        liste= os.listdir(uzanti)
        

    except WindowsError:
        
        yyy_metin=''
        yeni_metin=uzanti.split(chr(92))
        yeni_metin[-1]=''
        
        for i in yeni_metin:
            yyy_metin=yyy_metin+i+chr(92)

        print "uzanti",yyy_metin

        uzanti_kaydet(yyy_metin)



    


def dosya_kontrol():

    for dosya in liste:
        for harf in dosya:
            
            if harf==".":
                dosya_klasor = open("uzantidosyasi.uzanti", "r")
                metin = dosya_klasor.read()
                dosya_klasor.close()
                
                arama(metin+chr(92)+dosya,"merh")
                break
    

def arama(dosya_adi,kelime):


    dosya = open(dosya_adi, "r")
    metin = dosya.read()
    sayac=0
    for i in range(len(metin)-1):
        
        if metin[i]==kelime[sayac]:
            sayac+=1
            if sayac==len(kelime)-1:
                print "Dosya adi=",dosya_adi,"  No=",i,"  bulundu"
                break
        else:
            sayac=0
      
    dosya.close()
    


    

def klasor_kontrol():
    dosya_kontrol()
    
    for dosya in liste:
        anahtar=False
        for harf in dosya:
            
            if harf==".":
                anahtar=False

                break
            elif 0<len(dosya):
                anahtar=True
                
        if(anahtar==True):
            print "dosya",dosya
            dosya_klasor = open("uzantidosyasi.uzanti", "r")
            metin = dosya_klasor.read()
            dosya_klasor.close()
            
            uzanti_kaydet(metin+chr(92)+dosya)
            
            klasor_kontrol()







def baslama():
    
    uzanti_kaydet(adres)
    
    
    klasor_kontrol()

baslama()
    
