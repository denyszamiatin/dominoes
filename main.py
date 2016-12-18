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


def get_bones(count): # соблюдаем pep8: две строки сверху и снизу от функции
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


def find_doubles(players_bones): # соблюдаем pep8: две строки сверху и снизу от функции
    doubles = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (0, 0)] # соблюдаем pep8: пробелы после запятой
    for pair in doubles:
        for index in range(len(players_bones)):
            if pair in players_bones[index]:
                return index
    raise IndexError                         # returns Error if no doubles found
# отсутствие дублей у игрока не нарушает правила игры в домино и не должно вызывать ошибку в программе
# "Если дублей нет вообще, то ход с кости 5-6, и так далее по убыванию значений костей."
# поэтому лучше просто убрать raise. Если ничего не найдено, функция возвратит None, что соответствует правилам игры


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
        print('first goes player with double %d') % double_min
    else:
        print('first goes player with most points %d') % points_max


players_now_num = input_players_number() # перенести эти две строки в самый низ, после описания всех функций
players_bones = get_players(players_now_num) # list of lists of bones

dominoes = get_dominoes() # перенести эти две строки в самый низ, после описания всех функций
random.shuffle(dominoes)

# кто исправит, пожалуйста, удалите соотв. комментарий, этот в последнюю очередь.
