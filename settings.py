from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT_PATH, "src")
ITEMS_PATH = Path.joinpath(DATA_PATH, "items.csv")
