# Содержит код для планировщика задч

init -100 python:

    # Задать стиль рамки (фрейма)
    style.dp_frame = Style(style.frame)
    style.dp_vbox = Style(style.vbox)
    style.dp_hbox = Style(style.hbox)

    # Задать стиль вертикального бокса для вабора в каждом периоде
    style.dp_choices = Style(style.default)
    style.dp_choices_vbox = Style(style.vbox) 
    style.dp_choices.xalign = 0
    
    # Buttons.
    style.dp_choice_button = Style(style.button)
    style.dp_choice_button_text = Style(style.button_text)

    style.dp_done_button = Style(style.button)
    style.dp_done_button_text = Style(style.button_text)

    # Labels.
    style.dp_label = Style(style.label)
    style.dp_label_text = Style(style.label_text)

    # The title of the buttons.
    dp_done_title = "Завершить планирование"
    
    # A map from period name to the information we know about that period.
    __periods = { }

    # The period we're updating.
    __period = None
    
    class __Period(object):

        def __init__(self, name, var):
            self.name = name
            self.var = var
            self.acts = [ ]

    def dp_period(name, var):
        __periods[name] = store.__period = __Period(name, var)

    __None = object()
        
    def dp_choice(name, value=__None, enable="True", show="True"):

        if not __period:
            raise Exception("Choices must be part of a defined period.")

        if value is __None:
            value = name
        
        __period.acts.append((name, value, enable, show))

    def __set_noncurried(var, value):
        setattr(store, var, value)
        return True
        
    __set = renpy.curry(__set_noncurried)
        



label day_planner(periods):
    python hide:
        dp_period("Morning", "shed_morning")
        dp_choice("Office", "loc_office")

        dp_period("Afternoon", "shed_afternoon")
        dp_choice("Class", "loc_class",)
        
        dp_period("Evening", "shed_evening")
        dp_choice("School grounds", "loc_school_grounds")      

        renpy.choice_for_skipping()
    
label day_planner_repeat:

    if renpy.has_label("dp_callback"):
        call dp_callback

    python hide:
    
        ui.window(style=style.dp_frame)
        ui.vbox(style=style.dp_vbox)
        ui.hbox(style=style.dp_hbox)

        can_continue = True

        for p in periods:

            if p not in __periods:
                raise Exception("Period %r was never defined." % p)

            ui.window(style=style.dp_choices)
            ui.vbox(style=style.dp_choices_vbox)
            
            p = __periods[p]
            v = getattr(store, p.var)

            layout.label(p.name, "dp")

            valid_choice = False
            
            for name, value, enable, show in p.acts:
                show = eval(show)
                enable = eval(enable)

                selected = (v == value)
                
                if show:
                    layout.button(name, "dp_choice", clicked=__set(p.var, value), selected=selected, enabled=enable,)

                if show and enable and selected:
                    valid_choice = True

            if not valid_choice:
                can_continue = False
            
            ui.close()
                    
        ui.close() # hbox.
        

        layout.button(
            dp_done_title,
            "dp_done",
            clicked=ui.returns(False),
            enabled=can_continue)
        
        ui.close() # vbox

        layout.button("Вещи", clicked=ShowMenu('items'),yoffset=5,xoffset=4, xminimum=170)
        layout.button("Мери", clicked=ShowMenu('meri'),yoffset=36,xoffset=5,xminimum=170)
        
        
        ## Removed until added functionality or merged with phone.
#        if(new_messages > 0):
#            layout.button("Notifications ({color=[notification_color]}[new_messages]{/color})", clicked=ShowMenu('mailbox'),xoffset=815,yoffset=4,xminimum=200)
#        else:
#            layout.button("Notifications ([new_messages])", clicked=ShowMenu('mailbox'),xoffset=815,yoffset=4,xminimum=200)

    if ui.interact():
        jump day_planner_repeat
    else:
        return

