#!/usr/bin/env python3
from wallpaper import Wallpaper
from args import Args
from valid_path import ValidPath


class Wu:
    def __init__(self, args):
        self.args = args

    def run(self):
        try:
            self.args.parse()
            if not self.args.move():
                moved_image = ValidPath(self.args.image()).move(self.args.directory())
            else:
                moved_image = ValidPath(self.args.image()).existence()
            Wallpaper(moved_image).update_on_desktop().update_on_lockscreen()
        except ValueError as e:
            print(e, "Use -h or --help")
        except FileNotFoundError as e:
            print(e)


if __name__ == "__main__":
    Wu(Args()).run()
