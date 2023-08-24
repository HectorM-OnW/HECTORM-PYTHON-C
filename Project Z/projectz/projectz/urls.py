
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reportes/', include("reportes.urls"),),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout,name='logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset_form.html"), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_complete.html"), name='password_reset_complete')
]

