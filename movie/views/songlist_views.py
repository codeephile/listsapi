from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from movie.models import Songlist
from movie.serializers import SonglistSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def list(request):
    Slist = Songlist.objects.all()
    serializer = SonglistSerializer(Slist, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def upload(request):
    serializer = SonglistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def detail(request,pk):
    Slist = get_object_or_404(Songlist, pk=pk)
    serializer = SonglistSerializer(Slist)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def update(request, pk):
    Slist = get_object_or_404(Songlist, pk=pk)
    serializer = SonglistSerializer(Slist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def delete(request, pk):
    Slist = get_object_or_404(Songlist, pk=pk)
    Slist.delete()
    return Response({'detail': 'Song Deleted'}, status=status.HTTP_204_NO_CONTENT)