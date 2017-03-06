# -*- coding: utf-8 -*-

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Member
from .serializers import MemberBasicSerializer, BossSerializer, MemberCreateSerializer


class MemberListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Member.objects.all()
    serializer_class = MemberBasicSerializer


class BossListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Member.objects.get_all_boss()
    serializer_class = BossSerializer


class MemberDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Member.objects.all()
    serializer_class = BossSerializer


class MemberCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Member.objects.all()
    serializer_class = MemberCreateSerializer


