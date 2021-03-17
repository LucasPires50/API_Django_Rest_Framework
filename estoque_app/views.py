from estoque_app.models import Estoque
from estoque_app.serializers import EstoqueSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class EstoqueList(generics.ListAPIView):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

class EstoqueCreate(generics.ListCreateAPIView):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
                    

class EstoqueDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]




        
