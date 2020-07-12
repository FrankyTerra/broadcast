from core.api.permissions import CustomAccessPolicy


class BroadcastAccessPolicy(CustomAccessPolicy):
    """
    Права доступа трансляции
    """

    statements = [
        {
            'action': ['list', 'retrieve', 'create', 'update', 'destroy'],
            'principal': ['role:admin'],
            'effect': 'allow'
        },
        {
            'action': ['list', 'retrieve'],
            'principal': ['role:user', 'role:moderator'],
            'effect': 'allow'
        },
    ]
