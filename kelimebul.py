import os




def uzanti_kaydet(uzanti):
    global liste
    print "uzanti kaydet"

 
    ths = open("uzantidosyasi.uzanti", "w")
    ths.write(uzanti)
    ths.close()

    try:
        liste= os.listdir(uzanti)
        

    except WindowsError:


        return False
    
    return True

    


def dosya_kontrol(kelime):
    klasor_listesi=''

    for dosya in liste:
        kilit=False
        
        for harf in dosya:
            
            if harf==".":
                dosya_klasor = open("uzantidosyasi.uzanti", "r")
                metin = dosya_klasor.read()
                dosya_klasor.close()
                
                arama(metin+chr(92)+dosya,kelime)
                kilit= False
                break
            else:
                kilit= True
        if kilit==True:    
            klasor_listesi+=dosya+';'
    print klasor_listesi
        
    return klasor_listesi
    

def arama(dosya_adi,kelime):


    dosya = open(dosya_adi, "r")
    metin = dosya.read()
    sayac=0
    for i in range(len(metin)-1):
        
        if metin[i]==kelime[sayac]:
            sayac+=1
            if sayac==len(kelime)-1:
                print "Dosya adresi=",dosya_adi,"  No=",i,"  ****bulundu\n"
                break
        else:
            sayac=0
      
    dosya.close()
    


    

def klasor_kontrol(kelime):
    
    klasor_liste=dosya_kontrol(kelime)
    yeni_klas_liste=klasor_liste.split(';')
    print yeni_klas_liste


    if (len(yeni_klas_liste)!=1 and yeni_klas_liste[0]!='':
        for dosya in yeni_klas_liste:
            print dosya
            
            dosya_klasor = open("uzantidosyasi.uzanti", "r")
            metin = dosya_klasor.read()
            dosya_klasor.close()
    #////////////////////////
            print "*****************",metin+chr(92)+dosya
            if uzanti_kaydet(metin+chr(92)+dosya)==False:
                print "girildi"
                while uzanti_kaydet(metin+chr(92)+dosya)==False:
                    yyy_metin=''
                    yeni_metin=metin.split(chr(92))
                    
                    for al in range((len(yeni_metin)-1),0,-1):
                        
                        
                        if yeni_metin[al]!='':
                            yeni_metin[al]=''
                            break             
                    for i in yeni_metin:
                        yyy_metin=yyy_metin+i+chr(92)

                    metin=yyy_metin

            uzanti_kaydet(metin+chr(92)+dosya)
            klasor_kontrol(kelime)
    else:
        
#///////////////////////////////////////
        


def baslama():
    global adres

    adres=raw_input("Aranacak adres giriniz:  ")
    
    uzanti_kaydet(adres)
    kelime=raw_input("Aranacak kelime:")
    if len(kelime)<2:
        print("2 karakter veya daha fazla giriniz!!!!")
        baslama()
    
    klasor_kontrol(kelime)



baslama()
    
