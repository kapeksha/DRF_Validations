from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """
    Model to represent project.

    Attributes:
        name (str): name of project.
        description (str): description of project.
        start_date (date): start date of project.
        end_date (date): end date of project.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name_plural = "Projects" #For the plural verbose name display

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Model to represent a task.

    Attributes:
        name (str): name of task.
        description (str): description of task.
        status (str): current status of the task. Choices: 'to-do', 'in-progress', 'completed'.
        priority (int): priority of task.
        deadline (date): deadline for task.
        project (Project): project to which task belongs.
    """
    STATUS_CHOICES = [
        ('to-do', 'To Do'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.IntegerField()
    deadline = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Tasks" #For the plural verbose name display

    def __str__(self):
        return self.name


class TaskAssignment(models.Model):
    """
    Model to represent assignment of task to user.

    Attributes:
        task (Task): task being assigned.
        user (User): user to whom task is assigned.
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "TaskAssignments" #For the plural verbose name display

    def __str__(self):
        return f"{self.task.name}"


class Comment(models.Model):
    """
    Model to represent comment on task.

    Attributes:
        commenter_name (str): name of commenter.
        email (str): email of commenter.
        content (str): content of comment.
        task (Task): task on which comment is made.
    """
    commenter_name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comments" #For the plural verbose name display

    def __str__(self):
        return self.content