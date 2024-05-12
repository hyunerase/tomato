from rest_framework import serializers
from .models import Post, Comment
from django.utils import timezone

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']


class PostResponseSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at']

    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')

class CommentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']

class CommentResponseSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')

class PostDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    comments = CommentResponseSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        exclude=["user"]
    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')