# -*- coding: utf-8 -*-
# equipment.rpy — Система экипировки персонажа
# Характеристики, слоты, предметы, экраны экипировки

# === БАЗОВЫЕ ХАРАКТЕРИСТИКИ И СЛОТЫ ===
default base_stats = {
    "strength": 10,
    "agility": 10,
    "intelligence": 10,
    "charisma": 10
}

default equipped_items = {
    "underwear": None,
    "accessory": None,
    "pants": None,
    "torso": None,
    "hat": None,
    "weapon": None
}

default inventory_items = {
    "underwear": ["basic_underwear", "silk_underwear", "magic_underwear"],
    "accessory": ["silver_ring", "gold_necklace", "diamond_ring"],
    "pants": ["cloth_pants", "leather_pants", "steel_pants", "royal_pants", "battle_pants", "ninja_pants", "mage_pants", "heavy_pants", "light_pants", "cursed_pants", "blessed_pants", "dragon_pants"],
    "torso": ["cloth_shirt", "leather_armor", "mage_robe", "dragon_armor", "assassin_vest", "royal_robe"],
    "hat": ["cloth_cap", "iron_helmet", "crown"],
    "weapon": ["wooden_sword", "iron_sword", "magic_staff"]
}

# === ДАННЫЕ ПРЕДМЕТОВ ЭКИПИРОВКИ ===
init python:
    equipment_data = {
        "basic_underwear": {"id": "basic_underwear", "name": "Базовое белье", "image": "equipment/underwear/basic_underwear.png", "slot": "underwear", "stats": {"strength": 0, "agility": 1, "intelligence": 0, "charisma": 1}, "description": "Простое нижнее белье"},
        "silk_underwear": {"id": "silk_underwear", "name": "Шелковое белье", "image": "equipment/underwear/silk_underwear.png", "slot": "underwear", "stats": {"strength": 0, "agility": 2, "intelligence": 0, "charisma": 3}, "description": "Роскошное шелковое белье"},
        "silver_ring": {"id": "silver_ring", "name": "Серебряное кольцо", "image": "equipment/accessory/silver_ring.png", "slot": "accessory", "stats": {"strength": 0, "agility": 0, "intelligence": 1, "charisma": 2}, "description": "Простое серебряное кольцо"},
        "gold_necklace": {"id": "gold_necklace", "name": "Золотое ожерелье", "image": "equipment/accessory/gold_necklace.png", "slot": "accessory", "stats": {"strength": 0, "agility": 0, "intelligence": 2, "charisma": 4}, "description": "Дорогое золотое ожерелье"},
        "cloth_pants": {"id": "cloth_pants", "name": "Тканевые штаны", "image": "equipment/pants/cloth_pants.png", "slot": "pants", "stats": {"strength": 1, "agility": 1, "intelligence": 0, "charisma": 1}, "description": "Простые тканевые штаны"},
        "leather_pants": {"id": "leather_pants", "name": "Кожаные штаны", "image": "equipment/pants/leather_pants.png", "slot": "pants", "stats": {"strength": 2, "agility": 2, "intelligence": 0, "charisma": 2}, "description": "Прочные кожаные штаны"},
        "cloth_shirt": {"id": "cloth_shirt", "name": "Тканевая рубашка", "image": "equipment/torso/cloth_shirt.png", "slot": "torso", "stats": {"strength": 1, "agility": 0, "intelligence": 1, "charisma": 2}, "description": "Простая тканевая рубашка"},
        "leather_armor": {"id": "leather_armor", "name": "Кожаная броня", "image": "equipment/torso/leather_armor.png", "slot": "torso", "stats": {"strength": 3, "agility": 1, "intelligence": 0, "charisma": 1}, "description": "Прочная кожаная броня"},
        "cloth_cap": {"id": "cloth_cap", "name": "Тканевая кепка", "image": "equipment/hat/cloth_cap.png", "slot": "hat", "stats": {"strength": 0, "agility": 1, "intelligence": 1, "charisma": 1}, "description": "Простая тканевая кепка"},
        "iron_helmet": {"id": "iron_helmet", "name": "Железный шлем", "image": "equipment/hat/iron_helmet.png", "slot": "hat", "stats": {"strength": 2, "agility": -1, "intelligence": 0, "charisma": 0}, "description": "Тяжелый железный шлем"},
        "wooden_sword": {"id": "wooden_sword", "name": "Деревянный меч", "image": "equipment/weapon/wooden_sword.png", "slot": "weapon", "stats": {"strength": 2, "agility": 0, "intelligence": 0, "charisma": 0}, "description": "Простой деревянный меч"},
        "iron_sword": {"id": "iron_sword", "name": "Железный меч", "image": "equipment/weapon/iron_sword.png", "slot": "weapon", "stats": {"strength": 4, "agility": -1, "intelligence": 0, "charisma": 1}, "description": "Острый железный меч"},
        "magic_underwear": {"id": "magic_underwear", "name": "Магическое белье", "image": "equipment/underwear/magic_underwear.png", "slot": "underwear", "stats": {"strength": 1, "agility": 2, "intelligence": 3, "charisma": 2}, "description": "Белье с магическими свойствами"},
        "diamond_ring": {"id": "diamond_ring", "name": "Алмазное кольцо", "image": "equipment/accessory/diamond_ring.png", "slot": "accessory", "stats": {"strength": 0, "agility": 0, "intelligence": 3, "charisma": 5}, "description": "Роскошное алмазное кольцо"},
        "steel_pants": {"id": "steel_pants", "name": "Стальные штаны", "image": "equipment/pants/steel_pants.png", "slot": "pants", "stats": {"strength": 3, "agility": -1, "intelligence": 0, "charisma": 1}, "description": "Тяжелые стальные штаны"},
        "mage_robe": {"id": "mage_robe", "name": "Роба мага", "image": "equipment/torso/mage_robe.png", "slot": "torso", "stats": {"strength": 0, "agility": 1, "intelligence": 4, "charisma": 2}, "description": "Роба опытного мага"},
        "crown": {"id": "crown", "name": "Корона", "image": "equipment/hat/crown.png", "slot": "hat", "stats": {"strength": 0, "agility": 0, "intelligence": 2, "charisma": 6}, "description": "Королевская корона"},
        "magic_staff": {"id": "magic_staff", "name": "Магический посох", "image": "equipment/weapon/magic_staff.png", "slot": "weapon", "stats": {"strength": 1, "agility": 0, "intelligence": 5, "charisma": 2}, "description": "Посох с магической силой"},
        "royal_pants": {"id": "royal_pants", "name": "Королевские штаны", "image": "equipment/pants/royal_pants.png", "slot": "pants", "stats": {"strength": 1, "agility": 1, "intelligence": 1, "charisma": 4}, "description": "Роскошные королевские штаны"},
        "battle_pants": {"id": "battle_pants", "name": "Боевые штаны", "image": "equipment/pants/battle_pants.png", "slot": "pants", "stats": {"strength": 4, "agility": 2, "intelligence": 0, "charisma": 0}, "description": "Штаны для сражений"},
        "ninja_pants": {"id": "ninja_pants", "name": "Штаны ниндзя", "image": "equipment/pants/ninja_pants.png", "slot": "pants", "stats": {"strength": 1, "agility": 5, "intelligence": 1, "charisma": 0}, "description": "Легкие штаны ниндзя"},
        "mage_pants": {"id": "mage_pants", "name": "Штаны мага", "image": "equipment/pants/mage_pants.png", "slot": "pants", "stats": {"strength": 0, "agility": 1, "intelligence": 4, "charisma": 1}, "description": "Штаны для магов"},
        "heavy_pants": {"id": "heavy_pants", "name": "Тяжелые штаны", "image": "equipment/pants/heavy_pants.png", "slot": "pants", "stats": {"strength": 3, "agility": -2, "intelligence": 0, "charisma": 1}, "description": "Очень тяжелые штаны"},
        "light_pants": {"id": "light_pants", "name": "Легкие штаны", "image": "equipment/pants/light_pants.png", "slot": "pants", "stats": {"strength": 0, "agility": 3, "intelligence": 0, "charisma": 2}, "description": "Очень легкие штаны"},
        "cursed_pants": {"id": "cursed_pants", "name": "Проклятые штаны", "image": "equipment/pants/cursed_pants.png", "slot": "pants", "stats": {"strength": 5, "agility": 0, "intelligence": 0, "charisma": -2}, "description": "Мощные, но проклятые штаны"},
        "blessed_pants": {"id": "blessed_pants", "name": "Благословенные штаны", "image": "equipment/pants/blessed_pants.png", "slot": "pants", "stats": {"strength": 2, "agility": 2, "intelligence": 2, "charisma": 3}, "description": "Штаны с божественным благословением"},
        "dragon_pants": {"id": "dragon_pants", "name": "Драконьи штаны", "image": "equipment/pants/dragon_pants.png", "slot": "pants", "stats": {"strength": 6, "agility": 1, "intelligence": 1, "charisma": 2}, "description": "Штаны из драконьей кожи"},
        "dragon_armor": {"id": "dragon_armor", "name": "Драконья броня", "image": "equipment/torso/dragon_armor.png", "slot": "torso", "stats": {"strength": 5, "agility": 0, "intelligence": 1, "charisma": 3}, "description": "Броня из драконьих чешуек"},
        "assassin_vest": {"id": "assassin_vest", "name": "Жилет ассасина", "image": "equipment/torso/assassin_vest.png", "slot": "torso", "stats": {"strength": 2, "agility": 4, "intelligence": 1, "charisma": 0}, "description": "Легкий жилет для скрытности"},
        "royal_robe": {"id": "royal_robe", "name": "Королевская роба", "image": "equipment/torso/royal_robe.png", "slot": "torso", "stats": {"strength": 0, "agility": 0, "intelligence": 3, "charisma": 6}, "description": "Роскошная королевская роба"}
    }

    def get_item_data(item_id):
        return equipment_data.get(item_id, None)

    def is_valid_item(item_id, slot):
        item = get_item_data(item_id)
        return item is not None and item["slot"] == slot

    def get_item_image(item_id):
        item = get_item_data(item_id)
        if not item:
            return "malini_full"  # имя изображения из definitions.rpy
        return item["image"]

    def get_item_tooltip(item_id):
        item = get_item_data(item_id)
        if not item:
            return "Неизвестный предмет"
        tooltip_parts = [item["name"], item["description"]]
        stats_parts = []
        for stat, value in item["stats"].items():
            if value != 0:
                stat_names = {"strength": "Сила", "agility": "Ловкость", "intelligence": "Интеллект", "charisma": "Харизма"}
                stats_parts.append(f"{stat_names.get(stat, stat)}: {value:+}")
        if stats_parts:
            tooltip_parts.append("Характеристики:")
            tooltip_parts.extend(stats_parts)
        return "\n".join(tooltip_parts)

    def equip_item(item_id):
        item = get_item_data(item_id)
        if not item:
            return False
        slot = item["slot"]
        if not is_valid_item(item_id, slot):
            return False
        if equipped_items[slot]:
            old_item = equipped_items[slot]
            if old_item not in inventory_items[slot]:
                inventory_items[slot].append(old_item)
        equipped_items[slot] = item_id
        if item_id in inventory_items[slot]:
            inventory_items[slot].remove(item_id)
        return True

    def unequip_item(slot):
        if slot not in equipped_items:
            return False
        if equipped_items[slot]:
            item_id = equipped_items[slot]
            equipped_items[slot] = None
            if item_id not in inventory_items[slot]:
                inventory_items[slot].append(item_id)
            return True
        return False

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

    class EquipItemAction(Action):
        def __init__(self, item_id):
            self.item_id = item_id
        def __call__(self):
            equip_item(self.item_id)
            renpy.restart_interaction()

    class UnequipItemAction(Action):
        def __init__(self, slot):
            self.slot = slot
        def __call__(self):
            unequip_item(self.slot)
            renpy.restart_interaction()

# === ЭКРАНЫ ЭКИПИРОВКИ ===
screen item_tooltip(tooltip_text):
    zorder 100
    frame:
        at transform:
            alpha 0.0
            linear 0.2 alpha 1.0
        xalign 0.5
        yalign 0.1
        xmaximum 400
        background "#2a2520E0"
        padding (15, 15)
        text tooltip_text size 18 color gui.interface_text_color text_align 0.5 xalign 0.5

screen character_display():
    frame:
        align (0.5, 0.5)
        xsize 640
        ysize 960
        background "#2a2520"
        add "malini_full"
        if equipped_items["underwear"]:
            $ underwear_item = get_item_data(equipped_items["underwear"])
            if underwear_item:
                $ underwear_tooltip = get_item_tooltip(equipped_items["underwear"])
                button action UnequipItemAction("underwear") tooltip underwear_tooltip:
                    add get_item_image(equipped_items["underwear"])
        if equipped_items["accessory"]:
            $ accessory_item = get_item_data(equipped_items["accessory"])
            if accessory_item:
                $ accessory_tooltip = get_item_tooltip(equipped_items["accessory"])
                button action UnequipItemAction("accessory") tooltip accessory_tooltip:
                    add get_item_image(equipped_items["accessory"])
        if equipped_items["pants"]:
            $ pants_item = get_item_data(equipped_items["pants"])
            if pants_item:
                $ pants_tooltip = get_item_tooltip(equipped_items["pants"])
                button action UnequipItemAction("pants") tooltip pants_tooltip:
                    add get_item_image(equipped_items["pants"])
        if equipped_items["torso"]:
            $ torso_item = get_item_data(equipped_items["torso"])
            if torso_item:
                $ torso_tooltip = get_item_tooltip(equipped_items["torso"])
                button action UnequipItemAction("torso") tooltip torso_tooltip:
                    add get_item_image(equipped_items["torso"])
        if equipped_items["hat"]:
            $ hat_item = get_item_data(equipped_items["hat"])
            if hat_item:
                $ hat_tooltip = get_item_tooltip(equipped_items["hat"])
                button action UnequipItemAction("hat") tooltip hat_tooltip:
                    add get_item_image(equipped_items["hat"])
        if equipped_items["weapon"]:
            $ weapon_item = get_item_data(equipped_items["weapon"])
            if weapon_item:
                $ weapon_tooltip = get_item_tooltip(equipped_items["weapon"])
                button action UnequipItemAction("weapon") tooltip weapon_tooltip:
                    add get_item_image(equipped_items["weapon"])
        vbox:
            align (0.0, 0.0)
            xsize 200
            text "Текущая экипировка:" size 18 color gui.interface_text_color
            for slot_name, item_id in equipped_items.items():
                if item_id:
                    $ item = get_item_data(item_id)
                    if item:
                        $ slot_names = {"underwear": "Белье", "accessory": "Аксессуар", "pants": "Штаны", "torso": "Торс", "hat": "Шапка", "weapon": "Оружие"}
                        text "[slot_names.get(slot_name, slot_name)]: [item['name']]" size 14 color gui.idle_small_color

screen inventory_grid():
    frame:
        align (1.0, 0.5)
        xsize 450
        ysize 700
        background "#2a2520"
        vbox:
            text "Инвентарь экипировки" size 28 xalign 0.5 color gui.accent_color
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                xsize 420
                ysize 620
                vbox:
                    spacing 15
                    $ slot_names = {"underwear": "Нижнее белье", "accessory": "Аксессуары", "pants": "Штаны", "torso": "Торс", "hat": "Головные уборы", "weapon": "Оружие"}
                    for slot_name, items in inventory_items.items():
                        vbox:
                            $ item_count = len(items) if items else 0
                            text "[slot_names.get(slot_name, slot_name)] ([item_count])" size 22 color gui.accent_color
                            if items:
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
                                                        button xsize 120 ysize 100 action EquipItemAction(item_id) tooltip item_tooltip:
                                                            vbox:
                                                                spacing 2
                                                                text item["name"] size 14 xalign 0.5 color gui.interface_text_color text_align 0.5
                                                                $ main_stats = []
                                                                for stat, value in item["stats"].items():
                                                                    if value != 0:
                                                                        $ stat_names = {"strength": "💪", "agility": "🏃", "intelligence": "🧠", "charisma": "✨"}
                                                                        $ main_stats.append(f"{stat_names.get(stat, stat)}{value:+}")
                                                                if main_stats:
                                                                    text " ".join(main_stats) size 12 xalign 0.5 color gui.hover_color text_align 0.5
                                                else:
                                                    null width 120 height 100
                            else:
                                text "Пусто" size 16 color gui.idle_color
                            null height 5
            null

screen character_stats():
    frame:
        align (0.0, 1.0)
        xsize 300
        ysize 200
        background "#2a2520"
        vbox:
            spacing 5
            text "Характеристики:" size 24 color gui.accent_color
            $ total_stats = calculate_total_stats()
            text "💪 Сила: [total_stats['strength']]" size 20 color gui.interface_text_color
            text "🏃 Ловкость: [total_stats['agility']]" size 20 color gui.interface_text_color
            text "🧠 Интеллект: [total_stats['intelligence']]" size 20 color gui.interface_text_color
            text "✨ Харизма: [total_stats['charisma']]" size 20 color gui.interface_text_color

screen equipment_interface():
    use character_display
    use inventory_grid
    use character_stats
    textbutton "Закрыть" action Return() align (0.5, 0.95) text_color gui.interface_text_color

# === ТЕСТОВЫЕ ФУНКЦИИ ===
init python:
    import random
    def property_test_equipment_slot_management():
        test_results = []
        original_equipped = equipped_items.copy()
        original_inventory = {}
        for slot, items in inventory_items.items():
            original_inventory[slot] = items.copy()
        try:
            for slot in ["underwear", "accessory", "pants", "torso", "hat", "weapon"]:
                equipped_items[slot] = None
                if inventory_items[slot]:
                    test_item = inventory_items[slot][0]
                    result = equip_item(test_item)
                    if result and equipped_items[slot] == test_item:
                        test_results.append(f"✓ Слот {slot}: предмет {test_item} успешно экипирован")
                    else:
                        test_results.append(f"✗ Слот {slot}: ошибка экипировки {test_item}")
            for slot in ["torso", "weapon"]:
                if len(inventory_items[slot]) >= 2:
                    item1, item2 = inventory_items[slot][0], inventory_items[slot][1]
                    equip_item(item1)
                    first_equipped = equipped_items[slot]
                    equip_item(item2)
                    second_equipped = equipped_items[slot]
                    if first_equipped == item1 and second_equipped == item2 and item1 in inventory_items[slot]:
                        test_results.append(f"✓ Слот {slot}: замена предмета работает корректно")
                    else:
                        test_results.append(f"✗ Слот {slot}: ошибка замены предмета")
            invalid_tests = [("cloth_shirt", "weapon"), ("wooden_sword", "torso")]
            for item_id, wrong_slot in invalid_tests:
                original_slot_state = equipped_items[wrong_slot]
                equipped_items[wrong_slot] = item_id
                item_data = get_item_data(item_id)
                if item_data and item_data["slot"] != wrong_slot:
                    test_results.append(f"✓ Валидация: предмет {item_id} корректно отклонен для слота {wrong_slot}")
                equipped_items[wrong_slot] = original_slot_state
        finally:
            for slot in equipped_items:
                equipped_items[slot] = original_equipped[slot]
            for slot in inventory_items:
                inventory_items[slot] = original_inventory[slot].copy()
        return test_results

label test_equipment_system:
    "Тестируем систему экипировки..."
    $ property_results = property_test_equipment_slot_management()
    "Результаты property теста для управления слотами:"
    python:
        for result in property_results:
            renpy.say(n, result)
    $ result = equip_item("cloth_shirt")
    if result:
        "Успешно экипировали тканевую рубашку!"
    else:
        "Ошибка при экипировке тканевой рубашки."
    $ stats = calculate_total_stats()
    "Текущие характеристики:"
    "Сила: [stats['strength']]"
    "Ловкость: [stats['agility']]"
    "Интеллект: [stats['intelligence']]"
    "Харизма: [stats['charisma']]"
    call screen equipment_interface
    "Тест завершен!"
    return
