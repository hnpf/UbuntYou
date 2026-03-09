# ubuntyou

An Ubuntu debullshittifier that maintains the default aesthetic while removing telemetry, ads, and snaps!

## Features we have

- **Remove Snaps**: Purge `snapd` and all installed snaps, then pin `snapd` to prevent it from coming back.
- **Destroy Telemetry**: Disable Apport (crash popups), Whoopsie (data reporting), and Ubuntu Report.
- **Stop Terminal Ads**: Disable the annoying "Ubuntu Pro" and "motd-news" terminal advertisements. This shouldn't be in a Linux distro anyway.
- **Optimize APT**: Enable parallel downloads and reduce metadata overhead for faster updates.
- **Flatpak Integration**: Install Flatpak, Flathub, and the vanilla GNOME Software center.
- **Expert Tools**: Install GNOME Tweaks and the Extension Manager.

## Installation

Since this modifies system files, it should be run with `sudo`.

```bash
git clone https://github.com/hnpf/UbuntYou
cd UbuntYou

python3 -m ubuntyou.cli list

sudo python3 -m ubuntyou.cli apply --all

# this is for specific modules (ubuntyou/modules/)
sudo python3 -m ubuntyou.cli apply nosnaps nopro telemetry
```

## HOW TO REVERT

each module includes a `revert` method to undo the changes it made.

```bash
sudo python3 -m ubuntyou.cli revert nosnaps
```

## Development

the project is structured into modules under `ubuntyou/modules/`. to add a new task:
1. add a new class inheriting from `Module` in `ubuntyou/core/module.py`.
2. add `apply()`, `revert()`, and `is_applied()`.
3. register it in `ubuntyou/cli.py`.

## Safety

- **Non Destructive**: It does not remove the desktop environment or default theme.
- **Modular**: You only apply what you want.
- **Revertible**: Most changes can be undone easily.
