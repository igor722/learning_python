import random


# print(ai_auswahl)
spieler_name = str(input('Bitte Ihr Name eingeben: '))

punkte_ai = 0
punkte_player = 0

while True:
    ai_auswaehle = ['stein', 'schere', 'papier']
    ai_auswahl = ai_auswaehle[random.randint(0, 2)]
    player_auswahl = input('Bitte auswählen: 1 = Stein, 2 = Schere, 3 = Papier:  ')

    print(f'Computer hat {ai_auswahl} ausgewählt')

    # =======================PLAYER AUSGABE LOGIK=======================

    if player_auswahl == '1':
        print(f'{spieler_name} hat Stein ausgewählt')
    elif player_auswahl == '2':
        print(f'{spieler_name} hat Schere ausgewählt')
    elif player_auswahl == '3':
        print(f'{spieler_name} hat Papier ausgewählt')
    else:
        print('Bitte 1, 2 oder 3 auswählen!')

    # =======================AUSWÄHLE VERGLEICH=======================

    if ai_auswahl == 'stein' and player_auswahl == '1':
        print('Es ist Unetschieden!')
    elif ai_auswahl == 'stein' and player_auswahl == '2':
        punkte_ai += 1
        print('Computer hat gewonnen')
    elif ai_auswahl == 'stein' and player_auswahl == '3':
        punkte_player += 1
        print(f'{spieler_name} hat gewonnen')
    elif ai_auswahl == 'schere' and player_auswahl == '1':
        punkte_player += 1
        print(f'{spieler_name} hat gewonnen')
    elif ai_auswahl == 'schere' and player_auswahl == '2':
        print('Es ist Unetschieden!')
    elif ai_auswahl == 'schere' and player_auswahl == '3':
        punkte_ai += 1
        print('Computer hat gewonnen')
    elif ai_auswahl == 'papier' and player_auswahl == '1':
        punkte_ai += 1
        print('Computer hat gewonnen')
    elif ai_auswahl == 'papier' and player_auswahl == '2':
        punkte_player += 1
        print(f'{spieler_name} hat gewonnen')
    elif ai_auswahl == 'papier' and player_auswahl == '3':
        print('Es ist Unetschieden!')
    else:
        print('Bitte überprüfen Sie Ihre Eingabe!')

    print('##################################################################')
    print(f'Scoreboard:\n Computer={punkte_ai} {spieler_name}={punkte_player}')
    print('##################################################################')

    fertig = input(
        'Wiederholen? ENTER drücken; wenn fertig, "exit" eingeben:  ')
    if fertig == 'exit':
        break
