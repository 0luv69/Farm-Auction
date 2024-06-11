from rest_framework import serializers
from django.contrib.auth.models import User
from main_app.models import *
import uuid

class BioSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Bio
        fields = ['user', 'is_verified', 'is_owner', 'email_token']

class UserSerializer(serializers.ModelSerializer):
    email_token = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'email_token']
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': True}}

    def create(self, validated_data):
        email_token = validated_data.pop('email_token')
        is_owner = validated_data.pop('is_owner', False)
        user = User.objects.create_user(**validated_data)
        bio = Bio.objects.create(user=user, is_owner=is_owner, email_token= email_token)
        if is_owner:
            Owner.objects.create(bio = bio)
        Bidder.objects.create(bio=bio)    
        return user
    

class ProductSerializer(serializers.ModelSerializer):
    owner_user = serializers.CharField(write_only=True)
    class Meta:
        model = Product
        fields= '__all__'    

    def create(self, validated_data):
        owner_user_username = validated_data.pop('owner_user')
        try:
            owner = Owner.objects.get(bio__user__username=owner_user_username)
        except Owner.DoesNotExist:
            raise serializers.ValidationError(f"Owner with the \'{owner_user_username}\' username does not exist.")
        return Product.objects.create(owner_user=owner, **validated_data)


