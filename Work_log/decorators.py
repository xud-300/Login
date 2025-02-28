from functools import wraps  # Импортируем функцию wraps для сохранения информации о декорируемой функции
from django.http import HttpResponseForbidden  # Импортируем HttpResponseForbidden для возврата ошибки доступа
from .models import Profile  # Импортируем модель Profile для работы с профилями пользователей

# Декоратор для проверки роли пользователя
def role_required(allowed_roles):
    """
    Декоратор, который проверяет, имеет ли пользователь одну из разрешенных ролей.
    
    :param allowed_roles: Список разрешенных ролей.
    :return: Функция-декоратор.
    """
    def decorator(view_func):
        """
        Внутренняя функция-декоратор, которая оборачивает view-функцию.
        
        :param view_func: Функция представления, которая будет декорирована.
        :return: Обернутая функция представления.
        """
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            """
            Функция-обертка, которая выполняет проверку роли пользователя перед вызовом view-функции.
            
            :param request: HTTP-запрос.
            :return: HTTP-ответ или вызов view-функции.
            """
            # Получаем профиль текущего пользователя
            user_profile = Profile.objects.get(user=request.user)
            
            # Проверяем, имеет ли пользователь одну из разрешенных ролей
            if user_profile.role not in allowed_roles:
                # Если роль пользователя не входит в список разрешенных ролей, возвращаем ошибку доступа
                return HttpResponseForbidden("Вы не имеете прав для выполнения этой операции.")
            
            # Если проверка пройдена, вызываем оригинальную view-функцию
            return view_func(request, *args, **kwargs)
        
        return _wrapped_view  # Возвращаем обернутую функцию
    
    return decorator  # Возвращаем функцию-декоратор

# Декоратор для ограничения доступа только для редакторов и администраторов
editor_required = role_required(['editor', 'admin'])

# Декоратор для ограничения доступа только для администраторов
admin_required = role_required(['admin'])
