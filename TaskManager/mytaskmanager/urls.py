from django.urls import path
from .views import (
    ProjectListCreate, ProjectDetail,
    TaskListCreate, TaskDetail,
    TaskAssignmentListCreate, TaskAssignmentDetail,
    CommentListCreate, CommentDetail
)

urlpatterns = [
    path('projects/', ProjectListCreate.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-assignments/', TaskAssignmentListCreate.as_view(), name='taskassignment-list-create'),
    path('task-assignments/<int:pk>/', TaskAssignmentDetail.as_view(), name='taskassignment-detail'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]
