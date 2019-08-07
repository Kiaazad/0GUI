init offset = -1

## Say screen ##################################################################

screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        ysize 250 yalign 1.0 xfill True

        if who is not None:
            window:
                align(0.2,0.0)
                id "namebox"
                text who id "who"
        label what id "what" xsize 900 background None text_size 30

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

init python:
    config.character_id_prefixes.append('namebox')

## Choice screen ###############################################################
define menu_shuffle = 0
define menu_shuffle_keeper = 1
screen choice(items):
    style_prefix "cho"
    
    if menu_shuffle: # needs work
        on "hide" action SetVariable("menu_shuffle_keeper", 1) 
        if menu_shuffle_keeper:
            timer .001 action SetVariable("menu_shuffle_keeper", 0)
            $ renpy.random.shuffle(items)

    vbox:
        for i in items:
            textbutton i.caption action i.action xsize 1000 at btn

define config.narrator_menu = True

## Input screen ################################################################

screen input(prompt):
    style_prefix "inp"
    window:
        vbox:
            text prompt
            frame:
                xsize 400
                input id "input"

## Quick Menu screen ###########################################################

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "q"
            yalign 1.0
            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style q_button_text:
    size 16
style q_button:
    padding(8,4)

## NVL screen ##################################################################

screen nvl(dialogue, items=None):
    add "#0008"
    vbox:
        spacing 10
        for d in dialogue:
            window:
                background None
                id d.window_id
                hbox:
                    if d.who is not None:
                        text d.who:
                            id d.who_id

                    text d.what:
                        id d.what_id

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

define config.nvl_list_length = 7