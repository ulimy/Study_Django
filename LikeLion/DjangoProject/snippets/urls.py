from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns =[
    path('',views.snippet_List.as_view()),
    path('detail/<int:pk>',views.snippet_Detail.as_view()),
    path('user',views.UserList.as_view()),
    path('detail/<int:pk>',views.UserDetail.as_view()),
    path('api-auth',include('rest_framework.urls',namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
