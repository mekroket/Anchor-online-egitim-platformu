# Generated by Django 3.1.7 on 2021-04-10 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0014_alistirmamodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AlistirmaModel',
        ),
        migrations.AlterModelOptions(
            name='yazilarmodel',
            options={'verbose_name': 'Yazi', 'verbose_name_plural': ' Popüler Kurslar'},
        ),
    ]