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


class ProjectSerializer(serializers.ModelSerializer):
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
