# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import MEMBER_STATUS, MEMBER_STATUS_JAILED, MEMBER_STATUS_ACTIVE
from .managers import MemberManager


class Member(models.Model):
    objects = MemberManager()

    name = models.CharField(
        verbose_name=_(u'Name'),
        max_length=100,
        unique=True
    )
    age = models.IntegerField(
        verbose_name=_(u'Age'),
        default=0
    )
    status = models.IntegerField(
        verbose_name=_(u'Status'),
        choices=MEMBER_STATUS
    )
    boss = models.ForeignKey(
        'self',
        verbose_name=_(u'Boss'),
        related_name='subordinates',
        null=True,
        blank=True
    )
    jailed_boss = models.ForeignKey(
        'self',
        verbose_name=_(u'Jailed boss'),
        related_name='previous_subordinates',
        null=True,
        blank=True
    )

    @property
    def subordinates_count(self):
        return self.get_subordinates_count()

    def get_subordinates(self):
        return self.subordinates.all()

    def get_previous_subordinates(self):
        return self.previous_subordinates.all()

    def get_same_level_members(self):
        return self.boss.get_subordinates().exclude(pk=self.pk) if self.boss else Member.objects.none()

    def get_subordinates_count(self):
        return self.get_subordinates().count()

    def to_jail(self):
        self. status = MEMBER_STATUS_JAILED
        self.save()

    def to_freedom(self):
        self. status = MEMBER_STATUS_ACTIVE
        self.save()

    def find_substitute(self):
        substitute = self.get_same_level_members().order_by('-age').first()
        if not substitute:
            substitute = self.get_subordinates().order_by('-age').first()

        return substitute

    def __str__(self):
        return self.name


