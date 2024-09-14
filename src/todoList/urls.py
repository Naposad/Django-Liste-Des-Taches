from django.urls import path, include
from .views import CreateTodo, ToDoList, DeleteTodo, EditerTodo, Accueil
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('todo/', CreateTodo.as_view(), name='create-todo'),
    path('', ToDoList.as_view(), name='todo-list'),
    path('<str:slug>/todo-update/', EditerTodo.as_view(), name='update-todo'),
    path('<str:slug>/delete/', DeleteTodo.as_view(), name='delete-todo'),
    path('accueil/', Accueil.as_view(), name='accueil')
]