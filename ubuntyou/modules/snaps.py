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
        return not os.path.exists("/usr/bin/snap") and os.path.exists("/etc/apt/preferences.d/nosnap.pref")

    def apply(self) -> bool:
        try:
            result = subprocess.run("snap list", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                snaps = [line.split()[0] for line in result.stdout.strip().split('\n')[1:] if line.strip()]
                for snap in snaps:
                    subprocess.run(f"sudo snap remove --purge {snap}", shell=True, check=True)

            subprocess.run("sudo systemctl stop snapd", shell=True, check=True)
            subprocess.run("sudo apt purge -y snapd", shell=True, check=True)
            subprocess.run(
                "sudo rm -rf ~/snap /var/snap /var/lib/snapd /var/cache/snapd /usr/lib/snapd",
                shell=True, check=True
            )

            pin_content = "Package: snapd\nPin: release a=*\nPin-Priority: -10\n"
            with open("/tmp/nosnap.pref", "w") as f:
                f.write(pin_content)
            subprocess.run("sudo mv /tmp/nosnap.pref /etc/apt/preferences.d/nosnap.pref", shell=True, check=True)

            return True
        except subprocess.CalledProcessError:
            return False
        except Exception:
            return False

    def revert(self) -> bool:
        try:
            subprocess.run("sudo rm /etc/apt/preferences.d/nosnap.pref", shell=True, check=True)
            subprocess.run("sudo apt update && sudo apt install -y snapd", shell=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False
        except Exception:
            return False
