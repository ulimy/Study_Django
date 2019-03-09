from django.urls import path
from snippets import views

urlpatterns =[
    path('',views.snippet_List),
    path('detail/<int:pk>',views.snippet_Detail),
]
