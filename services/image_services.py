from django.core.exceptions import ValidationError


def get_path_upload_avatar_user(instance, file):

    return f'avatar/user_{instance.id}/{file}'


def get_path_upload_avatar_company(instance, file):

    return f'avatar/company_{instance.id}/{file}'


def validate_profile_image_size(file_obj):
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024**2:
        raise ValidationError(f"Max profile image size is {megabyte_limit}MB")


def validate_company_cover_image_size(file_obj):
    megabyte_limit = 4
    if file_obj.size > megabyte_limit * 1024**4:
        raise ValidationError(f"Max profile image size is {megabyte_limit}MB")
