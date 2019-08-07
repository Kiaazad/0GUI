init offset = -1
define config.thumbnail_width = 384
define config.thumbnail_height = 216
## Load and Save screens #######################################################

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))
    
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    style_prefix "sav"
    use game_menu(title):
        vbox:
            grid 3 2:
                for i in range(6):
                    $ slot = i + 1
                    button:
                        at btn
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot)
                        text FileTime(slot, format=_("{#file_time}%a, %H:%M - %b %d  %Y, "), empty=_("empty slot")) text_align .5
                        if FileSaveName(slot):
                            text FileSaveName(slot)
                        key "save_delete" action FileDelete(slot)

            hbox:
                textbutton _("<") action FilePagePrevious() at btn
                button:
                    at btn
                    key_events True
                    action page_name_value.Toggle()
                    input:
                        value page_name_value
                textbutton _(">") action FilePageNext() at btn
