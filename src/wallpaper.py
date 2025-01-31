from valid_path import ValidPath

import dbus


class Wallpaper:
    def __init__(self, image):
        self.image = image

    def update_on_desktop(self):
        js_code = f"""
        var allDesktops = desktops();
        for (i = 0; i < allDesktops.length; i++) {{
            d = allDesktops[i];
            d.wallpaperPlugin = "org.kde.image";
            d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
            d.writeConfig("Image", "file://{self.image}")
        }}
        """
        try:
            bus = dbus.SessionBus()
            plasma = dbus.Interface(
                bus.get_object("org.kde.plasmashell", "/PlasmaShell"),
                dbus_interface="org.kde.PlasmaShell",
            )
            plasma.evaluateScript(js_code)
            print(f"Update Desktop Wallpaper {self.image}")
        except dbus.DBusException as e:
            raise dbus.DBusException(f"Error updating wallpaper: {e}")
        except Exception as e:
            raise Exception(f"Anknown error occurred: {e}")
        return self

    def update_on_lockscreen(self):
        screen_lock_config = ValidPath("~/.config/kscreenlockerrc")
        new_config = f"""
[Greeter][Wallpaper][org.kde.image][General]
Image=file://{self.image}
PreviewImage=file://{self.image}
    """
        screen_lock_config.write(new_config)
        print(f"Update Loock Screen Wallpaper {self.image}")
        return self
