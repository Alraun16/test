from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import New
from .serializers import NewSerializer

class NewView(APIView):
    def get(self, request):
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        return Response({"news": serializer.data})

    def post(self, request):
        new = request.data.get('new')
        serializer = NewSerializer(data=new)
        if serializer.is_valid(raise_exception=True):
            new_saved = serializer.save()
        return Response({"success": "New '{}' created successfully".format(new_saved.title)})

    def put(self, request, pk):
        saved_ka1WkJsDsNA = get_object_or_404(New.objects.all(), pk=pk)
        data = request.data.get('new')
        serializer = NewSerializer(instance=saved_ka1WkJsDsNA, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            new_saved = serializer.save()

        return Response({
            "success": "New '{}' updated successfully".format(new_saved.title)
        })

    def delete(self, request, pk):
        new = get_object_or_404(New.objects.all(), pk=pk)
        new.delete()
        return Response({
            "message": "New with id `{}` has been deleted.".format(pk)
        }, status=204)