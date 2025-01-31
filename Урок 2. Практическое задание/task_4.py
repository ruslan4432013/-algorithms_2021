"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить не нужно!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_num(num, one_num=1, s_num=0):
    # Базовый случай
    if int(num) == 0:
        return print(s_num)
    # Шаг рекурсии
    else:
        s_num += one_num
        one_num /= -2
        return sum_num(int(num) - 1, one_num, s_num)


number = input('Введите количество элементов: ')

sum_num(number)
