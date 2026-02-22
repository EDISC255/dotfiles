import subprocess
from os import path
import json
import random
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


home_path=path.expanduser("~")
config_path=path.join(home_path, ".config")
qtile_config_path=path.join(config_path, "qtile")
autostart_path=path.join(qtile_config_path, "autostart.sh")

browser="brave"
code_editor="code"
graphic_file_manager="thunar"
terminal = "kitty"
terminal_file_manager="kitty ranger"


Super = "mod4"
alt = "mod1"
enter = "Return"
theme_path=path.join(qtile_config_path, "theme.json")

with open(theme_path,"r",encoding="utf-8") as theme_file:
    theme_config=json.load(theme_file)
#index=str(random.randint(1, 43))
keys = [
    # vim mode
    # navegación entre ventanas
    Key([Super], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([Super], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([Super], "j", lazy.layout.down(), desc="Move focus down"),
    Key([Super], "k", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(), desc="Move Super focus to other Super"),
    # mover las ventanas
    Key([Super, "shift"], "h", lazy.layout.shuffle_left(), desc="Move Super to the left"),
    Key([Super, "shift"], "l", lazy.layout.shuffle_right(), desc="Move Super to the right"),
    Key([Super, "shift"], "j", lazy.layout.shuffle_down(), desc="Move Super down"),
    Key([Super, "shift"], "k", lazy.layout.shuffle_up(), desc="Move Super up"),
    # control de tamaño de ventanas
    Key([Super, "control"], "h", lazy.layout.grow_left(), desc="Grow Super to the left"),
    Key([Super, "control"], "l", lazy.layout.grow_right(), desc="Grow Super to the right"),
    Key([Super, "control"], "j", lazy.layout.grow_down(), desc="Grow Super down"),
    Key([Super, "control"], "k", lazy.layout.grow_up(), desc="Grow Super up"),
    Key([Super], "n", lazy.layout.normalize(), desc="Reset all Super sizes"),
    
    # arrow mode
    # navegación entre ventanas
    Key([Super], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([Super], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([Super], "down", lazy.layout.down(), desc="Move focus down"),
    Key([Super], "up", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(), desc="Move Super focus to other Super"),
    # mover las ventanas
    Key([Super, "shift"], "left", lazy.layout.shuffle_left(), desc="Move Super to the left"),
    Key([Super, "shift"], "right", lazy.layout.shuffle_right(), desc="Move Super to the right"),
    Key([Super, "shift"], "down", lazy.layout.shuffle_down(), desc="Move Super down"),
    Key([Super, "shift"], "up", lazy.layout.shuffle_up(), desc="Move Super up"),
    # control de tamaño de ventanas
    Key([Super, "control"], "left", lazy.layout.grow_left(), desc="Grow Super to the left"),
    Key([Super, "control"], "right", lazy.layout.grow_right(), desc="Grow Super to the right"),
    Key([Super, "control"], "down", lazy.layout.grow_down(), desc="Grow Super down"),
    Key([Super, "control"], "up", lazy.layout.grow_up(), desc="Grow Super up"),
    
    Key([Super, "control"], "t", lazy.window.toggle_floating(), desc="Grow Super up"),
    Key([Super, "control"], "f", lazy.window.toggle_fullscreen(), desc="Grow Super up"),
    Key([Super], "n", lazy.layout.normalize(), desc="Reset all Super sizes"),

    Key(
        [Super, "shift"],
        enter,
       lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # QTILE WM
    Key([Super], enter, lazy.spawn(terminal), desc="Launch terminal"),
    Key([alt], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([alt], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([Super, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([Super], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([Super,"shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([Super], "end", lazy.next_layout(), desc="Toggle between layouts"),
    Key([Super], "home", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([alt, "control"], "delete", lazy.spawn("bash /home/eduardo/.config/qtile/scripts/logout.sh"), desc="Shutdown Qtile"),

    #aplicaciones
    Key([Super], "r", lazy.spawn("bash /home/eduardo/.config/qtile/scripts/apps.sh"),),
    Key([Super], "b", lazy.spawn(browser),),
    Key([Super], "c", lazy.spawn(code_editor),),
    Key([Super], "e", lazy.spawn(graphic_file_manager), ),

    #controles
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),),
    Key([Super], "Print", lazy.spawn("bash /home/eduardo/.config/qtile/scripts/screenshoter.sh"),),
    Key([], "Print", lazy.spawn("scrot -s"),),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("bash /home/eduardo/.config/qtile/scripts/volctl.sh +"),),
    Key([], "XF86AudioLowerVolume", lazy.spawn("bash /home/eduardo/.config/qtile/scripts/volctl.sh -"),),
    #Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+"),),
    #Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"),),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"),),
    Key([], "XF86AudioPause", lazy.spawn("playerctl play-pause"),),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"),),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"),),
]
# listado de iconos
# 1.- nf-md-arch
# 2.- nf-oct-terminal
# 3.- nf-cod-code
# 4.- nf-fa-code
# 4.- nf-fa-firefox
# 5.- nf-fa-music
groups = [Group(i) for i in [
    "[]","[]","[]","[]","[]",
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

widget_defaults = dict(
    font="Hack Nerd Font Mono",
    fontsize=10,
    padding=0,
)

extension_defaults = widget_defaults.copy()

#nf-cod-triangle_left
powerline={"text":"","fontsize":40,"padding":-5.5}

powerline_end={"text":"","fontsize":40,"padding":-5.5}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    inactive=theme_config["color_14"],
                    disable_drag=True,
                    active=theme_config["color_40"],
                    fontsize=12,
                    highlight_method='text',
                    this_current_screen_border=theme_config["color_17"],
                    background=theme_config["color_2"]
                #foreground=theme_config["color_"+str(index[5])],
                ),
                
                widget.Prompt(
                    foreground = theme_config["color_1"],
                    background = theme_config["color_10"] ,
                    ignore_dump_history =True,
                    record_history=False
                ),
                
                widget.WindowName(
                    foreground=theme_config["color_16"]
                ),
                
                widget.Chord(
                    chords_colors={
                        "launch": ("#9c9c9c", "#9c9c9c"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.TextBox(**powerline, foreground=theme_config["color_23"],), 
                widget.CPU(
                    background=theme_config["color_23"],
                    foreground=theme_config["color_43"],
                ),

                widget.TextBox(**powerline,foreground=theme_config["color_6"]),
                widget.Memory(
                    background=theme_config["color_6"],
                    foreground=theme_config["color_36"],
                ),
                
                widget.TextBox(
                    **powerline, foreground=theme_config["color_28"],
                ),
                widget.Clock(
                    format="%a %d/%m/%Y %I:%M %p",
                    background=theme_config["color_28"],
                    foreground=theme_config["color_13"],
                ),
                widget.TextBox(
                    **powerline, foreground=theme_config["color_17"],
                ),
                
                widget.CurrentLayout(
                    mode='both', icon_first=True,
                    background=theme_config["color_17"],
                    foreground=theme_config["color_25"],
                ),
                
                widget.TextBox(
                    **powerline,foreground=theme_config["color_1"],
                ),
                widget.Systray(
                    background = theme_config["color_1"],
                ),
                widget.TextBox(**powerline_end,
                               foreground=theme_config["color_13"]),
                widget.TextBox("Theme: "+theme_config["theme"], 
                               foreground=theme_config["color_13"])
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ],
            20,
            background = theme_config["color_24"]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        ),
    ),
]

# Drag floating layouts.
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
