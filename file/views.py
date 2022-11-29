# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.views import APIView
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.response import Response
# from .forms import formularioFile


from rest_framework import generics

from .models import File
from .serializers import FileSerializer


class FileView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


# class ProcessaFileView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]

#     def post(self, request):
#         serializer = FileSerializer(data=request.data)
#         print(serializer)
#         if not serializer.is_valid():
#             return HttpResponse(f"oops!")
#         serializer.save()
#         return HttpResponse(f"ok!")


# class FormView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "file.html"

#     def get(self, request):
#         serializer = FileSerializer()
#         return Response({"serializer": serializer})
