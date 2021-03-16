from django.contrib.admin import AdminSite
from django.contrib import admin
from . import models


class PageAdmin(models.Page):
    pass


class BlockAdmin(models.Block):
    pass


class ElementAdmin(models.Element):
    pass


class DataAdmin(models.Data):
    pass


admin.site.register(models.Page)
admin.site.register(models.Block)
admin.site.register(models.Element)
admin.site.register(models.Data)
