from django.contrib import admin
from .models import Project, Task, TaskAssignment, Comment

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'end_date']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'status', 'priority', 'deadline', 'project']


class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ['task','user']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['commenter_name','email','content','task']

# Registering models with their respective admin configurations
# admin.site.register()used to associate each model with its corresponding admin configuration.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskAssignment, TaskAssignmentAdmin)
admin.site.register(Comment, CommentAdmin)