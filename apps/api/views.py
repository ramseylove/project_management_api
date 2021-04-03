from rest_framework import generics
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.filter()
    serializer_class = IssueSerializer

    def get_queryset(self):
        return self.queryset.filter(project_id=self.kwargs['pk'])


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
