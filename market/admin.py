from django.contrib import admin
from .models import House, Book, Clothing, Other
# Register your models here.

admin.site.register(House)
admin.site.register(Book)
admin.site.register(Clothing)
admin.site.register(Other)
