from django.contrib import admin
from apps.base.models import InfoUser, Skills, Education,MyService, PersentShow, Blogs
from django.contrib.auth.models import User, Group


# Register your models here.
admin.site.register(Blogs)
admin.site.register(PersentShow)
admin.site.register(Education)
admin.site.register(InfoUser)
admin.site.register(MyService)
admin.site.register(Skills)

admin.site.unregister(User)
admin.site.unregister(Group)