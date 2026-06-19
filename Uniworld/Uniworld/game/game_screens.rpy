# -*- coding: utf-8 -*-
# game_screens.rpy — Игровые экраны (ресурсы, HUD)

# === ЭКРАН РЕСУРСОВ ===
screen resources():
    textbutton "🎒":
        align (1.0, 0.0)
        xoffset -10
        yoffset 10
        action Show("items_inventory")
        xsize 60
        ysize 60
        text_size 40
    frame:
        align (1.0, 0.0)
        xoffset -10
        yoffset 80
        vbox:
            spacing 5
            text "[hp_icon] Зворовье: [hp]" size 20
            text "[day_icon] День: [day]" size 20
            text "[actions_icon] Осталось действий: [actions_left]" size 20
            text "[gold_icon] Золото: [gold]" size 20
            text "[rep_icon] Репутация: [rep]" size 20
