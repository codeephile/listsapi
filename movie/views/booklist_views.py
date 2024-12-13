from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from movie.models import Booklist
from movie.serializers import BooklistSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def list(request):
    Blist = Booklist.objects.all()
    serializer = BooklistSerializer(Blist, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def upload(request):
    serializer = BooklistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def detail(request,pk):
    Blist = get_object_or_404(Booklist, pk=pk)
    serializer = BooklistSerializer(Blist)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def update(request, pk):
    Blist = get_object_or_404(Booklist, pk=pk)
    serializer = BooklistSerializer(Blist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def delete(request, pk):
    Blist = get_object_or_404(Booklist, pk=pk)
    Blist.delete()
    return Response({'detail': 'Book Deleted'}, status=status.HTTP_204_NO_CONTENT)