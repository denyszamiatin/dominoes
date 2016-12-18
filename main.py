# -*- coding: utf-8 -*-
# чтобы писать кирилицей, необходимо первой строкой указать 'coding: utf-8' как выше
# https://domino.keft.ru/help - правила игры
import random
import itertools


MAX_POINTS_COUNT = 7
PAIRS = 2
MIN_PLAYERS_NUMBER = 2
MAX_PLAYERS_NUMBER = 4
FIRST_BONES_NUMBER = 7
ID_PLAYER_WITH_MAX_POINTS = 0


def get_dominoes():
    return list(itertools.combinations_with_replacement(
        range(MAX_POINTS_COUNT),
        PAIRS
    ))


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


def first_step(players_profile):
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


def find_doubles(players_bones):
    doubles = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (0, 0)]
    for pair in doubles:
        for index in range(len(players_bones)):
            if pair in players_bones[index]:
                return index


def find_player_with_max_points(players_bones):
    max_points = 0
    id_player = 0
    for i in players_bones:
        points_of_player = 0    
        for j in i:
            points_of_player += sum(j)
        if max_points < points_of_player:
            max_points = points_of_player
            ID_PLAYER_WITH_MAX_POINTS = id_player
        id_player += 1
    return ID_PLAYER_WITH_MAX_POINTS


def goes_first(double_min, points_max):
    if double_min:
        print('first goes player with double %d' % double_min)
    else:
        print('first goes player with most points %d' % points_max)


def choose_bone(player_index_first_to_go, players_bones):
    for bone in (players_bones[player_index_first_to_go:] + players_bones[:player_index_first_to_go]):
        while True:
            print("You have the following bones\n", bone)
            bone_chosen_index = input("Please select bone's index to go: ")
            if validate_bone(bone_chosen_index): # I suppose here should come bone validation from issue #14
                placing_dominoes(player_index_first_to_go, bone_chosen_index)
                break

# issue 14 написано для тестирования choose_bone
# необходимо сделать и удалить комментарий
def validate_bone(bone_index):
    return True


def placing_dominoes(current_player, index_players_bone):
    current_players_bones = players_bones[current_player]
    players_bone = current_players_bones[index_players_bone-1]
    current_players_bones.delete[index_players_bone-1]
    bones_on_table = bones_on_table.insert(0, players_bone)
    return players_bones, bones_on_table


dominoes = get_dominoes()
random.shuffle(dominoes)

players_now_num = input_players_number()
players_bones = get_players(players_now_num)  # list of lists of bones
bones_on_table = []  # empty list for bones on the table
choose_bone(2, players_bones)