# mitarbeiterNr = 3
# mitarbeiterName = 'Müller, Karl'
# mitarbeiterAlter = 34
# mitarbeiterAdresse = 'Mühlenweg 1A, 01069 Dresden'
# telefonNummer = '0177-1234567'
# mitarbeiterBeruf = 'Fachinformatiker'
# verheiratet = True
# lohnsteuerklasse = 3
# kinderAnzahl = 3
# lohn = 2870.00

# print(type(mitarbeiterNr),type(mitarbeiterName),type(mitarbeiterAlter),type(mitarbeiterAdresse),type(telefonNummer),type(mitarbeiterBeruf),type(verheiratet),type(lohnsteuerklasse),type(kinderAnzahl),type(lohn))

# print('############################################################################')

# print(127%7)
# print(12345%100)
# print(121%11)
# print(8%2)
# print(9%2)
# print(3%5)

# print('############################################################################')

# x=12
# x+=12
# print(x)

# x=12
# x-=12
# print(x)

# x=12
# x*=12
# print(x)

# x=12
# x/=12
# print(x)

# x=12
# x%=12
# print(x)

# print('############################################################################')

# gefahreneKilometer = float(input('Bitte gefahrene kilometer eingeben: '))
# kraftstoffMenge    = float(input('Bitte gefahrene Strecke eingeben: '))
# durchschnittVerbrauch = kraftstoffMenge/gefahreneKilometer*100
# print('Durchschnittverbrauch beträgt '+str(durchschnittVerbrauch)+' liter pro 100 Kilometer')

# print('############################################################################')

# spannung = float(input('Bitte Spannung in V eingeben: '))
# staerke = float(input('Bitte Strömstärke in A eingeben: '))
# widerstand = spannung/staerke
# print('Widerstand beträgt '+str(widerstand)+' Ohm')
# print(f'Widerstand beträgt {widerstand} Ohm')

# print('############################################################################')

# hoehe        = int(input('Bitte die Höhe in px eingeben: '))
# breite       = int(input('Bitte die Breite in px eingeben: '))
# farbtiefe    = int(input('Bitte die Farbtiefe eingeben: '))
# bilderAnzahl = int(input('Wie viele Bilder? '))

# byteProPixel = farbtiefe/8
# pixel        = hoehe*breite
# speicherByte = pixel*byteProPixel

# print(f'Bytes pro pixel: {byteProPixel}')
# print(f'Sie benötigen {speicherByte/1024/1024/1024} GiB Speicherplatz')

# print('############################################################################')

# a=120
# b=10
# print(a%b)

# a=14
# b=3
# print(a%b)

# a=61
# b=17
# print(a%b)

# a=243
# b=13
# print(a%b)

# a=4
# b=5
# print(a%b)

# a=5
# b=4
# print(a%b)

# a=-5
# b=4
# print(a%b)

# a=-5
# b=-4
# print(a%b)

# a=5
# b=-4
# print(a%b)

# print('############################################################################')

# a=11
# a=a%10
# print(a)

# a=11
# a=a%a
# print(a)

# a=11
# a=a*a
# print(a)

# a=11
# a-=a/a
# print(a)

# a=11
# a+=a+a
# print(a)

# a=11
# a+=a*a+a
# print(a)

# a=11
# a=a+a*3+a
# print(a)

# a=11
# a=(a-1)/2+7
# print(a)

# a=11
# a-=a-a*4/2+a*a
# print(a)

# print('############################################################################')

# x=0
# x+=float(input("Wert1: "))
# x+=float(input("Wert2: "))
# x+=float(input("Wert3: "))
# x+=float(input("Wert4: "))
# x+=float(input("Wert5: "))
# print('Ergebnis:', x/5)

# print('############################################################################')

# #Eingabe
# u=float(input('Geben Sie bitte die Spannung in Volt ein: \n'))
# i=float(input('Geben Sie bitte die Stromstärke in Ampere ein: \n'))
# t=float(input('Geben Sie bitte die Zeit im Betrieb in minuten ein: \n'))

# #Widerstand ausrechnen
# r=u/i

# #Elektrischen Arbeit ausrechnen
# #Minuten in Sekunden umwandeln
# t=t*60
# #Elektrischen Arbeit in Wattsekunde
# w=u*i*t

# #Elektrische Leistung
# p=u*i

# #Ausgabe
# print(f'Widerstand beträgt {r} Ohm')
# print(f'Elektrische Arbeit beträgt {w*(1/3600000)} kWh')
# print('Elektrische Leistung beträgt', p)

# print('############################################################################')

#Eingabe
datenMenge=float(input('Geben Sie bitte die Datenmenge in MB ein: \n'))
datenUebertragungsRate=float(input('Geben Sie bitte die Datenübertragungsrate in Kbit/s ein: \n'))

#Rechnen
#MB ins bit umrechnen
datenMengeBit=datenMenge*8*1000*1000
#Zeit in Sekunden
zeit=datenMengeBit/datenUebertragungsRate
#Sekunden in Minuten umwandeln
zeit=zeit*60

print(f'Es ist {zeit} Minuten für Übertragung benötigt')