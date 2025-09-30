from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Project
from django.contrib.auth.mixins import LoginRequiredMixin   
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    
#Projects
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "core/project_list.html"
    context_object_name = "projects"
    
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "core/project_form.html"
    fields = ['name', 'description']
    success_url = reverse_lazy('core:project_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "core/project_detail.html"
    
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'description']
    template_name = "core/project_form.html"
    success_url = reverse_lazy('core:project_list')
    
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "core/project_confirm_delete.html"
    success_url = reverse_lazy('core:project_list')
    
#Tasks
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "core/task_list.html"
    context_object_name = "tasks"
    
    def get_queryset(self):
        qs =Task.objects.filter(project__owner=self.request.user)
        status = self.request.GET.get("status")
        priority = self.request.GET.get("priority")
        if status:
            qs = qs.filter(status=status)
        if priority:
            qs = qs.filter(priority=priority)
        return qs.order_by('due_date')
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "core/task_form.html"
    fields = ['title', 'description', 'project', 'assigned_to', 'status', 'priority', 'due_date']
    success_url = reverse_lazy('core:task_list')
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "core/task_detail.html"

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'project', 'assigned_to', 'status', 'priority', 'due_date']
    template_name = "core/task_form.html"
    success_url = reverse_lazy('core:task_list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "core/task_confirm_delete.html"
    success_url = reverse_lazy('core:task_list')