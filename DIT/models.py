from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here

class dm_session(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "dm_sessions"


# extend users
class extended_users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_pc = models.BooleanField()
    is_dm = models.BooleanField()
    dm_session_id = models.ForeignKey(dm_session, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "extended_users"

class characters(models.Model):
    users_id = models.ForeignKey(User, on_delete=models.CASCADE)

    character_name = models.CharField(max_length=50)
    character_level = models.IntegerField()
    character_xp = models.IntegerField()

    character_armor_class = models.IntegerField()
    character_initiative = models.IntegerField(null=True)
    character_speed = models.IntergerField()
    character_maxHealth = models.IntegerField()
    character_currentHealth = models.IntegerField()
    character_temporaryHealth = models.IntegerField()

    character_strength = models.IntegerField()
    character_dexterity = models.IntergerField()
    character_constitution = models.IntergerField()
    character_intelligence = models.IntergerField()
    character_wisdom = models.IntergerField()
    character_charisma = models.IntergerField()

    def __str__(self):
        return "characters"

class creatures(models.Model):
    dm_session_id = models.ForeignKey(dm_session, on_delete=models.CASCADE)
    creature_name = models.CharField(max_length=50)
    creature_health = models.IntegerField()
    creature_level = models.IntegerField()
    creature_armor_class = models.IntegerField()
    creature_initiative = models.IntegerField(null=True)
    def __str__(self):
        return "creatures"

# SIGNALS
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


