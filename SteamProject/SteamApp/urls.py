from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.UserViews import RegisterUserViewSet, UsersViewSet
from .views.GamesViews import JuegosViewSet
from .views.ProfileViews import EditProfileViewSet, PublicProfileViewSet, CustomTokenObtainPairView
from .views.BibliotecaViews import JuegosBibliotecaViewSet, JuegosBibliotecaPostViewSet
from .views.ChatViews import MensajesViewSet



router = DefaultRouter()
router.register(r'register', RegisterUserViewSet, basename='register')
router.register(r'users', UsersViewSet, basename='users')
router.register(r'juegos', JuegosViewSet, basename='juegos')
router.register(r'profiles', PublicProfileViewSet, basename='profiles')
router.register(r'juegosbiblioteca', JuegosBibliotecaViewSet, basename='juegosbiblioteca')



urlpatterns = [
    path('', include(router.urls)),


    path('chat/<int:pk>/', MensajesViewSet.as_view({'get': 'list'}), name='mensajes-list'),
    path('juegosbiblioteca/add', JuegosBibliotecaPostViewSet.as_view({'post': 'post'}), name='juegosbiblioteca-post'),
    path('juegos/<int:pk>/', JuegosViewSet.as_view({'put': 'put', 'delete': 'delete'}), name='juego-detail'),
    path('editprofile/<int:pk>/', EditProfileViewSet.as_view({'put': 'put'}), name='profile-detail'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]