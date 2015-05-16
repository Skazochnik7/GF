label bigletter(__pages): #Вывод скроллов с использованием меню
    $__pageIndex=0
    label letterbig_newpage:
    $screens.Show("letterbig", par1=__pages[__pageIndex])    
#    $screens.Show("ctc", d3, "bld1").Pause()

    python:
        choose = RunMenu(0.5, 0.9)
        if __pageIndex>0:
            choose.AddItem("<<< Вернуться ", None, str(-1))
        if __pageIndex<len(__pages)-1:
            choose.AddItem(" Продолжить >>>", None, str(1)) 
        choose.Show()
    if choose.choice!="":
        $__pageIndex+=int(choose.choice)
        jump letterbig_newpage

    $screens.Hide("letterbig") #, "ctc", d3, "bld1")
    return





label daphne_pre_04: #Письмо родителей Дафны Дамблдору
    call bigletter(["{size=-7}Новый конкурс!!!\n\n{/size}"
    "{size=-4}Рассказ о конкурсе{/size}\n\n ",
    "{size=-4}...Как вы знаете, в министерстве намечено очередное заседание по вопросам выделения фондов магическим учебным заведениям.\n\n "
    "Информируем вас, что если вами не будет достигнут достаточный прогресс, Дафна будет переведена в Дурмштанг - в академию, где умеют ценить настоящих чистокровных магов.\n\n "
    "Мы же в этом случае приложим все усилия, чтобы Хогвартс получил самое минимальное финансирование.{/size}\n\n "
    "{size=-3}Без особой надежды на ваш успех,\nОливия Гринграсс.{/size}"])

#    $event.Finalize()

#    call screen main_menu_01
