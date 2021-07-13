"""maniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from maniapp.views import PostsView
from maniapp import views
#from rest_framework.urlpatterns import format_suffix_patterns
"""from image.views import ImageView
from image import views"""
from rest_framework import routers
#from maniapp.views import ListUsers, CustomAuthToken
router = routers.DefaultRouter()

router.register(r'tasks', views.PostsView,'tasks')
#from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    #path('posts/',views.PostsView.as_view()),
    #path('posts/<int:pk>/',views.PostsView.as_view()),
    path('', include('maniapp.urls')),
    #path('api/users/', ListUsers.as_view()),
    #path('api/token/auth/', CustomAuthToken.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""