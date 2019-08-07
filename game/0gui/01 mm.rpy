init -100:
    ## Hide on MM, Hide on Nav, Hide on mobile, Show while replay Text, Action
    define menuz = [
        [1,0,0,1,_("Return"),Return()],
        [0,1,0,1,_("Start"),Start()],
        [1,0,0,0,_("Save"),ShowMenu("save")],
        [0,0,0,1,_("Load"),ShowMenu("load")],
        [0,0,0,1,_("Settings"),ShowMenu("preferences")],
        [1,0,0,1,_("Main Menu"),MainMenu()],
        [0,0,1,1,_("Quit"),Quit(confirm=not main_menu)],
        ]

init offset = -1

## Navigation screen ###########################################################

screen navigation(ii=0):
    style_prefix "nav"
    
    frame:
        align(.5,1.0)
        hbox:
            for i in menuz:
                if (main_menu and i[0]) or (not main_menu and i[1]) or (not renpy.variant("pc") and i[2]):
                    pass
                else:
                    $ ii=ii+1
                    button:
                        at btn
                        text i[4]
                        action i[5]


## Main Menu screen ############################################################

screen main_menu(ii=0):
    style_prefix "mm"
    tag menu
#    add bgs[0]
    
    frame:
        align(.5,1.0)
        hbox:
            for i in menuz:
                if (main_menu and i[0]) or (not main_menu and i[1]) or (not renpy.variant("pc") and i[2]):
                    pass
                else:
                    $ ii=ii+1
                    button:
                        at btn
                        text i[4]
                        action i[5]


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