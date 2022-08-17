from django.db import models

# Create your models here.

# ==================== QUERIES MODEL ==================
class Queries(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name