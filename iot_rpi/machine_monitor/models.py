from django.db import models

class Student(models.Model):
    rin = models.IntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    temp_dev_id = models.IntegerField()
    acc_dev_id = models.IntegerField()
    force_torque_dev_id = models.IntegerField()
    sound_dev_id = models.IntegerField()

class Temp_Sensor(models.Model):
    temp_dev_id = models.IntegerField()
    student_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    body_temp = models.FloatField()
    amb_temp = models.FloatField()

class Acc_Sensor(models.Model):
    acc_dev_id = models.IntegerField()
    student_id = models.IntegerField()
    data = models.DateField()
    time = models.TimeField()
    acc = models.FloatField()

class Force_Torque_Sensor(models.Model):
    force_torque_dev_id = models.IntegerField()
    student_id = models.IntegerField()
    data = models.DateField()
    time = models.TimeField()
    force = models.FloatField()

class Sound_Sensor(models.Model):
    sound_dev_id = models.IntegerField()
    student_id = models.IntegerField()
    data = models.DateField()
    time = models.TimeField()
    freq = models.FloatField()
