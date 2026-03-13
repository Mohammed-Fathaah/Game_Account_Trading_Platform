from django.db import models
from users.models import User
from marketplace.models import AccountListing
# Create your models here.
class Order(models.Model):
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    account_listing = models.ForeignKey(AccountListing,on_delete=models.CASCADE)

    status = models.CharField(max_length=50,default="pending")
    transfer_email = models.EmailField(blank=True,null=True)
    transfer_password = models.CharField(max_length=20,blank=True,null=True)

    transfer_proof = models.ImageField(upload_to='transfer_proofs/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.buyer}"