from django.db import models

#! Bu modül ile 2 farklı kodu tek koda indirgenir

class DateAbstractModel(models.Model):
    olusturulma_tarihi= models.DateTimeField(auto_now_add=True)
    düzenlenme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True