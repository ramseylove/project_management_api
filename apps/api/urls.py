from django.urls import path
from .views import ProjectList, ProjectDetail, IssueList, IssueDetail, IssueImageList, CommentList, CommentDetail, CommentImageList

urlpatterns = [
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('projects/', ProjectList.as_view()),
    path('issues', IssueList.as_view()),
    path('issues/issueimages', IssueImageList.as_view()),
    path('issues/<int:issue_id>/', IssueDetail.as_view()),
    path('issues/comments', CommentList.as_view()),
    path('issues/comments/<int:comment_id>/images/', CommentImageList.as_view()),
    path('issues/comments/<int:comment_id>/', CommentDetail.as_view()),

]