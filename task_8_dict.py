import logging

FILENAME = "logs/logfile_task_8.log"
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


def analyze_items(data):
    # ✔ Какие вещи взяли все три друга
    common_items = set.intersection(*[set(items) for items in data.values()])
    logger.info(f'Вещи, взятые всеми друзьями: {common_items}')

    # ✔ Какие вещи уникальны, есть только у одного друга
    unique_items_dict = {}
    for friend, items in data.items():
        unique_items = set(items)
        for other_friend, other_items in data.items():
            if friend != other_friend:
                unique_items -= set(other_items)
        if unique_items:
            unique_items_dict[friend] = unique_items
    logger.info(f'Уникальные вещи у каждого друга: {unique_items_dict}')

    # ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
    missing_items_dict = {}
    for friend in data:
        all_items_except_one = set.intersection(
            *(set(items) for other_friend, items in data.items() if other_friend != friend))
        missing_items = all_items_except_one - set(data[friend])
        if missing_items:
            missing_items_dict[friend] = missing_items
    logger.info(
        f'Вещи, которые есть у всех друзей кроме одного и имя друга: {missing_items_dict}')


if __name__ == '__main__':
    """
    Задание №8
    ✔ Три друга взяли вещи в поход. Сформируйте
    словарь, где ключ — имя друга, а значение —
    кортеж вещей. Ответьте на вопросы:

    ✔ Какие вещи взяли все три друга

    ✔ Какие вещи уникальны, есть только у одного друга

    ✔ Какие вещи есть у всех друзей кроме одного
    и имя того, у кого данная вещь отсутствует

    ✔ Для решения используйте операции
    с множествами. Код должен расширяться
    на любое большее количество друзей.
    """

    try:
        friends_data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
                        "Витя": ("Палатка", "Котелок", "Топор"),
                        "Петя": ("Палатка", "Котелок", "Топор", "Спирт"),
                        "Саша": ("Палатка", "Спирт")}

        analyze_items(friends_data)
    except Exception as e:
        logger.error(f'Произошла ошибка - {e}')
