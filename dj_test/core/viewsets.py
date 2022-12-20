from rest_framework import viewsets
from . import models
from . import serailizers

class StudentViewsets(viewsets.ModelViewSet):
    queryset = models.students.objects.all()
    serializer_class = serailizers.StudentSerailizer

class StudentDetailsWithoutIDViewsets(viewsets.ModelViewSet):
    queryset = models.students.objects.all()
    serializer_class = serailizers.StudentDataWithoutIDSerializer