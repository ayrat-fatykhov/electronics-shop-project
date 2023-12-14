from settings import ITEMS_NOT_COLON_PATH, ITEMS_NO_FILE_PATH
from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(ITEMS_NO_FILE_PATH)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(ITEMS_NOT_COLON_PATH)
    # InstantiateCSVError: Файл item.csv поврежден
