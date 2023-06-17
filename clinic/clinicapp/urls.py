from django.urls import path
from clinicapp import views

urlpatterns =[
    path('create',views.create),
    path('delete',views.delete),
    path('edit',views.edit),
]