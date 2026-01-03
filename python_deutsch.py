# #### Tag 1 (20.12.2025)  
# Ubung: Variablen
# Name='Abdulloh'
# Age=22
# stadt='Samarkand'
# print('Mein Name ist' , Name)
# print('Ich bin ', Age )
# print('Ich komme aus', stadt)

# Ubung:String 

# name='Anna'
# nachname='Tomis'
# print('Mein name ist', name ,'und mein Vorname ist ' , nachname )

# Operationen mit f-string 

# worter='sich einigen auf, allzu , Mittelweg, dominieren, sich beteiligen an ,Zeitspanne,Croudfunding '
# print(f'Ich habe heute die Nottige Worter beherscht ,wie {worter}')

# Sonderzeichen 
# print('Sehr geehrte Damen und Herren, \nich schreibe Ihnen , weil ich ein Problem habe.\nIch gehe morgen in die Schule nicht ')

# #### String-Methode Tag 2 (23.12.2025)

# .Upper()-Die Methode wandelt alle Buchstaben eines Textes in Großbuchstaben um.

# vorname='abdulloh'
# nachname='nurimov'
# print(f'mein Nachname ame ist {vorname.upper()} und mein Nachname ist {nachname.upper()

# .Lower()-die Methode wandelt alle Buchstaben eines textes in Kleinbuchstaben um.

# ziel='PYTHON LERNEN'
# print(ziel.lower())

# kanal='deutschify school'
# print(kanal.title())

# men='men nemis tili uqiyman'
# print(men.capitalize())

# name='abdulloh'
# nachname='nurimov'
# name_nachname=f'{name} {nachname}'
# name_nachname=name_nachname.capitalize()
# print(name_nachname)

# .lstrip()-die Methode entfernt Leerzeichen (oder Zeichen) am Anfang eines textes. links-left

# .rstrip()-die Methode entfernt alle Zeichen rechts (am Ende) eines Strings, standardmäßig Leerzeichen.

# .strip()-die Methode entfernt alle Leerzeichen oder bestimmte Zeichen am Anfang und Ende eines Strings.

# #### Tag 3 (24.12.2025)

# Input()- ist eine Funktion, die benutzt wird, um Daten vom benutzer einzugeben.

# name=input('Wie heisst du ?')
# print('Hallo,',name,"Wie geht es dir ? ")
 
# daten=input('gib dein Alter ein ?')
# print('Sehr gut\nDu bist Jahre alt', daten)


# Operationen mit Zahlen 

# In Python gibt es verschiedene Arten von Zahlen.

# 1-Ganze Zahlen (int=integer)
# Beispiel: 2, 4 , -5

# 2-Fliesskommazahlen (float)
# Beispiel: 3.2, 4.8 , -9.0 

# 3-Komplexe Zahlen (complex)

# x, y, z = 2, 0.9, -5
# print(x,y,z)

# bevolkerungs_zahl=7_345_567

# / Division geben nur float zruck 

# d=100/2

# // ist die ganzzahl-Division, die nur den ganzzahligen Teil zuruck, ohne Nachkommastellen.

# a=10/3

# radius=5
# Pi=3.14159
# flache=Pi*radius**2
# print('Flache des Kreisies', flache )

# r=8
# Pi=3.14
# umfang=2*Pi*r
# print('Umfang des Kreises',umfang)

# Type Casting - Datentyp umwandeln 

# name='Abu'
# alter='22'
# nachrecht=name+" "+alter + " ist Jahre alt"
# nachrecht=f'{name} ist {alter} Jahre Alt'
# print(nachrecht)

# g_jahr=int(input('Geben Sie Ihr Geburtsjahr ein:'))
# alter=2025-g_jahr
# print(alter)

# #### Tag 4 (25.12.2025)

# Operationen mit Liste 

# Eine Liste ist eine Sammlung von Elementen (Zahlen, Sring etw)

# namen=['Abdulloh','Nurislom','Shukrona','Doston']
# print(namen)

# kosten=[12, 35, 24, 45]
# print(kosten)

# Gemischte Listen-enthalt verschiedene gatentypen gleichzeitig.

# zahlen=[3 ,'zwei', 4,'Drei']
# print(zahlen)

# Leere Liste-enthalt keine Elemente 

# leere_liste=[]

# Die Zahlung in Listen - Die Zahlung beginnt bei 0 . Das erste Element hat den Index 0, das zweite 1, das dritte 2 usw.

# namen=['Abdulloh','Nurislom','Shukrona','Doston']
# print(namen[0])
# print(namen[1])
# print(namen[-1])
# print(namen[-2])
# print(namen[2].upper())
# print(namen[-1].lower())
# print(namen[3].title())

# kosten=[12, 35, 24, 45]
# print(kosten[0]-kosten[1]-12)

# #### Tag 5 (26.12.2025)

# Einzehlnes Element in der Liste andern 

# zahlen=[1,2,3,4,5,6]
# zahlen[2]=45
# print(zahlen)

# Mehrere Elemente andern

# mitbewerbern=['Abdulloh','Tom','Doston','Nurislom','Manzura']
# mitbewerbern[2:-1]=['Alisher','Bobir']
# print(mitbewerbern)

# .append()-fugen ein neues Element am Ende eienr hin.

# fruchte=['Apfel','Banane','Traube']
# fruchte.append('Birne')
# print(fruchte)


# .insert()-an bestimter Stelle einfugen

# fruchte=['Apfel','Banane','Traube']
# fruchte.insert(0,'Orange')
# print(fruchte)

# del-in einer Liste uber den Index loschen

# meine_liste=[21,23,45,89]
# del meine_liste[-2]
# print(meine_liste)

# kosten=[34,45,89]
# del kosten[2]
# print(kosten)

# .remove()-loschen ein Element nach seinem Wert aus einer Liste 

# remove_liste=['Verwand','Ausrede','Worter']
# remove_liste.remove('Worter')
# print(remove_liste)

# .pop()-loschtman einer Element aus einer Liste und bekommt es zuruck.

# einkauf_liste=['Banane','wurst','Apfel','Tomate']
# gekauft=einkauf_liste.pop(0)
# print("Men", gekauft ,'sotib oldim ')

# #### Tag 6 (27.12.2025)

# .sort()-sortiert die Liste aufsteigend von klein nach groS A-Z

# autos=['bmw','audie','toyoto','bentle']
# autos.sort()
# print(autos)

# zahlen=[4,5,9,8,0]
# zahlen.sort()
# print(zahlen)

# zahlen.sort(reverse=True)
# print(zahlen)

# autos.sort(reverse=True)
# print(autos)

# .sorted()-sortiert Daten aber andert die orginale Liste Nicht

# kosten=[12,34,56,78]
# print(sorted(kosten , reverse=True))

# print(sorted(kosten))

# tiere=['cut','mause','hund','monkiy']
# tiere.reverse()
# print(tiere)

# len()-es zahlt, wie viele Elenmente in der Liste hat 

# x=[2,4,6,4,5,5,4,3,3,3,3,4]
# uzunlik=len()
# print(x)

# # range()-es erstellt eine Liste von Zahlen

# zahlen=list(range(0,12))
# zahlen.sort(reverse=True)
# print(zahlen)

# gerade_zahlen=list(range(0,11,2))
# print(gerade_zahlen)

# ungerade_zahlen=list(range(100,1000,123))
# print(ungerade_zahlen)

# preise=(1200,2300,4500,5000)
# billig=min(preise)
# teuer=max(preise)
# zusammen=f'Der sehr gunstige Preis batragt {billig}, der teure Preis betragt {teuer}'
# print(zusammen)

# # Ausschnitt

# ausschnitt=[20,30,40,50]
# print(ausschnitt[1:3])

# print(ausschnitt[:3])

# print(ausschnitt[1:3])

# mein_autos=['bmw','audi','volvo','porsche']
# kopie_autos=mein_autos[:]
# print(kopie_autos)

# kopie_1=[1,2,3,4,5,]
# kopie_2=kopie_1[:]
# print(kopie_2)

# kopie_1.append("bmw")
# kopie_2.insert(0,'mers')

# Tupel-ist wie eine Liste , aber unveranderlich man kann Elemente nicht andern , hinzufugen oder loschen.
# Topel werden mit runden Klammen () geschrieben , Listen mit [].

# toys=('baby','cats','bus','cars')
# print(toys)

# toys=list(toys)
# toys.append('dade')
# print(toys)

# namen=['abdulloh','doston','manzura']
# namen_kopie=namen[:]
# print(namen_kopie)

# namen=['abdulloh','doston','manzura']
# namen=tuple(namen)
# namen=list(namen)

# #### Tag 7 (28.12.2025)

# zahlen=list(range(1,11))
# print(zahlen)

# for-ist eine Schleife. Eine Schleife bedeutet: Etwas wird mehrmals wiederholt.

# gaste=('Alisher','Bobir','Utkir') 
# for gast in gaste:
#    print('Hallo',gast)
#    print('Tschuss',gast)

# freunde=['Dilmurod','Shohruh','Javohir','Murod']
# for freund in freunde:
#       print(f'Sehr geehrtr {freund} \nich schreibe ihnen , weil ich eine Hochzeit mache.\nDeshalb muchte ich ihnen einladen.\nMit freundlichen grussen \nAbdulloh Nurimov')
   
# zahlen=list(range(2,11))   
# for zahl in zahlen:
#     print(f'{zahl} ist gleich dem Quadrat von {zahl**2}')

# zahlen=list(range(11))
# quadrat_list=[]
# for zahl in zahlen:
#     quadrat_list.append(zahl**2)
# print(zahlen)
# print(quadrat_list)

# sonlar=list(range(10,101))
# sonlar_kv=[]
# for son in sonlar:
#       sonlar_kv.append(son**3)
# print(sonlar)
# print(sonlar_kv)

# freunde=[]
# for n in range(5):
#     freunde.append(input(f'{n+1} wer ist ihr echte Freund'))
# print(freunde)
    
# namen=['Ali','Vali']
# for name in namen:
#     name_input=input(f'{name} wie geht es dir ')
# print(namen)
    
# bezahlt=[]
# for kosten in range(4):
#     bezahlt.append(input(f'{kosten} wie viel kostet ?'))
# print(bezahlt)

# namen=['abdulloh','dilmurod','doston']
# for n in namen:
#     print(f'in dieser Liste hat die Namen {n} mal wiederholt')
# print(f'Namen ist mal wiederholt {len(namen)}')

# zahlen=[]
# for zahl in range(11,100,2):
#     zahlen.append(zahl**3)
#     print(f'{zahl} ist gleich dem Quadrat von{zahl**3}')
    
# filme=[]   
# for film in range(5):
#     filme.append(input(f'{film+1} Was ist deine lieblins Film?'))
# print(filme)
    
# zahlen=[]  
# for zahl in range(5):
#     zahlen.append(input(f'{zahl+1} Was ist dein lieblingszahl?'))
# print(zahlen) 
# print(min(zahlen))
# print(max(zahlen))    

# # if

# cars=['audi','bmw','porschie','volvo']
# new_cars=[]
# for car in cars:
#     new_cars.append(car.title())
# print(new_cars)

# cars=['audi','bmw','porschie','volvo']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
# else:
#     print(car.title())

# cars=[]
# for car in range(11):
#     cars.append(car)
# print(cars)

# zahlen=list(range(1,5))
# kvs=[]
# for zahl in zahlen:
#     kvs.append(f'{zahl} ning kvsi {zahl**2} ga teng')
# print(zahlen)
# print(kvs)

# zahlen = range(1,6)

# for zahl in zahlen:
#     print(f'{zahl} ning kvadrati {zahl**2} ga teng')

# cars=['audie','bmw','volvo']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# name='Ali'
# name.lower()=='ali'
# print(name)

# namen=input('Wie heissen Sie\n-')
# if namen.lower() != 'abdulloh':
#     print(f'Hi {namen.title()} ich warte Abdulloh ')
# else:
#     print('Hi Abdulloh')

# kod=input('Gib dein Name\n-j')
# if kod.title() != 'Abdulloh':
#     print(f'das ist richtig {kod}')
# else:
#     print('das ist falsch')

# cars=['bmw','audie','volvo']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# names = ['ALI', 'vali', 'admin',  'hasan']
# for name in names :
#    if name == 'admin':
#        print(name.upper())
#    if name == 'ALI':
#        print(name.lower())
#    else:
#        print(name.title())
     
# ism=input('Ismingiz nima?\n>>>>')
# if ism.lower() != 'ali':
#     print(f'Uzur {ism.title()} biz Alini kutyabmiz')
# else:
#     print('Salom ,Ali ')

# name=input('Ismingizni kiriting\n>>>>?')
# if name.lower() == 'abu':
#     print('Salom ,Abu')
# else:
#     print(f'Salom {name.title()} , uzur biz Abuni kutyabmiz.')

# antwort=int(input("12*6 nechiga teng ?"))
# if antwort != 72:
#     print('Javob notugri')
# else:
#     print('Javob tugri')
    
# yosh=int(input('Yoshingiz nechida?')) 
# if yosh >= 18 :
#     print('Xush kelibsiz')
# else:
#     print('18 yoshdan kichiklar kirish taqiqlanadi!')

# login=input('Yangi login kiriting\n>>')
# if len(login) <=5 :
#     print('5 tadan kub belgi tanlang')
# else:
#     print('qabul qilindi')

# yil=int(input('Tugilgan yilingizni kiriting?'))
# if 2025-yil > 18 :
#     print('xush kelibsiz')
# else:
#     print(f'Yoshingiz {2025-yil}da ekan')
#     print('Kirish mumkin emas')

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car =='gm':
#         print(car.upper())
#     else: 
#         print(car.title())
        
    
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']    
# for car in cars:
#     if car !='gm':
#        print(car.title())
#     else:
#         print(car.upper())
    
# login=input('Ismingizni kiriting\n>>>>')
# if login.lower() == 'admin':
#     print('Xush kelibsiz Admin .\nFoydalanuvchilar ruyhatini kurasizmi?')
# else:
#     print(f'Xush kelibsiz {login.title()}')

# x=float(input('birinchi son'))
# y=float(input('ikkinchi son'))
# if x==y: print('Sonlar teng') 
# else:     print('sonlar teng emas')

# son = float(input("Istalgan son kiriting:"))
# print("Son manfiy") if son<0 else print("Son musbat")   

# #### Tag 8 (29.12.2025)

# # elif-es wird benutzt , wenn mehrere Bedeutungen gepruft werden sollen.

# yosh=int(input('Yoshingiz nechida?'))  
# if yosh <=4:
#     print('Sizga kirish tekin')
# elif yosh <= 7:
#     print("Sizga kirish 5000 so'm")
# elif yosh <= 12:
#     print("Sizga kirish 10000 so'm")
# else:
#     print('Sizga kirish mumkin emas')

# ish=input('Bugun nima kun ?\n>>>>')
# if ish.lower() == 'dushanba' or ish.lower()=='yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni')

# kun=input('Bugun nima kun?')
# harorat=float(input('Havo harorati qanday?'))
# if harorat >=30 and kun.lower() == 'yakshanba':
#     print('Ketdik aylanishga ')
# elif harorat <=30 and kun.lower() == 'dushanba':
#     print('Bugun uyda qolamiz')
    
# kun=input('Bugun nima kun?')
# harorat=float(input('Havo harorati qanday?'))
# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30 :
#     print('Ketdik chumilishga')
# elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat <=25:
#     print('Bugun sovuq uyda qolamiz')

# narh=15000
# choy=True
# salat=True
# if choy and salat:
#     narh=narh+10000
# elif choy or salat:
#     narh=narh+5000
# print(f'Jami {narh}')

# narh=20000
# suv=True
# olma=False
# if suv and olma:
#     print(f'Jami {narh+6000}')
# elif suv or choy:
#     print(f'Jami{narh+3000}')
    
# narh=200
# suv=1 
# salat=1
# olma=1 
# non=0
# if suv:
#     print('Mijoz suv oldi')
#     narh=narh+200
# if salat:
#     print('Mijoz salat oldi')
#     narh=narh+300
# if olma:
#     print('Mijoz olma oldi')
#     narh=narh+100
# if non:
#     print('Mijoz non olmadi')
#     narh=narh+500
# print(f'Jami {narh}')

# menu=['osh','shurva','xalim','kabob']
# print('osh' in menu)

# menu=['osh','shurva','xalim','kabob']
# ovqat=input('Nima ovqat yiysiz ?')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi')
# else:
#     print('Afsuski bizda bunday ovqat yuq')

# menu=['osh','shurva','xalim','kabob']
# buyurtmalar=['osh','xalim','kabob','tosh']
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f'Menyuda {taom} bor')
#     else:
#         print(f'Menyuda {taom} yuq')
          
# #### Tag 9 (1.1.2026)

# yosh=int(input('Yoshingiz nechida'))
# if yosh <= 12:
#     print('Sizga kirish tekin')
# else:
#         print('Sizhga kirish 10 ming')
    
# ruxsat=input('Ismingiz nima ?')
# if ruxsat.lower() == 'dilmurod':
#     print(f'Xush kelibsiz {ruxsat.lower()}  ?')
# else:
#     print(f'Xush kelibsiz {ruxsat.title()}, lekin biz Dilmurodni kutyabmiz')
    
# yosh=int(input('Yoshingizni kiriting ?'))
# if yosh >= 18:
#     print(f'Siz balog`atga yitgansiz')
# else:
#     print('Siz balogatga yitmagansiz')
    
# son=float(input('Son kiriting'))
# if son <= 0:
#     print('Son manfiy')
# else:
#     print('Son musbat')
    
# baxo=int(input('Baxoni kiriting ?'))
# if baxo <= 90 and baxo >= 100:
#     print('Alo')
# elif baxo <= 70 and baxo >= 89:
#     print('Yaxshi')
# elif baxo <= 50 and baxo >= 69:
#     print('Qoniqarli')
# elif baxo <= 0 and baxo >= 49:
#     print('Yiqildi')
# else:
#     print('Xatolik')

# baxo = int(input("Bahoni kiriting: "))

# if baxo >= 90 and baxo <= 100:
#     print("A'lo")
# elif baxo >= 70 and baxo <= 89:
#     print("Yaxshi")
# elif baxo >= 50 and baxo <= 69:
#     print("Qoniqarli")
# elif baxo >= 0 and baxo <= 49:
#     print("Yiqildi")
# else:
#     print("Noto‘g‘ri baho")

    
# login=input('Loginni kiriting')
# parol=int(input('Parolni kiriting'))
# if login.lower() == 'abdulloh' and parol==20033107:
#     print('Xush kelibsiz')
# elif login != 'abdulloh':
#     print('Parol xato')
# elif parol != 20033107:
#     print('Login xato')

# son = float(input("Juft son kiriting: "))
# if son >= 0:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")
    























    
    
    




