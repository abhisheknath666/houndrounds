# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.name'
        db.add_column(u'houndroundsapp_person', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Guest', max_length=128),
                      keep_default=False)

        # Adding field 'PetOwner.frequency'
        db.add_column(u'houndroundsapp_petowner', 'frequency',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PetOwner.schedule'
        db.add_column(u'houndroundsapp_petowner', 'schedule',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)


        # Changing field 'PetOwner.price'
        db.alter_column(u'houndroundsapp_petowner', 'price', self.gf('django.db.models.fields.IntegerField')(max_length=128, null=True))

    def backwards(self, orm):
        # Deleting field 'Person.name'
        db.delete_column(u'houndroundsapp_person', 'name')

        # Deleting field 'PetOwner.frequency'
        db.delete_column(u'houndroundsapp_petowner', 'frequency')

        # Deleting field 'PetOwner.schedule'
        db.delete_column(u'houndroundsapp_petowner', 'schedule')


        # Changing field 'PetOwner.price'
        db.alter_column(u'houndroundsapp_petowner', 'price', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'houndroundsapp.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'houndroundsapp.petowner': {
            'Meta': {'object_name': 'PetOwner'},
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['houndroundsapp.Person']"}),
            'pet_access': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'houndroundsapp.walker': {
            'Meta': {'object_name': 'Walker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['houndroundsapp.Person']"}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['houndroundsapp']