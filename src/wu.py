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
        except ValueError as e:
            print("Use -h or --help")
            return
        moved_image = ValidPath(self.args.image()).move(self.args.directory())
        Wallpaper(moved_image).update_on_desktop().update_on_lockscreen()


if __name__ == "__main__":
    wu = Wu(Args())
    wu.run()
