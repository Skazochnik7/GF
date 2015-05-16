label images_init:

    transform chibitrans(x1=0, x2=0, y=0, lag=1.0): 
        xpos x1 #координата X, из которой начинаем движение
        ypos y #высота, на которой проводим движение
        linear lag xpos x2 # опреация передвижения (скорость линейна )


    image ctc3 = Animation("ctc00.png", 0.2, "ctc01.png", 0.2, "ctc02.png", 0.2, "ctc03.png", 0.2, "ctc04.png", 0.5, "ctc03.png", 0.2, "ctc02.png", 0.2, "ctc01.png", 0.2, xpos=0.97, ypos=0.929, xanchor=1.0, yanchor=1.0)


    screen editorial_office( aImgs="pics/editorial_office.jpg", x1=0, x2=0, y=0, lag=1.0 ):   
        zorder -22
        add aImgs at chibitrans(x1, x2, y, lag) #chibitrans(700, 200, 10.0) # Transform( pos = ( 500, 500 ) )  #at gSumPos( aPos, element.position )


    screen stats: #House points screen.
#        add "03_hp/11_misc/points_02.png" at Position(xpos=0, ypos=1)  
        hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
            spacing 10 xpos 846 ypos 11#отступ для текста, если надо прямо в левом углу — убираем его        
            text "{size=-5}12345{/size}" #сумма текстом

    return

screen letterbig(par1=letter_text):
#    add "pics/grad_blue.png"
    zorder 9
    add "pics/scroll_w_big.png" at Position(xpos=40, ypos=30)  
    hbox: 
        spacing 40 xpos 150 ypos 80 xmaximum 480#отступ для текста, если надо прямо в левом углу — убираем его        
        text par1

