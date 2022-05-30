from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Article
from .comment import CommentSerializer

User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')

    comments = CommentSerializer(many=True, read_only=True)
    
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'movie_title','created_at', 'updated_at', 'user', 'like_users','comments',)

class ArticleListSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('id', 'username')

    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'movie_title','comment_count', 'like_count',)

