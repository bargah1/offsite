from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password

class shopsmodel(models.Model):
    name = models.CharField(max_length=20, default='default_value')
    bio = models.CharField(max_length=100, default='default_value')
    phone = models.IntegerField(null=True)
    photo1 = models.ImageField(upload_to='shop_photos/', default='shop_photos/default_image.jpg')
    photo2 = models.ImageField(upload_to='shop_photos/', default='shop_photos/default_image.jpg')
    photo3 = models.ImageField(upload_to='shop_photos/', default='shop_photos/default_image.jpg')
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=50, default='default_value')
    locationlink= models.CharField(max_length=50, default='default_value')
    password = models.CharField(max_length=128)
    is_subscribed = models.BooleanField(default=False)
    subscription_start = models.DateTimeField(null=True, blank=True)
    subscription_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

    def activate_subscription(self):
        """
        Method to activate a one-month subscription.
        """
        now = datetime.now()
        self.subscription_start = now
        self.subscription_end = now + timedelta(days=30)  # One month period
        self.is_subscribed = True
        self.save()

    def check_subscription_status(self):
        """
        Method to check and update subscription status based on current time.
        """
        if self.subscription_end and self.subscription_end < datetime.now():
            self.is_subscribed = False
            self.subscription_start = None
            self.subscription_end = None
            self.save()

    def save(self, *args, **kwargs):
        # Hash the password before saving the model instance
        if not self.pk:  # If the object is new (no primary key)
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
class offermodel(models.Model):
    shop=models.ForeignKey(shopsmodel,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='offer_photos/')
    name=models.CharField(max_length=50)
    description =models.CharField(max_length=100)

