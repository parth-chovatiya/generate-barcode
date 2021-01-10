from django.urls import path
from . import views


urlpatterns = [
    path('', views.barcode_generate),
    # path('download/', views.barcode_download, name='barcode-download'),
]