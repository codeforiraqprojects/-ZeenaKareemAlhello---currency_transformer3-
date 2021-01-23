from django.db import models

# Create your models here.
class c(models.Model):
    USD= models.FloatField(blank=False,null=False)
    IQD= models.FloatField(null=False)
    EUR= models.FloatField(null=False)
    MAD= models.FloatField(null=False)


class usd_to_currency(models.Model):
    USD= models.FloatField(blank=False,null=False)
    IQD= models.FloatField(null=False)
    EUR= models.FloatField(null=False)
    MAD= models.FloatField(null=False)

class dec_currency(models.Model):
    USD=models.TextField()
    IQD=models.TextField()
    EUR=models.TextField()
    MAD=models.TextField()


class signin(models.Model):
    fullname = models.CharField(blank=False, max_length=15)
    email=models.EmailField(blank=False)


    def __str__(self):
        if self.fullname == None:
            return "type NAME IS NULL"
        else:

            return self.fullname
