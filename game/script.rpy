init python:
    for o in {"00:he", "01:edi", "02:sukk"}:
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
                        defVals={"pos": gMakePos( 0, 100 ), "pos2": gMakePos( 0, 430 )}, 
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

    call images_init

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

    "хело"

    show image "pics/background.png"

    $screens.ShowD3("editorial_office").Show("stats")

    $he("~01")
    "1"
    $he.Visibility("body")
    "2"
    $he("Привет!")
    "3"
    $edi.Visibility("body")
    $edi("~01// И тебе того же")
    "4"
    return
