from rest_framework import serializers
from .models import StudentDetails, Grade


class StudentForm(serializers.ModelSerializer):
    Name = serializers.CharField(required=True)
    Roll_number = serializers.IntegerField(required=True)
    DOB = serializers.CharField(required=True)

    class Meta:
        model = StudentDetails
        fields = ('Name', 'Roll_number', 'DOB')


class GradeValidation(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('roll_no', 'Grade')
