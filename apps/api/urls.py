from django.urls import path
from .views import ProjectList, ProjectDetail, IssueList, IssueDetail

urlpatterns = [
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('projects/', ProjectList.as_view()),
    path('issues/<int:pk>/', IssueList.as_view()),
    path('issue/<int:pk>/', IssueDetail.as_view())
]