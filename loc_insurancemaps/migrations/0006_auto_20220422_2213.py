# Generated by Django 2.2.20 on 2022-04-22 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loc_insurancemaps', '0005_auto_20220302_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='jp2_url',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Document'),
        ),
    ]
