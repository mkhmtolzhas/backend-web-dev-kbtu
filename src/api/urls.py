from django.urls import include, path
from register.views import RegisterView
from llm.views import LLMView
from chat.views import ChatViewSet
from message.views import MessageViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


router = DefaultRouter()

router.register(r'chat', ChatViewSet, basename='chat')
router.register(r'message', MessageViewSet, basename='message')


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='register'),
    path('llm/', LLMView.as_view(), name='llm'),
]
