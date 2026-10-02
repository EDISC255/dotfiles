from os import path
import psutil
home_path=path.expanduser("~")
config_path=path.join(home_path, ".config")
qtile_config_path=path.join(config_path, "qtile")
autostart_path=path.join(qtile_config_path, "autostart.sh")
interfaces=psutil.net_if_stats()
nombres=list(interfaces.keys())
