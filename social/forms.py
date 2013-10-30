# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class SocialForm(forms.Form):
    facebook_wall = forms.BooleanField(initial=True,
                                       required=False,
                                       label=_(u'Импорт в VKontakte'))
    vk_wall = forms.BooleanField(initial=True,
                                 required=False,
                                 label=_(u'Импорт в Facebook'))
