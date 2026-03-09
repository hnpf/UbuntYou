import subprocess
import os
from ubuntyou.core.module import Module

class GnomeTools(Module):
    @property
    def name(self) -> str:
        return "GnomeTools"
    @property
    def description(self) -> str:
        return "Install GNOME Tweaks and Extension Manager."
    def is_applied(self) -> bool:
        return os.path.exists("/usr/bin/gnome-tweaks") and os.path.exists("/usr/bin/extension-manager")
    def apply(self) -> bool:
        try:
            subprocess.run("sudo apt update && sudo apt install -y gnome-tweaks gnome-shell-extension-manager", shell=True)
            return True
        except Exception:
            return False
    def revert(self) -> bool:
        try:
            subprocess.run("sudo apt purge -y gnome-tweaks gnome-shell-extension-manager", shell=True)
            return True
        except Exception:
            return False
