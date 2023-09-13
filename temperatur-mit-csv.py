try:
    datei_name = str(input('Bitte die Dateiname eingeben(ohne .txt):   '))
    datei_name = datei_name + '.csv'
    pfad_ordner = "C:\\Users\\Student\\Documents\\"
    pfad = pfad_ordner + datei_name
    file = open((pfad), "x+")
    print("Programm zur Berechnung einer Durchschnittstemperatur \n")
    print("Geben Sie bitte drei Temperaturwerte in °C ein!")
    temperatur1 = float(input("1. Wert: "))
    temperatur2 = float(input("2. Wert: "))
    temperatur3 = float(input("3. Wert: "))

    durchschnitt = (temperatur1 + temperatur2 + temperatur3) / 3
    string_durchnschnitt = str(durchschnitt)

    str_temperatur1 = str(temperatur1)
    str_temperatur2 = str(temperatur2)
    str_temperatur3 = str(temperatur3)

    file.write(str_temperatur1 + "\n")
    file.write(str_temperatur2 + "\n")
    file.write(str_temperatur3 + "\n")
    file.write(f"Durchnschnitt ist: {string_durchnschnitt}")
    file.close()

except Exception as e:
    print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
