from libqtile.config import Drag, Click
from libqtile.lazy import lazy
from .keymaps import Super

#modo flotante
mouse = [
    Drag([Super], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([Super], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([Super], "Button2", lazy.window.bring_to_front()),
]
