from django.contrib.auth.models import PermissionsMixin


class CustomPermissionsMixin(PermissionsMixin):

    def has_perm(self, perm, obj=None):

        if self.is_active and self.is_admin:
            return True

        return super().has_perm(self, perm, obj)