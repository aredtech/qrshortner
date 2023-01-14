from rest_framework.serializers import ModelSerializer
from .models import ShortUrls
from accounts.serializers import UserSerializer
import uuid


class UrlSerializer(ModelSerializer):
    
    class Meta:
        model = ShortUrls
        fields = ["url", 'created_at', 'last_modified_at', 'count']
        