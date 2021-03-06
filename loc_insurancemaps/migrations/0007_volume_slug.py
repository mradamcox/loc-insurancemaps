# Generated by Django 2.2.20 on 2022-05-14 17:58

from django.db import migrations, models

from loc_insurancemaps.models import Volume

def set_volume_slugs(apps, schema_editor):
    """Populate the new lookup fields on all volumes."""

    for v in Volume.objects.all():
        v.save()

class Migration(migrations.Migration):

    dependencies = [
        ('loc_insurancemaps', '0006_auto_20220422_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='volume',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RunPython(set_volume_slugs)
    ]
