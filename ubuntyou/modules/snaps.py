import os
import subprocess
from ubuntyou.core.module import Module

class NoSnaps(Module):
    @property
    def name(self) -> str:
        return "NoSnaps"
    @property
    def description(self) -> str:
        return "Permanently remove and disable Snaps."
    def is_applied(self) -> bool:
        # check if snapd is installed or if the pin exists
        return not os.path.exists("/usr/bin/snap") and os.path.exists("/etc/apt/preferences.d/nosnap.pref")
    def apply(self) -> bool:
        try:
            # 1. remove all snaps
            # We need to get the list of snaps first
            result = subprocess.run("snap list", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                snaps = [line.split()[0] for line in result.stdout.strip().split('
')[1:]]
                for snap in snaps:
                    subprocess.run(f"sudo snap remove --purge {snap}", shell=True)
            # 2. stop and remove snapd
            subprocess.run("sudo systemctl stop snapd", shell=True)
            subprocess.run("sudo apt purge -y snapd", shell=True)
            subprocess.run("sudo rm -rf ~/snap /var/snap /var/lib/snapd /var/cache/snapd /usr/lib/snapd", shell=True)
            # 3. Pin snapd to prevent reinstall
            pin_content = """Package: snapd
Pin: release a=*
Pin-Priority: -10
"""
            subprocess.run(f"echo '{pin_content}' | sudo tee /etc/apt/preferences.d/nosnap.pref", shell=True)
            return True
        except Exception:
            return False
    def revert(self) -> bool:
        try:
            subprocess.run("sudo rm /etc/apt/preferences.d/nosnap.pref", shell=True)
            subprocess.run("sudo apt update && sudo apt install -y snapd", shell=True)
            return True
        except Exception:
            return False
