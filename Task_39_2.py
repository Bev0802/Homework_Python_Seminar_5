'''39(2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, 
игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, 
внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие 
клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим поставить 
крестик или нолик, и проверку на победу(стоят ли крестики или нолик в ряд по диагонали, 
вертикали, горизонтали)'''

board = list(range(1, 10))
win_coordinates = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                   (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def show_board(): ## Выводим игровую доску с координатами.
    print('-------------')
    for i in range(3):
        for j in range(3):
            if j < 2:
                print('|', board[j+(i*3)], end=" ")
            else:
                print('|', board[j+(i*3)], '|', end="\n")
        print('-------------')

def checking_input(symbol): ## Ввод числа поля и провяем правильность ввода.
    while True:
        coordinate = int(
            input(f"Введите цифру поля от 1 до 9 куда вы ходите поставить {symbol}: "))
        if not (coordinate in board) or str(board[coordinate-1]) in "XO":
            print("Такого поля нет или поле уже занято. Выбери другое. ")
            continue
        board[coordinate-1] = symbol
        break

def checking_win(): ## Проверка выигрыша.
    for i in win_coordinates:
        if (board[i[0]-1]) == (board[i[1]-1]) == (board[i[2]-1]):
            return board[i[1]-1]
    
def Game(): ## Функция игры
    count = 0
    while count < 9:
        show_board()
        if count%2 == 0:
            checking_input("X")
        else:
            checking_input("O")
        if count > 3:
            winner = checking_win()
            if winner:
                show_board()
                print(f"Поздравляем! Выиграл {winner}")
                quit()
        count+=1
    show_board()
    return print("Игра окончена! Ничья. Победила дружба!")

Game()
