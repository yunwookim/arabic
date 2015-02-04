from django.contrib.auth.models import User
from django.db import models
import json


# Create your models here.
class Company(models.Model):
    name = models.CharField(default="WebLec")
    user_count = models.IntegerField()

    def __str__(self):
        return self.name

    def get_count(self):
        return self.user_count


class Class(models.Model):
    code = models.CharField()
    name = models.CharField()

    def __str__(self):
        return self.name

    def get_code(self):
        return self.code


class Lecture(models.Model):
    name = models.CharField()
    lec_code = models.CharField()
    lec_type = models.CharField()
    video = models.FileField(upload_to=u'video/', max_length=200)
    audio = models.FileField(upload_to=u'mp3/', max_length=200)

    def __str__(self):
        return self.name

    def get_type(self):
        return self.lec_type

    def get_video(self):
        return self.video

    def get_audio(self):
        return self.audio

    def get_code(self):
        return self.lec_code


class Student(models.Model):
    user = models.OneToOneField(User)
    curLec = models.CharField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.get_name() + "(" + self.user.get_username() + ")"

    def get_name(self):
        return self.user.last_name + self.user.first_name

    def set_curlec(self, x):
        self.curLec = json.dumps(x)

    def get_curlec(self):
        return json.load(self.curLec)

    def get_phone(self):
        return self.phone


