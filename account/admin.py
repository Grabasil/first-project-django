from django.contrib import admin
from .models import Company
from .models import Office
from .models import Cabinet
from .models import Assistant

# Register your models here.

admin.site.register(Company)
admin.site.register(Office)
admin.site.register(Cabinet)
admin.site.register(Assistant)
