"""web_developer_pe_2_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from apps.web.views import home,Contact
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login,logout
from apps.usuarios.views import Login,CrearUsuario

urlpatterns = [
	#path('jet/', include('jet.urls', 'jet')),
    #path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('administrador/', admin.site.urls),
    path('', home, name = 'home'),
    path('blog/', include('apps.blog.urls'), name = 'blog'),
    path('contacto/', Contact, name = 'contacto'),
    path('admin/', Login.as_view() ,name='login'),
    path('admin/logout/',logout, name = 'logout'),
    path('crear_usuario/',CrearUsuario.as_view(),name = 'crear_usuario'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
