from django.db import models

class FiyatlarModel(models.Model):
    sürüm = models.CharField(max_length=20)
    para_türü = models.CharField(max_length=20)
    ay_gün = models.CharField(max_length=20)
    indirim = models.CharField(max_length=15)

    deger1 = models.CharField(max_length=20)
    deger2 = models.CharField(max_length=20)
    deger3 = models.CharField(max_length=20)

    deger4 = models.CharField(max_length=20)
    deger5 = models.CharField(max_length=20)
    deger6 = models.CharField(max_length=20)
    deger7 = models.CharField(max_length=20)

    deger8 = models.CharField(max_length=20)
    deger9 = models.CharField(max_length=20)
    deger10 = models.CharField(max_length=20)
    deger11 = models.CharField(max_length=20)
    deger12 = models.CharField(max_length=20)


    deger13 = models.CharField(max_length=20)
    deger14 = models.CharField(max_length=20)
    deger15 = models.CharField(max_length=20)
    deger16 = models.CharField(max_length=20)
    deger17 = models.CharField(max_length=20)

    class Meta:
        db_table="Fiyatlar"
        verbose_name="Fiyatlar"
        verbose_name_plural="Fiyatlandırma"
    
    def __str__(self):
        return self.sürüm
    