from rest_framework import serializers
from .models import User, Message, Conversation

class UserSerializer(serializers.HyperlinkedModelSerializer): # Hyperlinking - Good RESTful design
    user_id = serializers.CharField(max_length=100)
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email',
                  'password_hash', 'phone_number', 'role', 'created_at', 'full_name'
                  ]
    
    def validate(self, data):
        if data['role'] == 'admin' and data['first_name'] == '':
            raise serializers.ValidationError('Admins must have a first name')
        return data
    
    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError('Emails must be gmail.com')
        return value

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'message_body', 'sent_at']

class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = Conversation
        name = ['conversation_id', 'participants_id', 'created_at']
