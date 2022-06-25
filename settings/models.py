from django.db import models

# Create your models here.






class Brand(models.Model):
    BRDName = models.CharField(max_length=50)
    BRDDesc = models.TextField(blank=True , null=True)

    def __str__(self):
        return self.BRDName



class Variant(models.Model):
    VARName = models.TextField(blank=True , null=True)
    VARDesc = models.TextField()

    def __str__(self):
        return self.VARName