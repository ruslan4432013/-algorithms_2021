"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""
from timeit import timeit

massive = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Оптимизированная функция
def func_1_optimize(nums):
    return [el for el in nums if el % 2 == 0]


# Замеры функций с помощью timeit
print(f"func_1: {timeit('func_1(massive)', globals=globals())} seconds")
print(f"func_1_optimize: {timeit('func_1_optimize(massive)', globals=globals())} seconds")

'''
Аналитика:
Вместо обычного заполнения списка циклом и создания нового массива лучше использовать 
"списковое включение" - list comprehension
Списковые включения считаются более «пайтонообразными», нежели циклы или функции map() и filter() для генерации списков. 
И как показывает функция timeit, list comprehension является более элегантным и быстрым, чем цикл
'''
