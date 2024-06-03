from django.db import models



class Project(models.Model):
    project = models.CharField(max_length=100)
    project_discription = models.CharField(max_length=300)
    project_cost = models.CharField(max_length=100)
    project_start_date = models.DateField(auto_now_add=False)
    project_deadLine = models.DateField(auto_now_add=False)
    employee_name = models.CharField(max_length=100)
    employee_email = models.CharField(max_length=255)


    def __str__(self):
        return self.project

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=125)

    def __str__(self):

        return self.first_name + "   " + self.last_name



