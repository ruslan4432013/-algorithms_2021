"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random

rand = random.randint(0, 100)  # Генерируем случайное значение от 1 до 100
print(rand)  # Для теста


def divine(n=10):
    number = int(input('Введите число: '))
    # Базовый случай если человек угадал
    if number == rand:
        return print('Вы угадали!')
    # Базовый случай если человек не угадал
    elif n == 1:
        return print(f'Вы проиграли( \nПравильный ответ: {rand}')
    # Шаг рекурсии
    else:
        n -= 1
        if number > rand:
            print(f'Указанное вами число больше загаданного, попробуйте еще раз, осталось {n} попыток')
            return divine(n)
        else:
            print(f'Указанное вами число меньше загаданного, попробуйте еще раз, осталось {n} попыток')
            return divine(n)


divine()
