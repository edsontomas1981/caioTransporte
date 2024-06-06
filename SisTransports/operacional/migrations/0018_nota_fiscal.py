# Generated by Django 4.1.7 on 2023-08-07 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operacional', '0017_alter_dtc_destinatario_fk_alter_dtc_remetente_fk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota_fiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave_acesso', models.CharField(max_length=50)),
                ('num_nf', models.CharField(max_length=20)),
                ('data_emissao', models.DateField()),
                ('natureza', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=100)),
                ('tipo_documento', models.CharField(max_length=100)),
                ('volume', models.CharField(max_length=20)),
                ('peso', models.CharField(max_length=20)),
                ('m3', models.CharField(max_length=20)),
                ('valor_nf', models.CharField(max_length=20)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('dtc_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notas_fiscais', to='operacional.dtc')),
                ('usuario_cadastro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notas_fiscais_cadastradas', to=settings.AUTH_USER_MODEL)),
                ('usuario_ultima_atualizacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notas_fiscais_atualizadas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]