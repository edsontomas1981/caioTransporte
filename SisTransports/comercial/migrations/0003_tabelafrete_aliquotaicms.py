# Generated by Django 4.0.6 on 2023-01-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0002_rename_fretevalor_cotacao_fretepeso'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabelafrete',
            name='aliquotaIcms',
            field=models.IntegerField(default=0),
        ),
    ]