# Generated by Django 3.2.2 on 2021-05-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipe', '0002_auto_20210507_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coating',
            name='density',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='coating',
            name='thickness',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='contents',
            name='flooded',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='contents',
            name='hydrotest',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='contents',
            name='installation_empty',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pipe',
            name='corrosion_allowance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pipe',
            name='pipe_density',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pipe',
            name='pipe_od',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pipe',
            name='pipe_wt',
            field=models.FloatField(),
        ),
    ]
