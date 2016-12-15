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
        players_profile.append(seven_bones(dominoes_list))  # the name of function depends on issue 5 and 1
    return(players_profile)

def firstStep(players_profile):
    player_start = 0
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

dominoes_list = [[0, 0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[4,0],
[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[6,0],[6,1],
[6,2],[6,3],[6,4],[6,5],[6,6]]



#issue 5
def seven_bones():
    import random
    dominoes_list = [[0, 0], [1, 0], [1, 1], [2, 2], [2, 1], [2, 0], [3, 3], [3, 2], [3, 1], [3, 0],
                     [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [5, 5], [5, 4], [5, 3], [5, 2], [5, 1], [5, 0],
                     [6, 6], [6, 5], [6, 4], [6, 3], [6, 2], [6, 1], [6, 0]]
    players_dominoes = []   #List of dominoes for Player
    count = 7               #Number of dominoes for Player
    random.shuffle(dominoes_list)
    print('7 bones for players: ')
    for i in range(len(dominoes_list)):
        if i < count:
            players_dominoes.append(dominoes_list[i])   #New list of dominoes for player
            del dominoes_list[i]                        #Deleting list of dominoes for player from DominoesList
    print (players_dominoes)
    print (dominoes_list)

seven_bones()
