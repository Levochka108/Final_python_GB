import logging


FILENAME = "logs/logfile_task_1.log"
FILEMODE = 'w'
FORMAT = '{levelname} - {asctime} - {msg}'
STYLE = '{'
ENCODING = 'utf-8'

# Настройка логгера
logging.basicConfig(filename=FILENAME,
                    filemode=FILEMODE,
                    format=FORMAT,
                    encoding=ENCODING,
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


def unique_elements(lst):
    try:
        unique_lst = list(set(lst))
        logging.info(f'Уникальный список - {unique_lst}')
        return unique_lst
    except Exception as e:
        logging.error(f'Произошла ошибка - {e}')
        return None


if __name__ == '__main__':
    """
    Задание №1
    ✔ Вручную создайте список с целыми числами, которые
    повторяются. Получите новый список, который содержит
    уникальные (без повтора) элементы исходного списка.
    """

    # решение 1
    lst = [3, 3, 4, 4, 5, 5, 6, 6, 5, 1]
    unique_elements(lst)

    # решение 2
    new_lst = []

    try:
        for el in lst:
            if el in new_lst:
                continue
            else:
                new_lst.append(el)
        logging.info(f'Уникальный список - {new_lst}')
    except Exception as e:
        logging.error(f'Произошла ошибка - {e}')
