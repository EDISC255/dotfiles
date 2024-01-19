import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

window = "mod4"
terminal = "alacritty"
alt="mod1"
enter="Return"

keys = [
    # navegacion entre ventanas
    Key([window], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([window], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([window], "down", lazy.layout.down(), desc="Move focus down"),
    Key([window], "up", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "tab", lazy.layout.next(), desc="Move window focus to other window"),
    # mover las ventanas
    Key([window, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([window, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([window, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([window, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    # control de tamaño de ventanas
    Key([window, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([window, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([window, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([window, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([window], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [window, "shift"],
        enter,
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # programas
    Key([window], enter, lazy.spawn(terminal), desc="Launch terminal"),
    Key([window], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([alt], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([window, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([alt, "control"], "delete", lazy.shutdown(), desc="Shutdown Qtile"),
# lazy.shutdown()    
    Key([window], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([window], "p", lazy.spawn("arandr"),),
    Key([window], "b", lazy.spawn("firefox"),),
    Key([window], "c", lazy.spawn("code"),),
    Key([window], "e", lazy.spawn("thunar"),),
    #controles

    #Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),),
    #Key([], "XF86AudioRiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),),
    #Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),),
    #Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+"),),
    #Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"),),
]
# listado de iconos
# 2.- nf-oct-terminal
groups = [Group(i) for i in [
    "[]","[]","[]","[]","[]","[]",
]]

for i, group in enumerate(groups):
    numWS = str(i+1)
    keys.extend([
            Key([window], numWS, lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([window, "shift"], numWS, lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Max(),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
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

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.currentlayout.CurrentLayoutIcon(),
                widget.GroupBox(
                    active='#ffffff',
                    disable_drag=True,
                    fontsize=17,
                    highlight_method='line'
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.CPU(
                    background='#383838'
                ),
                widget.Memory(
                    background='#383838'
                ),
                widget.Battery(
                    background='#383838'
                ),
                widget.BatteryIcon(
                    background='#383838'
                ),
                widget.PulseVolume(
                    background='#383838'
                ),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background='#383838',
                ),
                
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ],
            22,
            background="#1f1f1f"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        ),
        wallpaper = '~/.config/qtile/wallpaper.png',
        wallpaper_mode='stretch',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([window], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([window], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([window], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
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

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
