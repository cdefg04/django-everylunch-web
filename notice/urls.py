from django.urls import path

from notice import views

app_name = 'notice'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('modify/<int:pk>/', views.modify, name='modify'),
    path('detail/<int:pk>/delete/', views.delete, name='delete'),
]
