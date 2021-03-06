#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В операционных системах на базе Unix обычно присутствует утилита с названием head.
Она выводит первые десять строк содержимого файла, имя которого передается в качестве
аргумента командной строки. Напишите программу на Python, имитирующую поведение
этой утилиты. Если файла, указанного пользователем, не существует, или не задан
аргумент командной строки, необходимо вывести соответствующее сообщение об ошибке.
"""

import sys

if __name__ == "__main__":
    ten_lines = 10

    if len(sys.argv) != 2:
        print("В качестве аргумента командной строки передайте имя файла!", file=sys.stderr)
        sys.exit(1)

    try:
        # открываем файл на чтение
        with open(sys.argv[1], "r", encoding="utf-8") as file:

            # читаем первую строку из файла
            lines = file.readlines()

            # создаем список
            list_lines = []

            # запуск цикла, читаем строки пока не дойдём до 10
            count = 0
            for rows in lines:
                if count < ten_lines:
                    list_lines.append(rows)
                    count = count + 1

            print(*list_lines, end="\n")

    except IOError:
        # если возникнут проблемы с чтением файла, отображаем ошибку
        print("Ошибка при доступе к файлу", file=sys.stderr)
