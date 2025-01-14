#!/usr/bin/env python3
import dbus
import argparse
import os
from pathlib import Path


HOME = Path.home()
WALLPAPER_DIR = HOME / "Pictures" / "wallpapers"
SCREEN_LOCK_CONFIG = HOME / ".config" / "kscreenlockerrc"


def create_dir(path):
    path = Path(path)
    if not path.exists():
        print(f"Create directory {path}")
    path.mkdir(parents=True, exist_ok=True)


def rename_image(image_path):
    if image_path is None:
        return None
    image_path = Path(os.path.abspath(image_path))
    renamed_image_path = Path.joinpath(WALLPAPER_DIR, image_path.name)
    if not image_path.exists():
        print(f"Error: {image_path} does not exist.")
        return None
    if not image_path.is_file():
        print(f"Error: {image_path} is not a valid file.")
        return None
    image_path.rename(renamed_image_path)
    if not renamed_image_path.exists():
        print(f"Error: {renamed_image_path} move file.")
        return None
    print(f"{image_path} -> {renamed_image_path}")
    return renamed_image_path


def update_wallpaper(image_path):
    if not image_path.exists():
        print(f"Error: {image_path} does not exist.")
        return
    if not image_path.is_file():
        print(f"Error: {image_path} is not a valid file.")
        return
    js = f"""
    var allDesktops = desktops();
    for (i = 0; i < allDesktops.length; i++) {{
        d = allDesktops[i];
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
        d.writeConfig("Image", "file://{image_path}")
    }}
    """
    try:
        bus = dbus.SessionBus()
        plasma = dbus.Interface(
            bus.get_object("org.kde.plasmashell", "/PlasmaShell"),
            dbus_interface="org.kde.PlasmaShell",
        )
        plasma.evaluateScript(js)
        print(f"Wallpaper set successfully to {image_path}")
    except dbus.DBusException as e:
        print(f"DBus error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_lockscreen_wallpaper(image_path):
    if not image_path.exists():
        print(f"Error: {image_path} does not exist.")
        return
    if not image_path.is_file():
        print(f"Error: {image_path} is not a valid file.")
        return
    new_config = f"""
[Greeter][Wallpaper][org.kde.image][General]
Image=file://{image_path}
PreviewImage=file://{image_path}
"""
    try:
        with open(SCREEN_LOCK_CONFIG, "w") as kscreenlockerrc:
            kscreenlockerrc.write(new_config)
        print(f"Lockscreen wallpaper updated successfully to {image_path}")
    except IOError as e:
        print(f"Error writing to {SCREEN_LOCK_CONFIG}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KDE Wallpaper updater")
    parser.add_argument("--image", "-i", help="Path to image", default=None)
    parser.add_argument(
        "--directory",
        "-d",
        help="The directory where the updated wallpapers is moved to",
        default=None,
    )
    args = parser.parse_args()
    if args.directory is not None:
        WALLPAPER_DIR = Path(args.directory)
    create_dir(WALLPAPER_DIR)
    image_path = rename_image(args.image)
    if image_path is not None:
        update_wallpaper(image_path)
        update_lockscreen_wallpaper(image_path)
    else:
        print("Need help? use -h or --help")
