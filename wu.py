#!/usr/bin/env python3
import dbus
import argparse
import os
from pathlib import Path

HOME = str(Path.home())
WALLPAPERS_DIR = HOME + "Pictures/wallpapers"
SCREEN_LOCK_CONFIG = HOME + "/.config/kscreenlockerrc"


def update_wallpaper(filepath):
    js = f"""
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {{
        d = allDesktops[i];
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
        d.writeConfig("Image", "file://{filepath}")
    }}
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(
        bus.get_object("org.kde.plasmashell", "/PlasmaShell"),
        dbus_interface="org.kde.PlasmaShell",
    )
    plasma.evaluateScript(js)


def update_lockscreen_wallpaper(filepath):
    if os.path.exists(SCREEN_LOCK_CONFIG):
        new_data = []
        with open(SCREEN_LOCK_CONFIG, "r") as kscreenlockerrc:
            new_data = kscreenlockerrc.readlines()
            is_wallpaper_section = False
            for num, line in enumerate(new_data, 1):
                if "[Greeter][Wallpaper][" + "org.kde.image" + "][General]" in line:
                    is_wallpaper_section = True
                if "Image=" in line and is_wallpaper_section:
                    new_data[num - 1] = "Image=" + filepath + "\n"
                    break

        with open(SCREEN_LOCK_CONFIG, "w") as kscreenlockerrc:
            kscreenlockerrc.writelines(new_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KDE Wallpaper setter")
    parser.add_argument("--file", "-f", help="Wallpaper file name", default=None)
    parser.add_argument(
        "--plugin",
        "-p",
        help="Wallpaper plugin (default is org.kde.image)",
        default="org.kde.image",
    )
    parser.add_argument(
        "--timer",
        "-t",
        type=int,
        help="Time in seconds between wallpapers",
        default=900,
    )
    parser.add_argument(
        "--lock-screen", "-l", action="store_true", help="Set lock screen wallpaper"
    )
    args = parser.parse_args()

    if args.file != None:
        update_wallpaper(filepath=args.file)
        update_lockscreen_wallpaper(filepath=args.file)
    else:
        print("Need help? use -h or --help")
