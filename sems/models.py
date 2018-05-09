from django.db import models
from django.core.validators import FileExtensionValidator

class Program(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField(max_length=600, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    credits = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    picture = models.ImageField(null=True, blank=True, default='no-img.png')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Upload(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(validators=[FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx'])])

    def __str__(self):
        return self.name
