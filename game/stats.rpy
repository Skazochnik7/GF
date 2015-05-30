init -100 python:



    __dse_stats = [ ]

    class __Stat(object):

        def __init__(self, name, var, min, default, max):
            self.name = name            # The public name showed on the UI
            self.var = var              # Variable used to modify
            self.min = min              # Min value
            self.default = default      # Default value
            self.max = max              # Max value

    def __init_stats():
        for s in __dse_stats:
            setattr(store, s.var, s.default)

    config.start_callbacks.append(__init_stats)

    # Are called to register all stats.
    def register_stat(name, var, min, default, max):
        __dse_stats.append(__Stat(name, var, min, default, max))

    # Sets the max value of stat (v) to value (m).
    def update_stat_max(v, m):
        for s in __dse_stats:
            if v == s.var:
                s.min = m

    # Returns the max value of stat (v).
    def get_stat_max(v):
        for s in __dse_stats:
            v = s.var
            return s.max

    # Sets the min value of stat (v) to value (m).
    def update_stat_min(v, m):
        for s in __dse_stats:
            if v == s.var:
                s.min = m

    # Returns the min value of stat (v).
    def get_stat_min(v):
        for s in __dse_stats:
            if v == s.var:
                return s.min


    def sort_stats(type='normal'):
        v = 0
        # Returns the name of the highest stat.
        if type == 'max':
            for s in __dse_stats:
                if v > eval(s.var):
                    v = eval(s.var)
            return s.var
        # Returns the name of the lowest stat.
        if type == 'min':
            for s in __dse_stats:
                if v < eval(s.var):
                    v = eval(s.var)
            return s.var

        if (morale and behavior and academics and artistery and athletics and deviance and (100 - inhibition) ) == 100:
            return "maxed"
        elif (morale and behavior and academics and artistery and athletics and (100 - inhibition) == deviance):
            return "equal"


    # Make sure that no stat is less then min or more then max.
    def normalize_stats():
        for s in __dse_stats:

            v = getattr(store, s.var)

            if v > s.max:
                v = s.max
            if v < s.min:
                v = s.min

            setattr(store, s.var, v)

    # Base stats
    def display_stats(name=True, bar=False, value=True, max=False):

        normalize_stats()

        ui.window(style=style.stats_frame)
        ui.vbox(style=style.stats_vbox)

        layout.label("Statisticseee:", "stats")
        layout.label("Statisticseee:", "stats")

#        ui.side(['l', 'r', 'c'], style=style.stat_side)
        ui.side(['l', 'r', 'c'], style=style.stat_side)
        layout.label("he=", "stats")
        layout.label("123", "stat_value")
        ui.close()        

        ui.close()



label update:
    $ update_stat_max('inhibition', 100)
    "Debug!"
    return