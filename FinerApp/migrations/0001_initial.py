# Generated by Django 4.0.6 on 2022-09-15 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EMPRESA',
            fields=[
                ('empresa_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=20)),
                ('cantidad_productos', models.SmallIntegerField()),
                ('margen_contribucion_Total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TIPO_EMPRESA',
            fields=[
                ('tipo_empresa_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('tipo_empresa', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCTO',
            fields=[
                ('producto_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('c_v_u', models.FloatField()),
                ('participacion_ventas', models.FloatField()),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='FinerApp.empresa')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='tipo_empresa_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='FinerApp.tipo_empresa'),
        ),
        migrations.CreateModel(
            name='COSTO_VARIABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.CharField(max_length=50)),
                ('cantidad_compra', models.SmallIntegerField()),
                ('unidad_compra', models.FloatField()),
                ('precio_compra', models.SmallIntegerField()),
                ('unidades_utilizada', models.FloatField()),
                ('factor', models.FloatField()),
                ('margen_contribucion_peso', models.FloatField()),
                ('margen_contribucion_porcentaje', models.IntegerField()),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='FinerApp.producto')),
            ],
        ),
    ]
