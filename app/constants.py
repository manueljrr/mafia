# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

MEMBER_STATUS_ACTIVE = 1
MEMBER_STATUS_JAILED = 2

MEMBER_STATUS = (
    (MEMBER_STATUS_ACTIVE, _(u'Active')),
    (MEMBER_STATUS_JAILED, _(u'Jailed'))
)

MAX_SUBORDINATES_ALLOWED = 2



