# Generated by Django 4.1.4 on 2023-02-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnipop_api', '0022_itemspedidos_ida_lotes_pedidos_ida_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemspedidos',
            name='idA',
            field=models.IntegerField(db_column='idA', default=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lotespedidos',
            name='idA',
            field=models.IntegerField(db_column='idA', default=10, unique=True),
            preserve_default=False,
        ),
    ]
