from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentForm, GradeValidation
from .models import StudentDetails, Grade
from .serializers import StudentForm, GradeValidation
# Create your views here.
from rest_framework.decorators import api_view


@api_view(['POST', 'GET'])
def student(request):
    if request.method == 'POST':
        serialize_data = StudentForm(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        return Response(serialize_data.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        record = StudentDetails.objects.all()
        result = StudentForm(record, many=True)
        return Response(result.data, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def add_mark(request):
    if request.method == 'GET':
        record = Grade.objects.all()
        result = GradeValidation(record, many=True)
        return Response(result.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        result = GradeValidation(data=request.data)
        if result.is_valid():
            result.save()
            return Response(result.data, status=status.HTTP_201_CREATED)
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def results(request):
    t = StudentDetails.objects.all()
    n = t.count()
    a = Grade.objects.filter(Grade="A")
    a1 = a.count()
    b = Grade.objects.filter(Grade="B")
    b1 = b.count()
    c = Grade.objects.filter(Grade="C")
    c1 = c.count()
    f = Grade.objects.filter(Grade="F")
    f1 = f.count()
    dist = (a1/n)
    f_c = ((b1+c1)/n)
    pass_percent = ((n-f1)/n)
    return Response({"total_number_of_students": n,
                     "distinction_percentage": dist,
                     "first_class": f_c,
                     "pass_percentage": pass_percent}, status=status.HTTP_200_OK)