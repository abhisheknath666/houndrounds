# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'houndroundsapp_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'houndroundsapp', ['Person'])

        # Adding model 'Walker'
        db.create_table(u'houndroundsapp_walker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['houndroundsapp.Person'])),
            ('price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'houndroundsapp', ['Walker'])

        # Adding model 'PetOwner'
        db.create_table(u'houndroundsapp_petowner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['houndroundsapp.Person'])),
            ('pet_access', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'houndroundsapp', ['PetOwner'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'houndroundsapp_person')

        # Deleting model 'Walker'
        db.delete_table(u'houndroundsapp_walker')

        # Deleting model 'PetOwner'
        db.delete_table(u'houndroundsapp_petowner')


    models = {
        u'houndroundsapp.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'houndroundsapp.petowner': {
            'Meta': {'object_name': 'PetOwner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['houndroundsapp.Person']"}),
            'pet_access': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'houndroundsapp.walker': {
            'Meta': {'object_name': 'Walker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['houndroundsapp.Person']"}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['houndroundsapp']