#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cmath
import math
__author__ = 'petro-ew'
"""
11.
 Программа запрашивает два целых числа a и b.
  Найти и вывести на экран наибольший общий делитель a и b.
"""
"""
Алгоритм Евклида (нахождение наибольшего общего делителя)
Большее число делим на меньшее.
Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла).
Если есть остаток, то большее число заменяем на остаток от деления.
Переходим к пункту 1.

"""
a = int(input())
b = int(input())
while a!=0 and b!=0:
    if a > b:
        a = a % b #записываем остаток от деления
    else:
        b = b % a  #та же фигня

print(a+b) #так как мы не знаем что из них нуль складываем. так как один из них нуль нам пофиг.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cmath
import math
__author__ = 'petro-ew'
"""
11.
 Программа запрашивает два целых числа a и b.
  Найти и вывести на экран наибольший общий делитель a и b.
"""
"""
Алгоритм Евклида (нахождение наибольшего общего делителя)
Большее число делим на меньшее.
Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла).
Если есть остаток, то большее число заменяем на остаток от деления.
Переходим к пункту 1.

"""
a = int(input())
b = int(input())
while a!=0 and b!=0:
    if a > b:
        a = a % b #записываем остаток от деления
    else:
        b = b % a  #та же фигня

print(a+b) #так как мы не знаем что из них нуль складываем. так как один из них нуль нам пофиг.
