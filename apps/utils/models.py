from django.db import models
from django.contrib.auth import get_user_model


class TimestampUserMeta(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name='Created At')
    modified_at = models.DateField(auto_now=True, verbose_name='Modified At')
    created_by = models.ForeignKey(get_user_model(),
                                   default=1,
                                   on_delete=models.SET_DEFAULT,
                                   related_name='+')
    modified_by = models.ForeignKey(get_user_model(),
                                    null=True,
                                    default=None,
                                    on_delete=models.DO_NOTHING,
                                    related_name='+')

    class Meta:
        abstract = True
