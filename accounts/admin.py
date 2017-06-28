from django.contrib import admin
from accounts.models import UserProfile, UserAccount, PaymentProofs

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserAccount)
admin.site.register(PaymentProofs)