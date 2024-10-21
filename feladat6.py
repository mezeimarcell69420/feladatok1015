import random
szamlalo = 0
szamok = [random.randint(1, 12) for _ in range(20)]

for szam in szamok:
    if szam % 3 == 0:
        print (szam)
        szamlalo += 1
print("Összesen" ,szamlalo, "darab szám volt 3-mal osztható.")
