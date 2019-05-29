from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('<int:blog_id>',views.detail,name='detail'),
    path('new',views.new,name='new'),
    path('edit/<int:blog_id>',views.edit, name="edit"),
    path('delete/<int:blog_id>',views.delete, name="delete"),
    path('create',views.create, name='create'),
]
