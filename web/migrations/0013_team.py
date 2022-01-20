# Generated by Django 4.0.1 on 2022-01-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='team-members/')),
                ('name', models.CharField(max_length=128)),
                ('designation', models.CharField(max_length=128)),
            ],
        ),
    ]