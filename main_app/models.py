from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'image_store/', blank = True, null = True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "games"


class Character(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="characters")
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'image_store/', blank = True, null = True)


    def __str__(self):
        return f"{self.name} ({self.game})"

    class Meta:
        db_table = "characters"


class Move(models.Model):
    GUARD_CHOICES = [
        ("Low", "Low"),
        ("Mid", "Mid"),
        ("High", "High"),
    ]

    MOVE_CHOICES = [
        ("Normal", "Normal"),
        ("Special", "Special"),
    ]
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="moves")
    image = models.ImageField(upload_to = 'image_store/', blank = True, null = True)
    name = models.CharField(max_length=50)
    move_type = models.CharField(
        max_length=50,
        choices=MOVE_CHOICES,
        default="Normal")
    damage = models.CharField(max_length=10)
    guard_type = models.CharField(
        max_length=20,
        choices=GUARD_CHOICES, 
        default="Mid")
    start_up = models.IntegerField()
    active = models.IntegerField()
    recovery = models.IntegerField()
    onhit = models.CharField(max_length=50, blank = True, null = True)
    onblock = models.CharField(max_length=50, blank = True, null = True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.character} - {self.name}"

    class Meta:
        db_table = "moves"
