# ##queryset attribute specifies queryset used to retrieve data from database.
# ##serializer_class attribute specifies serializer class used to serialize or deserialize data for view.



# from rest_framework import generics
# from .models import Project, Task, TaskAssignment, Comment
# from .serializers import ProjectSerializer, TaskSerializer, TaskAssignmentSerializer, CommentSerializer

# class ProjectListCreate(generics.ListCreateAPIView):
#     """
#     API view to list all projects or create a new project.
#     """
#     queryset = Project.objects.all()  # retrieves all projects from db
#     serializer_class = ProjectSerializer  # serializer for Project instances

# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     API view to retrieve, update, or delete a project instance.
#     """
#     queryset = Project.objects.all()  # retrieves all projects
#     serializer_class = ProjectSerializer  # Project instances

# class TaskListCreate(generics.ListCreateAPIView):
#     """
#     API view to list all tasks or create a new task.
#     """
#     queryset = Task.objects.all()  # tasks
#     serializer_class = TaskSerializer  # Task instances

# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     API view to retrieve, update, or delete a task instance.
#     """
#     queryset = Task.objects.all()  # tasks
#     serializer_class = TaskSerializer  # Task instances

# class TaskAssignmentListCreate(generics.ListCreateAPIView):
#     """
#     API view to list all task assignments or create a new task assignment.
#     """
#     queryset = TaskAssignment.objects.all()  # all task assignments
#     serializer_class = TaskAssignmentSerializer  # TaskAssignment instances

# class TaskAssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     API view to retrieve, update, or delete a task assignment instance.
#     """
#     queryset = TaskAssignment.objects.all()  # all task assignments
#     serializer_class = TaskAssignmentSerializer  # TaskAssignment instances

# class CommentListCreate(generics.ListCreateAPIView):
#     """
#     API view to list all comments or create a new comment.
#     """
#     queryset = Comment.objects.all()  # retrieves all comments
#     serializer_class = CommentSerializer  # Comment instances

# class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     API view to retrieve, update, or delete a comment instance.
#     """
#     queryset = Comment.objects.all()  # retrieves all comments
#     serializer_class = CommentSerializer  # Comment instances




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Project, Task, TaskAssignment, Comment
from .serializers import ProjectSerializer, TaskSerializer, TaskAssignmentSerializer, CommentSerializer

class ProjectListCreate(APIView):
    """
    API view to list all projects or create a new project.
    """
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
    """
    API view to retrieve, update, or delete a project instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Project, pk=pk)
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskListCreate(APIView):
    """
    API view to list all tasks or create a new task.
    """
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    """
    API view to retrieve, update, or delete a task instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Task, pk=pk)
    
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskAssignmentListCreate(APIView):
    """
    API view to list all task assignments or create a new task assignment.
    """
    def get(self, request):
        task_assignments = TaskAssignment.objects.all()
        serializer = TaskAssignmentSerializer(task_assignments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskAssignmentDetail(APIView):
    """
    API view to retrieve, update, or delete a task assignment instance.
    """
    def get_object(self, pk):
        return get_object_or_404(TaskAssignment, pk=pk)
    
    def get(self, request, pk):
        task_assignment = self.get_object(pk)
        serializer = TaskAssignmentSerializer(task_assignment)
        return Response(serializer.data)
    
    def put(self, request, pk):
        task_assignment = self.get_object(pk)
        serializer = TaskAssignmentSerializer(task_assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        task_assignment = self.get_object(pk)
        task_assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentListCreate(APIView):
    """
    API view to list all comments or create a new comment.
    """
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    """
    API view to retrieve, update, or delete a comment instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Comment, pk=pk)
    
    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
