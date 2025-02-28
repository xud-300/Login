import os  # Импортируем модуль os для взаимодействия с операционной системой
import sys  # Импортируем модуль sys для взаимодействия с интерпретатором Python

def main():
    # Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE, указывающую на файл настроек Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    try:
        # Пытаемся импортировать функцию execute_from_command_line из django.core.management
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Если возникает ошибка импорта, выводим подробное сообщение об ошибке с предложением возможных решений
        raise ImportError(

        ) from exc

    # Выполняем команду, переданную через командную строку, используя аргументы, предоставленные в sys.argv
    execute_from_command_line(sys.argv)

# Эта часть кода выполняется только в том случае, если скрипт запускается напрямую, а не импортируется
if __name__ == '__main__':
    main()  # Вызов функции main
