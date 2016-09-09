from django.contrib import admin
# Register your models here.
from projects.models import FbLeads
from django.db import models


@admin.register(FbLeads)
class FbLeadsAdmin(admin.ModelAdmin):
    fields = ('fb_id', 'date_receive', 'field_data', 'email_send')

    # formfield_overrides = {
    #     models.TextField: {'field_data': RichTextEditorWidget},
    # }

    empty_value_display = '-empty-'
    search_fields = ['created_time']
    ordering = ['-created_time']


