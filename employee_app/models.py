from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employee(models.Model):
    Full_Name = models.CharField(max_length=100)
    Mobile_Number = models.CharField(max_length=20)
    Employee_Code = models.CharField(max_length=10)
    Position = models.ForeignKey(Position, on_delete=models.CASCADE)
