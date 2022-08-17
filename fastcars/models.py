from django.db import models
from django.contrib.auth.models import User
from admin_panel.models import Vehicle
# Create your models here.
# ================= TESTIMONIAL MODEL ====================
class Testimonial(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='testimonial')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, related_name='comments')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.description    

# ================ SUBSCRIPTION MODEL ====================
class Subscription(models.Model):
    email = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('email',)