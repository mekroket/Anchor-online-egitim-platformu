# Generated by Django 3.1.7 on 2021-04-04 11:36

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0012_delete_derslermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DerslerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=20)),
                ('resim', models.ImageField(upload_to='ders_resimleri')),
                ('icerik', models.TextField(max_length=150)),
                ('ücret', models.CharField(max_length=20)),
                ('tür', models.CharField(max_length=30)),
                ('kısa_özet1', models.CharField(max_length=50)),
                ('kısa_özet2', models.CharField(max_length=50)),
                ('kısa_özet3', models.CharField(max_length=50)),
                ('kısa_özet4', models.CharField(max_length=50)),
                ('kısa_özet5', models.CharField(max_length=50)),
                ('kısa_özet1_tanıtım', models.TextField()),
                ('kısa_özet1_tanıtım_baslik', models.TextField()),
                ('kısa_özet2_tanıtım', models.TextField()),
                ('kısa_özet2_tanıtım_baslik', models.TextField()),
                ('kısa_özet3_tanıtım', models.TextField()),
                ('kısa_özet3_tanıtım_baslik', models.TextField()),
                ('kısa_özet4_tanıtım', models.TextField()),
                ('kısa_özet4_tanıtım_baslik', models.TextField()),
                ('kısa_özet5_tanıtım', models.TextField()),
                ('kısa_özet5_tanıtım_baslik', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='baslik', unique=True)),
            ],
            options={
                'verbose_name': 'Dersler',
                'verbose_name_plural': 'Ders-Ekle',
                'db_table': 'DerslerTablo',
            },
        ),
    ]