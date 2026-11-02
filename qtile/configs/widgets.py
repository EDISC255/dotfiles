from libqtile.lazy import lazy
from libqtile import widget


from .theme import theme
from .flags import nombres, config_path

theme_config = theme()

def widgets_bar():
    return [
        wsps(),
        #widgets, text_close=" ", fg="color_1"
        widget.WindowName(foreground=theme_config["color_16"]),

        powerline("color_1"),
        widgetbox(Red, "RED", "color_1"),        

        powerline("color_11"),
        widgetbox(Memoria, "RAM", "color_11"),

        powerline("color_18"),
        widgetbox(Cpu, "CPU", "color_18"),

        powerline("color_21"),
        widgetbox(FechaHora, "FECHA" ,"color_21"),

        powerline("color_12"),
        widgetbox(VolBatBri, "STHW" ,"color_12"),

        powerline("color_17"),
        widget.CurrentLayout(mode='both', icon_first=True, foreground=theme_config["color_17"]),

        powerline(),
        widget.Systray(),

        powerline("color_13"),
        widget.TextBox(
            "Theme: "+theme_config["theme"],
            foreground=theme_config["color_13"]
        ),

    ]

def widgets_defaults():
    return [
        widget.CurrentLayout(),
        widget.GroupBox(),
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox("default config", name="default"),
        widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(),
        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        widget.QuickExit(),
    ]

def wsps():
    return widget.GroupBox(
        inactive=theme_config["color_14"],
        disable_drag=True,
        active=theme_config["color_40"],
        fontsize=12,
        highlight_method="text",
        this_current_screen_border=theme_config["color_17"]
    )

def widgetbox(widgets=[], text_close="widgetsbox", fg="color_1"):
    return widget.WidgetBox(widgets=widgets, text_closed=text_close, text_open="[X]", foreground=theme_config[fg])

def base(fg="color_1", bg="color_43"):
    return{
        "foreground": theme_config[fg],
        "background": theme_config[bg]
    }

def icon(i="i", fg="color_1"):
    return widget.TextBox(text=i, fontsize=25, padding=1, foreground=theme_config[fg])

def powerline(fg="color_1"):
    return widget.TextBox(text="", fontsize=40, padding=-5.5, foreground=theme_config[fg] )

Red=[
    powerline("color_1"),
    icon("", "color_1"),
    widget.Net(foreground=theme_config["color_1"], format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', interface=nombres[2]),

    powerline(),
    icon("󰈀", "color_1"),
    widget.Net(foreground= theme_config["color_1"], format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', interface=nombres[1])
]

Memoria=[
    powerline("color_8"),
    icon("", "color_8"),    
    widget.Memory(format='{MemUsed:.0f}{mm}',update_interval=2.0, foreground=theme_config["color_8"]),
    
    powerline("color_9"),
    icon("󰿡", "color_9"),
    widget.Memory(format='{SwapUsed:.0f}{ms}',update_interval=2.0, foreground=theme_config["color_9"])
]

Cpu=[
    powerline("color_23"),
    icon("󰻠", "color_23"),
    widget.CPU(foreground=theme_config["color_23"], format="{freq_current}GHz {load_percent}%"),

    powerline("color_5"),
    icon("", "color_5"),
    widget.ThermalSensor(foreground=theme_config["color_5"])
]

FechaHora=[
    powerline("color_3"),
    icon("", "color_3"),
    widget.Clock(format="%a %d/%m/%Y",  foreground=theme_config["color_3"]),

    powerline("color_32"),
    icon("󰥔", "color_32"),
    widget.Clock(format="%I:%M %p",foreground=theme_config["color_32"],)
]

VolBatBri=[
    powerline("color_10"),
    widget.Battery(foreground=theme_config["color_10"], discharge_char="󱟥", charge_char="󰂏", format='{char} {percent:2.0%}'),

    powerline("color_30"),
    icon("󰃠", "color_30"),
    widget.Backlight(foreground=theme_config["color_30"]),

    powerline("color_41"),
    icon("󰕾", "color_41"),
    widget.PulseVolume(foreground=theme_config["color_41"])
]
