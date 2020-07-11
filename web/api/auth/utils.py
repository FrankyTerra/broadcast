

def jwt_response_payload_handler(token, user=None, request=None):
    """
    Переопределенный метод чтобы возвращать смевте с токеном id пользователя
    """
    return {
        'token': token,
        'user_id': user.id,
    }
