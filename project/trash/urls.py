from django.urls import path


from . import views

urlpatterns = [
    path('', views.welcome, name='index'),
    path('about_us/', views.about_us),

]
