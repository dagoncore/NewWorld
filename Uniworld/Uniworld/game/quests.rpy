# -*- coding: utf-8 -*-
# quests.rpy — Система квестов
# Класс Quest, список квестов, экран квестов

init python:
    class Quest:
        def __init__(self, name, description, completed=False, quest_type="Основной сюжет"):
            self.name = name
            self.description = description
            self.completed = completed
            self.type = quest_type

# === КВЕСТЫ ===
default quest1 = Quest("Бюджет", "Заработайте немного денег", quest_type="Основной сюжет")
default quest2 = Quest("Второй квест", "Это описание второго квеста.", quest_type="Основной сюжет")
default all_quests = [quest1, quest2]

# === ФУНКЦИИ КВЕСТОВ ===
label add_quest(name, description, quest_type="Main"):
    $ new_quest = Quest(name, description)
    $ all_quests.append(new_quest)
    n "Квест '[name]' добавлен в ваш список квестов."

label complete_quest(quest_name):
    $ quest_to_complete = next((quest for quest in all_quests if quest.name == quest_name), None)
    if quest_to_complete:
        $ quest_to_complete.completed = True
        $ all_quests.remove(quest_to_complete)
    return

# === ЭКРАН КВЕСТОВ ===
screen quests():
    frame:
        align (0.0, 0.0)
        vbox:
            for quest in all_quests:
                if quest.completed:
                    text "[quest.name] (Завершен) [quest.type]" size 20
                else:
                    text "[quest.name] (Не завершен) [quest.type]" size 20
                    text "[quest.description]" size 15
