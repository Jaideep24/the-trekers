"""trekkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from trekkapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('trek/<int:pk>/', Detailedtrek.as_view(), name='detail_article'),
    path('cycling/<int:pk>/', DetailedCycle.as_view(), name='detail_cycle'),
    path('camping/<int:pk>/', DetailedCamp.as_view(), name='detail_camp'),
    path('tour/<int:pk>/', Detailedtour.as_view(), name='detail_tour'),
    path('contact', contact, name='contactform'),
    path('personaltrek', personal, name='personalform'),
    path('api/city',data_city),
    path('api/camping',data_camping),
    path('api/cycling',data_cycling),
    path('api/tours',data_tours),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)