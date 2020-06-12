from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
	path('', views.index, name = 'list'),
	path('update/<int:pk>', views.update_task, name = 'update_task'),
	path('delete/<int:pk>', views.delete, name = 'delete'),
	path('register/', views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='tasks/logout.html'), name='logout')
]
