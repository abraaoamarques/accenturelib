from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import CommentSerializer
import datetime
# Create your views here.

@api_view(['POST'])
def comment_list(request):
    if request.method == 'POST':
        comment_data = request.data
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)