# Generated by Django 4.0.6 on 2022-09-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinerApp', '0002_remove_tipo_empresa_tipo_empresa_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='p_v_u',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='margen_contribucion_Total',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='c_v_u',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]