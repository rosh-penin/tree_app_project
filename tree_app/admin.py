from django.contrib import admin

from .models import Menu, MenuMember


admin.site.register((Menu, MenuMember))
