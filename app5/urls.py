from app5.views import *
from django.urls import path
app_name='uday'
urlpatterns=[
    path('uday/',uday,name='uday'),
]