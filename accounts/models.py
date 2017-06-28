from django.db import models
from django.contrib.auth.models import User


BANKS = (
                      ('Access Bank', 'Access Bank'),
                      ('Citibank', 'Citibank'),
                      ('Diamond Bank', 'Diamond Bank'),
                      ('Ecobank', 'Ecobank'),
                      ('Fidelity Bank', 'Fidelity Bank'),
                      ('First Bank', 'First Bank'),
                      ('First City Monument Bank (FCMB)', 'First City Monument Bank (FCMB)'),
                      ('FSDH Merchant Bank', 'FSDH Merchant Bank'),
                      ('Guarantee Trust Bank (GTB)', 'Guarantee Trust Bank (GTB)'),
                      ('Heritage Bank', 'Heritage Bank'),
                      ('Keystone Bank', 'Keystone Bank'),
                      ('Rand Merchant Bank', 'Rand Merchant Bank'),
                      ('Skye Bank', 'Skye Bank'),
                      ('Stanbic IBTC Bank', 'Stanbic IBTC Bank'),
                      ('Standard Chartered Bank', 'Standard Chartered Bank'),
                      ('Sterling Bank', 'Sterling Bank'),
                      ('Suntrust Bank', 'Suntrust Bank'),
                      ('Union Bank', 'Union Bank'),
                      ('United Bank for Africa (UBA)', 'United Bank for Africa (UBA)'),
                      ('Unity Bank', 'Unity Bank'),
                      ('Wema Bank', 'Wema Bank'),
                      ('Zenith Bank', 'Zenith Bank')
)

TYPE = (
                      ('Savings', 'Savings'),
                      ('Current', 'Current'),
                      ('Credit', 'Credit'),
                      ('Others', 'Others'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    full_name = models.CharField(max_length=100,unique=True )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    picture_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="200")
    picture_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="200")

    def __unicode__(self):
        return self.user.username


class UserAccount(models.Model):
    user = models.OneToOneField(User, unique=True)
    account_name = models.CharField(max_length=100, default="", blank=False, unique=True)
    bank_name = models.CharField(choices=BANKS, blank=False, default="", max_length=80)
    account_number = models.CharField(max_length=10, default="", blank=False, unique=True)
    account_type = models.CharField(choices=TYPE, blank=False, default="", max_length=20)
    plan_type = models.CharField(default="", max_length=20)
    confirm1 = models.IntegerField(default=0)
    confirm2 = models.IntegerField(default=0)

    def __unicode__(self):
        return self.account_name


class PaymentProofs(models.Model):
    image = models.ImageField(upload_to='proof_images', blank=False)
