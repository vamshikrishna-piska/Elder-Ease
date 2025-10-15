from rest_framework import serializers
from app.models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "role", "age", "location", "mobile"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate_mobile(self, value):
        if value and (not value.isdigit() or len(value) < 10):
            raise serializers.ValidationError(
                "Enter a valid mobile number (digits only, at least 10)."
            )
        return value


class TaskSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    assigned_to_name = serializers.CharField(source='assigned_to.username', read_only=True)
     

    assigned_to = serializers.SlugRelatedField(
        queryset=User.objects.filter(role='helper'),
        slug_field='username',
        required=False,
        allow_null=True
        )

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ('created_by',)
