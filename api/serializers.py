from rest_framework import serializers
from .models import StudentDetails

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'
        
    # def create(self, validated_data):
    #     return StudentSerializer(**validated_data)  
    
    # def update(self, instance, validated_data):
    #     instance.firstname = validated_data.get('firstname', instance.firstname)
    #     instance.lastname = validated_data.get('lastname', instance.lastname)
    #     instance.mobile = validated_data.get('mobile', instance.mobile)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.save()
    #     return instance
