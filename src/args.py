import argparse


class Args:
    def parse(self):
        parser = argparse.ArgumentParser(description="KDE Wallpaper Updater")
        parser.add_argument(
            "--image", "-i", help="Path to image (required).", default=None
        )
        parser.add_argument(
            "--directory",
            "-d",
            help="Path to directory where the updated wallpapers is moved to (optional). Default is ~/Pictures/wallpapers.",
            default=None,
        )
        parser.add_argument(
            "--no-move",
            "-nm",
            help="Not move the image flag (optional). Default is False.",
            default=False,
        )
        self.args = parser.parse_args()
        if self.args.image is None:
            raise ValueError("The '--image' argument is required and must be provided.")

    def directory(self):
        if self.args.directory is None:
            return "~/Pictures/wallpapers"
        return self.args.directory

    def image(self):
        return self.args.image

    def move(self):
        return self.args.no_move
