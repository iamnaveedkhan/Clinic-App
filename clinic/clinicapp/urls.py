from django.urls import path
from clinicapp import views

urlpatterns =[
    path('add',views.add),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
]