from rest_framework import serializers
from .models import User, Message, Conversation

class UserSerializer(serializers.HyperlinkedModeSerializer): # Hyperlinking - Good RESTful design
    user_id = serializers.CharField(max_length=100)
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email',
                  'password_hash', 'phone_number', 'role', 'created_at', 'full_name'
                  ]

class MessageSerializer(serializers.HyperlinkedModeSerializer):
    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'message_body', 'sent_at']

class ConversationSerializer(serializers.HyperlinkedModeSerializer):
    class Meta:
        fields = Conversation
        name = ['conversation_id', 'participants_id', 'created_at']
