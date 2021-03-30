from django.db import models

class İletisimModel(models.Model):
    email = models.EmailField(max_length=250,blank=False,null=False)
    isim_soyisim = models.CharField(max_length=100)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)


    class Meta : 
        db_table = "iletisim"
        verbose_name = "İletisim"
        verbose_name_plural = "İletisim"

    def __str__(self):
        return self.email
    