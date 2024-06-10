from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Bio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    # profile_pic = models.ImageField(upload_to='profile_pics/')
    email = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_verified = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
    
    
    
class Owner(models.Model):
    bio = models.ForeignKey(Bio, on_delete=models.CASCADE)
    owner_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.bio.bio





class Bidder(models.Model):
    bio = models.ForeignKey(Bio, on_delete=models.CASCADE)
    bidder_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.bio.bio






class Product (models.Model):
    product_slug = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    # product_image = models.ImageField(upload_to='product_images/')
    location = models.CharField(max_length=200)
    prodeuct_category = models.CharField(max_length=200, choices=[('Electronics', 'Electronics'), ('Fashion', 'Fashion'), ('Home', 'Home'), ('Sports', 'Sports'), ('Toys', 'Toys')])
    product_date = models.DateTimeField(auto_now_add=True)
    owner_user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name


class History(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.product_name