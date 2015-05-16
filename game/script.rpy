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

    $he.SayWindow(1)
    $skaz.SayWindow(0)
    $fri.SayWindow(2)
    $edi.SayWindow(2)

    $Say("Утро началось как обычно.")

    $he.Visibility("body")
    $he("~01// Так, сегодня светский раут, потом бесплатно постоловаться у --- за статью о его харчевне, ужин у --- . Хотя, наверное, к --- не пригласят. Придется идти к ---, еда дрянь, но зато бесплатно.")
#    $he("Привет!")

    $skaz("Когда самое трудное твое решение - выбор куда ты пойдешь на ужин - поневоле расслабляешься.")


    $fri.Visibility("body")
    $fri("~01// Эй, Юджин, привет! Как тебе новость?")
    $he("Что за новость?")
    $fri("Эй, парень, что с тобой? На тебя не похоже, ты ведь всегда держишь нос по ветру!// Вот, читай!")
    $fri.Visibility()


    call bigletter(["{size=-7}Новый конкурс!!!\n\n{/size}"
    "{size=-4}Рассказ о конкурсе{/size}\n\n ",
    "{size=-4}...Как вы знаете, в министерстве намечено очередное заседание по вопросам выделения фондов магическим учебным заведениям.\n\n "
    "Информируем вас, что если вами не будет достигнут достаточный прогресс, Дафна будет переведена в Дурмштанг - в академию, где умеют ценить настоящих чистокровных магов.\n\n "
    "Мы же в этом случае приложим все усилия, чтобы Хогвартс получил самое минимальное финансирование.{/size}\n\n "
    "{size=-3}Без особой надежды на ваш успех,\nОливия Гринграсс.{/size}"])



    $edi.Visibility("body")
    $edi("Привет! Уже ввели в тему, хорошшо")


#ГГ читает: «Ищите женщину!»
#Великий император повелел собрать лучших принцесс и героинь, чтобы найти среди них наилучшую. 
#Ред. Читаешь уже? Отлично, потому что ты туда и поедешь.


 

    $he("~01// #Так, посмотрим что там такое.")
    $Say("Интересно.")
    return
