from .models import Product
from django.forms import ModelForm


class BarcodeForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['barcode']