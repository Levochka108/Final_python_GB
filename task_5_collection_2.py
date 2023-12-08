import logging

FILENAME = "logs/logfile_task_5.log"
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


def get_odd_indices(lst):
    return [i + 1 for i in range(len(lst)) if lst[i] % 2 == 1]


if __name__ == '__main__':
    """
    Задание №5
    ✔ Создайте вручную список с повторяющимися целыми числами.
    ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
    ✔ Нумерация начинается с единицы.
    """

    try:
        lst = [2, 2, 2, 3, 3, 5]
        lst_numbers = get_odd_indices(lst)
        logger.info(f'Исходный список: {lst}')
        logger.info(
            f'Список порядковых номеров нечетных элементов: {lst_numbers}')
    except Exception as e:
        logger.error(f'Произошла ошибка - {e}')
