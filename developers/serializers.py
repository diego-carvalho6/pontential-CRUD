from developers.models import Developer
from rest_framework import serializers

class DeveloperSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)
    idade = serializers.IntegerField()
    hobby = serializers.CharField(max_length=100)
    sexo = serializers.CharField(max_length=1)
    datanascimento = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])

class DeveloperModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'