from rest_framework import serializers
from .models import Folder, File
import shutil

class FileListSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=100)
    filelist = serializers.ListField(
        child = serializers.FileField(allow_empty_file = False, max_length = 100
        )
    )

    def zip_files(self,folder):
        shutil.make_archive(f'media/zip/{folder}' , 'zip' ,f'media/{folder}' )

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('filelist')
        files_list = []
        for file in files:
            file_obj = File.objects.create(folder=folder, my_file = file)
            files_list.append(file_obj)
        self.zip_files(folder.uid)      
        return {'files' : {} , 'folder' : str(folder.uid)}