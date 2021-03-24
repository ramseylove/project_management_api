from django.db import models
from django.contrib.auth import get_user_model

from apps.utils.models import TimestampUserMeta

class Client(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}'


class Project(TimestampUserMeta, models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    user = models.ForeignKey(get_user_model())
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, default='No client')

    class Priority(models.IntegerChoices):
        low = 1
        medium = 2
        high = 3

    priority = models.IntegerField(choices=Priority.choices, default=1, verbose_name='Project Priority')

    class Status(models.IntegerChoices):
        planning = 1
        ready = 2
        in_progress = 3
        in_review = 4
        finished = 5

    status = models.IntegerField(choices=Status.choices, default=1, verbose_name='Project Status')

    class __str__(self):
        return f'{self.name}'


class Issue(TimestampUserMeta, models.Model):
    summary = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Issue Description')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Status(models.IntegerChoices):
        on_hold = 1
        to_do = 2
        in_progress = 3
        in_review = 4
        done = 5

    status = models.IntegerField(choices=Status.choices, default=1, verbose_name='Issue Status')

    class Priority(models.IntegerChoices):
        low = 1
        medium = 2
        high = 3

    priority = models.IntegerField(choices=Priority.choices, default=1, verbose_name='Issue Priority')

    class IssueType(models.IntegerField):
        task = 1
        but = 2
        story = 3

    issueType = models.IntegerField(choices=IssueType.choices, default=1, verbose_name='Issue Type')

