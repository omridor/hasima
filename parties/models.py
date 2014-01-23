from django.db import models

class Party(models.Model):
    class Meta:
        verbose_name_plural = "parties"
    tla = models.CharField(max_length=5, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):  
          return self.tla
