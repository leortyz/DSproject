from django.urls import path
from trash.views import *
from rest_framework.authtoken import views

urlpatterns = [
    path('', Home.as_view()),
    path('about_us/', about_us),

]
