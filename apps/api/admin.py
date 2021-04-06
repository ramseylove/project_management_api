from django.contrib import admin
from .models import Client, Project, Issue, IssueImage

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Issue)
admin.site.register(IssueImage)

