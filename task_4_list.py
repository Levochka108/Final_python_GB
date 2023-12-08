import logging

FILENAME = "logs/logfile_task_4.log"
FILEMODE = 'w'
FORMAT = '%(levelname)s - %(asctime)s - %(message)s'
ENCODING = 'utf-8'

# Настройка логгера
logging.basicConfig(filename=FILENAME,
                    filemode=FILEMODE,
                    format=FORMAT,
                    encoding=ENCODING,
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


"""def remove_duplicates(lst):
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    return [item for item in lst if count_dict[item] != 2]"""


def remove_duplicates(lst):
    count_dict = {}
    new_lst = []

    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1

    for item in lst:
        if count_dict[item] == 1:
            new_lst.append(item)

    return new_lst


if __name__ == '__main__':
    """
    Задание №4
    ✔ Создайте вручную список с повторяющимися элементами.
    ✔ Удалите из него все элементы, которые встречаются дважды.
    """

    try:
        lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]
        new_lst = remove_duplicates(lst)
        logger.info(f'Исходный список: {lst}')
        logger.info(f'Список без повторений: {new_lst}')
    except Exception as e:
        logger.error(f'Произошла ошибка - {e}')
