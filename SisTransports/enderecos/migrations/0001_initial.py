# Generated by Django 4.0.6 on 2022-07-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enderecos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=8)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
    ]