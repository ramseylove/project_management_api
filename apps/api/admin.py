from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Client, Project, Issue, IssueImage


class ProjectAdmin(GuardedModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Client)
admin.site.register(Issue)
admin.site.register(IssueImage)

