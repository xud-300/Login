import os  # Импортируем модуль os для работы с переменными окружения
from django.core.wsgi import get_wsgi_application  # Импортируем функцию для получения WSGI-приложения

# Устанавливаем переменную окружения 'DJANGO_SETTINGS_MODULE' с указанием на файл настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Получаем WSGI-приложение Django, которое будет использоваться сервером для обработки запросов
application = get_wsgi_application()
