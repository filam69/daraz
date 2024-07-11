# urls.py in qr_codes app

from django.urls import path
from . import views

urlpatterns = [
    path('qrcodes/', views.upload_qr_codes, name='upload_qr_codes'),
]
