"""project16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_topic/',views.display_topic,name='display_topic'),
    path('display_webpage/',views.display_webpage,name='display_webpage'),
    path('display_delete/',views.display_delete,name='display_delete'),
    path('display_access/',views.display_access,name='display_access'),
    path('display_deletetopics/',views.display_deletetopics,name='display_deletetopics'),
    path('display_deleteaccess/',views.display_deleteaccess,name='display_deleteaccess'),
    path('update_topics/',views.update_access,name='update_topics'),
    path('update_webpage/',views.update_webpage,name='update_webpage'),
    path('update_access/',views.update_access,name='update_access'),
]
