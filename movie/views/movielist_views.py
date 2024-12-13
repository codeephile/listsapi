from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from movie.models import Movielist
from movie.serializers import MovielistSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def list(request):
    Mlist = Movielist.objects.all()
    serializer = MovielistSerializer(Mlist, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def upload(request):
    serializer = MovielistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def detail(request,pk):
    Mlist = get_object_or_404(Movielist, pk=pk)
    serializer = MovielistSerializer(Mlist)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def update(request, pk):
    Mlist = get_object_or_404(Movielist, pk=pk)
    serializer = MovielistSerializer(Mlist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def delete(request, pk):
    Mlist = get_object_or_404(Movielist, pk=pk)
    Mlist.delete()
    return Response({'detail': 'Movie Deleted'}, status=status.HTTP_204_NO_CONTENT)