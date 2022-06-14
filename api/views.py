from rest_framework import viewsets
from .models import StudentDetails
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class StudentViewset(viewsets.ModelViewSet):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentSerializer
    

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = StudentDetails.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = StudentDetails.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = StudentDetails.objects.get(pk=pk)
        serializer = StudentSerializer(instance=queryset ,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        
    def partial_update(self, request, pk=None):
        
        queryset = StudentDetails.objects.get(pk=pk)
        serializer = StudentSerializer(instance = queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        queryset = StudentDetails.objects.get(pk=pk)
        queryset.delete()
        return Response("Deleted Successfulyy")
   
    
class StudentGenericViewSet(viewsets.GenericViewSet):
    def get_queryset(self):
        queryset = StudentDetails.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.kwargs['pk'])
        return obj

    def list(self, request):
        queryset = self.get_queryset()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, **kwargs):
        obj = self.get_object()
        serializer = StudentSerializer(obj)
        return Response(serializer.data)



class StudentListMixinView(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.UpdateModelMixin,
                           generics.GenericAPIView):
    
    queryset = StudentDetails.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)