from django.db import models
from django.conf import settings

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='game_images/',null=True,blank=True)

    def __str__(self):
        return self.name
    

class AccountListing(models.Model):
    STATUS_CHOICES = (
        ('available','Available'),
        ('sold','Sold'),
        ('pending','Pending'),
    )

    seller = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    account_level = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.game.name}"