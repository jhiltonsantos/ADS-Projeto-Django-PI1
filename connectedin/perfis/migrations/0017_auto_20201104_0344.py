# Generated by Django 3.1.2 on 2020-11-04 03:44

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0016_auto_20201104_0343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postagem',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('data'), descending=True, nulls_last=True)]},
        ),
    ]
