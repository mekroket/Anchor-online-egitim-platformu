from django.db import models

class KurslarGörüntüle(models.Model):
    resim = models.ImageField(upload_to ="kurs_resimleri")
    baslik = models.CharField(max_length=50)
    icerik = models.TextField(max_length=100)


    class Meta:
        db_table = "KursGörüntüle"
        verbose_name ="KursGörünlüte"
        verbose_name_plural = "KurslarGörüntüle"

    def __str__(self):
        return self.baslik
    