from django.db import models

class Contact(models.Model):
    Sno= models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return "This is from" + self.name + '-' + self.email