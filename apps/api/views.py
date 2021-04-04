from rest_framework import generics
from .models import Project, Issue, Comment, IssueImage, CommentImage
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer, IssueImageSerializer


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
    queryset = IssueImage.objects.all()
    serializer_class = IssueImageSerializer

    def get_queryset(self):
        return self.queryset.filter(issue_id=self.kwargs['issue_id'])
