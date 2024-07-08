from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers.in_serializer import SerializerDepotIn
from account.serializer.serializer_in import UserSerializer
from .models import Debit
from account.models import CustomUser


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creerDebit(request):

    user = request.user
    if user.is_superuser: 
        emailAdmin = request.data['email']
        passwordAdmin = request.data['password']
        nomDebit = request.data['nom_debit']
        if not CustomUser.objects.filter(email=emailAdmin).exists():
            # Créer un nouvel utilisateur
            new_user_data = {'email': emailAdmin, 'password': passwordAdmin, 'is_admin':True}  
            serializeruser = UserSerializer(data=new_user_data)
            serializeruser.is_valid(raise_exception=True)
            utilisateur = serializeruser.save()

            # Créer un nouvel débit associé à l'utilisateur admin
            new_debit_data = {'nom_debit': nomDebit, 'user': utilisateur.id, 'visible': True}
            serializerdebit = SerializerDepotIn(data=new_debit_data)
            serializerdebit.is_valid(raise_exception=True)
            serializerdebit.save()

            return Response({"msg": "Nouveau compte et débit créés avec succès"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "Ce compte existe déjà"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"msg": "Vous n'êtes pas autorisé à créer un débit de boisson"}, status=status.HTTP_403_FORBIDDEN)