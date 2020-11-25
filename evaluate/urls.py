from django.urls import path

from evaluate import views

app_name = 'evaluate'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<int:pk>/delete/', views.delete, name='delete'),
]
