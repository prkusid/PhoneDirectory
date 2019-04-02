from django.contrib import admin
from PhoneDirectory.models import PhoneDirectory

# Register your models here.
class PhoneDirectoryAdmin(admin.ModelAdmin):
    list_display = ['name','phone_no']
    search_fields = ('name',)

admin.site.register(PhoneDirectory,PhoneDirectoryAdmin)
