from rest_framework import serializers
from django.contrib.auth.models import User
from main_app.models import *
import uuid

class BioSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Bio
        fields = ['user', 'is_verified', 'is_owner']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': True}}

    def create(self, validated_data):
        is_owner = validated_data.pop('is_owner', False)
        user = User.objects.create_user(**validated_data)
        bio = Bio.objects.create(user=user, is_owner=is_owner)
        if is_owner:
            Owner.objects.create(bio = bio)
        Bidder.objects.create(bio=bio)    
        return user