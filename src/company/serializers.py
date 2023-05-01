from rest_framework import serializers
from .models import Company


class CompanyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('company_name', 'industry', 'contact_phone',)


class CompanyInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
        depth = 2


class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('company_name', 'industry',)
