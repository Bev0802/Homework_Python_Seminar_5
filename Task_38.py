'''Задача 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".'''

text = "ааабваа! аааа, аабв вввв. Абв ггг"
text_list = text.split()
result = list(filter(lambda x: not "абв" in x.lower(), text_list)) 

print(result)