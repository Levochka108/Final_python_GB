import logging

FILENAME = "logs/logfile_task_6.log"
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


def print_words_aligned(text):
    shift = len(max(text, key=len))
    for n, word in enumerate(sorted(text), 1):
        logger.info(f'{n}. {word:>{shift}}')
        print(f"{n}. {word:>{shift}}")


if __name__ == '__main__':
    """
    Задание №6
    Пользователь вводит строку текста. Вывести каждое слово с новой строки.
    ✔ Строки нумеруются начиная с единицы.
    ✔ Слова выводятся отсортированными согласно кодировки Unicode.
    ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
    слова был один пробел между ним и номером строки.
    """

    try:
        user_input = input("Введите строку текста: ")
        words = user_input.split()
        print_words_aligned(words)
    except Exception as e:
        logger.error(f'Произошла ошибка - {e}')
