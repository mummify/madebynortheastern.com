# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Creator'
        db.create_table(u'madeby_creator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'madeby', ['Creator'])

        # Adding model 'Project'
        db.create_table(u'madeby_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'madeby', ['Project'])

        # Adding M2M table for field creators on 'Project'
        m2m_table_name = db.shorten_name(u'madeby_project_creators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'madeby.project'], null=False)),
            ('creator', models.ForeignKey(orm[u'madeby.creator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'creator_id'])


    def backwards(self, orm):
        # Deleting model 'Creator'
        db.delete_table(u'madeby_creator')

        # Deleting model 'Project'
        db.delete_table(u'madeby_project')

        # Removing M2M table for field creators on 'Project'
        db.delete_table(db.shorten_name(u'madeby_project_creators'))


    models = {
        u'madeby.creator': {
            'Meta': {'object_name': 'Creator'},
            'first': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'madeby.project': {
            'Meta': {'object_name': 'Project'},
            'creators': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': u"orm['madeby.Creator']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['madeby']