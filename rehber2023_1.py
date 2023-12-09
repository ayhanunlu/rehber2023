from tkinter import *
import tkinter.messagebox

pencere=Tk()
pencere.geometry("700x700+200+200")
pencere.title("Rehber Programı 1.0")
global kut
bulunan=0
def kontrol():
    global kut
    try:
        with open("veriler.dat","r",encoding="utf-8") as dosya:
            kut=dosya.readlines()
            return kut
    except FileNotFoundError:
        kut=[]
        return kut
kut=kontrol()
    
kut=kontrol()
print (kut)
def kaydet(kutuk):
    with open("veriler.dat","w",encoding="UTF-8") as dosya:
        dosya.writelines(kutuk)
        tkinter.messagebox.showinfo("Dikkat","Veri Kaydedildi!!!")
        return

def oku():
    global kut
    with open("veriler.dat","r",encoding="UTF-8") as dosya:
        kut=dosya.readlines()
        return kut
def verisorma():
    global kut
    global bulunan
    kut=kontrol()
    Frame2=Frame()
    def veriara():
        global kut
        global bulunan
        global toplamkayit
        toplamkayit=len(kut)
        
        arananveri=aramatext.get()
        if bulunan>=toplamkayit-1:
                    bulunan=0
        for i in range(bulunan,toplamkayit):
            print (f"Bulunan:{bulunan}")
            kut2=kut[i]
            kut3=kut2.split(",")
            mo=arananveri in kut3[0]
            if mo==True:
                Text1.delete(0,"end")
                Text1.insert(0,kut3[0])
                Text2.delete(0,"end")
                Text2.insert(0,kut3[1])
                Text3.delete(0,"end")
                Text3.insert(0,kut3[2])
                bulunan=i
                bulunan+=1
                print (i)
                
                break
                
            #print (kut3)
            #print(mo)
        
            

    arama=Label(Frame2,text="Aranan Kişi:",font="Times 20")
    aramatext=Entry(Frame2,font="Times 20")
    aramatus=Button(Frame2,text="Ara",font="Times 20",command=veriara)
    iptal=Button(Frame2,text="İptal",font="Times 20",command=Frame2.destroy)
    Etiket1=Label(Frame2,text="Ad-Soyad:",font="Times 20")
    Text1=Entry(Frame2,font="Times 20")
    Etiket2=Label(Frame2,text="Tel:",font="Times 20")
    Text2=Entry(Frame2,font="Times 20")
    Etiket3=Label(Frame2,text="E-mail:",font="Times 20")
    Text3=Entry(Frame2,font="Times 20")
    #Tus1=Button(Frame2,text="Kaydet",font="Times 20",command=kaydet2)
    #Tus2=Button(Frame2,text="İptal",font="Times 20",command=Frame1.destroy)


    Etiket1.grid(row=3,column=1)
    Text1.grid(row=3,column=2)
    Etiket2.grid(row=4,column=1)
    Text2.grid(row=4,column=2)
    Etiket3.grid(row=5,column=1)
    Text3.grid(row=5,column=2)
    #Tus1.grid(column=3,row=1)
    #Tus2.grid(column=3,row=2)
    arama.grid(column=1,row=1)
    aramatext.grid(column=2,row=1)
    aramatus.grid(column=3,row=1)
    iptal.grid(column=4,row=1)


    
    Frame2.grid()
    
    
    for i in range(0,toplamkayit):
        kut2=kut[i]
        kut3=kut2.split(",")
        print (kut3[0])
    

def verigirme():
    global kut
    kut=kontrol()
    def kaydet2():
        global kut
        kut=kontrol()
        kut.append(Text1.get()+","+Text2.get()+","+Text3.get()+"\n")
        print (kut)
        kaydet(kut)
        Frame1.quit
    Frame1=Frame()
    Etiket1=Label(Frame1,text="Ad-Soyad:",font="Times 20")
    Text1=Entry(Frame1,font="Times 20")
    Etiket2=Label(Frame1,text="Tel:",font="Times 20")
    Text2=Entry(Frame1,font="Times 20")
    Etiket3=Label(Frame1,text="E-mail:",font="Times 20")
    Text3=Entry(Frame1,font="Times 20")
    Tus1=Button(Frame1,text="Kaydet",font="Times 20",command=kaydet2)
    Tus2=Button(Frame1,text="İptal",font="Times 20",command=Frame1.destroy)


    Etiket1.grid(row=1,column=1)
    Text1.grid(row=1,column=2)
    Etiket2.grid(row=2,column=1)
    Text2.grid(row=2,column=2)
    Etiket3.grid(row=3,column=1)
    Text3.grid(row=3,column=2)
    Tus1.grid(column=3,row=1)
    Tus2.grid(column=3,row=2)


    Frame1.grid()
    




menu = Menu(pencere)
pencere.config(menu=menu)
dosyamenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Dosya",menu=dosyamenu) #ana başlık
dosyamenu.add_command(label="Veri Girme",command=verigirme)
dosyamenu.add_command(label="Veri Sorma",command=verisorma)
dosyamenu.add_command(label="Veri Listeleme")
dosyamenu.add_command(label="Çıkış",command=pencere.quit)





pencere.mainloop()