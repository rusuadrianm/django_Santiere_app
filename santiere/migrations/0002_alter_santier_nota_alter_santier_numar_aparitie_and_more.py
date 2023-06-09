# Generated by Django 4.1.7 on 2023-03-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santiere', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santier',
            name='nota',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='santier',
            name='numar_aparitie',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='santier',
            name='observatie',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='santier',
            name='tip_santier',
            field=models.CharField(choices=[('bransament', 'Bransament'), ('extindere', 'Extindere'), ('deviere', 'Deviere'), ('sistematizare', 'Sistematizare'), ('reabilitare', 'Reabilitare'), ('redimensionare', 'Redimensionare')], max_length=15),
        ),
    ]
