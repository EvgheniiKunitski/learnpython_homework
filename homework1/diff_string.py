# Практика: Сравнение строк

'''
Написать функцию, которая принимает на вход две строки
Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
Если строки одинаковые, вернуть 1
Если строки разные и первая длиннее, вернуть 2
Если строки разные и вторая строка 'learn', возвращает 3
Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты
'''


def string_compare(str1, str2):
    if type(str1) != str or type(str2) != str:
        return 0
    if str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == "learn":
        return 3

    # если немного преписать первое условие - можно обойтись без else и сразу возвращать 0
    # переделал

# по заданию не очень корректно сказано, здесь лучше самому написать код который
# будет вызывать функцию с разными параметрами
# ps и это все лучше обернуть тоже в функцию main
#main я сегодня не потяну, но несколько вводов сделаю
#input_str1 = input("введите первую строку: ")
input_str1 = 'blablacar'
#input_str2 = input("введите вторую строку: ")
input_str2 = 'ajo'
print(input_str1,input_str2)
print(string_compare(input_str1, input_str2))


input_str1 = 'work'
#input_str2 = input("введите вторую строку: ")
input_str2 = 'learn'
print(input_str1,input_str2)
print(string_compare(input_str1, input_str2))

input_str1 = 'learn1'
#input_str2 = input("введите вторую строку: ")
input_str2 = 'learn'
print(input_str1,input_str2)
print(string_compare(input_str1, input_str2))


input_str1 = 'student'
#input_str2 = input("введите вторую строку: ")
input_str2 = 1
print(input_str1,input_str2)
print(string_compare(input_str1, input_str2))
