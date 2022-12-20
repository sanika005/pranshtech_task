from rest_framework import serializers
from .models import students
from rest_framework.response import Response

class StudentSerailizer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'

class StudentDataWithoutIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ['name','age','current_position']
        