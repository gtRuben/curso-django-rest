# Generated by Django 4.0.4 on 2022-05-26 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('pontos_turisticos', '0004_pontoturistico_localizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacao.localizacao'),
        ),
    ]