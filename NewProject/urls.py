"""NewProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from assignment import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("assignment.urls")),
    path('works/',views.WorkViewSet.as_view(),name="works"),
    path('artists/',views.ArtistViewSet.as_view(),name="artists"),
    path('clients/',views.Clients,name="clients"),
    path('users/',views.UserViewSet.as_view(),name="users"),
    path('registration/',views.UserCreate,name="register"),
    path('artistcreate/',views.CreateArtist,name="create_artist"),
    path('clientcreate/',views.CreateClient,name="create_client"),
    path('workcreate/',views.CreateWork,name="create_work"),


]
