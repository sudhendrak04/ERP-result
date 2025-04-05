from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'roll_no'

    @action(detail=True, methods=['get'])
    def results(self, request, roll_no=None):
        student = self.get_object()
        data = {
            'name': student.name,
            'roll_no': student.roll_no,
            'attendance': student.attendance,
            'ia1': student.ia1,
            'ia2': student.ia2,
            'ese': student.ese,
            'lab_attendance': student.lab_attendance,
            'assignments': student.assignments,
            'practicals': student.practicals
        }
        return Response(data)
