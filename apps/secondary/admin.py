from django.contrib import admin
from apps.secondary.models import Secondary, Backend, Frontend, Desinger, Android, Colleagues

# from django.contrib.auth.models import User, Group

# Register your models here.

admin.site.register(Secondary)
admin.site.register(Backend)
admin.site.register(Frontend)
admin.site.register(Desinger)
admin.site.register(Colleagues)
admin.site.register(Android)

# admin.site.unregister(User)
# admin.site.unregister(Group)