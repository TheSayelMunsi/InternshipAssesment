from django.urls import include, path
from rest_framework import routers
from .views import *
from assignment import views
# router = routers.DefaultRouter()
# router.register(r'clients', ClientViewSet)
# router.register(r'registration', UserViewSet)
# router.register(r'Work', WorkViewSet)

# router.register(r'Artist', ArtistViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls')),
# ]