# Generated by Django 3.1.7 on 2021-04-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0013_derslermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlistirmaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soru_basligi', models.CharField(max_length=40)),
                ('siklar', models.CharField(max_length=40)),
                ('soru_sayisi', models.CharField(max_length=40)),
                ('cevaplar', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'alistirma',
                'verbose_name_plural': 'alistirma',
                'db_table': 'alistirma',
            },
        ),
    ]