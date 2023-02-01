# Generated by Django 4.1.4 on 2023-01-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnipop_api', '0009_alter_imagen_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='items',
            field=models.ManyToManyField(through='furnipop_api.ItemsPedidos', to='furnipop_api.item'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='lotes',
            field=models.ManyToManyField(through='furnipop_api.LotesPedidos', to='furnipop_api.lote'),
        ),
    ]
