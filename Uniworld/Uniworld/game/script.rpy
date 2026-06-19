# -*- coding: utf-8 -*-
# script.rpy — Главный сценарий игры
# Сюжет, игровая логика, локации
# Определения, механики и экраны вынесены в: definitions.rpy, equipment.rpy, inventory.rpy, quests.rpy, game_screens.rpy

# =============================================================================
# НАЧАЛО ИГРЫ
# =============================================================================

label start:
    call complete_quest("Второй квест")
    scene bg_main with fade_scene
    show screen resources
    show screen quests
    show m at left
    n "Очередной день в Сантауне!"
    call day_cycle
    return

# =============================================================================
# ЦИКЛ ДНЯ
# =============================================================================

label day_cycle:
    if gold > 100:
        call complete_quest("Бюджет")
    $ day += 1
    $ actions_left = 20
    # Рост помидора на грядке после прошедшего дня (после сна)
    if 1 <= tomato <= 3:
        $ tomato += 1
    n "День [day]: начинается новый день."

label day_keep:
    scene bg_main with fade_scene
    while actions_left > 0:
        menu:
            "Экипировка персонажа":
                call screen equipment_interface
                jump day_keep
            "Подобрать зелье":
                call item_add("Зелье 🧪", "Загадочное зелье, стоит ли eго пить?", "items/potion.png")
                jump day_keep
            "Выбросить зелье":
                call item_remove("Зелье 🧪")
                jump day_keep
            "Выйти из дома":
                jump go
    n "У меня совсем не осталось сил.. Нужно поспать."
    jump day_end

label go:
    scene bg_main_out with fade_scene
    while actions_left > 0:
        menu:
            "Отправиться в {color=#8ccb5e}Дом фермерши{/color}":
                jump food_base
            "Прогуляться по {color=#adffff}Жилому району{/color}":
                jump home_base
            "Идти в {color=#cc4949}Промышленный район{/color}":
                jump factory_base
            "Пойти в {color=#f79b31}Центр{/color}":
                jump center_base
            "Посетить {color=#5bc1fc}Логистико-исследовательский центр{/color}":
                jump explore_base
            "Вернуться домой":
                jump day_keep
            "Спать":
                n "Вы решили завершить день и лечь спать."
                jump day_end
    n "У меня совсем не осталось сил.. Нужно поспать."
    jump day_keep

# =============================================================================
# ДОМ ФЕРМЕРШИ
# =============================================================================

label food_base:
    scene food_base with fade_scene
    n "Куда мне нужно пойти?"
    menu:
        "Грядки":
            jump greenhouse
        "Войти в дом":
            jump storage
        "Вернуться":
            jump go

label greenhouse:
    scene food_base with fade_scene
    if actions_left > 10:
        menu:
            "Проверить грядки":
                scene garden with fade_scene
                if tomato >= 1:
                    show tomato_plant at tomato_on_bed
                if tomato == 0:
                    menu:
                        "Посадить помидор":
                            $ tomato = 1
                            n "Я посадил помидор."
                            jump greenhouse
                        "Вернуться":
                            jump food_base
                elif tomato <= 3:
                    n "Помидор ещё растёт (стадия [tomato]/4). Походи ещё день — поспи, и он подрастёт."
                    menu:
                        "Вернуться":
                            jump food_base
                else:
                    n "Помидоры созрели! Можно собрать урожай."
                    menu:
                        "Собрать урожай":
                            call item_add("Помидор 🍅", "Такой красный и сочный", "items/tomato.png")
                            $ tomato = 0
                            n "Урожай собран. Можно посадить снова."
                            jump greenhouse
                        "Вернуться":
                            jump food_base
            "Вернуться":
                jump food_base
            "Пойти домой":
                jump day_keep
    else:
        n "У меня нет сил."
        jump greenhouse

label storage:
    scene food_base_in with fade_scene
    menu:
        "Поработать на ферме (примерно +50 [gold_icon] золота)":
            python:
                import random
                gold_add = random.randint(25, 75)
            $ gold += gold_add
            $ rep += 1
            $ actions_left -= 5
            n "Сегодня удалось заработать [gold_add] [gold_icon] золота."
            jump storage
        "Пойти домой":
            jump day_keep

label lab:
    n "В разработке..."

# =============================================================================
# ЖИЛОЙ РАЙОН
# =============================================================================

label home_base:
    scene home_base with fade_scene
    n "Куда мне нужно пойти?"
    menu:
        "Апартаменты {color=#d5265b}Малини{/color}":
            jump malini_house
        "Черный рынок":
            jump darkshop
        "Вернуться":
            jump go

label darkshop:
    menu:
        "Купить нож (20 [gold_icon] золота)":
            call item_add("Нож 🔪", "Острый..")
            jump darkshop
        "Уйти":
            jump home_base

label malini_house:
    menu:
        "Постучать":
            n "тук-тук-тук.."
            if actions_left > 10:
                n "Похоже {color=#d5265b}Малини{/color} ещё на работе."
                jump home_base
            else:
                n "Дверь открывается"
                show malini_full
                malini "Привет! Заходи)"
                jump home_base

# =============================================================================
# ЦЕНТР
# =============================================================================

label center_base:
    scene center_base with fade_scene
    n "Куда мне нужно пойти?"
    menu:
        "Магазин":
            jump market
        "Вернуться":
            jump go

label market:
    menu:
        "Уйти":
            jump center_base

# =============================================================================
# ПРОМЫШЛЕННЫЙ РАЙОН
# =============================================================================

label factory_base:
    scene factory_base with fade_scene
    n "Куда мне нужно пойти?"
    menu:
        "Завод":
            jump factory
        "Вернуться":
            jump go

label factory:
    scene factory_base with fade_scene
    if actions_left > 10:
        show malini_full at left
    menu:
        "Поработать на заводе (примерно +200 [gold_icon] золота,+5 Репутации [rep_icon])":
            python:
                import random
                gold_add = random.randint(175, 250)
            $ gold += gold_add
            $ rep += 5
            $ actions_left -= 10
            n "Сегодня удалось заработать [gold_add] [gold_icon] золота, а также 5 репутации [rep_icon]."
            jump storage
        "Воровать запчасти(примерно +400 [gold_icon] золота, -50 Репутации [rep_icon])":
            python:
                import random
                gold_add = random.randint(375, 450)
            $ gold += gold_add
            $ rep -= 50
            $ actions_left -= 5
            n "Я украл запчастей на [gold_add] [gold_icon] золота. (-50 Репутации [rep_icon])"
            jump storage
        "Волонтёрство (примерно 25 [gold_icon] золота и 5 репутации [rep_icon])":
            python:
                import random
                gold_add = random.randint(0, 50)
            $ gold += gold_add
            $ rep += 5
            $ actions_left -= 5
            n "Сегодня удалось заработать [gold_add] [gold_icon] золота."
            jump storage
        "Вернуться":
            jump food_base

# =============================================================================
# ЛОГИСТИКО-ИССЛЕДОВАТЕЛЬСКИЙ ЦЕНТР
# =============================================================================

label explore_base:
    scene explore_base with fade_scene
    n "Куда мне нужно пойти?"
    menu:
        "Центр исследований":
            jump explore_room
        "Вернуться":
            jump go

label explore_room:
    scene explore_base with fade_scene
    if actions_left > 10:
        menu:
            "Поработать на заводе (примерно +200 [gold_icon] золота,+5 Репутации [rep_icon])":
                python:
                    import random
                    gold_add = random.randint(175, 250)
                $ gold += gold_add
                $ rep += 5
                $ actions_left -= 10
                n "Сегодня удалось заработать [gold_add] [gold_icon] золота, а также 5 репутации [rep_icon]."
                jump storage
            "Воровать металл(примерно +400 [gold_icon] золота, -50 Репутации [rep_icon])":
                python:
                    import random
                    gold_add = random.randint(375, 450)
                $ gold += gold_add
                $ rep -= 50
                $ actions_left -= 5
                n "Я украл металла на [gold_add] [gold_icon] золота. (-50 Репутации [rep_icon])"
                jump storage
            "Волонтёрство (примерно 25 [gold_icon] золота и 5 репутации [rep_icon])":
                python:
                    import random
                    gold_add = random.randint(0, 50)
                $ gold += gold_add
                $ rep += 5
                $ actions_left -= 5
                n "Сегодня удалось заработать [gold_add] [gold_icon] золота."
                jump storage
            "Вернуться":
                jump food_base

# =============================================================================
# ВЗАИМОДЕЙСТВИЯ
# =============================================================================

label interact:
    menu:
        "Поговорить с Алекс":
            show alex_happy
            alex "Привет, рад, что ты заглянул!"
            $ relationships += 5
            $ actions_left -= 1
            show alex_happy at left
            jump alex_dialog

label alex_dialog:
    menu:
        "Подарить подарок":
            n "Вы предложили подарок Алексу."
            jump alex_dialog
        "Попросить подарок":
            n "Алекс дает вам что-то в знак благодарности за доверие."
            jump alex_dialog
        "Уйти":
            hide alex_happy
            jump day_keep

# =============================================================================
# КОНЕЦ ДНЯ И СМЕРТЬ
# =============================================================================

label day_end:
    if hp < 1:
        jump death
    n "Я поужинал и лёг спать."
    n "..."
    jump day_cycle

label death:
    n "У меня темнеет в глазах..."
    n "Конец игры."
    return
