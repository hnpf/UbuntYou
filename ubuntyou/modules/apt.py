import os
import subprocess
from ubuntyou.core.module import Module

class AptSpeed(Module):
    @property
    def name(self) -> str:
        return "AptSpeed"

    @property
    def description(self) -> str:
        return "Optimize APT for faster updates and downloads."
    def is_applied(self) -> bool:
        return os.path.exists("/etc/apt/apt.conf.d/99ubuntyou-speed")
    def apply(self) -> bool:
        try:
            apt_conf = """# Optimized APT settings by ubuntyou
Acquire::Languages "none";
Acquire::http::Pipeline-Depth "5";
Binary::apt::APT::Max-Downloads "16";
APT::Color "1";
"""
            subprocess.run(f"echo '{apt_conf}' | sudo tee /etc/apt/apt.conf.d/99ubuntyou-speed", shell=True)
            return True
        except Exception:
            return False
    def revert(self) -> bool:
        try:
            subprocess.run("sudo rm /etc/apt/apt.conf.d/99ubuntyou-speed", shell=True)
            return True
        except Exception:
            return False
