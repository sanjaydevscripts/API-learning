# function based
# class based:API View/Mixins/Generics/Viewsets
#API view table for reading all records from student table

from students.models import Student
from students.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def StudentList(request):   #non primarykey based
    if(request.method=='GET'):
        s=Student.objects.all()
        stu=StudentSerializer(s,many=True)
        return Response(stu.data,status=status.HTTP_200_OK)

        #Api view for creating new record in Student table
    if(request.method=='POST'):
        s=StudentSerializer(data=request.data)#desrialization
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)



#primary key based
#api view for reading a specific record
@api_view(['GET'])
def StudentDetail(request,pk):
    if(request.method=='GET'):
        try:
            s=Student.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        stu=StudentSerializer(s)
        return Response(stu.data,status=status.HTTP_200_OK)