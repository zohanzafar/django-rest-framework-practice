from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Model Instance - Single Object
def get_student(request, pk):
    
    student = Student.objects.get(id = pk)

    serializer = StudentSerializer(student)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# Query set - Multiple Onbjects
def get_all_student(request):
    
    student = Student.objects.all()

    serializer = StudentSerializer(student, many=True)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type='application/json')