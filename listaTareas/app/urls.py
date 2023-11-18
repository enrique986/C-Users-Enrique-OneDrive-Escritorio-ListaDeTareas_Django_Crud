from django.urls import path
from . import views

urlpatterns=[

   path("", views.index, name="index" ),
   path("insert/", views.insert, name="insert" ),
   path("update", views.update, name="update"),
   path("update/<int:Tarea_id>",views.update_form, name="update_form"),
   path("delete/<int:Tarea_id>", views.delete, name="delete"),
  
]