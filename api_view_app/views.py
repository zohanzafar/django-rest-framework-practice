from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk = None):
    if request.method == 'GET':
   
        # id = request.data.get('pk')
        id = pk
        if id is not None:
            try:
                student_data = Student.objects.get(id = id)
                serializer = StudentSerializer(student_data)
                return Response(serializer.data)
            except:
                response = {
                    'error': 'User Not Found!'
                }
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            
        student_data = Student.objects.all()
        serializer = StudentSerializer(student_data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        python_data = request.data
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Data Created!'
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        # python_data = request.data
        # id = python_data.get('pk')
        id = pk

        student_data = Student.objects.get(id=id)
        serializer = StudentSerializer(student_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Data updated!'
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        # id = request.data.get('pk')
        id = pk

        student_data = Student.objects.get(id=id)
        serializer = StudentSerializer(student_data, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message' : 'Some Data Updated!'
            }
            return Response(response, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        # id = request.data.get('pk')
        id = pk

        try:
            student_data = Student.objects.get(id=id)
            student_data.delete()
            response = {
                'message': 'Data Deleted!'
            }
            return Response(response, status.HTTP_200_OK)
        except:
            response = {
                'error':'User deos not exist.'
            }
            return Response(response, status = status.HTTP_404_NOT_FOUND)