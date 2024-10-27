from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            data = Student.objects.get(id = id)
            serializer = StudentSerializer(data)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Data Created!'
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student_data = Student.objects.get(id = id)
        # partial true means some data will be updated if false wil have to update all the data
        serializer = StudentSerializer(student_data, data=python_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Data Updated!'
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        try:
            student_data = Student.objects.get(id=id)
            student_data.delete()
            response = {
                'message': 'Data Deleted!'
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        except:
            response = {
                'message': 'Some Error!'
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
            
    
        

        