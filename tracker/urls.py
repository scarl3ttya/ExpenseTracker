from django.urls import path
from .views import index, post_budget

app_name = 'tracker'

urlpatterns = [
    path('', index, name='index'),
    path('budget/', post_budget, name='post_budget'),
        
]