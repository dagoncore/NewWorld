# -*- coding: utf-8 -*-
# inventory.rpy — Система инвентаря предметов (не экипировка)
# Класс Item, предметы, добавление/удаление, экран инвентаря

init python:
    class Item:
        def __init__(self, name, description, image=None, wasted=False):
            self.name = name
            self.description = description
            self.image = image
            self.wasted = wasted

# === ПРЕДМЕТЫ ===
default all_items = [
    Item("Старый ключ 🔑", "Ржавый ключ от неизвестной двери", None),
    Item("Записка 📝", "Загадочная записка с координатами", None),
    Item("Монета 🪙", "Древняя золотая монета", None)
]

# === ФУНКЦИИ ИНВЕНТАРЯ ===
label item_add(name, description, image=None, wasted=False):
    $ item_exists = any(item.name == name for item in all_items)
    if item_exists:
        n "У вас уже есть предмет '[name]'."
        return
    $ new_item = Item(name, description, image, wasted)
    $ all_items.append(new_item)
    n "Предмет '[name]' добавлен в ваш инвентарь."
    return

label item_remove(item_name):
    $ item_to_remove = next((item for item in all_items if item.name == item_name), None)
    if item_to_remove:
        $ item_to_remove.wasted = True
        $ all_items.remove(item_to_remove)
        n "Предмет '[item_name]' удален из инвентаря."
    else:
        n "Предмет '[item_name]' не найден в инвентаре."
    return

# === ЭКРАН ИНВЕНТАРЯ ПРЕДМЕТОВ ===
screen items_inventory():
    modal True
    frame:
        align (0.5, 0.5)
        xsize 900
        ysize 700
        background "#2a2520"
        vbox:
            spacing 10
            hbox:
                xalign 0.5
                text "Инвентарь предметов" size 32 color gui.accent_color
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
                        $ items_per_row = 4
                        $ total_items = len(all_items)
                        $ rows_needed = (total_items + items_per_row - 1) // items_per_row
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
                                            background "#3d3832"
                                            action NullAction()
                                            hovered Show("item_tooltip", tooltip_text=full_description)
                                            unhovered Hide("item_tooltip")
                                            vbox:
                                                spacing 5
                                                xalign 0.5
                                                if item.image:
                                                    frame:
                                                        xsize 140
                                                        ysize 140
                                                        xalign 0.5
                                                        background "#4a4540"
                                                        add item.image:
                                                            xalign 0.5
                                                            yalign 0.5
                                                            xsize 130
                                                            ysize 130
                                                            fit "contain"
                                                else:
                                                    frame:
                                                        xsize 140
                                                        ysize 140
                                                        xalign 0.5
                                                        background "#4a4540"
                                                        text "?" size 60 xalign 0.5 yalign 0.5 color gui.idle_small_color
                                                text item.name size 16 xalign 0.5 color gui.interface_text_color text_align 0.5
                                                $ short_desc = item.description[:30] + "..." if len(item.description) > 30 else item.description
                                                text short_desc size 12 xalign 0.5 color gui.idle_small_color text_align 0.5
                                    else:
                                        null width 200 height 200
                    else:
                        text "Инвентарь пуст" size 24 xalign 0.5 color gui.idle_color
            textbutton "Закрыть" action Hide("items_inventory") xalign 0.5 ysize 40 xsize 200
