from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from posts.models import Post
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer
from posts.serializers import PostSerializer


class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryPostsAPIView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        posts = Post.objects.filter(category=category)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)