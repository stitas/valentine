from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('quiz', views.quiz, name='quiz'),
    path('valentinas', views.valentinee, name='valentine'),
    path('end',views.end, name='end'),
    path('no_end', views.no_end, name='no_end')
]
