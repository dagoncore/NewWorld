# Инициализация игры
define n = Character("Нарратор", color="#FFFFFF")
define k = Character("Карма", color="#00FF00")
define c = Character("Чарли", color="#F0E68C")

# Фоны
image bg_main = "backgrounds/background_home.jpg"
image food_base = "backgrounds/food_base.jpg"
image home_base = "backgrounds/home_base.jpg"
image explore_base = "backgrounds/explore_base.jpg"
image center_base = "backgrounds/center_base.jpg"
image factory_base = "backgrounds/factory_base.jpg"
image dig_base = "backgrounds/dig_base.jpg"

# Персонажи
# Карма
image k_full = "characters/karma/karma_full.png"
image k_smile = "characters/karma/karma_smile.png"
image k_blink = "characters/karma/karma_blink.png"
image k_nude = "characters/karma/karma_nude.png"
# Хейз
image h_full = "characters/haze/haze_full.png"

# Переменные ресурсов
default day_icon = "📅"
default actions_icon = "⏳"
default food_icon = "🍞"
default gold_icon = "🎟️"
default rep_icon = "⭐"
default hp_icon = "❤️"
default hp = 100
default food = 50
default gold = 20
default rep = 0
default day = 0
default starve = 0
default nsfw = 1
default food_price = 10
default actions_left = 20  # Лимит действий в день

#События
default storage_pussy = 0

# Определение класса для инвентаря
init python:
    class Item:
        def __init__(self, name, description, wasted=False):
            self.name = name
            self.description = description
            self.wasted = wasted

# Определения предметов
default all_items = []

# Функция для добавления нового предмета
label item_add(name, description, wasted=False):
    # Проверяем, есть ли уже предмет с таким именем
    $ item_exists = any(item.name == name for item in all_items)
    
    if item_exists:
        n "У вас уже есть предмет '[name]'."
        return  # Выходим из функции, если предмет уже есть
    $ new_item = Item(name, description)
    $ all_items.append(new_item)
    n "Предмет '[name]' добавлен в ваш инвентарь."
    return
# Функция для удаления предмета
label item_remove(item_name):
    $ item_to_remove = None
    # Ищем квест по имени
    $ item_to_remove = next((item for item in all_items if item.name == item_name), None)

    if item_to_remove:
        # Устанавливаем статус завершения квеста
        $ item_to_remove.wasted = True
        # Удаляем завершенный квест
        $ all_items.remove(item_to_remove)
    return

# Определение класса для квестов
init python:
    class Quest:
        def __init__(self, name, description, completed=False, quest_type="Основной сюжет"):
            self.name = name
            self.description = description
            self.completed = completed
            self.type = quest_type

# Определения квестов
default quest1 = Quest("Бюджет", "Заработайте немного денег", quest_type="Основной сюжет")
default quest2 = Quest("Второй квест", "Это описание второго квеста.", quest_type="Основной сюжет")
default all_quests = [quest1, quest2]

# Функция для добавления нового квеста
label add_quest(name, description, quest_type="Main"):
    $ new_quest = Quest(name, description)
    $ all_quests.append(new_quest)
    n "Квест '[name]' добавлен в ваш список квестов."

# Функция для завершения квеста
label complete_quest(quest_name):
    $ quest_to_complete = None
    # Ищем квест по имени
    $ quest_to_complete = next((quest for quest in all_quests if quest.name == quest_name), None)

    if quest_to_complete:
        # Устанавливаем статус завершения квеста
        $ quest_to_complete.completed = True
        # Удаляем завершенный квест
        $ all_quests.remove(quest_to_complete)
    return

# Экран ресурсов
screen resources():
    frame:
        align (1.0, 0.0)
        vbox:
            spacing 5
            text "[hp_icon] Зворовье: [hp]" size 20
            text "[day_icon] День: [day]" size 20
            text "[actions_icon] Осталось действий: [actions_left]" size 20
            text "[food_icon] Еда: [food]" size 20
            text "[gold_icon] Тепломарки: [gold]" size 20
            text "[rep_icon] Репутация: [rep]" size 20
screen quests():
    frame:
        align (0.0, 0.0)
        vbox:
            for quest in all_quests:
                if quest.completed:
                    text "[quest.name] (Завершен) [quest.type]" size 20
                    #$ all_quests.remove(quest)
                else:
                    text "[quest.name] (Не завершен) [quest.type]" size 20
                    text "[quest.description]" size 15
# Главный сценарий
label start:
    call complete_quest("Второй квест")
    scene bg_main
    show screen resources
    show screen quests
    show h_full at left
    n "Очередной день в Ядротауне.."
    call day_cycle
    return

label day_cycle:
    if gold > 100:
        call complete_quest("Бюджет")
    $ day += 1
    $ actions_left = 20
    n "День [day]: начинается новый день."
    label day_keep:
        scene bg_main
        while actions_left > 0:
            menu:
                "Посмотреть что у меня есть":
                    n "У меня есть.."
                    python:
                        # Создаем список строк для вывода
                        item_lines = []
                        for item in all_items:
                            item_lines.append(f"{item.name} - {item.description}")
                        # Объединяем строки в одну
                        item_text = "\n".join(item_lines)
                    # Выводим текст после блока python
                    n "[item_text]"
                    jump day_keep
                "Потерять карандаш":
                    call item_remove("Карандаш ✏️")
                    jump day_keep
                "Найти карандаш":
                    call item_add("Карандаш ✏️", "Я могу им написать что-то")
                    jump day_keep     
                "Выйти из дома":
                    jump go
    n "У меня совсем не осталось сил.. Нужно поспать."
    jump day_end
    label go:
        scene bg_main
        while actions_left > 0:
            menu:
                "Отправиться в {color=#8ccb5e}Пищевой комплекс{/color}":
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

### FOOD BASE #####################################################################
label food_base:
    scene food_base
    n "Куда мне нужно пойти?"
    menu:
        "Теплицы":
            jump greenhouse
        "Склад":
            jump storage
        "Лаборатория":
            jump lab
        "Вернуться":
            jump go

label greenhouse:
    scene food_base
    menu:
        "Поработать в теплицах (примерно +100 Тепломарки [gold_icon],+20 Еды [food_icon])":
            python:
                import random
                gold_add = random.randint(50, 150)
                food_add = 20
            $ gold += gold_add
            $ food += food_add
            $ rep += 1
            $ actions_left -= 5
            n "Сегодня удалось заработать [gold_add] тепломарок [gold_icon], а также я получил дополнительно 20 Еды [food_icon]."
            jump greenhouse
        "Вернуться":
            jump food_base            
        "Пойти домой":
            jump day_keep
label storage:
    scene food_base
    menu:
        "Поработать на складе (примерно +50 Тепломарки [gold_icon],+50 Еды [food_icon])":
            python:
                import random
                gold_add = random.randint(25, 75)
                food_add = 50
            $ gold += gold_add
            $ food += food_add
            $ rep += 1
            $ actions_left -= 5
            n "Сегодня удалось заработать [gold_add] тепломарок [gold_icon], а также я получил дополнительно [food_add] Еды [food_icon]."
            jump storage
        "Воровать (примерно +300 Еды [food_icon], -25 Репутации [rep_icon])":
            python:
                import random
                food_add = random.randint(200, 400)
            $ food += food_add
            $ rep -= 25
            $ actions_left -= 5
            n "Я украл [food_add] Еды [food_icon]. (-25 Репутации [rep_icon])"
            jump storage
        "Волонтёрство (примерно 25 тепломарок [gold_icon] и 5 репутации [rep_icon])":
            python:
                import random
                gold_add = random.randint(0, 50)
                food_add = 50
            $ gold += gold_add
            $ food += food_add
            $ rep += 5
            $ actions_left -= 5
            n "Сегодня удалось заработать [gold_add] тепломарок [gold_icon], а также я получил дополнительно [food_add] Еды [food_icon]."
            jump storage
        "Вернуться":
            jump food_base
label lab:
    n "В разработке..."

### HOME BASE #####################################################################
label home_base:
    scene home_base
    n "Куда мне нужно пойти?"
    menu:
        "Апартаменты {color=#d5265b}Кармы{/color}":
            jump karma_house
        "Черный рынок":
            jump darkshop        
        "Вернуться":
            jump go

label darkshop:
    menu:
        "Купить нож (20 [gold_icon] тепломарок)":
            call item_add("Нож 🔪", "Острый..")
            jump darkshop
        "Уйти":
            jump home_base

label karma_house:
    menu:
        "Постучать":
            n "тук-тук-тук.."
            if actions_left > 10:
                n "Похоже {color=#d5265b}Карма{/color} ещё на работе."
                jump home_base
            else:
                n "Дверь открывается"
                show k_full
                k "Привет! Заходи)"
                jump home_base

### CENTER BASE #####################################################################
label center_base:
    scene center_base
    n "Куда мне нужно пойти?"
    menu:
        "Магазин продуктов [food_icon]":
            jump market
        "Вернуться":
            jump go

label market:
    $ food_cost = food_price * 1
    menu:
        "Купить 10 еды [food_icon] за [food_cost] тепломарок [gold_icon]":
            if gold < food_cost:
                "Не хватает тепломарок..[gold_icon]"
                jump market
            else:
                "Вы приобрели 10 еды [food_icon]"
                $ gold -= food_cost
                $ food += 10
                jump market
        "Уйти":
            jump center_base

### FACTORY BASE #####################################################################
label factory_base:
    scene factory_base
    n "Куда мне нужно пойти?"
    menu:
        "Завод":
            jump factory
        "Вернуться":
            jump go
label factory:
    scene factory_base
    if actions_left > 10:
        show k_full at left
    menu:
        "Поработать на заводе (примерно +200 Тепломарки [gold_icon],+5 Репутации [rep_icon])":
            python:
                import random
                gold_add = random.randint(175, 250)
            $ gold += gold_add
            $ rep += 5
            $ actions_left -= 10
            n "Сегодня удалось заработать [gold_add] тепломарок [gold_icon], а также я получил дополнительно 5 репутации [rep_icon]."
            jump storage
        "Воровать запчасти(примерно +400 Тепломарки [gold_icon], -50 Репутации [rep_icon])":
            python:
                import random
                gold_add = random.randint(375, 450)
            $ gold += gold_add
            $ rep -= 50
            $ actions_left -= 5
            n "Я украл запчастей на [gold_add] тепломарок [gold_icon]. (-50 Репутации [rep_icon])"
            jump storage
        "Волонтёрство (примерно 25 тепломарок [gold_icon] и 5 репутации [rep_icon])":
            python:
                import random
                gold_add = random.randint(0, 50)
            $ gold += gold_add
            $ rep += 5
            $ actions_left -= 5
            n "Сегодня удалось заработать [gold_add] тепломарок [gold_icon]."
            jump storage
        "Вернуться":
            jump food_base
### EXPLORE BASE #####################################################################
label explore_base:
    scene explore_base
    n "Куда мне нужно пойти?"
    menu:
        "Центр исследований":
            jump explore_room
        "Вернуться":
            jump go
label explore_room:
    scene explore_base
    if actions_left > 10:
        menu:
            "Поработать на заводе (примерно +200 Тепломарки [gold_icon],+5 Репутации [rep_icon])":
                python:
                    import random
                    gold_add = random.randint(175, 250)
                $ gold += gold_add
                $ rep += 5
                $ actions_left -= 10
                n "Сегодня удалось заработать [gold_add] тепломарок [gold_icon], а также я получил дополнительно 5 репутации [rep_icon]."
                jump storage
            "Воровать металл(примерно +400 Тепломарки [gold_icon], -50 Репутации [rep_icon])":
                python:
                    import random
                    gold_add = random.randint(375, 450)
                $ gold += gold_add
                $ rep -= 50
                $ actions_left -= 5
                n "Я украл металла на [gold_add] тепломарок [gold_icon]. (-50 Репутации [rep_icon])"
                jump storage
            "Волонтёрство (примерно 25 тепломарок [gold_icon] и 5 репутации [rep_icon])":
                python:
                    import random
                    gold_add = random.randint(0, 50)
                $ gold += gold_add
                $ rep += 5
                $ actions_left -= 5
                n "Сегодня удалось заработать [gold_add] тепломарок [gold_icon]."
                jump storage
            "Вернуться":
                jump food_base


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
            # Логика для подарков
            jump alex_dialog
        "Попросить подарок":
            n "Алекс дает вам что-то в знак благодарности за доверие."
            # Логика получения предмета
            jump alex_dialog
        "Покажи киску":
            alex "Конечно!"
            hide alex_happy
            scene bg_alex_pussy
            n "Алекс демонстрирует свои дырочки."
            window hide
            $ renpy.pause()
            window auto
            scene bg_main
            show alex_happy at left
            jump alex_dialog
        "Уйти":
            hide alex_happy
            jump day_keep

label day_end:
    if hp < 1:
        jump death
    if food > 0:
        $ food -= 10
        n "Я поужинал и лёг спать"
    else:
        $ food_cost = food_price * 1
        if gold > food_cost:
            $ gold -= food_cost
            n "Я зашел в магазин продуктов перед сном, поел и лёг спать"
        else:  
            n "Я лёг спать голодным."
            $ starve += 1
            if starve > 3:
                "Голод слишком сильный, я умираю.. (-10 [hp_icon])"
                $ hp -= 10
                if hp < 0:
                    jump death
    n "..."
    jump day_cycle

label death:
    n "У меня темнеет в глазах..."
    n "Конец игры."
    return