from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from src.company.models import Company
from src.company.serializers import CompanyCreateSerializer, CompanyListSerializer, CompanyInformationSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def company_registration(request):
    user = request.user
    data = request.data
    user.is_seeker = False
    user.is_company = True
    company_serializer = CompanyCreateSerializer(data=data)
    if company_serializer.is_valid(raise_exception=True):
        company_serializer.save(user=user)

        return Response(company_serializer.data, status=status.HTTP_201_CREATED)

    return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def company_list(request):
    companies = Company.objects.all()
    company_list_serializer = CompanyListSerializer(data=companies, many=True)
    data = company_list_serializer.data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def about_company(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response('Does Not Exit', status=status.HTTP_404_NOT_FOUND)
    serializer = CompanyInformationSerializer(company)
    return Response(serializer.data, status=status.HTTP_200_OK)

