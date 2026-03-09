import os
import subprocess
from ubuntyou.core.module import Module

class NoPro(Module):
    @property
    def name(self) -> str:
        return "NoPro"
    @property
    def description(self) -> str:
        return "Remove Ubuntu Pro ads and popups."
    def is_applied(self) -> bool:
        # check if the package is removed or the specific apt hooks r gone
        return not os.path.exists("/usr/bin/pro")
    def apply(self) -> bool:
        try:
            # 1. remove the pro tool itself
            subprocess.run("sudo apt purge -y ubuntu-advantage-tools", shell=True)
            # 2. remove the MOTD hooks for pro
            subprocess.run("sudo rm -f /etc/update-motd.d/88-esm-announce /etc/update-motd.d/91-contract-ua-esm-status", shell=True)
            # 3. stop apt from suggesting pro entirely
            subprocess.run("sudo rm -f /etc/apt/apt.conf.d/20apt-esm-hook.conf", shell=True)
            return True
        except Exception:
            return False
    def revert(self) -> bool:
        try:
            subprocess.run("sudo apt install -y ubuntu-advantage-tools", shell=True)
            return True
        except Exception:
            return False
