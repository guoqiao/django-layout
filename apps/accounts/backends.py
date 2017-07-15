from django.contrib.auth.backends import ModelBackend
from . import models as m

UserModel = m.UserProxy


class UserProxyModelBackend(ModelBackend):
    """
    Make sure request.user is a UserProxy object.
    """
    def get_user(self, user_id):
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None


