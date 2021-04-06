from rest_framework import serializers
from .models import Project, Issue, Comment, IssueImage, CommentImage


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id',
                  'name',
                  'description',
                  'client',
                  'priority',
                  'status',)


class IssueImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueImage
        fields = ('issue_image', 'issue')


class IssueSerializer(serializers.ModelSerializer):
    issue_images = IssueImageSerializer(many=True)

    class Meta:
        model = Issue
        fields = (
            'id',
            'summary',
            'description',
            'project',
            'status',
            'priority',
            'issueType',
            'issue_images',
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'comment',
        )


class IssueImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueImage
        fields = (
            'id',
            'issue_image'
        )