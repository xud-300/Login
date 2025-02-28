import csv
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from .forms import UserRegistrationForm, CustomAuthenticationForm
from .models import Profile
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.dateformat import DateFormat
from .decorators import editor_required, admin_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils.formats import date_format
from openpyxl import Workbook
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import date
from django.conf import settings
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, PageTemplate
from django.db import transaction
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.db.models import Q


from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Profile

from django.db.models import Q


from django.contrib.auth.models import User
# Регистрация нового пользователя
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Проверка на существование пользователя с таким же именем
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return JsonResponse({'errors': {'username': ['Пользователь с таким именем уже существует.']}})
            
            user = form.save(commit=False)
            user.is_active = False  # Отключение учетной записи до активации
            user.save()

            # Проверяем или создаем профиль
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'full_name': form.cleaned_data.get('full_name', 'не указано'),
                }
            )

            if not created:
                # Обновляем существующий профиль, если он уже существует
                profile.full_name = form.cleaned_data.get('full_name', 'не указано')
                profile.save()

            return JsonResponse({'success': True, 'message': 'Ваш аккаунт успешно создан. Ожидайте активации.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/login.html', {'form': form, 'roles': Profile.ROLE_CHOICES})


from django.core.cache import cache
import time

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

from django.http import JsonResponse, HttpResponseRedirect  
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import render
import time
from django.core.cache import cache

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        client_ip = get_client_ip(request)
        failed_attempts_key = f'failed_attempts_{client_ip}'
        failed_attempts_data = cache.get(failed_attempts_key, (0, time.time()))

        failed_attempts, first_attempt_time = failed_attempts_data

        if time.time() - first_attempt_time > 120:  # 120 секунд = 2 минуты
            failed_attempts = 0
            first_attempt_time = time.time()

        failed_attempts += 1  # Увеличиваем количество неудачных попыток

        reset_captcha = failed_attempts >= 3

        form = CustomAuthenticationForm(request, data=request.POST, failed_attempts=failed_attempts, reset_captcha=reset_captcha)

        if form.is_valid():
            user = authenticate(request, username=username, password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                cache.delete(failed_attempts_key)  # Сбрасываем счетчик после успешного входа
                
                # Изменяем редирект на страницу карты
                return JsonResponse({'success': True, 'redirect_url': reverse('map_view')})
            else:
                cache.set(failed_attempts_key, (failed_attempts, first_attempt_time), timeout=120)
                return JsonResponse({
                    'success': False,
                    'message': 'Неверное имя пользователя или пароль.',
                    'reset_captcha': reset_captcha
                })
        else:
            cache.set(failed_attempts_key, (failed_attempts, first_attempt_time), timeout=120)
            return JsonResponse({
                'success': False,
                'message': 'Произошла ошибка. Попробуйте еще раз.',
                'reset_captcha': reset_captcha
            })
    else:
        client_ip = get_client_ip(request)
        failed_attempts_key = f'failed_attempts_{client_ip}'
        failed_attempts_data = cache.get(failed_attempts_key, (0, time.time()))
        failed_attempts, _ = failed_attempts_data

        form = CustomAuthenticationForm()
        registration_form = UserRegistrationForm()

        return render(request, 'registration/login.html', {
            'form': form,
            'registration_form': registration_form,
            'failed_attempts': failed_attempts
        })



from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def map_view(request):
    return render(request, 'index.html')  # Отображаем карту

# Выход пользователя
def user_logout(request):
    logout(request)
    return redirect('login')
