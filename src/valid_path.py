from pathlib import Path
import random
import string


class ValidPath:
    def __init__(self, path):
        self.path = Path(path).expanduser().absolute()

    def move(self, new_dir_path):
        moved_dir = Path(new_dir_path).expanduser().absolute()
        if not moved_dir.exists():
            moved_dir.mkdir(parents=True, exist_ok=True)
            print(f"Create directory {moved_dir}")
        moved_path = Path(moved_dir, self.path.name).absolute()
        if not self.path.exists():
            raise FileNotFoundError(f"File {self.path} does not exist.")
        if moved_path.exists():
            random_sequence = "".join(
                random.choices(string.ascii_letters + string.digits, k=8)
            )
            moved_path = moved_path.with_name(
                moved_path.stem + "_" + random_sequence + moved_path.suffix
            )
        self.path.rename(moved_path)
        print(f"Move {self.path} -> {moved_path}")
        return ValidPath(moved_path)

    def write(self, text):
        try:
            with open(self.path, "w") as file:
                file.write(text)
        except IOError as e:
            raise IOError(f"Error writing to {self.path}: {e}")

    def __str__(self):
        return str(self.path)
