from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage),
    path('count/', views.count, name='count')
]

urlpatterns += staticfiles_urlpatterns()