# Generated by Django 2.2.20 on 2022-04-12 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('georeference', '0003_georefsession_prepsession_sessionbase_trimsession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masksession',
            name='layer',
        ),
        migrations.RemoveField(
            model_name='masksession',
            name='user',
        ),
        migrations.RemoveField(
            model_name='splitevaluation',
            name='document',
        ),
        migrations.RemoveField(
            model_name='splitevaluation',
            name='user',
        ),
        migrations.DeleteModel(
            name='GeoreferenceSession',
        ),
        migrations.DeleteModel(
            name='MaskSession',
        ),
        migrations.DeleteModel(
            name='SplitEvaluation',
        ),
    ]
