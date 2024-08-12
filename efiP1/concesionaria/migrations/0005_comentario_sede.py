# Generated by Django 5.1 on 2024-08-09 05:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesionaria', '0004_pais_auto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='concesionaria.auto')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gerente', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('ciudad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionaria.ciudad')),
                ('provincia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionaria.provincia')),
            ],
        ),
    ]
