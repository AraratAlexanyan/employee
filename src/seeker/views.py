from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import CreateSeekerSerializer, SeekerInfoSerializer
from .models import Seeker


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def seeker_registration(request):
    user = request.user
    data = request.data
    user.is_seeker = True
    user.is_company = False
    seeker_serializer = CreateSeekerSerializer(data=data)
    if seeker_serializer.is_valid(raise_exception=True):
        seeker_serializer.save(user=user)
        return Response(seeker_serializer.data, status=status.HTTP_201_CREATED)
    return Response(seeker_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def seeker_info(request, pk):
    try:
        seeker = Seeker.objects.get(id=pk)

    except Seeker.DoesNotExist:
        return Response('User does exist')
    serializer_data = SeekerInfoSerializer(seeker).data
    return Response(serializer_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def seekers_list(request):
    try:
        seeker = Seeker.objects.prefetch_related('education')

    except Seeker.DoesNotExist:
        return Response('User does exist')
    serializer_data = SeekerInfoSerializer(seeker, many=True).data
    return Response(serializer_data, status=status.HTTP_200_OK)
