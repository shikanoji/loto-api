from django.contrib import admin
from app.models import Record
# Register your models here.

@admin.register(Record)
class Record(admin.ModelAdmin):
    list_display = ["_id", "date", "recordType", "values"]
    admin.register(Record)