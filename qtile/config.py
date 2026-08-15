import subprocess
from os import path
import json
from libqtile import hook
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


home_path=path.expanduser("~")
config_path=path.join(home_path, ".config")
qtile_config_path=path.join(config_path, "qtile")
autostart_path=path.join(qtile_config_path, "autostart.sh")

Super = "mod4"
alt = "mod1"
theme_path=path.join(qtile_config_path, "theme.json")

vim_mode = {"on":["l", "h", "j", "k"], "off":["right", "left", "down", "up"]}

with open(theme_path,"r",encoding="utf-8") as theme_file:
    theme_config=json.load(theme_file)

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
# espacios de trabajo
# listado de iconos
# 1.- nf-md-arch
# 2.- nf-oct-terminal
# 3.- nf-cod-code
# 3.- nf-fa-code
# 4.- nf-fa-firefox
# 5.- nf-fa-music
groups = [Group(i) for i in [
    "[]","[]","[]","[]","[]",
]]

for i, group in enumerate(groups):
    numWS = str(i+1)
    keys.extend([
            Key([Super], numWS, lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key([Super, "shift"], numWS, lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
        ]
    )
#distribuciones de ventanas

layout_style={"margin": 3,"border_normal":theme_config["color_29"],"border_focus": theme_config["color_17"], "border_width": 2}

layouts = [
   layout.Columns(**layout_style),
   layout.MonadTall(**layout_style),
   layout.Max(**layout_style),
    #layout.Tile(**layout_style),
    #layout.Bsp(**layout_style),
    #layout.Matrix(**layout_style),
    #layout.Stack(num_stacks=2),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#barra de estado
widget_defaults = dict(
    font="Hack Nerd Font Mono",
    fontsize=10,
    padding=0,
)

extension_defaults = widget_defaults.copy()

powerline_spawn={"text":"","fontsize":40,"padding":-5.5}
powerline={"text":"","fontsize":40,"padding":-5.5}

#nf-fa-memory
#nf-md-swap_horizontal_circle
#nf-md-cpu_64_bit
#nf-fa-thermometer

Memoria=[
    widget.TextBox(**powerline, foreground=theme_config["color_8"]),
    widget.TextBox(text="",fontsize=25,padding=1, foreground=theme_config["color_8"]),
    widget.Memory(format='{MemUsed:.0f}{mm}',update_interval=2.0, foreground=theme_config["color_8"]), 
    
    widget.TextBox(**powerline, foreground=theme_config["color_9"]),
    widget.TextBox(text="󰿡",fontsize=25,padding=1, foreground=theme_config["color_9"]),
    widget.Memory(format='{SwapUsed:.0f}{ms}',update_interval=2.0, foreground=theme_config["color_9"])]

Cpu=[
    widget.TextBox(**powerline, foreground=theme_config["color_23"]),
    widget.TextBox(text="󰻠",fontsize=25,padding=1, foreground=theme_config["color_23"]),
    widget.CPU(foreground=theme_config["color_23"], format="{freq_current}GHz {load_percent}%"),

    widget.TextBox(**powerline, foreground=theme_config["color_5"]),
    widget.TextBox(text="",fontsize=20,padding=1, foreground=theme_config["color_5"]),
    widget.ThermalSensor(foreground=theme_config["color_5"]),]

FechaHora=[
    widget.TextBox(**powerline, foreground=theme_config["color_3"],),
    widget.TextBox(text="",fontsize=25,padding=1, foreground=theme_config["color_3"],mouse_callbacks={"Button1": lazy.spawn("sh " +config_path + "/dmenu/calendar.sh '"                   + theme_config["color_13"][0]+"' '" + theme_config["color_24"][0]+"' '"+ theme_config["color_40"][0] +"' '"+ theme_config["color_43"][0] +"'")}),
    widget.Clock(format="%a %d/%m/%Y",  foreground=theme_config["color_3"],),
    
    widget.TextBox(**powerline, foreground=theme_config["color_32"],),
    widget.TextBox(text="󰥔",fontsize=25,padding=1, foreground=theme_config["color_32"]),
    widget.Clock(format="%I:%M %p",foreground=theme_config["color_32"],),]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    inactive=theme_config["color_14"],
                    disable_drag=True,
                    active=theme_config["color_40"],
                    fontsize=12,
                    highlight_method="text",
                    this_current_screen_border=theme_config["color_17"],
                ),
                widget.Prompt(
                    foreground = theme_config["color_43"],
                    background = theme_config["color_10"] ,
                    ignore_dump_history =True,
                    record_history=False
                ),

                widget.TextBox(**powerline_spawn, foreground=theme_config["color_14"],),                 
                widget.WindowName(
                    foreground=theme_config["color_16"]
                ),
  
                widget.Chord(
                    chords_colors={
                        "launch": ("#9c9c9c", "#9c9c9c"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.TextBox(**powerline, foreground=theme_config["color_11"]),
                widget.WidgetBox(widgets=Memoria, text_closed="RAM", text_open="[X]",foreground=theme_config["color_11"]),

                widget.TextBox(**powerline, foreground=theme_config["color_18"]),
                widget.WidgetBox(widgets=Cpu, text_closed="CP0", text_open="[X]", foreground=theme_config["color_18"]),

                widget.TextBox(**powerline, foreground=theme_config["color_21"]),
                widget.WidgetBox(widgets=FechaHora, text_closed="FECHA", text_open="[X]", foreground=theme_config["color_21"]),

                widget.TextBox(**powerline, foreground=theme_config["color_17"],),
                widget.CurrentLayout(
                    mode='both', icon_first=True,
                    foreground=theme_config["color_17"],
                ),

                widget.TextBox(**powerline, foreground=theme_config["color_10"],),
                widget.Battery(foreground=theme_config["color_10"], 
                            discharge_char="󱟥", 
                            charge_char="󰂏",
                            format='{char} {percent:2.0%}'),
                
                widget.TextBox(
                    **powerline,foreground=theme_config["color_1"],
                ),
                
                widget.Systray(),
                
                widget.TextBox(**powerline,
                               foreground=theme_config["color_13"]),
                widget.TextBox("Theme: "+theme_config["theme"],
                               foreground=theme_config["color_13"]),

#                widget.TextBox("sh " +config_path + "/dmenu/logout.sh '"+ theme_config["color_13"][0]+"' '" + theme_config["color_24"][0]+"' '"+ theme_config["color_40"][0] +"' '"+ theme_config["color_24"][0] +"'")
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ],
            20,
            background = theme_config["color_24"]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        ),
    ),
]

#modo flotante
mouse = [
    Drag([Super], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([Super], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([Super], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "qtile"

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(autostart_path)