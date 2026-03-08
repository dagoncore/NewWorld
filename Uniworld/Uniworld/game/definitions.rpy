# -*- coding: utf-8 -*-
# definitions.rpy — Базовые определения игры
# Персонажи, фоны, изображения, переменные ресурсов

# === ПЕРСОНАЖИ ===
define n = Character("Нарратор", color="#FFFFFF")
define malini = Character("Малини", color="#00FF00")
define marta = Character("Марта", color="#F0E68C")

# === ФОНЫ ===
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

# === ПЕРЕХОДЫ МЕЖДУ СЦЕНАМИ ===
# Потемнение 0.3 сек при смене сцены (fade out → fade in)
define fade_scene = Fade(0.3, 0, 0.3)

# === ИЗОБРАЖЕНИЯ ПЕРСОНАЖЕЙ ===
# Малини (в папке лежат: m.PNG, m_smile.PNG, m_think.PNG)
image m = "characters/malini/m.PNG"
image malini_full = "characters/malini/m.PNG"
image malini_smile = "characters/malini/m_smile.PNG"
image malini_blink = "characters/malini/m_think.PNG"
# Марта
image marta_full = "characters/marta/marta_full.png"
image marta_smile = "characters/marta/marta_smile.png"

# === ПЕРЕМЕННЫЕ РЕСУРСОВ ===
default day_icon = "📅"
default actions_icon = "⏳"
default gold_icon = "🟡"
default rep_icon = "⭐"
default hp_icon = "❤️"
default hp = 100
default gold = 20
default rep = 0
default day = 0
default actions_left = 20  # Лимит действий в день
default tomato = 0  # 0 = нет растения, 1–4 = стадия роста (4 = можно собрать)

# === ПОМИДОРЫ: стадии роста из sheet (файл 1024x1024, верхняя полоса = 4 кадра по 256x384) ===
# Явно используем Image() и Crop для надёжной загрузки
image tomato_stage1 = Crop((0, 0, 256, 384), Image("images/plants/tomato.png"))
image tomato_stage2 = Crop((256, 0, 256, 384), Image("images/plants/tomato.png"))
image tomato_stage3 = Crop((512, 0, 256, 384), Image("images/plants/tomato.png"))
image tomato_stage4 = Crop((768, 0, 256, 384), Image("images/plants/tomato.png"))
# Динамическое изображение: подставляется tomato_stage1 … tomato_stage4 по переменной tomato
image tomato_plant = "tomato_stage[tomato]"
# Позиция помидора на экране грядки (центр)
transform tomato_on_bed:
    xalign 0.5
    yalign 0.5
    zoom 1.0

