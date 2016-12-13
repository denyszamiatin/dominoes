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
        players_profile.append(dominoes_dealing(dominoes_list))  # the name of function depends on issue 5 and 1
    return(players_profile)

def firstStep(players_profile):
    full_list = players_profile
    double_list = []
    k = 0
    for user_list in full_list:
        for num in user_list:
            if num[0] == num[1]: double_list.append(num[0])

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

dominoes_list = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[4,0],
[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[6,0],[6,1],
[6,2],[6,3],[6,4],[6,5],[6,6]]