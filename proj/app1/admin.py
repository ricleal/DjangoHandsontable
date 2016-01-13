
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Data, Reduction, Entry

# Register your models here.
admin.site.register(Data)
admin.site.register(Reduction)
admin.site.register(Entry)
