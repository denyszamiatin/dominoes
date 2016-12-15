# https://domino.keft.ru/help - правила игры

import itertools


MAX_POINTS_COUNT = 7
PAIRS = 2
MIN_PLAYERS_NUMBER = 2
MAX_PLAYERS_NUMBER = 4
FIRST_BONES_NUMBER = 7


def get_dominoes():
    return list(itertools.combinations_with_replacement(
        range(MAX_POINTS_COUNT),
        PAIRS
    ))


dominoes = get_dominoes()


def get_bones(count):
    global dominoes
    bones = dominoes[:count]
    dominoes = dominoes[count:]
    return bones


def input_players_number():
    while True:
        try:
            players_number = int(input('Enter number of players: '))
            if MIN_PLAYERS_NUMBER <= players_number <= MAX_PLAYERS_NUMBER:
                return players_number
            print('Players number out of range')
        except ValueError:
            print('Invalid number')


def get_players(players_number):
    return [get_bones(FIRST_BONES_NUMBER) for _ in range(players_number)]


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
