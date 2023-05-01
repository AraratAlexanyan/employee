from django.core.validators import FileExtensionValidator
from django.db import models

from services.image_services import get_path_upload_avatar_user, validate_profile_image_size
from src.base_user.models import BaseAccount
from src.job.models import Job


class Seeker(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    user = models.OneToOneField(BaseAccount, on_delete=models.CASCADE, related_name='seeker', default=None)

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16)
    citizen = models.CharField(max_length=64, blank=True, null=True)
    skills = models.TextField()
    first_login = models.DateTimeField(blank=True, null=True)
    languages = models.TextField()
    github_acc = models.URLField(blank=True, null=True)
    linkedin_acc = models.URLField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    hobbies = models.TextField(blank=True, null=True)
    education = models.ManyToManyField('University', default=1, blank=True, null=True, related_name="seekers")
    about = models.TextField(max_length=2048, blank=True, null=True)
    applied_jobs = models.ForeignKey(Job, default=None, on_delete=models.SET_NULL, blank=True, null=True)

    profile_image = models.ImageField(
        default='user_image_def.jpg',
        upload_to=get_path_upload_avatar_user,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'bmp']),
                    validate_profile_image_size]
    )

    def __str__(self):
        return self.full_name


class University(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name
