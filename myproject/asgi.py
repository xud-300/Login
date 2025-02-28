import os
from django.core.asgi import get_asgi_application

# Устанавливаем переменную окружения для указания настроек Django
# Это необходимо, чтобы указать Django, какой файл настроек использовать
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Создаем экземпляр ASGI-приложения
# ASGI (Asynchronous Server Gateway Interface) — это стандарт для асинхронных приложений на Python
# get_asgi_application — функция, которая возвращает объект приложения ASGI, 
# который будет использован сервером для обработки запросов
application = get_asgi_application()
