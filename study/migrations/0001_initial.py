# Generated by Django 3.1.7 on 2021-03-30 15:35

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='İletisimModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('isim_soyisim', models.CharField(max_length=100)),
                ('mesaj', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'İletisim',
                'verbose_name_plural': 'İletisim',
                'db_table': 'iletisim',
            },
        ),
        migrations.CreateModel(
            name='KategoriModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=30, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='isim', unique=True)),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
                'db_table': 'kategori',
            },
        ),
    ]
