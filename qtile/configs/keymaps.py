from libqtile.config import Key
from libqtile.lazy import lazy
from .flags import config_path
from .theme import theme
Super = "mod4"
alt = "mod1"
vim_mode = {"on":["l", "h", "j", "k"], "off":["right", "left", "down", "up"]}
theme_config = theme()
keys=[Key(key[0],key[1],*key[2:]) for key in [
    # Navegacion entre ventanas
    ([Super], vim_mode["off"][0], lazy.layout.right()),
    ([Super], vim_mode["off"][1], lazy.layout.left()),
    ([Super], vim_mode["off"][2], lazy.layout.down()),
    ([Super], vim_mode["off"][3], lazy.layout.up()),
    # Intercambio de ventanas
    ([Super, "shift"], vim_mode["off"][0], lazy.layout.shuffle_right()),
    ([Super, "shift"], vim_mode["off"][1], lazy.layout.shuffle_left()),
    ([Super, "shift"], vim_mode["off"][2], lazy.layout.shuffle_down()),
    ([Super, "shift"], vim_mode["off"][3], lazy.layout.shuffle_up()),
    # Tamaño de ventanas
    ([Super, "control"], vim_mode["off"][0], lazy.layout.grow_right()),
    ([Super, "control"], vim_mode["off"][1], lazy.layout.grow_left()),
    ([Super, "control"], vim_mode["off"][2], lazy.layout.grow_down()),
    ([Super, "control"], vim_mode["off"][3], lazy.layout.grow_up()),
    # Manejo de ventanas
    ([alt], "F4", lazy.window.kill()), #cerrar
    ([alt], "q", lazy.window.kill()), #cerrar
    ([alt], "tab", lazy.layout.next()), #cambio de foco   
    ([alt, "shift"], "tab", lazy.layout.prev()), #cambio de foco
    ([Super, "control"], "r", lazy.reload_config()),
    ([Super], "tab", lazy.next_layout()), #cambio de distribucion
    ([Super,"shift"], "tab", lazy.prev_layout()),#cambio de distribucion
    #menus
    ([Super], "r", lazy.spawn("sh " +config_path + "/dmenu/apps.sh '"                   + theme_config["color_13"][0]+"' '" + theme_config["color_24"][0]+"' '"+ theme_config["color_40"][0] +"' '"+ theme_config["color_43"][0] +"'")),
    ([Super], "p", lazy.spawn("sh " +config_path + "/dmenu/monitor-manager.sh '"        + theme_config["color_13"][0]+"' '" + theme_config["color_24"][0]+"' '"+ theme_config["color_40"][0] +"' '"+ theme_config["color_43"][0] +"'")),
    ([alt, "control"], "delete", lazy.spawn("sh " +config_path + "/dmenu/logout.sh '"   + theme_config["color_13"][0]+"' '" + theme_config["color_24"][0]+"' '"+ theme_config["color_40"][0] +"' '"+ theme_config["color_43"][0] +"' qtile")),
    ([Super], "Print", lazy.spawn("sh " +config_path + "dmenu/screenshoter.sh '"        + theme_config["color_13"][0]+"' '" + theme_config["color_24"][0]+"' '"+ theme_config["color_40"][0] +"' '"+ theme_config["color_43"][0] +"'")),
    ([], "Print", lazy.spawn("sh " +config_path + "/dmenu/screenshoter.sh '"            + theme_config["color_13"][0]+"' '" + theme_config["color_24"][0]+"' '"+ theme_config["color_40"][0] +"' '"+ theme_config["color_43"][0] +"'")),
    #aplicaciones 
    ([Super], "b", lazy.spawn("brave")),
    ([Super], "c", lazy.spawn("code")),
    ([Super], "e", lazy.spawn("thunar")),
    ([Super], "Return", lazy.spawn("kitty")),
    #control de volumen de audio
    ([], "XF86AudioRaiseVolume", lazy.spawn("sh "+config_path+"/volctl.sh +"),),
    ([], "XF86AudioLowerVolume", lazy.spawn("sh "+config_path+"/volctl.sh -"),),
    ([], "XF86AudioMute", lazy.spawn("sh "+config_path+"/volctl.sh +-"),),
    #control de brillo
    ([], "XF86MonBrightnessUp", lazy.spawn("sh "+config_path+"/brictl.sh +"),),
    ([], "XF86MonBrightnessDown", lazy.spawn("sh "+config_path+"/brictl.sh -"),),
    #control de audio
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"),),
    ([], "XF86AudioPause", lazy.spawn("playerctl play-pause"),),
    ([], "XF86AudioNext", lazy.spawn("playerctl next"),),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous"),),

    ([Super], "i", lazy.spawn("playerctl play-pause"),),
    ([Super], "o", lazy.spawn("playerctl next"),),
    ([Super], "u", lazy.spawn("playerctl previous"),),
]]