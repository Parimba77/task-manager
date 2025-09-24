from django.contrib import admin
from .models import Project, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=('name', 'owner', 'created_at')
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('title', 'project', 'status', 'priority', 'assigned_to')
    list_filter=('status', 'priority', 'project')