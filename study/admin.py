from django.contrib import admin
from study.models import KategoriModel,YazilarModel,YorumModel,İletisimModel
from ckeditor.fields import RichTextField


#! Admin özelleştirme burda gerçekkleşir
admin.site.register(KategoriModel)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    list_display =(
        "baslik","olusturulma_tarihi","düzenlenme_tarihi"
    )
    search_fields = ("baslik","icerik")


@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display=(
        "yazan","olusturulma_tarihi","düzenlenme_tarihi"
    )
    search_fields=("yazan_username",)


@admin.register(İletisimModel)
class İletisimAdmin(admin.ModelAdmin):
    list_display=(
        "email","olusturulma_tarihi",
    )
    search_fields=("email",)
