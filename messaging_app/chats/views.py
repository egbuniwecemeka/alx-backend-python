from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


# Create your views here.
""" 
    DRF ModelViewSet expects certain class attributes

    eg queryset, serializer_class, permission_classes,
    ordering_fields, search_fields, filterset_fields, filter_backends
    etc.
"""
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Enabling filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['conversation', 'sender_id']    # exact matches
    search_fields = ['message_body']    # search by test
    ordering_fields = ['sent_at']  # sorts by time

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(sender_id=request.data)

        return Response(
            {"message": "Message sent successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )
