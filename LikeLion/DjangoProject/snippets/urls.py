from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    path('',views.snippet_List),
    path('detail/<int:pk>',views.snippet_Detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
