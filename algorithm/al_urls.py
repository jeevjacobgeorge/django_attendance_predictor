from django.urls import path
from . import views

urlpatterns = [
  path('',views.att_pred,name='attendance'),
  path('attendance/',views.att_pred,name='attendance1'),

] 