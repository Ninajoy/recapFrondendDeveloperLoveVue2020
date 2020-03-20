from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TalkSerializer
from .models import Talk

class TalkViewSet(viewsets.ModelViewSet):
	serializer_class = TalkSerializer
	queryset = Talk.objects.all()
