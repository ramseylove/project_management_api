from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from .models import Project, Issue, Comment, IssueImage, CommentImage
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer, IssueImageSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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


class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.filter()
    serializer_class = IssueSerializer

    def get_queryset(self):
        queryset = Issue.objects.all()
        project_id = self.request.query_params.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        # return self.queryset.filter(project_id=self.kwargs['project_id'])
        return queryset


class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(issue_id=self.kwargs['pk'])


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class IssueImageList(generics.ListCreateAPIView):
    serializer_class = IssueImageSerializer

    def get_queryset(self):
        queryset = IssueImage.objects.all()
        issue_id = self.request.query_params.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(issue_id=issue_id)
        return queryset
        # return self.queryset.filter(issue_id=self.kwargs['issue_id'])

    def create(self, request, *args, **kwargs):
        issue = None
        issue_image = request.data

        if request.query_params.get('issue_id'):
            issue = Issue.objects.get(pk=request.query_params.get('issue_id'))
            print(issue)
            if issue:
                new_image = IssueImage.objects.create(issue_image=issue_image['issue_image'], issue=issue)
            else:
                return Response("issue_required", status=status.HTTP_400_BAD_REQUEST)

        new_image.save()

        serializer = IssueImageSerializer(new_image)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

