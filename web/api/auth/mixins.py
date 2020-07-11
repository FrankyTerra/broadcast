from rest_framework import exceptions


class GetRequestUserAsObjectMixin:
    def get_object(self) -> 'User':
        user = self.request.user

        if not user:
            raise exceptions.NotFound

        return user
