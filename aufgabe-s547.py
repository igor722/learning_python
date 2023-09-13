try:
    langjaehriges_mittel=18.23
    print("Programm zur Berechnung einer Durchschnittstemperatur \n")
    print ( "Geben Sie bitte drei Temperaturwerte in °C ein!" )
    temperatur1 = float(input( "l. Wert: " ))
    temperatur2 = float(input( "2. Wert: " ))
    temperatur3 = float(input( "3. Wert: " ))
    durchschnitt = (temperatur1+temperatur2+temperatur3) / 3
    print("Sie haben folgende Temperaturen eingegeben: {0} °C, {1} °C, {2} °C".format(temperatur1,temperatur2,temperatur3))
    print("Die Durchschnittstemperatur beträgt: {0:.2f} °C".format(durchschnitt))
    if durchschnitt >= langjaehriges_mittel:
        if durchschnitt > langjaehriges_mittel:
            print( "Die Temperatur liegt über dem langjährigen Mittel" ) 
        else:
            print( "Die Temperatur entspricht dem langjährigen Mittel" )
    else:
        print( "Die Temperatur liegt unter dem langjährigen Mittel" )
except Exception as e:
    print( "Es ist folgender Fehler aufgetreten: \n" + e.args[0])