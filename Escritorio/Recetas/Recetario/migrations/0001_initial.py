# Generated by Django 2.2.12 on 2022-04-19 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la receta', max_length=100)),
                ('ingredientes', models.CharField(help_text='Ingredientes', max_length=1000)),
                ('pasos', models.CharField(help_text='pasos a seguir en la receta', max_length=2000)),
                ('prioridad', models.CharField(blank=True, max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
