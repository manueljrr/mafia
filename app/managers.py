# -*- coding: utf-8 -*-

from django.db import models


class MemberManager(models.Manager):

    def find_by_name(self, name):
        return self.filter(name__iexact=name)

    def get_big_boss(self):
        return self.filter(boss__isnull=True).first()

    def get_all_boss(self):
        return self.exclude(subordinates__isnull=True)

    def get_plain_members(self):
        return self.exclude(subordinates__isnull=False)

