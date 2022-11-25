from django.db import models

# Create your models here.
class Facilities(models.Model):
    facility_id = models.AutoField(primary_key=True)
    facility_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'facilities'