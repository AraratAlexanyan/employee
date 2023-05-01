from django.conf import settings
from django.core.mail import send_mail
from itsdangerous import URLSafeTimedSerializer
from rest_framework import status
from rest_framework.response import Response


def email_send_activation(email):
    tokenizer = URLSafeTimedSerializer(settings.SECRET_KEY)
    serialized_token = tokenizer.dumps({
        'email': email,
    })

    verify_url = f'{settings.BASE_URL}/base_user/verify_token?token={serialized_token}'

    send_mail(
        'Verification',
        'Verify your email',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=f'<a href={verify_url}>Click to verify email</a>'
    )


def verify_account(request):
    _token = request.GET.get("token")

    if not _token:
        return Response(
            dict(message="Verification Failed: token's missing"),
            status=status.HTTP_400_BAD_REQUEST)

    tokenizer = URLSafeTimedSerializer(settings.SECRET_KEY)

    try:
        data = tokenizer.loads(_token, max_age=settings.VERIFICATION_TIME_IN_SECONDS)
        return data
    except ValueError:
        return Response(
            dict(message="Verification Failed: token's expired"),
            status=status.HTTP_400_BAD_REQUEST)
