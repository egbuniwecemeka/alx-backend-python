from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializers = ConversationSerializer
    permissions = permissions.IsAuthenticated

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message
    serializers = MessageSerializer
    permissions = permissions.IsAuthenticated