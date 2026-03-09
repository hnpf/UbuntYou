import sys
import subprocess
from rich.console import Console
from rich.table import Table
import click
console = Console()
from ubuntyou.modules.snaps import NoSnaps
from ubuntyou.modules.telemetry import NoTelemetry
from ubuntyou.modules.apt import AptSpeed
from ubuntyou.modules.pro import NoPro
from ubuntyou.modules.flatpak import FlatpakSet
from ubuntyou.modules.gnome import GnomeTools
console = Console()

MODULES = [
    NoSnaps(),
    NoTelemetry(),
    AptSpeed(),
    NoPro(),
    FlatpakSet(),
    GnomeTools(),
]

def run_shell(cmd: str, check=True) -> subprocess.CompletedProcess:
    """Helper to run shell commands safely."""
    try:
        return subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error running:[/] {cmd}\n{e.stderr}")
        raise

@click.group()
def main():
    """Ubunt-you. The Ubuntu Debullshittifier"""
    if sys.platform != "linux":
        console.print("[bold yellow]Warning:[/] This tool is designed specifically for Ubuntu. Running on other distros COULD lead to errors.")

@main.command()
def list():
    """List all current modules."""
    table = Table(title="Current Modules")
    table.add_column("Name", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Description")
    for mod in MODULES:
        status = "[green]Applied[/]" if mod.is_applied() else "[yellow]Pending[/]"
        table.add_row(mod.name, status, mod.description)
    console.print(table)

@main.command()
@click.option("--all", is_flag=True, help="Apply all modules.")
@click.argument("module_names", nargs=-1)
def apply(all, module_names):
    """Apply specific modules."""
    targets = MODULES if all else [m for m in MODULES if m.name.lower() in [n.lower() for n in module_names]]
    
    if not targets:
        console.print("[red]No modules selected or found.[/]")
        return

    for mod in targets:
        console.print(f"[bold blue]Applying {mod.name}...[/]")
        if mod.apply():
            console.print(f"[bold green]✓ {mod.name} applied successfully.[/]")
        else:
            console.print(f"[bold red]✗ Failed to apply {mod.name}.[/]")

@main.command()
@click.option("--all", is_flag=True, help="Revert all modules.")
@click.argument("module_names", nargs=-1)
def revert(all, module_names):
    """Revert specific modules."""
    targets = MODULES if all else [m for m in MODULES if m.name.lower() in [n.lower() for n in module_names]]
    
    if not targets:
        console.print("[red]No modules selected or found.[/]")
        return

    for mod in targets:
        console.print(f"[bold blue]Reverting {mod.name}...[/]")
        if mod.revert():
            console.print(f"[bold green]✓ {mod.name} reverted successfully![/]")
        else:
            console.print(f"[bold red]✗ Failed to revert {mod.name}.[/]")

if __name__ == "__main__":
    main()
