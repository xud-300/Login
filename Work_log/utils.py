def get_client_ip(request):
    """
    Функция для получения IP-адреса клиента из запроса.
    
    :param request: HTTP-запрос, содержащий информацию о клиенте.
    :return: Строка с IP-адресом клиента.
    """
    # Пытаемся получить IP-адрес из заголовка 'HTTP_X_FORWARDED_FOR'
    ip = request.META.get('HTTP_X_FORWARDED_FOR')

    # Если заголовок 'HTTP_X_FORWARDED_FOR' отсутствует, используем 'REMOTE_ADDR'
    if ip is None:
        ip = request.META.get('REMOTE_ADDR')
    else:
        # Если 'HTTP_X_FORWARDED_FOR' содержит несколько IP-адресов, берем первый (это IP клиента)
        ip = ip.split(',')[0]
    
    # Возвращаем IP-адрес клиента
    return ip
