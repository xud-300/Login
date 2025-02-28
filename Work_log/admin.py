from django.contrib import admin
from .models import Profile

# Класс админки для профиля пользователя
class ProfileAdmin(admin.ModelAdmin):
    # Отображаемые поля
    list_display = ('user', 'full_name', 'is_active')
    # Фильтры
    list_filter = ('is_active',)
    # Поля для поиска
    search_fields = ('user__username', 'full_name')
    # Действия
    actions = ['activate_users', 'deactivate_users']

    # Метод для активации пользователей
    def activate_users(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, "Selected users were successfully activated.")

    # Метод для деактивации пользователей
    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected users were successfully deactivated.")

    activate_users.short_description = "Activate selected users"
    deactivate_users.short_description = "Deactivate selected users"

# Регистрация моделей в админке
admin.site.register(Profile, ProfileAdmin)
