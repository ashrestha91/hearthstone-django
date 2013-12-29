# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AvatarClass'
        db.create_table(u'myapp_avatarclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'myapp', ['AvatarClass'])

        # Adding model 'Rarity'
        db.create_table(u'myapp_rarity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'myapp', ['Rarity'])

        # Adding model 'CardType'
        db.create_table(u'myapp_cardtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'myapp', ['CardType'])

        # Adding model 'Card'
        db.create_table(u'myapp_card', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('avatar_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.AvatarClass'])),
            ('rarity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.Rarity'])),
            ('card_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.CardType'])),
            ('race', self.gf('django.db.models.fields.TextField')()),
            ('mana_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('attack', self.gf('django.db.models.fields.IntegerField')()),
            ('health', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'myapp', ['Card'])


    def backwards(self, orm):
        # Deleting model 'AvatarClass'
        db.delete_table(u'myapp_avatarclass')

        # Deleting model 'Rarity'
        db.delete_table(u'myapp_rarity')

        # Deleting model 'CardType'
        db.delete_table(u'myapp_cardtype')

        # Deleting model 'Card'
        db.delete_table(u'myapp_card')


    models = {
        u'myapp.avatarclass': {
            'Meta': {'object_name': 'AvatarClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'myapp.card': {
            'Meta': {'object_name': 'Card'},
            'attack': ('django.db.models.fields.IntegerField', [], {}),
            'avatar_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.AvatarClass']"}),
            'card_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.CardType']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'health': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mana_cost': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'race': ('django.db.models.fields.TextField', [], {}),
            'rarity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.Rarity']"})
        },
        u'myapp.cardtype': {
            'Meta': {'object_name': 'CardType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'myapp.rarity': {
            'Meta': {'object_name': 'Rarity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['myapp']