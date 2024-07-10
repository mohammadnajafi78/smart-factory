from django.db import models


class Exhaustacion(models.Model):

    class Meta:
        tagid = models.IntegerField()
        floatvalue = models.FloatField()

    class Meta:
        db_table = "sqlt_data_2_2023_12"
        app_label = 'quickstart'