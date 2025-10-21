from django.urls import include, path
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet

# Base router
router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Nested router for messages inside conversation
conversation_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')



urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(conversation_router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
