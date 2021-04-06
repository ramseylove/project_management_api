from django.urls import path
from .views import ProjectList, ProjectDetail, IssueList, IssueDetail, IssueImageList

urlpatterns = [
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('projects/', ProjectList.as_view()),
    path('issues', IssueList.as_view()),
    path('issue/issueimages', IssueImageList.as_view()),
    path('issue/<int:pk>/', IssueDetail.as_view()),

]