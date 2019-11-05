from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
# For filtering queries
# class UserProfileManager(models.Manager):
#     def get_queryset(self):
#         return super(UserProfileManager, self).get_queryset().filter(city='Bloom')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.TextField()
    city = models.CharField(max_length=50)
    website = models.URLField(null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='profile_pics', blank=True)

    # For filtering queries
    # bloom = UserProfileManager()

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

    def __str__(self):
        return self.user.username