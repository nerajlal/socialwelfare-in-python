from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(orphanage_members)
admin.site.register(orphanage_product)
admin.site.register(orphanage_donation)
admin.site.register(orphanage_purchase)
admin.site.register(orphanage_adoption)
admin.site.register(orphanage_sponsor)