from django.urls import include, path
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'conversation', ConversationViewSet)

urlpattern = [
    path("api/", include(router.urls)), # Link API views to URLs automatically
    path("api/api-auth/", include('rest_framework.urls', namespace='rest_framework'))
]