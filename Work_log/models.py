from django.db import models  # Импортируем модуль models для создания моделей Django
from django.contrib.auth.models import User  # Импортируем встроенную модель User для управления пользователями
from django.utils import timezone  # Импортируем утилиту timezone для работы с датой и временем
from datetime import timedelta

# Модель Profile для хранения дополнительных данных о пользователях
class Profile(models.Model):

    # Поля модели Profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь один-к-одному с моделью User; при удалении пользователя удаляется и профиль
    full_name = models.CharField(max_length=255)  # Поле для хранения полного имени пользователя
    is_active = models.BooleanField(default=False)  # Поле для активации/деактивации аккаунта пользователя

    def __str__(self):
        return self.user.username  # Возвращает строковое представление профиля, отображающее имя пользователя

