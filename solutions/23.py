#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys
"""
23. 
Написать функцию,
 берущую в качестве аргумента строку из двух слов,
  разделенных пробелом,
   и возвращающую строку,
    состоящую из тех же слов,
     поменяных местами.
Пример: "Дмитрий Платонов" -> "Платонов Дмитрий"
"""
s = "Дмитрий Платонов"

def str1(s):
	s = s.split(" ")
	s.reverse()
	z = s[0] + " " + s[1]
	#print(s, z)
	return z
print(str1(s)) 