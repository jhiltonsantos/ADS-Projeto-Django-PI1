# Generated by Django 3.1.2 on 2020-10-18 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_auto_20201018_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convite',
            name='convidado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convites_recebidos', to='perfis.perfil'),
        ),
    ]
