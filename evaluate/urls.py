from django.urls import path

from evaluate import views

app_name = 'evaluate'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<int:pk>/delete/', views.delete, name='delete'),
]
