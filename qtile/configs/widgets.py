from libqtile.lazy import lazy
from libqtile import widget
from libqtile.lazy import lazy
from .theme import theme
from .flags import nombres, config_path

theme_config = theme()
powerline_spawn={"text":"","fontsize":40,"padding":-5.5}
powerline={"text":"","fontsize":40,"padding":-5.5}

def base(fg="color_1", bg="color_43"):
    return{
        "foreground": theme_config[fg],
        "background": theme_config[bg]
    }
def icon(i="i", fg="color_1"):
    return widget.TextBox(text=i,fontsize=25,padding=1, foreground=theme_config[fg],),

def powerline(fg="color_1"):
    return widget.TextBox(text="",fontsize=40, padding=-5.5,foreground=theme_config[fg] )

Red=[
    powerline(),
    icon("", "color_1"),
    widget.Net(foreground=theme_config["color_1"], format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', interface=nombres[2]),

    powerline(),
    icon("󰈀", "color_1"),
    widget.Net(foreground= theme_config["color_1"], format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', interface=nombres[1])]

Memoria=[
    widget.Memory(format='{MemUsed:.0f}{mm}',update_interval=2.0, foreground=theme_config["color_8"]), 
    powerline(),
    icon("󰿡", "color_1"),    
    widget.Memory(format='{SwapUsed:.0f}{ms}',update_interval=2.0, foreground=theme_config["color_9"])]

Cpu=[
    powerline(),
    icon("󰻠", "color_1"),    
    widget.CPU(foreground=theme_config["color_23"], format="{freq_current}GHz {load_percent}%"),
    powerline(),
    icon("", "color_1"),    
    widget.ThermalSensor(foreground=theme_config["color_5"]),]

FechaHora=[
    powerline(),
    icon("", "color_1"),    
    widget.Clock(format="%a %d/%m/%Y",  foreground=theme_config["color_3"],),

    powerline(),
    icon("󰥔", "color_1"),    
    widget.Clock(format="%I:%M %p",foreground=theme_config["color_32"],),]

VolBatBri=[
    powerline(),
    widget.Battery(foreground=theme_config["color_10"], discharge_char="󱟥", charge_char="󰂏", format='{char} {percent:2.0%}'),
    
    powerline(),
    icon("󰃠", "color_1"),
    widget.Backlight(foreground=theme_config["color_30"]),

    powerline(),
    icon("󰕾", "color_1"),
    widget.PulseVolume(foreground=theme_config["color_41"])]

def wsps():
    return widget.GroupBox(
        inactive=theme_config["color_14"],
        disable_drag=True,
        active=theme_config["color_40"],
        fontsize=12,
        highlight_method="text",
        this_current_screen_border=theme_config["color_17"])

def widgetbox(widgets, text_close=" ", fg="color_1"):
    return widget.WidgetBox(widgets=widgets, text_closed=text_close, text_open="[X]",foreground=theme_config[fg]),

widget_defaults = dict(
    font="Hack Nerd Font Mono",
    fontsize=10,
    padding=0,
)
    

extension_defaults = widget_defaults.copy()
