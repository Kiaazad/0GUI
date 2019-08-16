init offset = -1
init python:
    class gui0: # this class needs lots of optimization but it works for now
        def __init__(self, texts, frames, accent, f_accent, boarders, t_alp, f_alp):
            self.texts = color(texts)
            if frames[0] == "#":
                self.frames = color(frames)
            else:
                self.frames = frames
            self.accent = accent
            self.f_accent = f_accent
            
            self.boarders = boarders
            self.t_alp = t_alp
            self.f_alp = f_alp
            self.txt()
            self.frm()
        ### Text
        def txt(self):
            self.t_ins = self.texts.opacity(self.t_alp[0])
            self.t_idl = self.texts.opacity(self.t_alp[1])
            self.t_hov = self.texts.opacity(self.t_alp[2]).interpolate_hsv(self.accent, 1)
            
            self.t_slc_ins = self.texts.opacity(self.t_alp[0]).interpolate_hsv(self.accent, .21)
            self.t_slc_idl = self.texts.opacity(self.t_alp[1]).interpolate_hsv(self.accent, .5)
            self.t_slc_hov = self.texts.opacity(self.t_alp[2]).interpolate_hsv(self.accent, 1)
        ### Frames
        def frm(self):
            if type(self.frames) == Color:
                self.f_ins = self.frames.opacity(self.f_alp[0])
                self.f_idl = self.frames.opacity(self.f_alp[1])
                self.f_hov = self.frames.opacity(self.f_alp[2]).rotate_hue(self.f_accent)
                
                self.f_slc_ins = self.frames.opacity(self.f_alp[0]).rotate_hue(self.f_accent)
                self.f_slc_idl = self.frames.opacity(self.f_alp[1]).rotate_hue(self.f_accent)
                self.f_slc_hov = self.frames.opacity(self.f_alp[2]).rotate_hue(self.f_accent)
            else:
                self.f_ins = Frame(im.MatrixColor(self.frames,im.matrix.desaturate()), self.boarders[0], self.boarders[1])
                self.f_idl = Frame(self.frames, self.boarders[0], self.boarders[1])
                self.f_hov = Frame(im.MatrixColor(self.frames,im.matrix.hue(120)), self.boarders[0], self.boarders[1])

                self.f_slc_ins = Frame(im.MatrixColor(self.frames,im.matrix.desaturate()), self.boarders[0], self.boarders[1])
                self.f_slc_idl = Frame(im.MatrixColor(self.frames,im.matrix.hue(240)), self.boarders[0], self.boarders[1])
                self.f_slc_hov = Frame(im.MatrixColor(self.frames,im.matrix.hue(240)), self.boarders[0], self.boarders[1])
            
            ### Bars
            if type(self.frames) == Color:
                self.r_bar = self.frames.opacity(self.f_alp[1])
                self.l_bar = self.frames.opacity(self.f_alp[2])
                self.r_bar_hov = self.frames.opacity(self.f_alp[1]).rotate_hue(self.f_accent)
                self.l_bar_hov = self.frames.opacity(self.f_alp[2]).rotate_hue(self.f_accent)
            else:
                self.r_bar = Frame(im.MatrixColor(self.frames,im.matrix.desaturate()), self.boarders[0], self.boarders[1])
                self.l_bar = Frame(self.frames, self.boarders[0], self.boarders[1])
                self.r_bar_hov = Frame(im.MatrixColor(self.frames,im.matrix.desaturate()), self.boarders[0], self.boarders[1])
                self.l_bar_hov = Frame(im.MatrixColor(self.frames,im.matrix.hue(120)), self.boarders[0], self.boarders[1])

### Change these ###############################################################

define thm = gui0(
    "#fff", # text color
    "0GUI/frame/001.png", # frame color or image
    "#fd0", # accent color
    .33, # frame accent color offset
    (16, 16), # frame boarders size
    [.2, 1, 1], # text alpha [insensitive, idle, hover] from 0 to 1
    [.2, .7, 1], # frame alpha [insensitive, idle, hover] from 0 to 1
    )
define bgs = [
    "#444", # Main menu background
    "#000d", # Screens background
    "#000d", # Dimmed overlay
    ]

transform btn:
    parallel:
        xoffset renpy.random.randint(-1000, 1000) alpha 0 xzoom .01
        pause renpy.random.random()/4
        
        ease .2 xoffset 0 xzoom 1 alpha 1
    parallel:
        on idle:
            easein .2 additive 0
        on hover:
            easein .2 additive .3
        on selected_idle:
            easein .2 additive .2
        on selected_hover:
            easein .2 additive .3
        on insensitive:
            easein .2 additive 0

### Styles #####################################################################

style default:
    align(.5,.5)
    padding(20,20)
    spacing 10
    # font ""
    # size 30
    
    color thm.t_idl
    hover_color thm.t_hov
    selected_color thm.t_slc_idl
    selected_hover_color thm.t_slc_hov

    background thm.f_idl
    hover_background thm.f_hov
    selected_background thm.f_slc_idl
    selected_hover_background thm.f_slc_hov

    # hover_sound "0gui/sfx/hover.mp3"
    # activate_sound "0gui/sfx/select.mp3"

    left_bar thm.l_bar
    right_bar thm.r_bar
    hover_left_bar thm.l_bar_hov
    hover_right_bar thm.r_bar_hov


