from django.contrib import admin
from django.urls import path, include
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]


# 127.0.0.1:8000 기본 url
# 127.0.0.1:8000/ 