from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'alunos', AlunosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
]
