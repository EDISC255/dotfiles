from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from .theme import theme
from .flags import nombres, config_path
from .widgets import wsps, widgetbox
theme_config = theme()
#barra de estado
widget_defaults = dict(
    font="Hack Nerd Font Mono",
    fontsize=10,
    padding=0,
)
def status_bar(widgets):
    return bar.Bar(widgets, 20, background = theme_config["color_24"])
# screens =[Screen(top=status_bar(widgets))] 
extension_defaults = widget_defaults.copy()

powerline_spawn={"text":"","fontsize":40,"padding":-5.5}
powerline={"text":"","fontsize":40,"padding":-5.5}

#nf-fa-memory
#nf-md-swap_horizontal_circle
#nf-md-cpu_64_bit
#nf-fa-thermometer
Red=[
    widget.TextBox(**powerline, foreground=theme_config["color_1"]),
    widget.TextBox(text="",fontsize=25,padding=1, foreground=theme_config["color_1"],),
    widget.Net(foreground= theme_config["color_1"], format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', interface=nombres[2]),
    widget.TextBox(**powerline, foreground=theme_config["color_1"]),
    widget.TextBox(text="󰈀",fontsize=25,padding=1, foreground=theme_config["color_1"],),
    widget.Net(foreground= theme_config["color_1"], format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', interface=nombres[1] ), ]

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
    widget.TextBox(text="",fontsize=25,padding=1, foreground=theme_config["color_3"],mouse_callbacks={"Button1": lazy.spawn("sh " +config_path + "/dmenu/calendar.sh '"+ theme_config["color_13"][0]+"' '" + theme_config["color_24"][0]+"' '"+ theme_config["color_40"][0] +"' '"+ theme_config["color_43"][0] +"'")}),
    widget.Clock(format="%a %d/%m/%Y",  foreground=theme_config["color_3"],),

    widget.TextBox(**powerline, foreground=theme_config["color_32"],),
    widget.TextBox(text="󰥔",fontsize=25,padding=1, foreground=theme_config["color_32"]),
    widget.Clock(format="%I:%M %p",foreground=theme_config["color_32"],),]

VolBatBri=[
    widget.TextBox(**powerline, foreground=theme_config["color_10"],),
    widget.Battery(foreground=theme_config["color_10"], discharge_char="󱟥", charge_char="󰂏", format='{char} {percent:2.0%}'),

    widget.TextBox(**powerline,foreground=theme_config["color_30"]),
    widget.TextBox(text="󰃠",fontsize=25,padding=1, foreground=theme_config["color_30"]),
    widget.Backlight(foreground=theme_config["color_30"]),

    widget.TextBox(**powerline,foreground=theme_config["color_41"]),
    widget.TextBox(text="󰕾",fontsize=25,padding=1, foreground=theme_config["color_41"]),
    widget.PulseVolume(foreground=theme_config["color_41"]),]

screens = [
    Screen(
        top=bar.Bar(
            [
                wsps(),
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

                widget.TextBox(**powerline, foreground=theme_config["color_1"]),
                widgetbox(Red, "RED"),
                #widget.WidgetBox(widgets=Red, text_closed="RED", text_open="[X]",foreground=theme_config["color_1"]),

                widget.TextBox(**powerline, foreground=theme_config["color_11"]),
                widget.WidgetBox(widgets=Memoria, text_closed="RAM", text_open="[X]",foreground=theme_config["color_11"]),

                widget.TextBox(**powerline, foreground=theme_config["color_18"]),
                widget.WidgetBox(widgets=Cpu, text_closed="CPU", text_open="[X]", foreground=theme_config["color_18"]),

                widget.TextBox(**powerline, foreground=theme_config["color_21"]),
                widget.WidgetBox(widgets=FechaHora, text_closed="FECHA", text_open="[X]", foreground=theme_config["color_21"]),

                widget.TextBox(**powerline, foreground=theme_config["color_12"]),
                widget.WidgetBox(widgets=VolBatBri, text_closed="VBB", text_open="[X]", foreground=theme_config["color_12"]),

                widget.TextBox(**powerline, foreground=theme_config["color_17"],),
                widget.CurrentLayout(
                    mode='both', icon_first=True,
                    foreground=theme_config["color_17"],
                ),
                widget.TextBox(**powerline, foreground=theme_config["color_1"],),
                widget.Systray(),
                widget.TextBox(**powerline,
                               foreground=theme_config["color_13"]),
                widget.TextBox("Theme: "+theme_config["theme"],
                               foreground=theme_config["color_13"]),
            ],
            20,
            background = theme_config["color_24"]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        ),
    ),
]
