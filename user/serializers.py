# user/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, Task
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
import random
import string


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['role', 'phone_number', 'address']  


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = UserProfileSerializer()  # Nested UserProfileSerializer to handle profile creation

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']  

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        # Create the User instance
        user = User.objects.create_user(**validated_data)

        # Create the UserProfile instance
        UserProfile.objects.create(user=user, **profile_data)

        return user
    

class OperatorRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email']

    def create(self, validated_data):
        # Generate a random temporary password for the operator
        print("Validated data:", validated_data)
        temp_password = self.generate_temp_password()

        # Create the User instance with the temporary password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=temp_password
        )
        print("user:", user)

        UserProfile.objects.create(user=user, role="Operator")

        print("UserProfile:", UserProfile)

        return {
            'username': user.username,
            'email': user.email,
            'temporary_password': temp_password
        }

    def generate_temp_password(self):
        # Generate a random temporary password with a length of 8 characters
        characters = string.ascii_letters + string.digits 
        temp_password = ''.join(random.choices(characters, k=8))
        return temp_password
    
    def to_representation(self, instance):
        """
        Override the to_representation method to explicitly return the temporary_password
        """
        representation = super().to_representation(instance)

        # Explicitly add the temporary_password to the response
        representation['temporary_password'] = instance.get('temporary_password', None)

        return representation


class ProfileUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)
    phone_number = serializers.CharField(max_length=15, required=False, allow_blank=True)
    address = serializers.CharField(max_length=255, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'password']

    def validate_password(self, value):
        try:
            password_validation.validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value

    def update(self, instance, validated_data):
        # Update required fields
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        # Update optional fields (phone_number and address)
        user_profile = instance.userprofile
        user_profile.phone_number = validated_data.get('phone_number', user_profile.phone_number)
        user_profile.address = validated_data.get('address', user_profile.address)
        user_profile.save()

        # Update password
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField()  # Display operator's username
    created_by = serializers.StringRelatedField()  # Display manager's username
    machine = serializers.StringRelatedField()  # Display machine's name

    class Meta:
        model = Task
        fields = ['id', 'description', 'assigned_to', 'created_by', 'machine', 'status', 'created_at', 'deadline']
