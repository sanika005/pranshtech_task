from core.viewsets import StudentViewsets, StudentDetailsWithoutIDViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student',StudentViewsets)
router.register('list-students',StudentDetailsWithoutIDViewsets)