import logging

FILENAME = "logs/logfile_task_7.log"
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


def count_letters_with_count(data):
    dct = {}
    for el in data:
        val = data.count(el)
        dct[el] = val
    return dct


def count_letters_without_count(data):
    dct = {}
    for el_1 in data:
        count = 0
        for el_2 in data:
            if el_1 == el_2:
                count += 1
        dct[el_1] = count
    return dct


def count_letters_with_get(data):
    my_dict = {}
    for char in data:
        if char.isalpha():
            my_dict[char] = my_dict.get(char, 0) + 1
    return my_dict


if __name__ == '__main__':
    """
    Задание №7
    ✔ Пользователь вводит строку текста.
    ✔ Подсчитайте сколько раз встречается
    каждая буква в строке без использования
    метода count и с ним.
    ✔ Результат сохраните в словаре, где ключ —
    символ, а значение — частота встречи
    символа в строке.
    ✔ Обратите внимание на порядок ключей.
    Объясните почему они совпадают
    или не совпадают в ваших решениях.
    """

    try:
        user_input = input("Введите строку текста: ")

        # Решение 1 с использованием метода count
        result_1_with_count = count_letters_with_count(user_input)
        logger.info(f'Решение 1 с использованием count: {result_1_with_count}')

        # Решение 1 без использования метода count
        result_1_without_count = count_letters_without_count(user_input)
        logger.info(
            f'Решение 1 без использования count: {result_1_without_count}')

        # Решение 2 без использования метода count
        result_2_with_get = count_letters_with_get(user_input)
        logger.info(f'Решение 2 с использованием get: {result_2_with_get}')
    except Exception as e:
        logger.error(f'Произошла ошибка - {e}')
