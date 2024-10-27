from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    def roll_range_check(roll):
        if roll > 250:
            raise serializers.ValidationError('Seat are full!')
        
    roll = serializers.IntegerField(validators = [roll_range_check])

    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    def validate_name(self, value):
        if value[0].lower() == 'x':
            raise serializers.ValidationError('The should not starts with X.')
        return value
    
    def validate(self, data):
        roll = data.get('roll')
        city = data.get('city')

        if roll < 1:
            raise serializers.ValidationError('Invalid roll number.')
        
        if city.lower() == 'islamabad':
            raise serializers.ValidationError('Student from Islamabad can not apply.')
        
        return data