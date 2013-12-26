from django.db import models

# Create your models here.
class AvatarClass(models.Model):
  name = models.TextField()

class Rarity(models.Model):
  name = models.TextField()

class CardType(models.Model):
  name = models.TextField()

class Card(models.Model):
  name = models.TextField(null=False)
  avatar_class = models.ForeignKey(AvatarClass, null=False)
  rarity = models.ForeignKey(Rarity, null=False)
  card_type = models.ForeignKey(CardType, null=False)
  race = models.TextField()
  mana_cost = models.IntegerField(null=False)
  attack = models.IntegerField()
  health = models.IntegerField()
  description = models.TextField()
