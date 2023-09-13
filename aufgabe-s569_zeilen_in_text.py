pfad = "C:\\Users\\Student\\Documents\\pass.txt"

file = open((pfad), "r")
lines = file.readlines()
print(len(lines))
line_auswahl = int(input("Welche Zeile wollen Sie lesen:  "))
print(lines[line_auswahl-1])
