from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, value):
        """
        Custom validation for the 'name' field.
        Ensure that the name is not empty and does not exceed a certain length.
        """
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError("Name cannot exceed 100 characters.")
        return value

    def validate_description(self, value):
        """
        Custom validation for the 'description' field.
        Ensure that the description does not exceed a certain length.
        """
        if len(value) > 500:
            raise serializers.ValidationError("Description cannot exceed 500 characters.")
        return value
