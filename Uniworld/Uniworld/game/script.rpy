# Инициализация игры
define n = Character("Нарратор", color="#FFFFFF")
define k = Character("Карма", color="#00FF00")
define c = Character("Чарли", color="#F0E68C")

# Фоны
image bg_main_out = "backgrounds/hero_home.png"
image bg_main = "backgrounds/hero_home_in.png"
image garden = "backgrounds/garden.png"
image food_base = "backgrounds/farmer_home_out.png"
image food_base_in = "backgrounds/farmer_home_in.png"
image home_base = "backgrounds/home_base.jpg"
image explore_base = "backgrounds/explore_base.jpg"
image center_base = "backgrounds/center_base.jpg"
image factory_base = "backgrounds/factory_base.jpg"
image dig_base = "backgrounds/dig_base.jpg"

# Персонажи
# Малини
image m_f = "characters/karma/karma_full.png"
image k_smile = "characters/karma/karma_smile.png"
image k_blink = "characters/karma/karma_blink.png"
image m = "characters/malini/m.png"
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
default tomato = 0

#События
default storage_pussy = 0

# === СИСТЕМА ЭКИПИРОВКИ ===

# Базовые характеристики персонажа
default base_stats = {
    "strength": 10,
    "agility": 10,
    "intelligence": 10,
    "charisma": 10
}

# Текущая экипировка (слот: id предмета или None)
default equipped_items = {
    "underwear": None,    # Нижнее белье
    "accessory": None,    # Аксессуар
    "pants": None,        # Штаны
    "torso": None,        # Торс
    "hat": None,          # Шапка
    "weapon": None        # Оружие
}

# Доступные предметы в инвентаре (слот: список id предметов)
default inventory_items = {
    "underwear": ["basic_underwear", "silk_underwear", "magic_underwear"],
    "accessory": ["silver_ring", "gold_necklace", "diamond_ring"],
    "pants": ["cloth_pants", "leather_pants", "steel_pants", "royal_pants", "battle_pants", "ninja_pants", "mage_pants", "heavy_pants", "light_pants", "cursed_pants", "blessed_pants", "dragon_pants"],
    "torso": ["cloth_shirt", "leather_armor", "mage_robe", "dragon_armor", "assassin_vest", "royal_robe"],
    "hat": ["cloth_cap", "iron_helmet", "crown"],
    "weapon": ["wooden_sword", "iron_sword", "magic_staff"]
}

# Определение класса для инвентаря
init python:
    class Item:
        def __init__(self, name, description, image=None, wasted=False):
            self.name = name
            self.description = description
            self.image = image  # None если нет изображения
            self.wasted = wasted

# === ОПРЕДЕЛЕНИЯ ПРЕДМЕТОВ ЭКИПИРОВКИ ===
init python:
    # Словарь всех предметов экипировки
    equipment_data = {
        # Нижнее белье
        "basic_underwear": {
            "id": "basic_underwear",
            "name": "Базовое белье",
            "image": "equipment/underwear/basic_underwear.png",
            "slot": "underwear",
            "stats": {"strength": 0, "agility": 1, "intelligence": 0, "charisma": 1},
            "description": "Простое нижнее белье"
        },
        "silk_underwear": {
            "id": "silk_underwear", 
            "name": "Шелковое белье",
            "image": "equipment/underwear/silk_underwear.png",
            "slot": "underwear",
            "stats": {"strength": 0, "agility": 2, "intelligence": 0, "charisma": 3},
            "description": "Роскошное шелковое белье"
        },
        
        # Аксессуары
        "silver_ring": {
            "id": "silver_ring",
            "name": "Серебряное кольцо",
            "image": "equipment/accessory/silver_ring.png", 
            "slot": "accessory",
            "stats": {"strength": 0, "agility": 0, "intelligence": 1, "charisma": 2},
            "description": "Простое серебряное кольцо"
        },
        "gold_necklace": {
            "id": "gold_necklace",
            "name": "Золотое ожерелье",
            "image": "equipment/accessory/gold_necklace.png",
            "slot": "accessory", 
            "stats": {"strength": 0, "agility": 0, "intelligence": 2, "charisma": 4},
            "description": "Дорогое золотое ожерелье"
        },
        
        # Штаны
        "cloth_pants": {
            "id": "cloth_pants",
            "name": "Тканевые штаны",
            "image": "equipment/pants/cloth_pants.png",
            "slot": "pants",
            "stats": {"strength": 1, "agility": 1, "intelligence": 0, "charisma": 1},
            "description": "Простые тканевые штаны"
        },
        "leather_pants": {
            "id": "leather_pants",
            "name": "Кожаные штаны", 
            "image": "equipment/pants/leather_pants.png",
            "slot": "pants",
            "stats": {"strength": 2, "agility": 2, "intelligence": 0, "charisma": 2},
            "description": "Прочные кожаные штаны"
        },
        
        # Торс
        "cloth_shirt": {
            "id": "cloth_shirt",
            "name": "Тканевая рубашка",
            "image": "equipment/torso/cloth_shirt.png",
            "slot": "torso",
            "stats": {"strength": 1, "agility": 0, "intelligence": 1, "charisma": 2},
            "description": "Простая тканевая рубашка"
        },
        "leather_armor": {
            "id": "leather_armor",
            "name": "Кожаная броня",
            "image": "equipment/torso/leather_armor.png", 
            "slot": "torso",
            "stats": {"strength": 3, "agility": 1, "intelligence": 0, "charisma": 1},
            "description": "Прочная кожаная броня"
        },
        
        # Головные уборы
        "cloth_cap": {
            "id": "cloth_cap",
            "name": "Тканевая кепка",
            "image": "equipment/hat/cloth_cap.png",
            "slot": "hat", 
            "stats": {"strength": 0, "agility": 1, "intelligence": 1, "charisma": 1},
            "description": "Простая тканевая кепка"
        },
        "iron_helmet": {
            "id": "iron_helmet",
            "name": "Железный шлем",
            "image": "equipment/hat/iron_helmet.png",
            "slot": "hat",
            "stats": {"strength": 2, "agility": -1, "intelligence": 0, "charisma": 0},
            "description": "Тяжелый железный шлем"
        },
        
        # Оружие
        "wooden_sword": {
            "id": "wooden_sword",
            "name": "Деревянный меч",
            "image": "equipment/weapon/wooden_sword.png",
            "slot": "weapon",
            "stats": {"strength": 2, "agility": 0, "intelligence": 0, "charisma": 0},
            "description": "Простой деревянный меч"
        },
        "iron_sword": {
            "id": "iron_sword",
            "name": "Железный меч",
            "image": "equipment/weapon/iron_sword.png",
            "slot": "weapon",
            "stats": {"strength": 4, "agility": -1, "intelligence": 0, "charisma": 1},
            "description": "Острый железный меч"
        },
        
        # Дополнительные предметы для демонстрации скролла
        "magic_underwear": {
            "id": "magic_underwear",
            "name": "Магическое белье",
            "image": "equipment/underwear/magic_underwear.png",
            "slot": "underwear",
            "stats": {"strength": 1, "agility": 2, "intelligence": 3, "charisma": 2},
            "description": "Белье с магическими свойствами"
        },
        "diamond_ring": {
            "id": "diamond_ring",
            "name": "Алмазное кольцо",
            "image": "equipment/accessory/diamond_ring.png",
            "slot": "accessory",
            "stats": {"strength": 0, "agility": 0, "intelligence": 3, "charisma": 5},
            "description": "Роскошное алмазное кольцо"
        },
        "steel_pants": {
            "id": "steel_pants",
            "name": "Стальные штаны",
            "image": "equipment/pants/steel_pants.png",
            "slot": "pants",
            "stats": {"strength": 3, "agility": -1, "intelligence": 0, "charisma": 1},
            "description": "Тяжелые стальные штаны"
        },
        "mage_robe": {
            "id": "mage_robe",
            "name": "Роба мага",
            "image": "equipment/torso/mage_robe.png",
            "slot": "torso",
            "stats": {"strength": 0, "agility": 1, "intelligence": 4, "charisma": 2},
            "description": "Роба опытного мага"
        },
        "crown": {
            "id": "crown",
            "name": "Корона",
            "image": "equipment/hat/crown.png",
            "slot": "hat",
            "stats": {"strength": 0, "agility": 0, "intelligence": 2, "charisma": 6},
            "description": "Королевская корона"
        },
        "magic_staff": {
            "id": "magic_staff",
            "name": "Магический посох",
            "image": "equipment/weapon/magic_staff.png",
            "slot": "weapon",
            "stats": {"strength": 1, "agility": 0, "intelligence": 5, "charisma": 2},
            "description": "Посох с магической силой"
        },
        
        # Дополнительные штаны для тестирования скролла
        "royal_pants": {
            "id": "royal_pants",
            "name": "Королевские штаны",
            "image": "equipment/pants/royal_pants.png",
            "slot": "pants",
            "stats": {"strength": 1, "agility": 1, "intelligence": 1, "charisma": 4},
            "description": "Роскошные королевские штаны"
        },
        "battle_pants": {
            "id": "battle_pants",
            "name": "Боевые штаны",
            "image": "equipment/pants/battle_pants.png",
            "slot": "pants",
            "stats": {"strength": 4, "agility": 2, "intelligence": 0, "charisma": 0},
            "description": "Штаны для сражений"
        },
        "ninja_pants": {
            "id": "ninja_pants",
            "name": "Штаны ниндзя",
            "image": "equipment/pants/ninja_pants.png",
            "slot": "pants",
            "stats": {"strength": 1, "agility": 5, "intelligence": 1, "charisma": 0},
            "description": "Легкие штаны ниндзя"
        },
        "mage_pants": {
            "id": "mage_pants",
            "name": "Штаны мага",
            "image": "equipment/pants/mage_pants.png",
            "slot": "pants",
            "stats": {"strength": 0, "agility": 1, "intelligence": 4, "charisma": 1},
            "description": "Штаны для магов"
        },
        "heavy_pants": {
            "id": "heavy_pants",
            "name": "Тяжелые штаны",
            "image": "equipment/pants/heavy_pants.png",
            "slot": "pants",
            "stats": {"strength": 3, "agility": -2, "intelligence": 0, "charisma": 1},
            "description": "Очень тяжелые штаны"
        },
        "light_pants": {
            "id": "light_pants",
            "name": "Легкие штаны",
            "image": "equipment/pants/light_pants.png",
            "slot": "pants",
            "stats": {"strength": 0, "agility": 3, "intelligence": 0, "charisma": 2},
            "description": "Очень легкие штаны"
        },
        "cursed_pants": {
            "id": "cursed_pants",
            "name": "Проклятые штаны",
            "image": "equipment/pants/cursed_pants.png",
            "slot": "pants",
            "stats": {"strength": 5, "agility": 0, "intelligence": 0, "charisma": -2},
            "description": "Мощные, но проклятые штаны"
        },
        "blessed_pants": {
            "id": "blessed_pants",
            "name": "Благословенные штаны",
            "image": "equipment/pants/blessed_pants.png",
            "slot": "pants",
            "stats": {"strength": 2, "agility": 2, "intelligence": 2, "charisma": 3},
            "description": "Штаны с божественным благословением"
        },
        "dragon_pants": {
            "id": "dragon_pants",
            "name": "Драконьи штаны",
            "image": "equipment/pants/dragon_pants.png",
            "slot": "pants",
            "stats": {"strength": 6, "agility": 1, "intelligence": 1, "charisma": 2},
            "description": "Штаны из драконьей кожи"
        },
        
        # Дополнительные торсы
        "dragon_armor": {
            "id": "dragon_armor",
            "name": "Драконья броня",
            "image": "equipment/torso/dragon_armor.png",
            "slot": "torso",
            "stats": {"strength": 5, "agility": 0, "intelligence": 1, "charisma": 3},
            "description": "Броня из драконьих чешуек"
        },
        "assassin_vest": {
            "id": "assassin_vest",
            "name": "Жилет ассасина",
            "image": "equipment/torso/assassin_vest.png",
            "slot": "torso",
            "stats": {"strength": 2, "agility": 4, "intelligence": 1, "charisma": 0},
            "description": "Легкий жилет для скрытности"
        },
        "royal_robe": {
            "id": "royal_robe",
            "name": "Королевская роба",
            "image": "equipment/torso/royal_robe.png",
            "slot": "torso",
            "stats": {"strength": 0, "agility": 0, "intelligence": 3, "charisma": 6},
            "description": "Роскошная королевская роба"
        }
    }
    
    # Функция для получения данных предмета
    def get_item_data(item_id):
        return equipment_data.get(item_id, None)
    
    # Функция для проверки валидности предмета
    def is_valid_item(item_id, slot):
        item = get_item_data(item_id)
        return item is not None and item["slot"] == slot
    
    # Функция для безопасного получения изображения предмета
    def get_item_image(item_id):
        item = get_item_data(item_id)
        if not item:
            return "characters/karma/karma_full.png"  # Заглушка
        
        # Возвращаем путь к изображению (Ren'Py сам обработает отсутствующие файлы)
        return item["image"]
    
    # Функция для создания tooltip предмета
    def get_item_tooltip(item_id):
        item = get_item_data(item_id)
        if not item:
            return "Неизвестный предмет"
        
        tooltip_parts = [item["name"], item["description"]]
        
        # Добавляем характеристики
        stats_parts = []
        for stat, value in item["stats"].items():
            if value != 0:
                stat_names = {
                    "strength": "Сила",
                    "agility": "Ловкость", 
                    "intelligence": "Интеллект",
                    "charisma": "Харизма"
                }
                stats_parts.append(f"{stat_names.get(stat, stat)}: {value:+}")
        
        if stats_parts:
            tooltip_parts.append("Характеристики:")
            tooltip_parts.extend(stats_parts)
        
        return "\n".join(tooltip_parts)

# Определения предметов
default all_items = [
    Item("Старый ключ 🔑", "Ржавый ключ от неизвестной двери", None),
    Item("Записка 📝", "Загадочная записка с координатами", None),
    Item("Монета 🪙", "Древняя золотая монета", None)
]

# === ФУНКЦИИ УПРАВЛЕНИЯ ЭКИПИРОВКОЙ ===
init python:
    # Функция для экипировки предмета
    def equip_item(item_id):
        item = get_item_data(item_id)
        if not item:
            return False
            
        slot = item["slot"]
        
        # Проверяем валидность слота
        if not is_valid_item(item_id, slot):
            return False
        
        # Если в слоте уже есть предмет, возвращаем его в инвентарь
        if equipped_items[slot]:
            old_item = equipped_items[slot]
            if old_item not in inventory_items[slot]:
                inventory_items[slot].append(old_item)
        
        # Экипируем новый предмет
        equipped_items[slot] = item_id
        
        # Удаляем предмет из инвентаря
        if item_id in inventory_items[slot]:
            inventory_items[slot].remove(item_id)
            
        return True
    
    # Функция для снятия экипировки
    def unequip_item(slot):
        if slot not in equipped_items:
            return False
            
        if equipped_items[slot]:
            item_id = equipped_items[slot]
            equipped_items[slot] = None
            
            # Возвращаем предмет в инвентарь
            if item_id not in inventory_items[slot]:
                inventory_items[slot].append(item_id)
            return True
        return False
    
    # Функция для расчета общих характеристик
    def calculate_total_stats():
        total_stats = base_stats.copy()
        
        for slot, item_id in equipped_items.items():
            if item_id:
                item = get_item_data(item_id)
                if item and "stats" in item:
                    for stat, value in item["stats"].items():
                        if stat in total_stats:
                            total_stats[stat] += value
                        
        return total_stats

# === CUSTOM ACTIONS ДЛЯ ЭКИПИРОВКИ ===
init python:
    # Action для экипировки предмета без закрытия экрана
    class EquipItemAction(Action):
        def __init__(self, item_id):
            self.item_id = item_id
        
        def __call__(self):
            equip_item(self.item_id)
            renpy.restart_interaction()
    
    # Action для снятия экипировки без закрытия экрана
    class UnequipItemAction(Action):
        def __init__(self, slot):
            self.slot = slot
        
        def __call__(self):
            unequip_item(self.slot)
            renpy.restart_interaction()

# Функция для добавления нового предмета
label item_add(name, description, image=None, wasted=False):
    # Проверяем, есть ли уже предмет с таким именем
    $ item_exists = any(item.name == name for item in all_items)
    
    if item_exists:
        n "У вас уже есть предмет '[name]'."
        return  # Выходим из функции, если предмет уже есть
    
    $ new_item = Item(name, description, image, wasted)
    $ all_items.append(new_item)
    n "Предмет '[name]' добавлен в ваш инвентарь."
    return

# Функция для удаления предмета
label item_remove(item_name):
    $ item_to_remove = None
    # Ищем предмет по имени
    $ item_to_remove = next((item for item in all_items if item.name == item_name), None)

    if item_to_remove:
        # Устанавливаем статус использования предмета
        $ item_to_remove.wasted = True
        # Удаляем использованный предмет
        $ all_items.remove(item_to_remove)
        n "Предмет '[item_name]' удален из инвентаря."
    else:
        n "Предмет '[item_name]' не найден в инвентаре."
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
    # Кнопка инвентаря в правом верхнем углу (над ресурсами)
    textbutton "🎒":
        align (1.0, 0.0)  # Прижато к правому верхнему углу
        xoffset -10  # Небольшой отступ от края
        yoffset 10
        action Show("items_inventory")
        xsize 60
        ysize 60
        text_size 40
    
    # Ресурсы прижаты к правому краю, ниже кнопки
    frame:
        align (1.0, 0.0)
        xoffset -10  # Отступ от правого края
        yoffset 80  # Отступ сверху (под кнопкой инвентаря)
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

# === ЭКРАНЫ СИСТЕМЫ ЭКИПИРОВКИ ===

# Экран для отображения tooltip
screen item_tooltip(tooltip_text):
    zorder 100
    
    frame:
        at transform:
            alpha 0.0
            linear 0.2 alpha 1.0
        
        xalign 0.5
        yalign 0.1
        xmaximum 400
        background "#000000E0"  # Полупрозрачный черный
        padding (15, 15)
        
        text tooltip_text:
            size 18
            color "#FFFFFF"
            text_align 0.5
            xalign 0.5

# Экран инвентаря предметов (не экипировка)
screen items_inventory():
    modal True
    
    # === НАСТРОЙКА ЦВЕТОВ ===
    # Измените эти значения для изменения цветовой схемы
    $ bg_color = "#111112"        # Основной фон окна (темно-синий)
    $ title_color = "#FFFFFF"     # Цвет заголовка (золотой)
    $ card_bg_color = "#434345"   # Фон карточек предметов (синий)
    $ item_name_color = "#FFFFFF" # Цвет названия предмета (белый)
    $ item_desc_color = "#FFFFFF" # Цвет описания предмета (светло-серый)
    $ empty_text_color = "#FFFFFF" # Цвет текста "Инвентарь пуст" (серый)
    
    frame:
        align (0.5, 0.5)
        xsize 900
        ysize 700
        background bg_color  # Используем настраиваемый цвет
        
        vbox:
            spacing 10
            
            # Заголовок
            hbox:
                xalign 0.5
                text "Инвентарь предметов" size 32 color title_color
            
            # Viewport со скроллом
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                xsize 870
                ysize 580
                
                vbox:
                    spacing 10
                    
                    if all_items:
                        # Подсчитываем количество предметов и строк
                        $ items_per_row = 4
                        $ total_items = len(all_items)
                        $ rows_needed = (total_items + items_per_row - 1) // items_per_row
                        
                        # Создаем сетку предметов
                        for row in range(rows_needed):
                            hbox:
                                spacing 15
                                for col in range(items_per_row):
                                    $ item_index = row * items_per_row + col
                                    if item_index < total_items:
                                        $ item = all_items[item_index]
                                        
                                        $ full_description = item.name + "\n\n" + item.description
                                        
                                        button:
                                            xsize 200
                                            ysize 200
                                            background card_bg_color
                                            action NullAction()
                                            hovered Show("item_tooltip", tooltip_text=full_description)
                                            unhovered Hide("item_tooltip")
                                            
                                            vbox:
                                                spacing 5
                                                xalign 0.5  # Центрируем весь vbox
                                                
                                                # Изображение предмета (квадратное, центрированное)
                                                if item.image:
                                                    frame:
                                                        xsize 140
                                                        ysize 140
                                                        xalign 0.5  # Центрируем по горизонтали
                                                        background Solid("#555555")
                                                        
                                                        add item.image:
                                                            xalign 0.5
                                                            yalign 0.5
                                                            xsize 130
                                                            ysize 130
                                                            fit "contain"
                                                else:
                                                    # Заглушка если нет изображения (квадратная, центрированная)
                                                    frame:
                                                        xsize 140
                                                        ysize 140
                                                        xalign 0.5  # Центрируем по горизонтали
                                                        background Solid("#555555")
                                                        text "?" size 60 xalign 0.5 yalign 0.5 color "#FFFFFF"
                                                
                                                # Название предмета (центрированное)
                                                text item.name size 16 xalign 0.5 color item_name_color text_align 0.5
                                                
                                                # Описание (короткое, центрированное)
                                                $ short_desc = item.description[:30] + "..." if len(item.description) > 30 else item.description
                                                text short_desc size 12 xalign 0.5 color item_desc_color text_align 0.5
                                    else:
                                        # Пустое место для выравнивания
                                        null width 200 height 200
                    else:
                        text "Инвентарь пуст" size 24 xalign 0.5 color empty_text_color
            
            # Кнопка закрытия
            textbutton "Закрыть" action Hide("items_inventory") xalign 0.5 ysize 40 xsize 200

# Экран отображения персонажа с экипировкой
screen character_display():
    frame:
        align (0.5, 0.5)
        xsize 640
        ysize 960
        background "#0a0a0a"  # Темно-синий фон
        
        # Базовое изображение персонажа (используем существующее изображение)
        add "characters/karma/karma_full.png"  # Используем существующее изображение как заглушку
        
        # Слои экипировки в правильном порядке (снизу вверх) с возможностью клика для снятия
        # Порядок слоев: underwear, accessory, pants, torso, hat, weapon
        
        # 1. Нижнее белье (самый нижний слой)
        if equipped_items["underwear"]:
            $ underwear_item = get_item_data(equipped_items["underwear"])
            if underwear_item:
                $ underwear_tooltip = get_item_tooltip(equipped_items["underwear"])
                button:
                    action UnequipItemAction("underwear")
                    tooltip underwear_tooltip
                    add get_item_image(equipped_items["underwear"])
                
        # 2. Аксессуар
        if equipped_items["accessory"]:
            $ accessory_item = get_item_data(equipped_items["accessory"])
            if accessory_item:
                $ accessory_tooltip = get_item_tooltip(equipped_items["accessory"])
                button:
                    action UnequipItemAction("accessory")
                    tooltip accessory_tooltip
                    add get_item_image(equipped_items["accessory"])
                
        # 3. Штаны
        if equipped_items["pants"]:
            $ pants_item = get_item_data(equipped_items["pants"])
            if pants_item:
                $ pants_tooltip = get_item_tooltip(equipped_items["pants"])
                button:
                    action UnequipItemAction("pants")
                    tooltip pants_tooltip
                    add get_item_image(equipped_items["pants"])
                
        # 4. Торс
        if equipped_items["torso"]:
            $ torso_item = get_item_data(equipped_items["torso"])
            if torso_item:
                $ torso_tooltip = get_item_tooltip(equipped_items["torso"])
                button:
                    action UnequipItemAction("torso")
                    tooltip torso_tooltip
                    add get_item_image(equipped_items["torso"])
                
        # 5. Шапка
        if equipped_items["hat"]:
            $ hat_item = get_item_data(equipped_items["hat"])
            if hat_item:
                $ hat_tooltip = get_item_tooltip(equipped_items["hat"])
                button:
                    action UnequipItemAction("hat")
                    tooltip hat_tooltip
                    add get_item_image(equipped_items["hat"])
                
        # 6. Оружие (самый верхний слой)
        if equipped_items["weapon"]:
            $ weapon_item = get_item_data(equipped_items["weapon"])
            if weapon_item:
                $ weapon_tooltip = get_item_tooltip(equipped_items["weapon"])
                button:
                    action UnequipItemAction("weapon")
                    tooltip weapon_tooltip
                    add get_item_image(equipped_items["weapon"])
        
        # Показываем информацию о текущей экипировке
        vbox:
            align (0.0, 0.0)
            xsize 200
            text "Текущая экипировка:" size 18 color "#FFFFFF"
            for slot_name, item_id in equipped_items.items():
                if item_id:
                    $ item = get_item_data(item_id)
                    if item:
                        $ slot_names = {
                            "underwear": "Белье",
                            "accessory": "Аксессуар", 
                            "pants": "Штаны",
                            "torso": "Торс",
                            "hat": "Шапка",
                            "weapon": "Оружие"
                        }
                        text "[slot_names.get(slot_name, slot_name)]: [item['name']]" size 14 color "#CCCCCC"

# Экран инвентаря экипировки
screen inventory_grid():
    frame:
        align (1.0, 0.5)
        xsize 450
        ysize 700
        background "#0a0a0a"  # Простой синий фон вместо изображения
        
        vbox:
            text "Инвентарь экипировки" size 28 xalign 0.5 color "#FFD700"
            
            # Добавляем viewport для скролла
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                xsize 420
                ysize 620
                
                vbox:
                    spacing 15
                    
                    # Словарь для перевода названий слотов
                    $ slot_names = {
                        "underwear": "Нижнее белье",
                        "accessory": "Аксессуары", 
                        "pants": "Штаны",
                        "torso": "Торс",
                        "hat": "Головные уборы",
                        "weapon": "Оружие"
                    }
                    
                    # Словарь цветов для разных типов слотов
                    $ slot_colors = {
                        "underwear": "#FF69B4",
                        "accessory": "#FFD700", 
                        "pants": "#8B4513",
                        "torso": "#4169E1",
                        "hat": "#32CD32",
                        "weapon": "#DC143C"
                    }
                    
                    for slot_name, items in inventory_items.items():
                        vbox:
                            $ item_count = len(items) if items else 0
                            text "[slot_names.get(slot_name, slot_name)] ([item_count])" size 22 color slot_colors.get(slot_name, "#FFD700")
                            
                            if items:  # Если есть предметы в слоте
                                # Используем hbox с переносом для лучшего отображения множества предметов
                                $ items_per_row = 3
                                $ rows_needed = (len(items) + items_per_row - 1) // items_per_row
                                
                                vbox:
                                    spacing 5
                                    for row in range(rows_needed):
                                        hbox:
                                            spacing 8
                                            for col in range(items_per_row):
                                                $ item_index = row * items_per_row + col
                                                if item_index < len(items):
                                                    $ item_id = items[item_index]
                                                    $ item = get_item_data(item_id)
                                                    if item:
                                                        $ item_tooltip = get_item_tooltip(item_id)
                                                        button:
                                                            xsize 120
                                                            ysize 100
                                                            action EquipItemAction(item_id)
                                                            tooltip item_tooltip
                                                            
                                                            vbox:
                                                                spacing 2
                                                                # Показываем название предмета
                                                                text item["name"] size 14 xalign 0.5 color "#FFFFFF" text_align 0.5
                                                                
                                                                # Показываем основные характеристики
                                                                $ main_stats = []
                                                                for stat, value in item["stats"].items():
                                                                    if value != 0:
                                                                        $ stat_names = {
                                                                            "strength": "💪",
                                                                            "agility": "🏃",
                                                                            "intelligence": "🧠",
                                                                            "charisma": "✨"
                                                                        }
                                                                        $ main_stats.append(f"{stat_names.get(stat, stat)}{value:+}")
                                                                
                                                                if main_stats:
                                                                    text " ".join(main_stats) size 12 xalign 0.5 color "#90EE90" text_align 0.5
                                                else:
                                                    # Пустое место для выравнивания
                                                    null width 120 height 100
                            else:
                                text "Пусто" size 16 color "#888888"
                            
                            null height 5  # Отступ между категориями

# Экран характеристик персонажа
screen character_stats():
    frame:
        align (0.0, 1.0)
        xsize 300
        ysize 200
        background "#0a0a0a"  # Темно-зеленый фон
        
        vbox:
            spacing 5
            text "Характеристики:" size 24 color "#FFD700"
            $ total_stats = calculate_total_stats()
            text "💪 Сила: [total_stats['strength']]" size 20 color "#FF6B6B"
            text "🏃 Ловкость: [total_stats['agility']]" size 20 color "#4ECDC4"
            text "🧠 Интеллект: [total_stats['intelligence']]" size 20 color "#45B7D1"
            text "✨ Харизма: [total_stats['charisma']]" size 20 color "#96CEB4"

# Главный экран экипировки
screen equipment_interface():
    # Отображение персонажа
    use character_display
    
    # Инвентарь
    use inventory_grid
    
    # Характеристики
    use character_stats
    
    # Кнопка закрытия
    textbutton "Закрыть" action Return() align (0.5, 0.95)

# === ТЕСТОВЫЕ ФУНКЦИИ ===

# Property тест для управления слотами экипировки
init python:
    import random
    
    def property_test_equipment_slot_management():
        """
        Property 2: Equipment Slot Management
        Validates: Requirements 2.2, 2.4
        
        Для любого предмета, экипированного в слот, система должна сохранить этот предмет 
        в правильном слоте и заменить любой ранее экипированный предмет в этом слоте
        """
        test_results = []
        
        # Сохраняем исходное состояние
        original_equipped = equipped_items.copy()
        original_inventory = {}
        for slot, items in inventory_items.items():
            original_inventory[slot] = items.copy()
        
        try:
            # Тест 1: Экипировка предмета в пустой слот
            for slot in ["underwear", "accessory", "pants", "torso", "hat", "weapon"]:
                # Очищаем слот
                equipped_items[slot] = None
                
                # Берем случайный предмет для этого слота
                if inventory_items[slot]:
                    test_item = inventory_items[slot][0]
                    
                    # Экипируем предмет
                    result = equip_item(test_item)
                    
                    # Проверяем результат
                    if result and equipped_items[slot] == test_item:
                        test_results.append(f"✓ Слот {slot}: предмет {test_item} успешно экипирован")
                    else:
                        test_results.append(f"✗ Слот {slot}: ошибка экипировки {test_item}")
            
            # Тест 2: Замена экипированного предмета
            for slot in ["torso", "weapon"]:  # Тестируем на двух слотах
                if len(inventory_items[slot]) >= 2:
                    item1 = inventory_items[slot][0]
                    item2 = inventory_items[slot][1]
                    
                    # Экипируем первый предмет
                    equip_item(item1)
                    first_equipped = equipped_items[slot]
                    
                    # Экипируем второй предмет (должен заменить первый)
                    equip_item(item2)
                    second_equipped = equipped_items[slot]
                    
                    # Проверяем замену
                    if (first_equipped == item1 and 
                        second_equipped == item2 and 
                        item1 in inventory_items[slot]):
                        test_results.append(f"✓ Слот {slot}: замена предмета работает корректно")
                    else:
                        test_results.append(f"✗ Слот {slot}: ошибка замены предмета")
            
            # Тест 3: Проверка валидности слотов
            invalid_tests = [
                ("cloth_shirt", "weapon"),  # Рубашка в слот оружия
                ("wooden_sword", "torso"),  # Меч в слот торса
            ]
            
            for item_id, wrong_slot in invalid_tests:
                original_slot_state = equipped_items[wrong_slot]
                
                # Пытаемся экипировать предмет в неправильный слот напрямую
                equipped_items[wrong_slot] = item_id
                
                # Проверяем, что система не позволяет это
                item_data = get_item_data(item_id)
                if item_data and item_data["slot"] != wrong_slot:
                    test_results.append(f"✓ Валидация: предмет {item_id} корректно отклонен для слота {wrong_slot}")
                
                # Восстанавливаем состояние
                equipped_items[wrong_slot] = original_slot_state
            
        finally:
            # Восстанавливаем исходное состояние
            for slot in equipped_items:
                equipped_items[slot] = original_equipped[slot]
            for slot in inventory_items:
                inventory_items[slot] = original_inventory[slot].copy()
        
        return test_results

label test_equipment_system:
    "Тестируем систему экипировки..."
    
    # Запускаем property тест
    $ property_results = property_test_equipment_slot_management()
    "Результаты property теста для управления слотами:"
    python:
        for result in property_results:
            renpy.say(n, result)
    
    # Тестируем экипировку предмета
    $ result = equip_item("cloth_shirt")
    if result:
        "Успешно экипировали тканевую рубашку!"
    else:
        "Ошибка при экипировке тканевой рубашки."
    
    # Показываем характеристики
    $ stats = calculate_total_stats()
    "Текущие характеристики:"
    "Сила: [stats['strength']]"
    "Ловкость: [stats['agility']]"
    "Интеллект: [stats['intelligence']]"
    "Харизма: [stats['charisma']]"
    
    # Открываем интерфейс экипировки
    call screen equipment_interface
    
    "Тест завершен!"
    return
# Главный сценарий
label start:
    call complete_quest("Второй квест")
    scene bg_main
    show screen resources
    show screen quests
    show m at left
    n "Очередной день в Сантауне!"
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
                "Экипировка персонажа":
                    call screen equipment_interface
                    jump day_keep
                # "Тест системы экипировки":
                #     call test_equipment_system
                #     jump day_keep
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
        scene bg_main_out
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

### FOOD BASE #####################################################################
label food_base:
    scene food_base
    n "Куда мне нужно пойти?"
    menu:
        "Грядки":
            jump greenhouse
        "Войти в дом":
            jump storage
        "Вернуться":
            jump go

label greenhouse:
    scene food_base
    if actions_left > 10:
        menu:
            "Проверить грядки":
                scene garden
                if 1 <= tomato < 3:
                    $ tomato += 1
                    n "Помидор немного подрос." 
                    jump greenhouse
                elif tomato == 0:
                    menu:
                        "Посадить помидор":
                            $ tomato = 1
                            n "Я посадил помидор."
                            jump greenhouse
                        "Вернуться":
                            jump greenhouse
                else:
                    n "Помидоры выросли!"
                    menu:
                        "Собрать урожай":
                            call item_add("Помидор 🍅", "Такой красный и сочный", "items/tomato.png")
                            $ tomato = 0 # Обычно после сбора урожай обнуляется
                            jump greenhouse
                        "Вернуться":
                            jump greenhouse
            "Вернуться":
                jump food_base            
            "Пойти домой":
                jump day_keep
    else:
        n "У меня нет сил."
        jump greenhouse
label storage:
    scene food_base_in
    menu:
        "Поработать на ферме (примерно +50 монет [gold_icon],+50 Еды [food_icon])":
            python:
                import random
                gold_add = random.randint(25, 75)
                food_add = 50
            $ gold += gold_add
            $ food += food_add
            $ rep += 1
            $ actions_left -= 5
            n "Сегодня удалось заработать [gold_add] монет [gold_icon], а также я получил дополнительно [food_add] Еды [food_icon]."
            jump storage
        "Пойти домой":
            jump day_keep
        # "Воровать (примерно +300 Еды [food_icon], -25 Репутации [rep_icon])":
        #     python:
        #         import random
        #         food_add = random.randint(200, 400)
        #     $ food += food_add
        #     $ rep -= 25
        #     $ actions_left -= 5
        #     n "Я украл [food_add] Еды [food_icon]. (-25 Репутации [rep_icon])"
        #     jump storage
        # "Волонтёрство (примерно 25 тепломарок [gold_icon] и 5 репутации [rep_icon])":
        #     python:
        #         import random
        #         gold_add = random.randint(0, 50)
        #         food_add = 50
        #     $ gold += gold_add
        #     $ food += food_add
        #     $ rep += 5
        #     $ actions_left -= 5
        #     n "Сегодня удалось заработать [gold_add] тепломарок [gold_icon], а также я получил дополнительно [food_add] Еды [food_icon]."
        #     jump storage
        # "Вернуться":
        #     jump food_base
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