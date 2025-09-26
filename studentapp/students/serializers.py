from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
        class Meta:
            model=Student
            fields=['id','name','age','place']
#ModelSerializer class is used for serialization/deserialization
#for converting django native to json format or for converting json to django native types