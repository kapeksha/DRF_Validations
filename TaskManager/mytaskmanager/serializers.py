
##serializers are classes that provide way to control how complex data types, like querysets&model instances
##They allows to translate data in your Django models into formats like JSON or XML, which can rendered into HTTP responses.


# from rest_framework import serializers
# from .models import Project, Task, TaskAssignment, Comment

# class ProjectSerializer(serializers.ModelSerializer):
#     """
#     Serializer for Project model.
#     """
#     class Meta:
#         model = Project
#         fields = '__all__'

# class TaskSerializer(serializers.ModelSerializer):
#     """
#     Serializer for Task model.
#     """
#     class Meta:
#         model = Task
#         fields = '__all__'

# class TaskAssignmentSerializer(serializers.ModelSerializer):
#     """
#     Serializer for TaskAssignment model.
#     """
#     class Meta:
#         model = TaskAssignment
#         fields = '__all__'

# class CommentSerializer(serializers.ModelSerializer):
#     """
#     Serializer for Comment model.
#     """
#     class Meta:
#         model = Comment
#         fields = '__all__'


from rest_framework import serializers
from .models import Project, Task, TaskAssignment, Comment
from django.utils import timezone

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Project name must be at least 3 characters long.")
        return value


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value


class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = '__all__'

    def validate(self, data):
        if data['user'] is None:
            raise serializers.ValidationError("User must be assigned.")
        if data['task'] is None:
            raise serializers.ValidationError("Task must be assigned.")
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment text cannot be empty.")
        return value



