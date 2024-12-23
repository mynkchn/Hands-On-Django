from django.db import models


# Create your models here.

class Emp(models.Model) :
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    working=models.BooleanField(default=True)
    course=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    name=models.CharField(max_length=100)
    testimonial=models.TextField()
    image=models.ImageField(upload_to='testimonial/')
    rating=models.IntegerField()
    def __str__(self):
      return self.name
 
