from core.api.permissions import CustomAccessPolicy


class CommentAccessPolicy(CustomAccessPolicy):
    """
    Права доступа коментария
    """

    statements = [
        {
            'action': ['list', 'retrieve'],
            'principal': ['role:user', 'role:moderator', 'role:admin'],
            'effect': 'allow'
        },
        {
            'action': ['create'],
            'principal': ['role:user', 'role:moderator', 'role:admin'],
            'effect': 'allow'
        },
        {
            'action': ['destroy'],
            'principal': ['role:user'],
            'effect': 'allow',
            'condition': 'is_author',
        },
        {
            'action': ['destroy'],
            'principal': ['role:moderator', 'role:admin'],
            'effect': 'allow'
        },
    ]

    def is_author(self, request, view, action) -> bool:
        """
        Проверка: пользователь является автором объекта
        """
        comment = view.get_object()
        return request.user == comment.user
