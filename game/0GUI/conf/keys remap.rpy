

init python:
    config.keymap['screenshot'] = [ 'o', 'alt_K_s', 'alt_shift_K_s' ]
    config.keymap['toggle_fullscreen'] = [ 'alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11' ]
    config.keymap['developer'] = [ 'K_F9', 'alt_shift_K_d' ]
    config.keymap['director'] = ['K_F8']
    config.keymap['reload_game'] = [ 'K_F5', 'alt_shift_K_r' ]
    
    
    config.keymap['focus_left'].append('a')
    config.keymap['focus_right'].append('d')
    config.keymap['focus_up'].append('w')
    config.keymap['focus_down'].append('s')
    
    config.keymap['bar_left'].append('a')
    config.keymap['bar_right'].append('d')
    config.keymap['bar_up'].append('w')
    config.keymap['bar_down'].append('s')
    
    config.keymap['bar_activate'].append('e')
    config.keymap['bar_deactivate'].append('e')
    
    config.keymap['button_select'].append('e')