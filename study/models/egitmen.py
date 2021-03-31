from django.db import models

class EgitmenModel(models.Model):
    resim = models.ImageField(upload_to = "egitmen_resimleri")
    isim = models.CharField(max_length=50)
    ünvan = models.CharField(max_length=60)
    tanıma = models.TextField(max_length=100)

    class Meta:
        db_table = "Egitmen"
        verbose_name = "Egitmen"
        verbose_name_plural = "Egitmenler"

    def __str__(self):
        return self.isim
    