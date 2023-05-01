from django.core.validators import FileExtensionValidator
from django.db import models

from services.image_services import get_path_upload_avatar_company, validate_profile_image_size
from src.base_user.models import BaseAccount
from src.job.models import Job


class Company(models.Model):
    user = models.OneToOneField(BaseAccount, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=64, verbose_name='Company name')
    industry = models.CharField(max_length=128, verbose_name='Industry')
    date_of_foundation = models.PositiveSmallIntegerField(null=True, blank=True)
    number_of_employees = models.PositiveSmallIntegerField(null=True, blank=True)
    location = models.CharField(max_length=256, verbose_name='Company Location', null=True, blank=True)
    description = models.TextField(max_length=2048, verbose_name='About this company', null=True, blank=True)
    contact_phone = models.CharField(max_length=32, null=True, blank=True)
    company_icon = models.ImageField(
        default='company.ico',
        upload_to=get_path_upload_avatar_company,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'bmp', 'ico']),
                    validate_profile_image_size]
    )
    active_jobs = models.ManyToManyField(Job, default=None,blank=True, null=True)

    def __str__(self):
        return self.company_name

