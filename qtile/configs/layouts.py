from libqtile import layout
from libqtile.config import Match
from .theme import theme
theme_config=theme()

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