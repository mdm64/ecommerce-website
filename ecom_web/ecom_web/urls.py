
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from user import views as views_1
from django.contrib.auth import views as views_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('signup/',views_1.signUpForm, name='signup-page' ),
    path('login/', views_2.LoginView.as_view(template_name = 'user/login.html'), name='login-page'),
    path('logout/', views_2.LogoutView.as_view(template_name = 'user/logout.html'), name='logout-page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)