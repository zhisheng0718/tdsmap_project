from django.db import models

# Create your models here.

class TdsModel(models.Model):
    area = models.CharField("区市町",max_length=50)
    facility = models.CharField("施設名称",max_length=100)
    address = models.CharField("所在地",max_length=100)
    spot = models.CharField("水飲み栓設置場所",max_length=100)
    entry = models.CharField("入場料等",max_length=100)
    type = models.CharField("タイプ",max_length=50)
    jis = models.IntegerField("市区町村コード")