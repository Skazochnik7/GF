label part2:
    "ОСНОВНАЯ ЧАСТЬ. Инициализация"


# Главная петля
label init_day:
    "Инициализация нового дня"

    python: 
        normalize_stats()

    call day_planner(["Утро", "День", "Вечер"])

    call morning_processing
    call afternoon_processing
    call evening_processing

    call done_day

    jump init_day


return

label morning_processing:
    "УТРО. Локация [shed_morning]. Переходим, обрабатываем..."
    call expression shed_morning
return    

label afternoon_processing:
    "ДЕНЬ. Локация [shed_afternoon]. Переходим, обрабатываем..."
return    

label evening_processing:
    "ВЕЧЕР: Локация [shed_evening]. Переходим, обрабатываем..."
return    

label done_day:
    "НОЧЬ. Подведение итогов"
return    
