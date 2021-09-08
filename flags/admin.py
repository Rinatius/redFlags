from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from flags.models import Entity, Tender, Flag, Irregularity, Classifier, Bid, Lot
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Entity)
admin.site.register(Tender)
admin.site.register(Lot)
admin.site.register(Bid)
admin.site.register(Classifier)
admin.site.register(Irregularity)
admin.site.register(Flag)