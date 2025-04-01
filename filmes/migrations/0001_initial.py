# Generated by Django 5.1.7 on 2025-04-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('ano_lancamento', models.IntegerField()),
                ('duracao', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
    ]
