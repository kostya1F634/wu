from pathlib import Path
import random
import string


class ValidPath:
    def __init__(self, path):
        self.path = path

    def exists(self):
        path = Path(self.path).expanduser().absolute()
        if path.exists():
            return True

    def create(self, is_file=True):
        path = Path(self.path).expanduser().absolute()
        if is_file:
            path.touch(exist_ok=True)
        else:
            path.mkdir(parents=True, exist_ok=True)

    def move(self, new_dir_path):
        path = Path(self.path).expanduser().absolute()
        moved_dir = Path(new_dir_path).expanduser().absolute()
        if not moved_dir.exists():
            moved_dir.mkdir(parents=True, exist_ok=True)
            print(f"Create directory {moved_dir}")
        moved_path = Path(moved_dir, path.name).absolute()
        if not path.exists():
            raise FileNotFoundError(f"File {path} does not exist.")
        if moved_path.exists():
            random_sequence = "".join(
                random.choices(string.ascii_letters + string.digits, k=8)
            )
            moved_path = moved_path.with_name(
                moved_path.stem + "_" + random_sequence + moved_path.suffix
            )
        path.rename(moved_path)
        print(f"Move {path} -> {moved_path}")
        return ValidPath(moved_path)

    def write(self, text):
        path = Path(self.path).expanduser().absolute()
        try:
            with open(path, "w") as file:
                file.write(text)
        except IOError as e:
            raise IOError(f"Error writing to {path}: {e}")

    def __str__(self):
        return str(self.path)
