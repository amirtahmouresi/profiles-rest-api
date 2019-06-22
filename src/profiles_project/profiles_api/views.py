from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [
            'Use HTTP methodes as functions(get, post, patch, put, delete)',
            'It is similar to traditional Django view',
            'Gives more control over your logic',
            'Is mapped manualy to Urls'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
