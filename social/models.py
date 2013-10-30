# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

class FacebookAccessToken(models.Model):
    facebook_access_token = models.CharField(max_length=200,
                                             verbose_name=_(u'Токен'))
    facebook_group_id = models.CharField(max_length=50,
                                         verbose_name=_(u'Group ID'))

    class Meta:
        verbose_name = _(u'Токен доступа Facebook')
        verbose_name_plural = _(u'Токены доступа Facebook')

    def __unicode__(self):
        return '{0}'.format(_(u'Facebook token'))

class VkontakteAccessToken(models.Model):
    vkontakte_access_token = models.CharField(max_length=200,
                                              verbose_name=_(u'Токен'))
    vkontakte_group_id = models.CharField(max_length=50,
                                          verbose_name=_(u'Group ID'))

    class Meta:
        verbose_name = _(u'Токен доступа Vkontakte')
        verbose_name_plural = _(u'Токены доступа VKontakte')

    def __unicode__(self):
        return '{0}'.format(_(u'Vkontakte token'))


