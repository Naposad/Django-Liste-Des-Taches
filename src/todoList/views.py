from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, TemplateView
from .models import ToDo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class CreateTodo(CreateView):
    model = ToDo
    template_name = 'todo/create_todo.html'
    fields = ['name', 'date', 'date_end', 'completed']
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        # Associer l'utilisateur connecté comme auteur de la tâche
        form.instance.mytodo = self.request.user
        return super().form_valid(form)


class ToDoList(ListView, LoginRequiredMixin):
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        # Filtrer les tâches pour l'utilisateur connecté
        return ToDo.objects.filter(mytodo=self.request.user)


class DeleteTodo(PermissionRequiredMixin, DeleteView, LoginRequiredMixin):
    model = ToDo
    success_url = reverse_lazy('todo-list')
    template_name = 'todo/delete_todo.html'
    permission_required = ['ToDo.delete_todo']


class EditerTodo(PermissionRequiredMixin, UpdateView, LoginRequiredMixin):
    model = ToDo
    template_name = 'todo/update_todo.html'
    fields = ['name', 'completed']
    success_url = reverse_lazy('todo-list')
    permission_required = ['ToDo.change_todo']


class Accueil(TemplateView):
    template_name = 'todo/todo.html'
