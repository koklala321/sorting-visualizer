from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mergeSort/', views.mergeSort, name="mergeSort"),
    path('quickSort/', views.quickSort, name="quickSort"),
    path('selectionSort/', views.selectionSort, name="selectionSort"),
    path('bubbleSort/', views.bubbleSort, name="bubbleSort")
]