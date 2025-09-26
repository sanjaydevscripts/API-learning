# function based
# class based:API View/Mixins/Generics/Viewsets
#API view table for reading all records from student table

from students.models import Student
from students.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET'])
def StudentList(request):
    if(request.method=='GET'):
        s=Student.objects.all()
        stu=StudentSerializer(s,many=True)
        return Response(stu.data,status=status.HTTP_200_OK)
