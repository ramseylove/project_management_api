from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin

from .models import Project, Issue, Comment, IssueImage, CommentImage

# TODO Make Images writeable through Issue or Comment with nested serialization


class IssueImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueImage
        fields = (
            'id',
            'issue_image',
            'issue',
        )
        read_only_fields = ['issue']


class IssueSerializer(serializers.ModelSerializer):
    issue_images = IssueImageSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = (
            'id',
            'summary',
            'description',
            # 'project',
            'status',
            'priority',
            'issueType',
            'issue_images',
        )
        depth = 1


class ProjectSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    issues = IssueSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id',
                  'name',
                  'description',
                  'client',
                  'priority',
                  'status',
                  'issues',)
        depth = 1

    def get_permissions_map(self, created):
        # current_user = self.context['request'].user
        customer_user = Group.objects.get(name='customer_user')
        customer_manager = Group.objects.get(name='customer_manager')
        developer = Group.objects.get(name='developer')
        admin_manager = Group.objects.get(name='admin_manager')

        return {
            'view_project': [customer_user, customer_manager, developer, admin_manager],
            'add_project': [admin_manager],
            'change_project': [admin_manager],
            'delete_project': [admin_manager]
        }


class CommentImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentImage
        fields = (
            'id',
            'comment_image',
            'comment',
        )
        read_only_fields = ['comment']


class CommentSerializer(serializers.ModelSerializer):
    comment_images = CommentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'comment',
            'comment_images',
        )
