from django.urls import path
from . import views

urlpatterns = [
  path('attendance',views.att_pred,name='attendance'),

]