from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.

# ================= PROFILE MODEL ===================
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profiles')
    image = models.ImageField(
    validators=[FileExtensionValidator(['jpg', 'jpeg'])], upload_to='profile_images', default="/static/images/user.jpg")


    def __str__(self):
        return self.user.username
