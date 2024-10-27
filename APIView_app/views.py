from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentAPI(APIView):
    
    def get(self, request, pk = None, format = None):
        id = pk
        if id is not None:
            try:
                student_data = Student.objects.get(id = id)
                serializer = StudentSerializer(student_data)
                return Response(serializer.data)
            except:
                response = {
                    'error': 'User not Found!'
                }
                return Response(response, status=status.HTTP_404_NOT_FOUND)
        student_data = Student.objects.all()
        serializer = StudentSerializer(student_data, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Data Created!'
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format = None):
        pk = pk
        student_data = Student.objects.get(id = pk)
        serializer = StudentSerializer(student_data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Data Updated!'
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format = None):
        id = pk
        student_data = Student.objects.get(id = id)
        serializer = StudentSerializer(student_data, data = request.data, partial = True)
        if serializer.is_valid(): 
            serializer.save()
            response = {
                'message': 'Updated Some Data!'
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        id = pk 
        try:
            student_data = Student.objects.get(id = id)
            student_data.delete()
            response = {
                'message': 'Data Deleted!'
            }
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {
                'error': 'User not found!'
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)