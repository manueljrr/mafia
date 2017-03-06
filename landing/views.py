# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'landing/index.html'


class MemberView(TemplateView):
    template_name = 'landing/member.html'


