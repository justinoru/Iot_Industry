from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'rin',
            'first_name',
            'last_name',
        )
        model = Student