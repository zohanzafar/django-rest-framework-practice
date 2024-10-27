from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        print(request.body)
        stream = io.BytesIO(json_data)
        # JSON Data to Python
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializer = StudentSerializer(data=python_data)
                                       
        if serializer.is_valid():
            serializer.save()
            message = {
                'message': 'Data Created!'
            }
            json_data = JSONRenderer().render(message)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)        
        return HttpResponse(json_data, content_type='application/json')
