from django.contrib import admin
from .models import Client, Project, Issue

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Issue)

