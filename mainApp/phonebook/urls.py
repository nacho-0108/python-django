from django.urls import path
from phonebook import views

app_name = 'PB'

urlpatterns = [
    path('', views.test),
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('detail/<int:userId>/', views.detail, name='D'),
    path('update/<int:userId>/', views.update, name='update'),
]

# ' ' 는 아무 값도 없다는 뜻

