from django.urls import path
from .views import creerDebit, creerAutreCompte

urlpatterns = [
    path('create-debit/', creerDebit, name="creer-debit"),
    path('create-order-account/', creerAutreCompte, name="create-order-account")
]