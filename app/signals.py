# -*- coding: utf-8 -*-

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from .models import Member
from .constants import MEMBER_STATUS_ACTIVE, MEMBER_STATUS_JAILED
from .tasks import send_member_to_jail, set_member_to_freedom


@receiver(pre_save, sender=Member)
def member_status_changed(sender, **kwargs):
    instance = kwargs['instance']

    if instance.pk:
        old_instance = Member.objects.get(pk=instance.pk)

        if old_instance.status != instance.status:
            if instance.status == MEMBER_STATUS_JAILED:
                # Reestructurar por preso
                send_member_to_jail.delay(instance.pk)
            elif instance.status == MEMBER_STATUS_ACTIVE:
                # Reestruturar por libre
                set_member_to_freedom.delay(instance.pk)


@receiver(pre_save, sender=Member)
def validate_only_one_big_boss(sender, **kwargs):
    instance = kwargs['instance']

    if not instance.pk and not instance.boss and not instance.jailed_boss:
        big_boss = Member.objects.get_big_boss()
        if big_boss:
            raise Exception('Already exists a big boss in the organization')


