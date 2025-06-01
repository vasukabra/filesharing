from django.shortcuts import render
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .templates import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def download(request, uid):
    return render(request, 'download.html', {'uid' : uid})

class HandleFileUpload(APIView):
    
    def post(self, request):
        data = request.data
        serializer = serializers.FileListSerializer(data=data)
        if serializer.is_valid():
            url = serializer.save()
            print(serializer.validated_data)
            print(url['folder'])
            return Response(
                {'message': 'file uploaded succesfully', 'url' : url['folder']}
            )
        else:
            print(serializer.errors)
            return Response(serializer.errors)





        

