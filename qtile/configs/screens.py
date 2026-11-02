from libqtile import bar
from libqtile.config import Screen
from .theme import theme
from .flags import nombres, config_path
from .widgets import widgets_defaults, widgets_bar
#pantallas y barra de estado

theme_config = theme()

widget_defaults = dict(
    font="Hack Nerd Font Mono",
    fontsize=10,
    padding=0,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        #barra de estado
        top=bar.Bar(
            widgets_bar(),
            20,
            background = theme_config["color_24"]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        ),
    ),
]
