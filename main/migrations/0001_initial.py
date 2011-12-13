# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Artist'
        db.create_table('main_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('information', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('main', ['Artist'])

        # Adding model 'Album'
        db.create_table('main_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Artist'])),
            ('information', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('main', ['Album'])

        # Adding model 'Song'
        db.create_table('main_song', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lyrics', self.gf('django.db.models.fields.TextField')()),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Artist'], null=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Album'], null=True)),
            ('information', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('main', ['Song'])


    def backwards(self, orm):
        
        # Deleting model 'Artist'
        db.delete_table('main_artist')

        # Deleting model 'Album'
        db.delete_table('main_album')

        # Deleting model 'Song'
        db.delete_table('main_song')


    models = {
        'main.album': {
            'Meta': {'object_name': 'Album'},
            'album': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'main.artist': {
            'Meta': {'object_name': 'Artist'},
            'artist': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'main.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Album']", 'null': 'True'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Artist']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'lyrics': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'song': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['main']
