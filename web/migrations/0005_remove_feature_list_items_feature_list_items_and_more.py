# Generated by Django 4.0.1 on 2022-01-18 17:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_featurelist_remove_feature_list_items_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='list_items',
        ),
        migrations.AddField(
            model_name='feature',
            name='list_items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.DeleteModel(
            name='FeatureList',
        ),
    ]
