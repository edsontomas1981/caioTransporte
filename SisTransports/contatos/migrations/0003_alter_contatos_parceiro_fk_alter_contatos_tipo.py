# Generated by Django 4.0.6 on 2023-02-13 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parceiros', '0001_initial'),
        ('contatos', '0002_contatos_parceiro_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='parceiro_fk',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='parceiros.parceiros'),
        ),
        migrations.AlterField(
            model_name='contatos',
            name='tipo',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='contatos.tipo_contatos'),
        ),
    ]