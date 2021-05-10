from django.db import models

# Create your models here.


class StudentDetails(models.Model):
    Name = models.CharField(max_length=50)
    Roll_number = models.IntegerField(primary_key=True)
    DOB = models.CharField(max_length=50)

    def __int__(self):
        return self.Roll_number


class Grade(models.Model):
    roll_no = models.OneToOneField(StudentDetails, on_delete=models.CASCADE)
    Grade = models.CharField(max_length=50)

    def __int__(self):
        return self.roll_no
