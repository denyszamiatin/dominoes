def playersNumber():
    while True:
        try:
            players_number = int(input('Enter number of players: '))
            break
        except ValueError:
            print('Invalid number')

    print(players_number, 'players')
    return players_number

playersNumber()

def players_profile(players_number):
    i = 0
    players_profile = []
    for i in range(players_number):
        players_profile.append(dominoes_dealing(dominoes_list)) # the name of function depends on issue 5 and 1
    return(players_profile)

def firstStep(full_list):
    double_list = []
    double = k = 0
    for user_list in full_list:
        for num in user_list:
            if num[0] == num[1]:
                double = num[0]
                double_list.append(double)

    min = double_list[0]
    for i in double_list:
        if min > i:
            min = i
    print('minimal bone is - ', min)
    while k < len(double_list):
        if double_list[k] == min:
            player_start = k + 1
        k += 1
    print('player', player_start, 'please start the game')
    return player_start
