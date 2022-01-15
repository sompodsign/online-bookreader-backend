from django.urls import path
from .views import UserViewSet as sompod


urlpatterns = [
    path('', sompod.as_view({'get': 'list'}), name='hi'),
    ]
