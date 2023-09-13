## Aufgabe 3

anzahl = 25
i = 0
j = 1
r = 1
while i < anzahl:
    print(j, end="   ")
    j=j+r
    if j==5: r=-1
    if j==1: r=1
    i=i+1


##Aufgabe 4
##Stromkosten gesamt
stromKostenGesamt = 500
'''Berechnung des Durchshnitts'''
durchschnitt = stromKostenGesamt / 12
"""Ausgabe"""
print("durchschnittliche Stromkosten pro Monat in Euro:", durchschnitt)