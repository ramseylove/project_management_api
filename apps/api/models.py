from datetime import datetime
from django.db import models
from django.utils.deconstruct import deconstructible
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
import os

from apps.utils.models import TimestampUserMeta


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        timestamp = str(datetime.now().timestamp()).split('.')[0]
        if instance.issue_id:
            filename = f"{instance.issue_id}/{timestamp}-{instance.issue.id}.{ext}"
        elif instance.issue_id and instance.comment.id:
            filename = f"{instance.issue_id}/comment_images/{timestamp}-{instance.comment.id}.{ext}"
        else:
            filename = f"{timestamp}-no_issue-comment.{ext}"  # should throw error

        return os.path.join(self.path, filename)


issue_images_folder = PathAndRename('/issue_images')


class Client(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}'


class Project(TimestampUserMeta, models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.SET_DEFAULT, default=1)

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

    def __str__(self):
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

    class IssueType(models.IntegerChoices):
        task = 1
        bug = 2
        story = 3

    issueType = models.IntegerField(choices=IssueType.choices, default=1, verbose_name='Issue Type')

    def __str__(self):
        return f'{self.summary}'


class Comment(TimestampUserMeta, models.Model):
    comment = models.TextField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment}'


class IssueImage(TimestampUserMeta, models.Model):
    issue_image = ProcessedImageField(upload_to=issue_images_folder,
                                      processors=[ResizeToFit(1000)],
                                      format='JPEG',
                                      options={'quality': 90})
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="issue_images")


class CommentImage(TimestampUserMeta, models.Model):
    comment_image = ProcessedImageField(upload_to=issue_images_folder,
                                        processors=[ResizeToFit(1000)],
                                        format='JPEG',
                                        options={'quality': 90})
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
