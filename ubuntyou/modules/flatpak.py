import subprocess
import os
from ubuntyou.core.module import Module

class FlatpakSet(Module):
    @property
    def name(self) -> str:
        return "FlatpakSet"
    @property
    def description(self) -> str:
        return "Set up flatpak, flathub, and Gnome software."
    def is_applied(self) -> bool:
        return os.path.exists("/usr/bin/flatpak")
    def apply(self) -> bool:
        try:
            # 1. install flatpak and Gnome software
            subprocess.run("sudo apt update && sudo apt install -y flatpak gnome-software gnome-software-plugin-flatpak", shell=True)
            # 2. add flathub
            subprocess.run("flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo", shell=True)
            return True
        except Exception:
            return False
    def revert(self) -> bool:
        try:
            subprocess.run("sudo apt purge -y flatpak gnome-software-plugin-flatpak", shell=True)
            return True
        except Exception:
            return False
