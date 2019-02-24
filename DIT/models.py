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
    character_class = models.CharField(max_length=50)
    character_race = models.CharField(max_length=50)
    character_alignment = models.CharField(max_length=50)

    character_level = models.IntegerField()
    character_xp = models.IntegerField()

    character_armor_class = models.IntegerField()
    character_initiative = models.IntegerField(null=True)
    character_speed = models.IntegerField()

    character_height_feet = models.IntegerField()
    character_height_inches = models.IntegerField()
    character_age = models.IntegerField()
    character_weight= models.IntegerField()
    character_maxHealth = models.IntegerField()
    character_currentHealth = models.IntegerField()
    character_temporaryHealth = models.IntegerField()

    character_strength = models.IntegerField()
    character_dexterity = models.IntegerField()
    character_constitution = models.IntegerField()
    character_intelligence = models.IntegerField()
    character_wisdom = models.IntegerField()
    character_charisma = models.IntegerField()


    def __str__(self):
        return "characters"

class creatures(models.Model):
    dm_session_id = models.ForeignKey(dm_session, on_delete=models.CASCADE)

    creature_name = models.CharField(max_length=50)
    creature_size = models.CharField(max_length=50)
    creature_type = models.CharField(max_length=50)
    creature_subtype = models.CharField(max_length=50)
    creature_alignment = models.CharField(max_length=50)
    creature_armor_class = models.IntegerField()
    creature_health = models.IntegerField()
    creature_temporary_health = models.IntegerField()
    creature_hit_dice = models.IntegerField()
    creature_speed = models.IntegerField()
    creature_speed_swim = models.IntegerField()
    creature_strength = models.IntegerField()
    creature_dexterity = models.IntegerField()
    creature_constitution = models.IntegerField()
    creature_intelligence = models.IntegerField()
    creature_wisdom = models.IntegerField()
    creature_charisma = models.IntegerField()

    creature_constitution_save = models.IntegerField()
    creature_intelligence_save = models.IntegerField()
    creature_wisdom_save = models.IntegerField()
    creature_history = models.IntegerField()
    creature_perception = models.IntegerField()
    creature_challenge_rating = models.IntegerField()

    creature_initiative = models.IntegerField(null=True)

    def __str__(self):
        return "creatures"

class damage_vulnerabilities(models.Model):

class damage_resistances(models.Model):

class damage_immunities(models.Model):

class condition_immunities(models.Model):

class senses(models.Model):

class languages(models.Model):

class special_abilities(models.Model):

class actions(models.Model):

class legendary_actions(models.Model):

# SIGNALS
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


