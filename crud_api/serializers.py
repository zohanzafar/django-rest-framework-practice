from rest_framework import serializers
from .models import Student

def starts_with_x(value):
    if value[0].lower() == 'x':
        raise serializers.ValidationError('Letter must not be starts with X!')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100, validators = [starts_with_x])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    def validate_roll(self, value):
        if value < 1:
            raise serializers.ValidationError('Wrong Roll!')
        return value
    
    # Data parameter will get all the data as dictionary
    def validate(self, data):
        student_name = data.get('name')
        student_city = data.get('city')

        # if 'error' in student_name:
        #     raise serializers.ValidationError('Wrong Name!')
        # if 'karachi' in student_city.lower():
        #     raise serializers.ValidationError('Not for KHI!')
        
        if 'error' in student_name.lower():
            raise serializers.ValidationError('Wrong Name!')
        if 'karachi' in student_city.lower():
            raise serializers.ValidationError('Not for KHI!')

        return data
     