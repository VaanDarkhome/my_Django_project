from django.shortcuts import render

from rest_feamework import viewsets

from lms import Curator
from lms.seialisers import CuratorSerializer


class CuratorViewSet(viewsets.ModelVeilSet):
    queryset = Curator.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = CuratorSerializer