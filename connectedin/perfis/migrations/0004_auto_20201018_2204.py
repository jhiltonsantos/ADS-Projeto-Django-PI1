# Generated by Django 3.1.2 on 2020-10-18 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_perfil_contatos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convite',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convites_feitos', to='perfis.perfil'),
        ),
    ]
