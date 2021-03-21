#Zad1
'''f=open("plik.txt", "w")
for x in range(1,100):
    if x % 4 == 0:
        f.write(x.__str__())
        f.write("\n")
f.close()'''
#Zad2
'''f=open("plik.txt", "r")
for line in f:
    print(line)
f.close()'''
#Zad3
'''with open("plik2.txt", "w") as file:
    file.write("linia1 \n")
    file.write("linia2 \n")
    file.write("linia3 \n")

with open("plik2.txt", "r")as file:
    for line in file:
        print(line, end="")'''
#Zad4
'''class NaZakupy:
    nazwa_produku =""
    ilosc=0
    jednostka_miary = "j"
    cena_jed = 0.00

    def __init__(self,np,i,jm,cj):
        self.nazwa_produku = np
        self.ilosc = i
        self.jednostka_miary = jm
        self.cena_jed = cj
    def wyswietl_produkt(self):
        print(self.nazwa_produku)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
    def ile_produktu(self):
        a= self.ilosc
        print(a," " + self.jednostka_miary)
    def ile_kosztuje(self,ile):
        return ile * self.cena_jed

obiekt = NaZakupy("ziemniak", 1, "kg", 2.00)
obiekt.wyswietl_produkt()
obiekt.ile_produktu()'''
#Zad5
'''class Ciag:
    lista = []

    def wyswietl_dane(self):
        for x in self.lista:
            print(x)

    def pobierz_elementy(self):
        ile = eval(input("podaj liczbe wszystkich elemntow ciagow: "))
        for x in range(0, ile):
            self.lista.append(eval(input((x+1).__str__() + ". element:")))

    def pobierz_parametry(self):
        ile = eval(input("podaj liczbe wszystkich elemntow ciagow: "))
        pierwsza = eval(input("podaj pierwszy wyraz ciagu: "))
        roznica = eval(input("podaj roznice miedzy wyrazamia ciagu: "))
        self.lista.append(pierwsza)
        for x in range(1, ile):
            self.lista.append(pierwsza + roznica * x)
    def policz_sume(self):
        suma = 0
        for x in self.lista:
            suma = suma + x
        return suma
    def policz_elementy(self):
        print("Nie rozumiem treści zadania")


obiekt = Ciag()
obiekt.pobierz_parametry()
obiekt.wyswietl_dane()
print(obiekt.policz_sume())'''
#Zad6
'''class Robaczek:
    x = 0
    y = 0
    krok = 1

    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.krok = k

    def idz_w_gore(self,ile_krokow):
        self.y = self.y + self.krok*ile_krokow
    def idz_w_dol(self,ile_krokow):
        self.y = self.y - self.krok*ile_krokow
    def idz_w_lewo(self,ile_krokow):
        self.x = self.x - self.krok*ile_krokow
    def idz_w_prawo(self,ile_krokow):
        self.x = self.x + self.krok*ile_krokow
    def pokaz_gdzie_jestes(self):
        print("pozycja X, Y:", self.x, self.y)

teddy = Robaczek(0,0,1)
teddy.pokaz_gdzie_jestes()
teddy.idz_w_gore(2)
teddy.pokaz_gdzie_jestes()
teddy.idz_w_prawo(5)
teddy.pokaz_gdzie_jestes()
teddy.idz_w_dol(1)
teddy.pokaz_gdzie_jestes()
teddy.idz_w_lewo(4)
teddy.pokaz_gdzie_jestes()'''