from django.urls import include, path
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet

router = routers.NestedDefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'conversations', ConversationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]