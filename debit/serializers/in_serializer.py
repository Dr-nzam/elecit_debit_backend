from rest_framework import serializers
from debit.models import Debit

class SerializerDepotIn(serializers.ModelSerializer):
    class Meta:
        model = Debit
        fields = ['nom_debit','user', 'visible']