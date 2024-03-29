
import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

window = "mod4"
terminal = guess_terminal()
alt="mod1"
keys = [
    # Switch between windows
    Key([window], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([window], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([window], "k", lazy.layout.down(), desc="Move focus down"),
    Key([window], "i", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "tab", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([window, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([window, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([window, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([window, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([window, "control"], "j", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([window, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([window, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([window, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([window], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    
    Key(
        [window, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([window], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([window], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([window], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [window],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([window], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([window, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([alt, "control"], "delete", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([window], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([window], "o", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),),
    Key([window], "p", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),),
]

groups = [Group(i) for i in [
    "[]","[]","[]","[]","[]","[]"
]]

for i, group in enumerate(groups):
    numWS=str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([window], numWS, lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [window, "shift"],
                numWS,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([window, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
    def style():
        return {"margin":5, "border_focus":["#323759", "#272C4B"], "border_width":2}
layout_style = style() 
layouts = [
    layout.Max(),
    # layout.Columns(**layout_style),
    layout.MonadTall(**layout_style),
    # layout.Matrix(**layout_style),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
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
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
               
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
                 widget.GroupBox(
                    disable_drag=True,
                    highlight_method='line'
                ),
             #   widget.currentlayout.CurrentLayoutIcon(),
                
                widget.CPU(),
              
                widget.Memory(),

                widget.Net(),

                widget.Clock(format="%a %d/%m/%Y %I:%M %p"),
               
                widget.Systray(),
                
            ],
            24,
            background="#434465"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
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
floats_kept_above = True
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

wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home=os.path.expanduser("~")
    subprocess.Popen([home+'/.config/qtile/autostart.sh'])