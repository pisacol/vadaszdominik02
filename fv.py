import os
import random


def main():
    bszam1=[]
    bszam2=[]
    bszam3=[]
    bszam4=[]
    ertek=random.randint(0,9)
    ertek1=random.randint(0,9)
    ertek2=random.randint(0,9)
    ertek3=random.randint(0,9)
    bszam1=(ertek,ertek1,ertek2,ertek3)
    ertek4=random.randint(0,9)
    ertek5=random.randint(0,9)
    ertek6=random.randint(0,9)
    ertek7=random.randint(0,9)
    bszam2=(ertek4,ertek5,ertek6,ertek7)

    ertek8=random.randint(0,9)
    ertek9=random.randint(0,9)
    ertek10=random.randint(0,9)
    ertek11=random.randint(0,9)
    bszam3=(ertek8,ertek9,ertek10,ertek11)
    ertek13=random.randint(0,9)
    ertek14=random.randint(0,9)
    ertek15=random.randint(0,9)
    ertek16=random.randint(0,9)
    bszam4=(ertek13,ertek14,ertek15,ertek16)

def lejarat():
    ev=random.randint(21,25)
    ho=random.randint(0,12)
    if ho < 10:
        int(0+ho)
    lej=(ev +"/"+ ho)

def fv2():
    penz1=(65000)
    penz2=(80000)
    penz3=(200000)
    if ev = 21:
        print(penz1)
        
    elif ev = 22:
        print(penz1)

    elif ev = 23:
        print(penz2)
        
    elif ev = 24:
       print(penz2)
    else:
        print(penz3)

def randnev():
    knev=str(["jozsi","sanyi","Kata","béla","Betti","eva","beni","peti","erika"])
    vnev=str(["kovacs","molnar","Kiss","toth","nagy","horvath","szabo","Papp","farkas"])

    nev=random.choice(knev) +" "+ random.choice(vnev)
    print(nev)





