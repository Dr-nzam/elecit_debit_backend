from django.urls import path
from .views import creerDebit

urlpatterns = [
    path('create-debit/', creerDebit, name="creer-debit")
]