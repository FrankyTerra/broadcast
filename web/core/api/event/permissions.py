from core.api.permissions import CustomAccessPolicy


class EventAccessPolicy(CustomAccessPolicy):
    """
    Права доступа события
    """

    statements = [
        {
            'action': ['list', 'retrieve'],
            'principal': ['role:user', 'role:moderator', 'role:admin'],
            'effect': 'allow'
        },
        {
            'action': ['create', 'update', 'destroy'],
            'principal': ['role:admin'],
            'effect': 'allow'
        },
    ]
