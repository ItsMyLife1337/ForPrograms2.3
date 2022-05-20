#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Задание 3. Вариант 3. Дано предложение. Удалить из него все символы с n1-го по n2-й (n1 <= n2).

if __name__ == '__main__':
    predlog = str(input("Введите предложение: "))

    print("Введите диапазон для удаления: ")
    n1 = int(input())
    n2 = int(input())

    print(predlog[:n1], predlog[n2+1:])
