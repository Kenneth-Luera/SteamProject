from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.UserViews import RegisterUserViewSet, UsersViewSet
from .views.GamesViews import JuegosViewSet


router = DefaultRouter()
router.register(r'register', RegisterUserViewSet, basename='register')
router.register(r'users', UsersViewSet, basename='users')
router.register(r'juegos', JuegosViewSet, basename='juegos')

urlpatterns = [
    path('', include(router.urls)),

    path('juegos/<int:pk>/', JuegosViewSet.as_view({'put': 'put', 'delete': 'delete'}), name='juego-detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]