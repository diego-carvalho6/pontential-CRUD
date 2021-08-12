from developers.serializers import DeveloperModelSerializer, DeveloperSerializer
from developers.models import Developer
from developers.paginations import CustomPagination

from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.

class DeveloperView(generics.ListAPIView):
    serializer_class = DeveloperSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^nome', '^idade', "^hobby", "^datanascimento", "^sexo"]
    pagination_class = CustomPagination
    
    def get_queryset(self):
        query_list = Developer.objects.all()
        return query_list

    def post(self, request):
        
        serializer = DeveloperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        developer = Developer.objects.create(**serializer.validated_data)
        
        serializer = DeveloperSerializer(developer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class DeveloperByIdView(APIView):

    def get(self, request, developer_id=""):
        
        developer = get_object_or_404(Developer, id=developer_id)
        serializer = DeveloperSerializer(developer)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, developer_id=""):
    
        serializer = DeveloperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        developer = Developer.objects.filter(id=developer_id).update(**serializer.validated_data)
        
        developer = get_object_or_404(Developer, id=developer_id)
    
        serializer = DeveloperSerializer(developer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, developer_id=""):
        
        developer = get_object_or_404(Developer, id=developer_id)
        
        developer.delete()
        
        return Response("", status=status.HTTP_204_NO_CONTENT)