from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


class Product(models.Model):
    name = models.CharField(max_length=200)
    country_id = models.CharField(max_length=1, null=True)
    manufacturer_id = models.CharField(max_length=6, null=True)
    product_id = models.CharField(max_length=5, null=True)
    barcode = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        CODE128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = CODE128(f'{self.country_id}{self.manufacturer_id}{self.product_id}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.name}.png', File(rv), save=False)
        return super().save(*args, **kwargs)
