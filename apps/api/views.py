from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response

from .models import Project, Issue, Comment, IssueImage, CommentImage
from .serializers import \
    ProjectSerializer, \
    IssueSerializer, \
    CommentSerializer, \
    IssueImageSerializer, \
    CommentImageSerializer

# TODO create relations between objects related_name like issues to issue_images
# TODO Ability to upload images to Issue or Comment with nested serialization
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'project_id'

    def get_queryset(self):
        user = get_user_model()
        if self.request.user.is_authenticated:
            user = user.objects.get(id=self.request.user.id)
            profile = user.userprofile
            print(type(profile))
        else:
            user = user.objects.get(id=1)
            profile = user.userprofile
        return super(ProjectList, self).get_queryset().filter(userprofile=profile)


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'project_id'


class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.filter()
    serializer_class = IssueSerializer
    # lookup_field = 'issue_id'

    def get_queryset(self):
        if self.kwargs['project_id']:
            queryset = Issue.objects.filter(project_id=self.kwargs['project_id'])
            if queryset.exists():
                return queryset
            else:
                raise NotFound(f'Project not found')
        else:
            raise NotFound(f'Project id not found in url')

    def perform_create(self, serializer):
        # issue_id = self.request.data['issue']
        # issue = Issue.objects.filter(pk=issue_id)
        if self.kwargs['project_id']:
            queryset = Project.objects.filter(pk=self.kwargs['project_id'])
            if queryset.exists():
                serializer.save(project=queryset.first())
            else:
                raise NotFound(f'Comment does not exist for the id: {issue_id}')


class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    lookup_url_kwarg = 'issue_id'


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'issue_id'

    def get_queryset(self):
        if self.kwargs['issue_id']:
            queryset = Comment.objects.filter(issue_id=self.kwargs['issue_id'])
            if queryset.exists():
                return queryset
            else:
                raise NotFound(f'Issue not found')
        else:
            raise NotFound(f'Issue id not found in url')

    def perform_create(self, serializer):
        issue_id = self.kwargs['issue_id']
        issue = Issue.objects.filter(pk=issue_id)
        if issue.exists():
            serializer.save(issue=issue.first())
        else:
            raise NotFound(f'Comment does not exist for the id: {issue_id}')


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'


class CommentImageList(generics.ListCreateAPIView):
    serializer_class = CommentImageSerializer
    lookup_field = 'comment_id'

    def get_queryset(self):
        if self.kwargs['comment_id']:
            queryset = CommentImage.objects.filter(comment_id=self.kwargs['comment_id'])
            if queryset.exists():
                return queryset
            else:
                raise NotFound(f'Comment not found')
        else:
            raise NotFound(f'Comment id not found in url')

    def perform_create(self, serializer):
        comment_id = self.kwargs['comment_id']
        comment = Comment.objects.filter(pk=comment_id)
        if comment.exists():
            serializer.save(comment=comment.first())
        else:
            raise NotFound(f'Comment does not exist for the id: {comment_id}')


class IssueImageList(generics.ListCreateAPIView):
    serializer_class = IssueImageSerializer
    lookup_field = 'issue_id'

    def get_queryset(self):
        if self.kwargs['issue_id']:
            queryset = IssueImage.objects.filter(issue_id=self.kwargs['issue_id'])
            if queryset.exists():
                return queryset
            else:
                raise NotFound(f'Issue not found')
        else:
            raise NotFound(f'Issue id not found in url')

    def perform_create(self, serializer):
        issue_id = self.kwargs['issue_id']
        issue = Issue.objects.filter(pk=issue_id)
        if issue.exists():
            serializer.save(comment=issue.first())
        else:
            raise NotFound(f'Comment does not exist for the id: {issue_id}')

