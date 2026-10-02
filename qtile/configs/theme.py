from os import path
import json
from .flags import qtile_config_path
def theme():
    theme_path=path.join(qtile_config_path, "theme.json")
    with open(theme_path,"r",encoding="utf-8") as theme_file:
        theme_config=json.load(theme_file)
    return theme_config