from django.contrib import admin
from .models import TdsModel

#django-import-exportで管理画面にCSVエクスポート機能を追加
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

#admin.site.register(TdsModel)

#ModelResourceを継承したクラスを追加
class TdsModelResource(resources.ModelResource):
    class Meta:
        model = TdsModel

@admin.register(TdsModel)
class TdsModelAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display = ('area', 'facility', 'address', 'spot', 'entry', 'type', 'jis')
    resource_class = TdsModelResource