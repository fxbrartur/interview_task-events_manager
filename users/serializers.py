from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from urllib.request import urlopen
from django.core.files.base import ContentFile
import os


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()
    image_url = serializers.URLField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'created_at', 'password', 'token', 'image_url']

    def create(self, validated_data):
        image_url = validated_data.pop('image_url', None)
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()

        if image_url:
            img_temp = urlopen(image_url)
            img_filename = os.path.basename(image_url)
            user.image.save(img_filename, ContentFile(img_temp.read()), save=True)

        Token.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key
