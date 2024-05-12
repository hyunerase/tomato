from .models import Post, Comment
from .serializers import PostSerializer, PostResponseSerializer, CommentRequestSerializer, CommentResponseSerializer, PostDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PostResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = PostDetailSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = PostResponseSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    serializer = CommentRequestSerializer(data=request.data)
    if serializer.is_valid():
        new_comment = serializer.save(post=post)
        response = CommentResponseSerializer(new_comment)
        return Response(response.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_comments(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    serializer = CommentResponseSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)