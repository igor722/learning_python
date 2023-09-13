def status_anzeigen(anzahl_parkplätze_belegt, eingang_frei, ausgang_frei, vermietet):

    if eingang_frei == False or ausgang_frei == False or vermietet == True:
        print("Parkhaus ist gesperrt.")
    else:
        if anzahl_parkplätze_belegt >= 475:
            print("Parkplatz ist belegt.")
        else:
            print("Parkhause ist frei.")


status_anzeigen(480,False,False,True)