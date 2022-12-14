# Generated by Django 4.0.6 on 2022-09-24 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinerApp', '0004_remove_costo_variable_cantidad_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='cantidad_productos',
        ),
        migrations.AlterField(
            model_name='costo_variable',
            name='producto_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinerApp.producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='empresa_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinerApp.empresa'),
        ),
    ]
