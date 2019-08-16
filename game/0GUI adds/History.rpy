init -83 python:
    try:
        mmm.add(
            gui0_menu(
                _("History"),
                ShowMenu("history"),
                True, False, True
                ),
            )
    except:
        pass

init offset = -1

screen history():
    tag menu
    predict False
    use game_menu(_("History")):
        style_prefix "his"
        if not _history_list:
            label _("The dialogue history is empty.")
        else:
            viewport:
                xysize(1000,800)
                draggable True
                yinitial 1.0
                frame:
                    xfill True
                    has vbox
                    for h in _history_list:
                        hbox:
                            if h.who:
                                label h.who:
                                    if "color" in h.who_args:
                                        text_color h.who_args["color"]

                            $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                            text what



define gui.history_allow_tags = set()
