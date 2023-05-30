from django.db import models

# Create your models here.


# Create your models here.
class abc(models.Model):
    imgf = models.ImageField(upload_to='fashion')

    def __str__(self):
        return self.imgf

class abc1(models.Model):
    imgp = models.ImageField(upload_to='personal')

    def __str__(self):
        return self.imgp



class abc2(models.Model):
    imgpr = models.ImageField(upload_to='product')

    def __str__(self):
        return self.imgpr


class abc3(models.Model):
    imgw = models.ImageField(upload_to='wedding')

    def __str__(self):
        return self.imgw

