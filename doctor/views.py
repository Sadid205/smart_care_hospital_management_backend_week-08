from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import filters,pagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.

class DoctorPagination(pagination.PageNumberPagination):
    page_size  = 1 
    page_size_query_param = page_size
    max_page_size = 100


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    pagination_class = DoctorPagination
    serializer_class = serializers.DoctorSerializer


class DesignationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set,view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

class AvailableTimeSerializer(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]

class SpecializationSerializer(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer