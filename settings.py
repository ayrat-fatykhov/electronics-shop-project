from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT_PATH, "src")
ITEMS_PATH = Path.joinpath(DATA_PATH, "items.csv")
# Ссылка для проверки исключения при отсутствия файла
ITEMS_NO_FILE_PATH = Path.joinpath(DATA_PATH, "item.csv")
# Ссылка для проверки исключения при поврежденном файле
ITEMS_NOT_COLON_PATH = Path.joinpath(DATA_PATH, "items_not_one_colon.csv")
