from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *
from django.http import HttpResponseRedirect

class ImageDetail(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        response = super(ImageDetail, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/test')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer