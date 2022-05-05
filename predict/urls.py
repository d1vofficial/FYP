from django.urls import path,include
from . import views

app_name = 'predict'

urlpatterns = [
    path('', views.predict ,name = 'predict'),
    path('predict/', views.predict_changes ,name = 'submit_prediction'),
]
