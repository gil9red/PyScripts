#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# http://lurkmore.to/Язык_падонков
#
# # Учитезь правильна гаваридь! Урок 1.
# http://h.ua/story/79874/
#
# https://ru.wikipedia.org/wiki/Жаргон_падонков


text = """Конечно, там еще много работы. Нужно корректно переводить слова с несколькими значениями, улучшать перевод
разных форм глаголов, сделать настраиваемый уровень перевода для разных уровней владения английским, готовить
упражнения для запоминания новых слов. Этим я буду заниматься на досуге в ближайшие месяцы. """

# беспесды, там исчо питцот работы. нужно корректно пириводить слова с нисколькими значенийами, улучшать пириводчег
# разных форм глаголофф, сделать настраиваемый уровень пиривода для разных уровней владенийа онглийским, готовить
# упражненийа для запаминанийа новых слофф. этим йа буду занимацца на досуге в ближайшие месяцы.

# Ключом будет русское слово, значением -- слова в олбанском языке
ru_ol_dict = dict()


def tr(word):
    """Функция возвращает слово в олбанском диалекте."""

    word = word.replace('я', 'йа')
    word = word.replace('е', 'и')
    word = word.replace('в', 'фф')
    word = word.replace('тьс', 'цц')

    if word.endswith('к'):
        word = word.replace('к', 'г')

    return word


# Ищем слова и добвляем в словарь
import re
for match in re.findall('\w+', text):
    ru_ol_dict[match] = tr(match)

# Проходим по словарю и заменяем слова на олбанские
for ru, ol in ru_ol_dict.items():
    text = text.replace(ru, ol)

print(text)
