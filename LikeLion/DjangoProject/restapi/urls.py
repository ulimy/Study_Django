from .views import post_list,post_detail
from django.urls import path

urlpatterns = [
    path('post/',post_list,name='post-list'),
    path('post/<int:pk>/',post_detail,name='post-detail')
]
