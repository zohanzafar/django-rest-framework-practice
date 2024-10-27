from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    #  Validators
    def start_with_z(value):
        if value[0].lower() != 'z':
            raise serializers.ValidationError('Name must start with Z!')

    name = serializers.CharField(validators=[start_with_z])

    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # Will select all fields
        # fields = '__all__'
        #  Exclude will not select those fields
        # exclude = ['roll']

    #  Field Level
    def validate_roll(self, value):
        if value < 1:
            raise serializers.ValidationError('Roll Error!')
        return value
    
    # Object Level
    def validate(self, data):
        student_name = data.get('name')
        student_city = data.get('city')
        if student_name.lower() == 'error' or student_city.lower() == 'karachi':
            raise serializers.ValidationError('Some Errors!')
        return data