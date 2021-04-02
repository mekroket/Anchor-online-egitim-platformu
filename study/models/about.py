from django.db import models

class AboutModel(models.Model):
    isim = models.CharField(max_length=20)
    ünvan = models.CharField(max_length=30)
    resim = models.ImageField(upload_to ="hakkımda")
    tanıma = models.TextField(max_length=150)

    class Meta:
        db_table = "Hakkimda"
        verbose_name = "Hakkimda"
        verbose_name_plural="Ceo"

    def __str__(self):
        return self.isim
    