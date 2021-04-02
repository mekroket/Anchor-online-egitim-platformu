from django.db import models


class DerslerModel(models.Model):
    baslik = models.CharField(max_length=20)
    resim = models.ImageField(upload_to = "ders_resimleri")
    icerik = models.TextField(max_length=150)
    ücret = models.CharField(max_length=20)
    tür = models.CharField(max_length=30)
    #! yazar = models.ForeignKey("account.CustomUserModel",related_name="yazilar",on_delete=models.CASCADE)

    class Meta:
        db_table = "DerslerTablo"
        verbose_name = "Dersler"
        verbose_name_plural = "Ders-Ekle"

    def __str__(self):
        return self.baslik
    