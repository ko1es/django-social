# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookAccessToken'
        db.create_table(u'social_facebookaccesstoken', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebook_access_token', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('facebook_group_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'social', ['FacebookAccessToken'])

        # Adding model 'VkontakteAccessToken'
        db.create_table(u'social_vkontakteaccesstoken', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vkontakte_access_token', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('vkontakte_group_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'social', ['VkontakteAccessToken'])


    def backwards(self, orm):
        # Deleting model 'FacebookAccessToken'
        db.delete_table(u'social_facebookaccesstoken')

        # Deleting model 'VkontakteAccessToken'
        db.delete_table(u'social_vkontakteaccesstoken')


    models = {
        u'social.facebookaccesstoken': {
            'Meta': {'object_name': 'FacebookAccessToken'},
            'facebook_access_token': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'facebook_group_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'social.vkontakteaccesstoken': {
            'Meta': {'object_name': 'VkontakteAccessToken'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vkontakte_access_token': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vkontakte_group_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['social']