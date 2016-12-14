def playersNumber():
    while True:
        try:
            players_number = int(input('Enter number of players: '))
            break
        except ValueError:
            print('Invalid number')

    print(players_number, 'players')
    return players_number

while True:
    if 2 <= (playersNumber()) <=4:
        break
    print('Game allow 2-4 players')

def players_profile(players_number):
    players_profile = []
    for i in range(players_number):
        players_profile.append(dominoes_dealing(dominoes_list))  # the name of function depends on issue 5 and 1
    return(players_profile)

def firstStep(players_profile):
    full_list = players_profile
    double_list = []
    for user_list in full_list:
        for num in user_list:
            if num[0] == num[1]: double_list.append(num[0])
    min_b = min(double_list)
    player_start = double_list.index(min_b) + 1
    print('minimal bone is - ', min_b)
    print('player', player_start, 'please start the game')
    return player_start