from django.db import models


class Linkmodel(models.Model):

    inputlink= models.CharField(max_length=1000, null=True)
    short= models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.short