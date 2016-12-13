def playersNumber():
    while True:
        try:
            players_number = int(input('Enter number of players: '))
            break
        except ValueError:
            print('Invalid number')

    print(players_number, 'players')

playersNumber()
