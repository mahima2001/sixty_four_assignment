from django.urls import path

from . import views# . means current directory


app_name='assignment'
urlpatterns=[
    path("",views.index,name="index"),
    
]