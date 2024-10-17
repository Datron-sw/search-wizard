from django.urls import path
from . import views 


urlpatterns = [
    path('',views.home_redirect),
    path('google/',views.google, name='google'),
    path('yandex/',views.yandex, name='yandex'),
    path('brave/',views.brave, name='brave'),  
    path('edge/',views.edge, name='edge'),
    path('tara/',views.tarayici_seçimi, name='tara'),
]
