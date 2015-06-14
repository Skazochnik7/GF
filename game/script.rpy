init python:
    for o in {"00:he", "01:edi", "02:sukk", "03:fri", "04:skaz"}:
        oo=o.split(":")
        WTXmlLinker.prepareCharacterResources( oo[1], 
        '00_ex_characters', '00_ex_characters/'+oo[0]+'_'+oo[1], '00_ex_characters/'+oo[0]+'_'+oo[1])


init:
    # Scenario initialization
    python:
        global arr
        global entries

    $arr=dict()
    $entries=[]

    python:
        global this
        this=This()
        global event
        global screens
        screens=ScreenCollection()
        global choose
        choose=None
        global time
        time=Time()
        global music
        music=Music()

# Подключение модуля отладки 
    python:
        global debug
        global _test
    $debug=Debug(3) # Если 0 - ничего не происходит, иначе сбрасывает значения перемнных в файл debug.txt
    $debug.SaveHeader()


# Определение персонажей игры.
    python:
        itemList=[]

        global he
        he=RegEntry(Person("he", "Юджин", CharacterExData(WTXmlLinker.getLinkerKey_he()),
                        defVals={"pos": gMakePos( 0, 100 ), "pos2": gMakePos( 0, 130 )}, 
            constVals={"pos_door": gMakePos( 350, 0 ), "pos_doorleft": gMakePos( 300, 0 ), "pos_center": POS_140})
        )


        global fri
        fri=RegEntry(Person("fri", "Друг", CharacterExData(WTXmlLinker.getLinkerKey_fri()),
                        defVals={"pos": gMakePos( 500, 100 ), "pos2": gMakePos( 0, 430 )}, 
            constVals={"pos_door": gMakePos( 350, 0 ), "pos_doorleft": gMakePos( 300, 0 ), "pos_center": POS_140})
        )

        global edi
        edi=RegEntry(Person("edi", "Редактор", CharacterExData(WTXmlLinker.getLinkerKey_edi()),
                        defVals={"pos": gMakePos( 500, 100 ), "pos2": gMakePos( 0, 430 )}, 
            constVals={"pos_door": gMakePos( 350, 0 ), "pos_doorleft": gMakePos( 300, 0 ), "pos_center": POS_140})
        )
    
        global sukk
        sukk=RegEntry(Person("sukk", "Меридиана", CharacterExData(WTXmlLinker.getLinkerKey_sukk()),
                        defVals={"pos": POS_140, "pos2": gMakePos( 0, 430 )}, 
            constVals={"pos_door": gMakePos( 350, 0 ), "pos_doorleft": gMakePos( 300, 0 ), "pos_center": POS_140})
        )

        global skaz
        skaz=RegEntry(Person("skaz", "", CharacterExData(WTXmlLinker.getLinkerKey_fri()),
                        defVals={"pos": gMakePos( 500, 100 ), "pos2": gMakePos( 0, 430 )}, 
            constVals={"pos_door": gMakePos( 350, 0 ), "pos_doorleft": gMakePos( 300, 0 ), "pos_center": POS_140})
        )

        shed_morning = None
        shed_afternoon = None
        shed_evening = None

        if persistent.mod_disable_original_stats == False:
        # Stats that will be shown on the "main" GUI
            register_stat("Morale", "morale", 0, 5, 100)
            register_stat("Behavior", "behavior", 5, 0, 100)
            register_stat("Academics", "academics", 10, 0, 100)
            register_stat("Artistery", "artistery", 10, 0, 100)
            register_stat("Athletics", "athletics", 10, 0, 100)
            register_stat("Deviance", "deviance", 0, 0, 100)
            register_stat("Inhibition", "inhibition", 75, 100, 100)

# Ивенты
        this.Where({"OFFICE"},"dorothy")     .AddStep("dorothy_01", weight=50,                ready= lambda e: True )
        this.Where({"OFFICE"},"dorothy_menu")     .AddStep("dorothy_menu",                 done= lambda e: False  )


        this.AddEvent("dorothy_menu_01:Пункт1", ready= lambda e: True)
        this.AddEvent("dorothy_menu_02:Пункт2", ready= lambda e: True)

    call images_init
# Включить обработку перехода по меткам (label). 
    $onLabelExecute=lambda s: OnLabelExecute(s)





# Игра начинается здесь.
label start:
# Если поставть флаг, более вменяемые сообщения о некоторых ошибках при сохранении. На саму игру не влияет
    init python:
         config.use_cpickle = False


    # Ending class initialization
#    call Ending_constants
#    python:
#        global end
#    $ end = Ending ()

    # Создание elog должно стоять перед вызовами GetValue, так что лучше его сделать сразу после метки start
    call start_elog
    call after_load
    $event=" " # Инициализация

#    call part1
    call part2
    call part3
return





label dp_callback:

    $ display_stats()
#    $ display_extra_stats()
    return