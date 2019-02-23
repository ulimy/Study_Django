from . import views
from django.urls import path
# media 사용을 위해 settings 필요
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.portfolio,name="portfolio"),
]

# 이미 setting.py 에서 url을 정의 했으므로 이를 더하기만 하면 됨
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
