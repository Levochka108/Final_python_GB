import logging

FILENAME = "logs/logfile_task_3.log"
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


def create_type_dict(tuple_obj):
    type_dict = {}
    for el in tuple_obj:
        obj_type = type(el)
        if obj_type not in type_dict:
            type_dict[obj_type] = []
        type_dict[obj_type].append(el)
    return type_dict


if __name__ == '__main__':
    """
    Задание №3
    ✔ Создайте вручную кортеж содержащий элементы разных типов.
    ✔ Получите из него словарь списков, где:
    ключ — тип элемента,
    значение — список элементов данного типа.
    """

    tuple_obj = (1, 2.1, True, None, 'string', 3, 4, 5, False, 'elem')

    try:
        type_dict = create_type_dict(tuple_obj)
        logger.info(f'Словарь списков: {type_dict}')
    except Exception as e:
        logger.error(f'Произошла ошибка - {e}')
