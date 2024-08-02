# from django.urls import path
# from .views import RegisterView, LoginView, UserView, LogoutView

# urlpatterns = [
#     path('register', RegisterView.as_view()),
#     path('login', LoginView.as_view()),
#     path('user', UserView.as_view()),
#     path('logout', LogoutView.as_view()),
# ]

from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
