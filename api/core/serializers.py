from rest_framework import serializers
from .models import Talk

class TalkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Talk
		# image = models.FileField()
		fields = '__all__'
		# read_only_fields = ['theme']
