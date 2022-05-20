#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Усложнённое. В - 3. Дано слово. Определить, сколько различных букв в нем.

if __name__ == '__main__':
    slovo = input("Введите слово: ")
    print("Разных букв: ", len(set(slovo)))
