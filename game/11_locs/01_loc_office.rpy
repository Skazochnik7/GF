label loc_office:
    "В ОФИСЕ, текст в зависимости от параметров"
    $ this.RunStep("OFFICE") # Если 

    # if event.duration!=0: №Если ивент такого рода, что дальше не нужно обрабатывать (например, по ходу девушка убежала), то выйти
#        return

return    

label dorothy_01:
    $say("",event.Name+" Я В ОБЫЧНОМ ИВЕНТЕ!!!!!!!!!!!!")
return event.Finalize()

label dorothy_menu:
    $say("",event.Name+" Я В МЕНЮ!")
    # Строим ранменю из группы ивентов 
    #
    $ choose = RunMenu()
    python:
        for e in this.List:
            debug.SaveString(str(e.Name))
            if "dorothy_menu_" in e.Name: 
                debug.SaveString(str(e.IsActive()))
                if e.IsActive():
                    choose.AddItem(e._caption, e.Name, e.Name)
    $ choose.Show()


return event.Finalize()