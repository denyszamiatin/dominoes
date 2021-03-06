# -*- coding: utf-8 -*-
# чтобы писать кириллицей, необходимо первой строкой указать 'coding: utf-8' как выше
# https://domino.keft.ru/help - правила игры
import random
import itertools

MAX_POINTS_COUNT = 7
PAIRS = 2
MIN_PLAYERS_NUMBER = 2
MAX_PLAYERS_NUMBER = 4
FIRST_BONES_NUMBER = 7
ID_PLAYER_WITH_MAX_POINTS = 0
LEFT = 0
RIGHT = 1
NUMBER_OF_BONES_TO_TAKE = 1
players_dict = {}
bones_on_table = []


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


def shuffle_dominoes():
    random.shuffle(dominoes)


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


def find_player_with_min_double(players):
    for double in [(x, x) for x in range(1, MAX_POINTS_COUNT)] + [(0, 0)]:
        for player, bones in enumerate(players):
            if double in bones:
                return double, player
    raise ValueError('There are no doubles')


def find_player_with_max_points(players):
    first_player = 0
    max_bone = (0, 0)
    for player, bones in enumerate(players):
        if max(bones) > max_bone:
            first_player = player
            max_bone = max(bones)
    return max_bone, first_player


def get_first_move_player(players):
    try:
        return find_player_with_min_double(players)
    except ValueError:
        return find_player_with_max_points(players)


def print_player(player):
    print("You have the following bones\n", player)


def input_bone_index(player):
    while True:
        bone_index = input("Please select bone's index to go: ")
        if validate_bone(bone_index, player):
            return int(bone_index)


def move_first(bone, player):
    player.remove(bone)
    bones_on_table.append(bone)


def move(player):
    print_bones_on_table()
    try:
        check_player_before_move(player)
        print_player(player)
        bone_index = input_bone_index(player)
        bone, where = input_side(player[bone_index])
        place_domino(bone, where)
        player.remove(player[bone_index])
    except ValueError:
        pass


def input_side(bone):
    while True:
        try:
            where = int(input("Select the side\nLEFT - 0\nRIGHT - 1\n"))
            if 0 <= where < 2:
                return validate_side(bone, where)
        except ValueError:
            print('Invalid number')


def validate_side(bone, where):
    if where:
        if bone[LEFT] == bones_on_table[-RIGHT][RIGHT]:
            return bone, RIGHT
        elif bone[RIGHT] == bones_on_table[-RIGHT][RIGHT]:
            return sort_bone(bone), RIGHT
        else:
            print("Can't move right. Only left")
            if bone[LEFT] == bones_on_table[LEFT][LEFT]:
                return sort_bone(bone), LEFT
            else:
                return bone, LEFT
    else:
        if bone[LEFT] == bones_on_table[LEFT][LEFT]:
            return sort_bone(bone), LEFT
        elif bone[RIGHT] == bones_on_table[LEFT][LEFT]:
            return bone, LEFT
        else:
            print("Can't move left. Only right")
            if bone[LEFT] == bones_on_table[-RIGHT][RIGHT]:
                return bone, LEFT
            else:
                return sort_bone(bone), LEFT


def game_loop(players):
    bone, player_to_move = get_first_move_player(players)
    move_first(bone, players[player_to_move])
    while True:
        player_to_move = (player_to_move + 1) % len(players)
        move(players[player_to_move])


def can_move(player):
    for bone in player:
        if bones_on_table[LEFT][LEFT] in bone or \
                        bones_on_table[-RIGHT][RIGHT] in bone:
            return True
    return False


def check_player_before_move(player):
    while not can_move(player):
        print("You don't have any bone to move. Take one")
        add_bone_to_player_if_miss(player)


def validate_bone(bone_index, player):
    try:
        bone_index = int(bone_index)
    except:
        return False
    return bones_on_table[LEFT][LEFT] in player[bone_index] or \
                bones_on_table[-RIGHT][RIGHT] in player[bone_index]


def place_domino(bone, where):
    if not where:
        bones_on_table.insert(LEFT, bone)
    else:
        bones_on_table.append(bone)


def sort_bone(bone):
    return tuple(reversed(bone))


def print_bones_on_table():
    print("Current bones on table:\n", bones_on_table)


def add_player_to_dict_of_players():
    for player in range(players_number):
        players_dict[player] = {'bones': [], 'priority_move': None}


def add_bones_to_dict_of_players():
    if len(players_bones) != players_number:
        raise ValueError('Not enough players')
    for player, bones in enumerate(players_bones):
        players_dict[player]['bones'] = bones


def add_priority_to_dict_of_players():
    first_player_index = get_first_move_player(players_bones)
    player_index = 0
    while player_index < players_number:
        players_dict[first_player_index % players_number]['priority_move'] = \
            player_index
        player_index += 1
        first_player_index += 1


def is_bones_left(dominoes):
    return bool(dominoes)


def add_bone_to_player_if_miss(player):
    if is_bones_left(dominoes):
        player.append(get_bones(NUMBER_OF_BONES_TO_TAKE)[0])
    else:
        raise ValueError("There are no bones left. You miss a go")


def remove_player_bone(bone_index, player):
        return player.players_dict.pop(bone_index, None)


dominoes = get_dominoes()
players_number = input_players_number()
shuffle_dominoes()
players_bones = get_players(players_number)
game_loop(players_bones)