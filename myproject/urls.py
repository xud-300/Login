from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь для админ панели
    path('', include('Work_log.urls')),  # Включение URL из приложения Work_log
]