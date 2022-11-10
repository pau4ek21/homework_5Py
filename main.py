# # Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# # За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# from random import *
# # Делается проверка правильности ввода конфет
# def candy_check(name):
#     how_much_candy_do_you_take = int(input(f'{name}, введите количество конфет которое возьмете, не более 28: '))
#     while how_much_candy_do_you_take < 1 or how_much_candy_do_you_take > 28:
#         how_much_candy_do_you_take = int(input(f'{name} введите количество конфет не более 28: '))
#     return how_much_candy_do_you_take
# # Показывает кто сколько взял конфет и сколько осталось
# def leftover_candy(name, took, amount, remain):
#     print(f'У {name} на руках {amount} конфет, сейчас взял(а) {took}, осталось в игре: {remain}\n')
#
#
#
# player_1 = input('Введите имя первого игрока: ')
# player_2 = input('Введите имя второго игрока: ')
# amount_candies = int(input('Введите количество конфет на столе: '))
#
# firts_move = randint(1, 2)
# if firts_move:
#     print(f'первым ходит {player_1}')
# else:
#     print(f'первым ходит {player_2}')
#
# count = 0
# count_1 = 0
#
# while amount_candies > 28:
#     if firts_move:
#         amount = candy_check(player_1)
#         count += amount
#         amount_candies -= amount
#         firts_move = False
#         leftover_candy(player_1, amount, count, amount_candies)
#     else:
#         amount = candy_check(player_2)
#         count_1 += amount
#         amount_candies -= amount
#         firts_move = True
#         leftover_candy(player_2, amount, count_1, amount_candies)
#
# if firts_move:
#     print(f'победил {player_1}')
# else:
#     print(f'победил {player_2}')


#================================================================================


# # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input('введите текст который хотите удалить: ')
# text = text.split()
# new_text = list(filter(lambda x: 'abc' not in x, text))
# print(' '.join(new_text))

#================================================================================

# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
#
# def Exp4(type = 0, string = ''):
#
#     #type = 0  -- сжатие        Exp4(0, 'fff dddd bbbb aaa')
#
#     #type = 1  -- распаковка    Exp4(1, '3f 4d 4b 3a')
#
#     if type == 0:
#
#         count = {}
#
#         for s in string.split(): #'fff dddd bbbb aaa'
#
#           for i in s:
#
#             if i in count:
#
#                 count[i] += 1
#
#             else:
#
#                 count[i] = 1
#
#         ss = ''
#
#         for key in count:
#
#             ss = ss + f'{count[key]}{key}' + ' '
#
#         print(ss[:-1])
#
#     else:
#
#         list = []
#
#         for s in string.split(): #'3f 4d 4b 3a'
#
#             cnt = ''
#
#             chr = ''
#
#             for i in s:
#
#                 if i.isdigit():
#
#                     cnt += i
#
#                 else:
#
#                     chr += i
#
#             list.append(chr*int(cnt))
#
#         print(' '.join(list))
#
# print(Exp4(0, 'fff dddd bbbb aaa'))
# print(Exp4(1, '3f 4d 4b 3a'))



