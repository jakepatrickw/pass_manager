from django.contrib import admin
from django.urls import path
from password_storage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.ListPassword.as_view(), name='ListPasswords'),
    path('create/', views.CreatePassword.as_view(), name='CreatePassword'),
    path('delete/<int:id>/', views.DeletePassword.as_view(), name='DeletePassword'),
    path('update/<int:id>/', views.UpdatePassword.as_view(), name='UpdatePassword'),
]
