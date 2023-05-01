from rest_framework import serializers
from . import models


class SeekerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seeker
        fields = ('full_name', 'phone_number', 'citizen', 'skills', "languages", "github_acc",
                  "linkedin_acc", "gender", "hobbies", "about", "profile_image", "education")
        depth = 2


class CreateSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seeker
        fields = ('full_name', 'phone_number', 'skills', 'languages', 'gender')


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.University
        fields = ('name', 'location')
