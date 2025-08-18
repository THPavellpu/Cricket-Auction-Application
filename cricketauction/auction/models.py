from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=[('Batsman', 'Batsman'), ('Bowler', 'Bowler'), ('All-Rounder', 'All-Rounder')])
    image = models.ImageField(upload_to='players/')
    is_sold = models.BooleanField(default=False)
    bid_price = models.IntegerField(default=500)
    has_been_shown = models.BooleanField(default=False)  # to track if player has been processed
    is_unsold = models.BooleanField(default=False)       # to retry in the next round
    
    def __str__(self):
        return self.name