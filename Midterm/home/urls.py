
from django.urls import path
from . import views 

urlpatterns = [
     path('',views.home,name = 'home'),
     path('todo/',views.todo,name = 'todo'),
     path('taskform/',views.taskform,name = 'taskform'),
      path('taskssDelete/<str:id>/',views.taskdelete,name='taskdelete'),
path('taskUpdate/<str:id>/',views.taskupdate,name='taskupdate'),
     
]
