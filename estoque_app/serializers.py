from estoque_app.models import Estoque
from rest_framework import serializers

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = ['id', 'nome', 'valor']