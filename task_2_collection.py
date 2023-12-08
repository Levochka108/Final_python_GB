import logging

FILENAME = "logs/logfile_task_2.log"
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


def process_data(data):
    try:
        int_value = int(data)
        if int_value > 0:
            logger.info(
                f'Преобразовано в целое положительное число - {int_value}')
        else:
            logger.warning(
                f'Отрицательное число преобразовано в положительное - {int_value}')
    except ValueError:
        logger.debug(
            f'Невозможно преобразовать {data} к целому положительному числу')

    try:
        float_value = float(data)
        logger.info(f'Преобразовано в вещественное число - {float_value}')
    except ValueError:
        logger.debug(f'Невозможно преобразовать {data} к вещественному числу')

    if isinstance(data, str):
        if data.islower():
            logger.info(f'Строка в нижнем регистре - {data}')
        else:
            logger.info(
                f'Строка преобразована в нижний регистр - {data.lower()}')


if __name__ == '__main__':
    """
    Задание №2
    Пользователь вводит данные. Сделайте проверку данных
    и преобразуйте если возможно в один из вариантов ниже:
    ✔ Целое положительное число
    ✔ Вещественное положительное или отрицательное число
    ✔ Строку в нижнем регистре, если в строке есть
    хотя бы одна заглавная буква
    ✔ Строку в нижнем регистре в остальных случаях
    """

    user_data = [1, 2.1, True, -5, "Sds"]

    for data in user_data:
        process_data(data)
