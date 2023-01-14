from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ShortUrls
from .serializers import UrlSerializer
from rest_framework import status
import uuid
# Create your views here.

'''View to Redirect the user to the particular website once he/she scans the url'''
class ShortUrlView(APIView):
    
    def get(self, request, url):
       url_queryset = get_object_or_404(ShortUrls, shorten_url=url)
       print(request.build_absolute_uri("/"))
       return redirect(url_queryset.url)

'''View to generate short url and return in to the user'''
class ShortUrlManageView(APIView):

    def get(self, request, url):
        url_queryset = get_object_or_404(ShortUrls, shorten_url=url)
        serializer = UrlSerializer(url_queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = UrlSerializer(data=request.data)

        if serializer.is_valid():
            short_string = str(uuid.uuid4())[0:5]
            serializer.save(shorten_url=short_string, count=1)
            return_data = serializer.data
            return_data["short_url"]=request.build_absolute_uri("/")+short_string

            return Response(return_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
