from django.db import models
from study.abstract_model import DateAbstractModel
from study.models import YazilarModel




#! Yorumlar İçin eklenmesi Greken Modüller
class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE,related_name="yorum")
    yazi = models.ForeignKey(YazilarModel,on_delete=models.CASCADE,related_name="yorumlar")
    yorum = models.TextField()
    

    class Meta:
        db_table = "yorum"
        verbose_name = "Yorum"
        verbose_name_plural ="Yorumlar"
    
    def __str__(self):
        return self.yazan.username  # todo Bu daha sonra eklenicek
    
    