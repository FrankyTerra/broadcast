from core.api.permissions import CustomAccessPolicy


class EventTypeAccessPolicy(CustomAccessPolicy):
    """
    Права доступа типа события
    """

    statements = [
        {
            'action': ['list', 'retrieve', 'create', 'update', 'destroy'],
            'principal': ['role:admin'],
            'effect': 'allow'
        }
    ]


class EventTypeChoiceAccessPolicy(CustomAccessPolicy):
    """
    Права доступа типа события
    """

    statements = [
        {
            'action': ['list'],
            'principal': ['role:admin'],
            'effect': 'allow'
        }
    ]
