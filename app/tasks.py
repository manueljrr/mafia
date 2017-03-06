# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.shortcuts import get_object_or_404

from .models import Member


@shared_task
def send_member_to_jail(member_id):

    member = get_object_or_404(Member, pk=member_id)

    member_substitute = member.find_substitute()

    if member_substitute:
        # Store the jailed boss
        member.get_subordinates().update(jailed_boss=member)
        # Move subordinates to substitute
        member.get_subordinates().exclude(pk=member_substitute.pk).update(boss=member_substitute)

        # Change substitute boss if is a subordinate
        if member.boss is not member_substitute.boss:
            member_substitute.boss = member.boss
            member_substitute.jailed_boss = member
            member_substitute.save()

    return "%s was jailed, %s is the substitute" % (member.name, member_substitute.name)


@shared_task
def set_member_to_freedom(member_id):

    member = get_object_or_404(Member, pk=member_id)

    previous_subordinates = member.get_previous_subordinates()

    previous_subordinates.update(jailed_boss=None, boss=member)

    return "%s is now free" % member.name



