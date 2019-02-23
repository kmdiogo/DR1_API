from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here

# extend users
class extended_users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_pc = models.BooleanField()
    is_dm = models.BooleanField()

class characters(models.Model):
    users_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=50)
    character_health = models.IntegerField()
    character_level = models.IntegerField()
    character_armor_class = models.IntegerField()
    character_initiative = models.IntegerField(null=True)

class dm_session(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class creatures(models.Model):
    dm_session_id = models.ForeignKey(dm_session, on_delete=models.CASCADE)
    creature_name = models.CharField(max_length=50)
    creature_health = models.IntegerField()
    creature_level = models.IntegerField()
    creature_armor_class = models.IntegerField()
    creature_initiative = models.IntegerField(null=True)

# SIGNALS
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


