from django.urls import path
from clinicapp import views

urlpatterns =[
    path('add',views.add),
    path('delete',views.delete),
    path('edit',views.edit),
]