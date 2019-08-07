init offset = -1

## Preferences screen ##########################################################

screen preferences():
    tag menu
    style_prefix "pre"
    use game_menu(_("Settings")):
        vbox:
            if renpy.variant("pc"):
                frame:
                    has hbox
                    label _("Display") at btn
                    if _preferences.fullscreen:
                        textbutton _("Window") action Preference("display", "window") at btn
                    else:
                        textbutton _("Window") action Preference("display", "any window") at btn
                    textbutton _("Fullscreen") action Preference("display", "fullscreen") at btn

            frame:
                has hbox
                label _("Rollback Side") at btn
                textbutton _("Disable") action Preference("rollback side", "disable") at btn
                textbutton _("Left") action Preference("rollback side", "left") at btn
                textbutton _("Right") action Preference("rollback side", "right") at btn

            frame:
                has hbox
                label _("Skip") at btn
                textbutton _("Unseen Text") action Preference("skip", "toggle") at btn
                textbutton _("After Choices") action Preference("after choices", "toggle") at btn
                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) at btn

            hbox:
                frame:
                    has fixed
                    bar value Preference("text speed") at btn
                    label _("Text Speed") at btn
                    
                frame:
                    has fixed
                    bar value Preference("auto-forward time") at btn
                    label _("Auto-Forward Time") at btn

            hbox:
                if config.has_music:
                    frame:
                        has fixed
                        bar value Preference("music volume") at btn
                        label _("Music Volume") at btn

                if config.has_sound:
                    frame:
                        has fixed
                        bar value Preference("sound volume") at btn
                        label _("Sound Volume") at btn
                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)

                if config.has_voice:
                    frame:
                        has fixed
                        bar value Preference("voice volume") at btn
                        label _("Voice Volume") at btn
                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)
                        

            if config.has_music or config.has_sound or config.has_voice:
                frame:
                    has hbox
                    textbutton _("Mute All"):
                        at btn
                        action Preference("all mute", "toggle")





style pre_slider:
    xysize(300,40)

style pre_fixed:
    fit_first True
style pre_label:
    background None