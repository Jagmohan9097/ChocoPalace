from django.contrib import admin
from .models import Product
from .models import Mobile
from .models import Contact



# Register your models here.
admin.site.register(Product)
admin.site.register(Mobile)
admin.site.register(Contact)

