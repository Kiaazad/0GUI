init -100 python:
    class gui0_menu:
        def __init__(self, name, act, mm, nav, rep):
            self.name = name
            self.act = act
            self.mm = mm
            self.nav = nav
            self.rep = rep
    class gui0_menuz:
        def __init__(self):
            self.list = []
        def add(self, x):
            self.list.append(x)
init -99:
    define mmm = gui0_menuz()

init -98 python:
    try:
        mmm.add(
            gui0_menu(
                _("Return"),
                Return(),
                True, False, True
                ),
            )
        mmm.add(
            gui0_menu(
                _("Start"),
                Start(),
                False, True, True
                ),
            )
    except:
        pass

init -80 python:
    try:
        mmm.add(
            gui0_menu(
                _("Main Menu"),
                MainMenu(),
                True, False, True
                ),
            )
        mmm.add(
            gui0_menu(
                _("Quit"),
                Quit(confirm=not main_menu),
                False, False, True
                ),
            )
    except:
        pass

init offset = -1

## Navigation screen ###########################################################

screen navigation(m = mmm):
    style_prefix "nav"
    
    frame:
        align(.5,1.0)
        hbox:
            for i in m.list:
                if (main_menu and i.mm) or (not main_menu and i.nav) and i.rep:
                    pass
                else:
                    button:
                        at btn
                        text i.name
                        action i.act


## Main Menu screen ############################################################

screen main_menu(m = mmm):
    style_prefix "mm"
    tag menu
#    add bgs[0]
    
    frame:
        align(.5,1.0)
        hbox:
            for i in m.list:
                if (main_menu and i.mm) or (not main_menu and i.nav) and i.rep:
                    pass
                else:
                    button:
                        at btn
                        text i.name
                        action i.act


## Game Menu screen ############################################################

screen game_menu(title):
    style_prefix "gm"
    add bgs[1]
    transclude

    use navigation

    label title margin(40,40) align(1.0,0.0) at btn
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style gm_viewport:
    xfill True xalign .5