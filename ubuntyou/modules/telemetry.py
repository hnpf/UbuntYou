import os
import subprocess
from ubuntyou.core.module import Module

class NoTelemetry(Module):
    @property
    def name(self) -> str:
        return "NoTelemetry"
    @property
    def description(self) -> str:
        return "Disable crash reporting, telemetry, and terminal ads"
    def is_applied(self) -> bool:
        if os.path.exists("/etc/default/apport"):
            with open("/etc/default/apport", "r") as f:
                if "enabled=1" in f.read():
                    return False
        return True
    def apply(self) -> bool:
        try:
            # 1. Disable Apport, aka: crash popups
            subprocess.run("sudo systemctl stop apport.service", shell=True)
            subprocess.run("sudo systemctl disable apport.service", shell=True)
            subprocess.run("sudo sed -i 's/enabled=1/enabled=0/g' /etc/default/apport", shell=True)
            # 2. Disable Whoopsie, aka: Ubuntu error reporting
            subprocess.run("sudo systemctl stop whoopsie", shell=True)
            subprocess.run("sudo systemctl disable whoopsie", shell=True)
            # 3. Disable Ubuntu report
            subprocess.run("ubuntu-report send no", shell=True)
            subprocess.run("sudo apt purge -y ubuntu-report", shell=True)
            # 4. Disable motd-news (terminal ads)
            subprocess.run("sudo sed -i 's/ENABLED=1/ENABLED=0/g' /etc/default/motd-news", shell=True)
            # 5. Disable popularity-contest (these names are so trash)
            subprocess.run("sudo apt purge -y popularity-contest", shell=True)
            return True
        except Exception:
            return False

    def revert(self) -> bool:
        try:
            subprocess.run("sudo sed -i 's/enabled=0/enabled=1/g' /etc/default/apport", shell=True)
            subprocess.run("sudo systemctl enable apport.service", shell=True)
            subprocess.run("sudo systemctl start apport.service", shell=True)
            return True
        except Exception:
            return False
