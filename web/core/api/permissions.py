from typing import List
from rest_access_policy import AccessPolicy


class CustomAccessPolicy(AccessPolicy):
    """
    Кастомная проверка прав
    """
    group_prefix = 'role:'

    def get_user_group_values(self, user) -> List[str]:
        if user.role:
            return [user.role]
        return []

    def has_permission(self, request, view) -> bool:
        if request.user.is_superuser:
            return True
        return super().has_permission(request, view)
