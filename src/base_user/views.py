from rest_framework.decorators import api_view

from .models import BaseAccount
from .serializers import BaseUserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from. import services


@api_view(('POST',))
def base_user_registration(request):
    if request.method == 'POST':
        serializer = BaseUserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
            base_user = serializer.save()

            data['response'] = 'Successfully registered new email'
            data['email'] = base_user.email
            data['info'] = 'Please check your email to activate account'

            services.email_send_activation(base_user.email)

        else:
            data = serializer.errors
        return Response(data)


@api_view(('GET',))
def base_user_email_verify(request):

    data = services.verify_account(request)

    try:
        email = data['email']
    except ValueError:
        return Response(
            dict(message="Verification Failed: something bad happened"),
            status=status.HTTP_400_BAD_REQUEST)

    try:
        user = BaseAccount.objects.get(email=email)
    except BaseAccount.DoesNotExist:
        return Response(
            dict(message="Verification Failed: something bad happened"),
            status=status.HTTP_400_BAD_REQUEST)

    user.is_active = True
    user.save()
    return Response(status=status.HTTP_204_NO_CONTENT)