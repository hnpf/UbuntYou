# ubuntyou 

A modular debullshittifier for Ubuntu that maintains the default aesthetic while removing telemetry, ads, and snaps. It's safe, revertible, and designed to make Ubuntu feel like your OS again.

## Quick Install

To get started, clone the repo and run the installation script. It will make sure Python 3, pip, and all necessary dependencies are installed.

```bash
git clone https://github.com/hnpf/UbuntYou
cd UbuntYou
./install.sh
```

## Usage

After running the installer, you can use the `ubuntyou` command directly from anywhere.

### List Available Modules
See what can be modified and their current status:
```bash
ubuntyou list
```

### Apply Changes
Apply all modules at once:
```bash
sudo ubuntyou apply --all
```

Or apply specific modules (e.g., just remove snaps and telemetry):
```bash
sudo ubuntyou apply nosnaps telemetry
```

### Revert Changes
Every module is safe and revertible. If you miss something, just undo it:
```bash
sudo ubuntyou revert nosnaps
```

## Features

- **`NoSnaps`**: Purge `snapd` and ALL INSTALLED SNAPS, then pin the package to prevent reinstallation.
- **`NoTelemetry`**: Disable crash reporting (Apport/Whoopsie), Ubuntu Report, and terminal ads (`motd-news`).
- **`AptSpeed`**: Optimize APT with parallel downloads and reduced metadata overhead.
- **`NoPro`**: Remove Ubuntu Pro ads and remove the `ubuntu-advantage-tools` package.
- **`FlatpakSet`**: Set up Flatpak, Flathub, and the vanilla GNOME Software center (much better for Flatpaks).
- **`GnomeTools`**: Install essential tools like GNOME Tweaks and the Extension Manager.

## Modular Architecture

`ubuntyou` is built to be easily extendable. Each module is a self-contained Python class in `ubuntyou/modules/`.

To add a new feature:
1. Make a new file in `ubuntyou/modules/` (e.g., `mirror_opt.py`).
2. Inherit from the `Module` base class.
3. Register in `ubuntyou/cli.py`.

## Safety And Philosophy

- **Respect the UI**: We dont change the default theme or nuke the desktop environment. It still looks like Ubuntu, just.. better.
- **No Mystery Meat**: Every command run by a module is transparent and can be audited and modified in the source code.
- **Fully Revertible**: We aim for 100% revertability for every change made!
