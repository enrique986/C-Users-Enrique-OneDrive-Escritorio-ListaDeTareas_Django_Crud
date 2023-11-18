from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Tarea
from django.urls import reverse

def index(request):
    template= loader.get_template("app/index.html")
    db_data=Tarea.objects.all()
    context = {
        "db_data":db_data[::-1],
        "update":None
    }
    
    #return HttpResponse(template.render(context))
    return render(request,"app/index.html",context)

def insert(request):
    try:
          Tarea_subject = request.POST["subject"]
          Tarea_description = request.POST["description"]
          if Tarea_subject =="" or Tarea_description =="":
               raise ValueError("el texto no puede estar vacio") 
          db_data = Tarea(subject=Tarea_subject, description = Tarea_description)
          db_data.save()
          return HttpResponseRedirect(reverse("index"))
    except ValueError as err:
         print (err)
         return HttpResponseRedirect(reverse("index"))
    
def update(request):
     Tarea_id = request.POST["id"]
     Tarea_subject = request.POST["subject"]
     Tarea_description = request.POST["description"] 
     db_data =Tarea.objects.get(pk=Tarea_id)
     db_data.subject = Tarea_subject
     db_data.description = Tarea_description
     db_data.save()
     return HttpResponseRedirect(reverse("index"))
    
def update_form(request,Tarea_id):
     db_data = Tarea.objects.all()
     db_data_only = Tarea.objects.get(pk=Tarea_id)
     print (db_data_only)
     context ={
          "db_data":db_data[::-1],
          "update":db_data_only
     }
     return render(request,"app/index.html",context)

    
def delete(request, Tarea_id):
     db_data = Tarea.objects.filter(id=Tarea_id)
     db_data.delete()
     return HttpResponseRedirect(reverse("index"))

