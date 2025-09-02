from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
    class Meta:
        db_table = 'games'

class Character(models.Model):
    name = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name ='game')

    def __str__(self):
        return f'{self.name}'
    class Meta:
        db_table = 'characters'

class Move(models.Model):
    Guard_choices = [
        ('Low', 'Low'),
        ('Mid', 'Mid'),
        ('High', 'High')
        ]
    move_choices = [
        ('Normal','Special'),
        ('Normal', 'Special')
    ]
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name ='move')
    name = models.CharField(max_length=50)
    move_type = models.CharField(
        max_length=50,
        choices= move_choices,
        default='Normal'
        )
    damage = models.CharField(max_length=10)
    guard_type = models.CharField(
        max_length=20,
        choices= Guard_choices,
        default='Mid'
    )
    start_up = models.IntegerField()
    active = models.IntegerField()
    recovery = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.character} - {self.name}'

    class Meta:
        db_table = 'moves'
