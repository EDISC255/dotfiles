from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keymaps import Super, keys

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
