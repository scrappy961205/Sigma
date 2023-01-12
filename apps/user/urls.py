from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user.views import *

app_name = 'user'

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('user/list/', UserListView.as_view(), name='user_list'),
    path('user/add/', UserCreateView.as_view(), name='user_add'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    # path('api/', include(router.urls)),
]
