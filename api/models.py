from django.db import models

class StudentDetails(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.firstname
    
    