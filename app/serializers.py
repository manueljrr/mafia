# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from .models import Member
from .constants import MAX_SUBORDINATES_ALLOWED, MEMBER_STATUS


class MemberBasicSerializer(serializers.ModelSerializer):

    boss_name = serializers.StringRelatedField(source='boss')

    def to_representation(self, instance):
        member = super(MemberBasicSerializer, self).to_representation(instance)
        member['status'] = dict(MEMBER_STATUS)[instance.status]
        return member

    class Meta:
        model = Member
        fields = ('id', 'name', 'age', 'status', 'boss_name', 'boss', 'subordinates_count')


class MemberCreateSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        new_member = super(MemberCreateSerializer, self).to_representation(instance)
        new_member['id'] = instance.id
        return new_member

    class Meta:
        model = Member
        fields = ('name', 'age', 'status', 'boss')


class SubordinateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'name', 'age', 'status', 'subordinates_count')


class BossSerializer(serializers.ModelSerializer):

    subordinates = SubordinateSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        member = super(BossSerializer, self).to_representation(instance)
        if instance.subordinates_count > MAX_SUBORDINATES_ALLOWED:
            member['warning'] = _(u'ALERT! this boss has more than %d subordinates' % MAX_SUBORDINATES_ALLOWED)
        return member

    class Meta:
        model = Member
        fields = ('id', 'name', 'age', 'status', 'subordinates_count', 'subordinates')



