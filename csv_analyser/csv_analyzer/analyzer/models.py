from django.db import models

# Create your models here.
from django.db import models

class CSVFile(models.Model):
    file = models.FileField(upload_to='csv_files/')