from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.TextField()
    city = models.CharField(max_length=50)
    website = models.URLField(null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='pics')

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

    def __str__(self):
        return self.user.username