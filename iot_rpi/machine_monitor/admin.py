from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Temp_Sensor)
admin.site.register(Acc_Sensor)
admin.site.register(Force_Torque_Sensor)
admin.site.register(Sound_Sensor)


