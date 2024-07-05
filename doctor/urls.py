from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views
router = DefaultRouter()
router.register('list',views.DoctorViewSet)
router.register('designation',views.DesignationViewSet)
router.register('specialization',views.SpecializationSerializer)
router.register('available_time',views.AvailableTimeSerializer)
urlpatterns = [
    path('',include(router.urls))
]

