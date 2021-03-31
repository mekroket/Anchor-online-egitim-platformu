from django.db import models
from autoslug import AutoSlugField
from study.models import KategoriModel
from ckeditor.fields import RichTextField
from study.abstract_model import DateAbstractModel

class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to="yazi_resimleri")
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from = "baslik",unique=True)
    kategoriler = models.ManyToManyField(KategoriModel,related_name="yazi")
    yazar = models.ForeignKey("account.CustomUserModel",related_name="yazilar",on_delete=models.CASCADE)
    ücret = models.CharField(max_length=20)
    
    class Meta:
        db_table ="Yazi"
        verbose_name = "Yazi"
        verbose_name_plural  = "Yazilar"

    def __str__(self):
        return self.baslik
    