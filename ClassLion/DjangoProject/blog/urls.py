from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('detail/<int:blog_pk>',views.detail,name="detail"),
    path('new/',views.new,name='new'),
    path('create/',views.create,name="create")
]
