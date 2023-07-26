from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('budget/', views.post_budget, name='post_budget'),
    path('expense/', views.post_expense, name='post_expense'),
        
]