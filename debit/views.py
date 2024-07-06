from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from account.serializer.serializer_in import UserSerializer
from .models import Debit
from account.models import CustomUser

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creerDebit(request):

    user = request.user
    if user.is_superadmin :
        emailAdmin =request.data['email']
        passwordAdmin = request.data['password']
        nomDebit = request.data['nom_debit']
        print("*-*-*-*-*--**--*--*-****-")
        print(nomDebit)
        if CustomUser.objects.filter(email=emailAdmin).exists():
            serializer = UserSerializer(email = emailAdmin, password = passwordAdmin)
            # serializer.save()
            
        else:
            return Response({"msg":"Ce compte existe deja"}, status=status.HTTP_200_OK)
    else:
        return Response({"msg":"Vous n'etes pas autorise a creer un debit de boison"}, 
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg":"Creation terminee"}, status=status.HTTP_200_OK)