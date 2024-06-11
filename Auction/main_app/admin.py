from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Bio)
admin.site.register(Owner)
admin.site.register(Bidder)
admin.site.register(Product)
admin.site.register(History)