'''39(1). Создайте программу для игры с конфетами человек против человека. 
Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, 
вписывая желаемое количество конфет. 
Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
В качестве дополнительного усложнения можно:
    a) Добавьте игру против бота (где бот берет рандомное количество конфет от 0 до 28)
    b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое 
    количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту)
'''
import random

## Человек против человека
def Man_versus_man():
    # Вводим основные данные
    total_sweets = int(input("Введите общее количество конфет: "))
    candies_one_turn = int(input(
        "Введите максимальное количество конфет, которое можно взять за один ход: "))
    player_1 = input("Введите имя первого игрока: ")
    player_2 = input("Введите имя второго игрока: ")

    # Жеребьевка рандомная
    toss = random.choice([player_1, player_2])
    print(f'Ваш ход {toss}.')

    # Основаня часть
    while total_sweets >= 0:
        turn = int(input(f"{toss}, возьмите конфеты, но не больше {candies_one_turn}: "))
        if turn > candies_one_turn or turn <= 0:
            while turn > candies_one_turn or turn <= 0:
                turn = int(input(f"{toss}, попробуйте ещё, от 0 до {candies_one_turn}: "))
        total_sweets -= turn

        if total_sweets > 0:
            print(f"Осталось {total_sweets} конфет.")
        else:
            print(f"Конфет больше нет, победил {toss}! Поздравляем!")
            break
        toss = player_2 if toss == player_1 else player_1
## Человек против бота
def Man_vs_bot():
    total_sweets = int(input("Введите общее количество конфет: "))
    candies_one_turn = int(input("Введите максимальное количество конфет, которое можно взять за один ход: "))
    player_1 = input("Введите имя игрока: ")
    player_2 = "bot"

    toss = random.choice([player_1, player_2])
    print(f'Ваш ход {toss}.')

    while total_sweets >= 0:
        if toss == player_1:
            turn = int(input(f"{toss}, возьмите конфеты, но не больше {candies_one_turn}: "))
        else:
            b = candies_one_turn+1
            turn = random.randint(1, b)
            if turn > total_sweets:
                turn = total_sweets
            print(f"bot взял {turn} конфет")

        if turn > candies_one_turn or turn <=0:
            while turn > candies_one_turn or turn <= 0:
                turn = int(input(f"{toss}, попробуйте ещё, от 0 до {candies_one_turn}: "))
        total_sweets -= turn

        if total_sweets > 0:
            print(f"Осталось {total_sweets} конфет.")
        else:
            print(f"Конфет больше нет, победил {toss}! Поздравляем!")
            break
        toss = player_2 if toss == player_1 else player_1
## Человек против умногобота
def Man_vs_smartbot():
    total_sweets = int(input("Введите общее количество конфет: "))
    candies_one_turn = int(input("Введите максимальное количество конфет, которое можно взять за один ход: "))
    player_1 = input("Введите имя игрока: ")
    player_2 = "smart bot"

    toss = random.choice([player_1, player_2])
    print(f'Ваш ход {toss}.')

    while total_sweets > 0:
        if toss == player_1:
            turn = int(input(f"{toss}, возьмите конфеты, но не больше {candies_one_turn}: "))
        else:
            if candies_one_turn == total_sweets:
                turn = candies_one_turn
            elif total_sweets%candies_one_turn==0:
                turn = candies_one_turn-1
            else: 
                turn = total_sweets%candies_one_turn-1
            if turn == 0:
                   turn = 1
            print(f"bot взял {turn} конфет")

        if turn > candies_one_turn or turn <= 0:
            while turn > candies_one_turn or turn <= 0:
                turn = int(input(f"{toss}, попробуйте ещё, от 0 до {candies_one_turn}: "))
        total_sweets -= turn

        if total_sweets > 0:
            print(f"Осталось {total_sweets} конфет.")
        else:
            print(f"Конфет больше нет, победил {toss}! Поздравляем!")
            break
        toss = player_2 if toss == player_1 else player_1


Man_versus_man()
Man_vs_bot()
Man_vs_smartbot()