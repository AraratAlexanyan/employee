from rest_framework import serializers

from src.base_user.models import BaseAccount


class BaseUserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = BaseAccount
        fields = ('email', 'password', 'password2',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        base_user = BaseAccount(
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password2 != password:
            raise serializers.ValidationError(
                'Passwords doesnt match please check again!'
            )
        base_user.set_password(password)
        base_user.save()
        return base_user
