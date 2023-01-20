'''40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Модуль сжатия:
Для чисел:
Входные данные:
111112222334445
/от 0 до 9/
/на выходе строчка/
Выходные данные:
5142233415
Также должно работать и для букв:
Входные данные:
AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
Выходные данные:
6A1F2D7C1A17E
/юникод, таблица аски/
(5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
Модуль восстановления работет в обратную сторону - из строки выходных данных, 
получить строку входных данных.'''

##Функция сжатия
def CompressionModule(data):
    unicod = ""
    while data != "":
        count = 1
        for j in range(1,((len(data)))):
            if data[0] == (data[j]):
                count=count+1
            else: break
        unicod = unicod+(str(count) + data[0])
        data = data[(j):(len(data))]
        if len(data) == 1 and unicod[-1] == data[0]:
            data = ""

    return unicod

##Функция восстановления
def RecoveryModule(data):
    unicod = ""
    lens = (len(data)-1)
    for i in range(0,(len(data)-1),2):
        unicod = unicod+((int(data[i]))*data[i+1])
    
    return unicod
   

############
string = 'AAAAAAFDDCCCCCCCAEEEEEEEEE'        #6A1F2D7C1A9E
numbers = '111112222334445'                   #5142233415

print(string:=(CompressionModule(string)))
print(numbers:=(CompressionModule(numbers)))

print(RecoveryModule(string))
print(RecoveryModule(numbers))
