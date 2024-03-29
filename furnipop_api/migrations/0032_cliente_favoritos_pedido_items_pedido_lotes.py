# Generated by Django 4.1.4 on 2023-01-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnipop_api', '0031_alter_itemspedidos_pedido_alter_lotespedidos_lote'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='favoritos',
            field=models.ManyToManyField(to='furnipop_api.item'),
        ),
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
